"""ASSESSMENT_SERVICE: kanonisches Assessment, Orchestrierung der Engines und Neuberechnung.

Ablauf nach ARCHITECTURE.md Abschnitt 5: Katalogversionen fixieren, Regelpfade
ausführen (RULE_ENGINE), Anwendbarkeit bestimmen (APPLICABILITY_ENGINE),
Gap-Status ableiten (GAP_ENGINE) und je RR ein RRResult aus Lesesicht
(REQUIREMENT_SERVICE), Herleitung (ApplicabilityEngine.explain) und Gap-Ergebnis
bilden. Jede Auswertung ist vollständig und zustandslos; eine Neuberechnung
ist eine vollständige Neuauswertung des aktuellen Eingabestands (SR-040).
Zeitpunkte, Assessment-ID, Revision, Zustand und Sprache sind Metadaten und gehen
nicht in den fachlichen Fingerprint ein. Der Kern ist zustandslos und ohne
Persistenz; Lebenszyklus, Revisionen und Audit-Protokoll führt die
Anwendungsschicht (assessment_application.py).
"""

from __future__ import annotations

import dataclasses
import uuid
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from types import MappingProxyType
from typing import Any, Iterable, Mapping

from regscoutx.applicability_engine import (
    ApplicabilityEngine,
    ApplicabilityExplanation,
    ApplicabilityResult,
)
from regscoutx.catalog_repository import CatalogRepository
from regscoutx.domain import (
    ID_NAMESPACE,
    METADATA,
    ApplicableRequirement,
    Applicability,
    CatalogVersionSet,
    DecisionResult,
    EngineRun,
    Language,
    LocalizedText,
    canonical,
    checked_fields,
    fingerprint,
)
from regscoutx.errors import (
    CatalogValidationError,
    CatalogVersionMismatchError,
    InvalidInputError,
    UnexpectedEndStateError,
)
from regscoutx.evidence_service import EvidenceReference, EvidenceService
from regscoutx.gap_engine import (
    AnswerState,
    GapAssessment,
    GapEngine,
    GapResult,
    GapResultStatus,
    MeasureMappingStatus,
    MeasurePlan,
)
from regscoutx.requirement_service import RequirementService
from regscoutx.rule_engine import RuleEngine

INPUT_FIELDS = ("profile",)
INPUT_OPTIONAL = ("answers", "evidence")


class AssessmentState(Enum):
    DRAFT = "DRAFT"
    FINALISED = "FINALISED"


@dataclass(frozen=True)
class ProductProfile:
    """Kontrollierte Produkteingaben als flache, sortierte Schlüssel-Wert-Paare (DATA_MODEL ProductProfile)."""

    answers: tuple[tuple[str, Any], ...]

    @classmethod
    def of(cls, answers: Mapping[str, Any]) -> ProductProfile:
        if not isinstance(answers, Mapping):
            raise InvalidInputError("profile", answers, "must be a mapping")
        for key in answers:
            if not isinstance(key, str):
                raise InvalidInputError("profile", key, "input keys must be strings")
        return cls(tuple(sorted(answers.items())))

    def as_dict(self) -> dict[str, Any]:
        return dict(self.answers)


@dataclass(frozen=True)
class AssessmentInput:
    """Maschinenlesbare Eingabe einer Bewertung: Produktprofil, Erfüllungsbewertungen, Nachweisreferenzen."""

    profile: ProductProfile
    answers: tuple[GapAssessment, ...] = ()
    evidence: tuple[EvidenceReference, ...] = ()

    @classmethod
    def from_mapping(cls, data: Any) -> AssessmentInput:
        values = checked_fields("assessment_input", data, INPUT_FIELDS, INPUT_OPTIONAL)
        lists = {}
        for name in INPUT_OPTIONAL:
            items = values.get(name, [])
            if not isinstance(items, (list, tuple)):
                raise InvalidInputError(name, items, "must be a list")
            lists[name] = items
        return cls(
            profile=ProductProfile.of(values["profile"]),
            answers=tuple(GapAssessment.from_mapping(item) for item in lists["answers"]),
            evidence=tuple(EvidenceReference.from_mapping(item) for item in lists["evidence"]),
        )


@dataclass(frozen=True)
class LifecyclePhase:
    code: str
    label: LocalizedText


@dataclass(frozen=True)
class PlannedEvidenceType:
    evidence_type_key: str
    label: LocalizedText


@dataclass(frozen=True)
class PlannedMeasure:
    measure_key: str
    label: LocalizedText
    evidence_types: tuple[PlannedEvidenceType, ...]


@dataclass(frozen=True)
class MeasureMapping:
    """Vorgesehene Maßnahmen und Nachweisarten aus RR_MEASURE; bei REVIEW_REQUIRED leer."""

    status: MeasureMappingStatus
    measures: tuple[PlannedMeasure, ...]


@dataclass(frozen=True)
class RRResult:
    """Ergebnis einer RR: Katalogsicht, Herleitung der Anwendbarkeit und Gap-Ergebnis."""

    requirement_result_id: str
    requirement_id: str
    title: LocalizedText
    requirement_text: LocalizedText
    theme_cluster: str
    lifecycle_phases: tuple[LifecyclePhase, ...]
    applicability: ApplicableRequirement
    explanation: ApplicabilityExplanation
    measure: MeasureMapping
    gap: GapResult

    @property
    def primary_sources(self) -> tuple[str, ...]:
        return self.explanation.primary_sources

    @property
    def supplementary_sources(self) -> tuple[str, ...]:
        return self.explanation.supplementary_sources

    @property
    def gap_status(self) -> GapResultStatus:
        return self.gap.status


@dataclass(frozen=True)
class ResultCounts:
    """Summen nach Anwendbarkeit und Gap-Status (Codes als Schlüssel), Gaps nach SR-015."""

    total: int
    applicability: Mapping[str, int]
    gap_status: Mapping[str, int]
    gaps: int
    measure_review_required: int
    answers_review_required: int


@dataclass(frozen=True)
class AssessmentChange:
    """Vorher/Nachher-Differenz zweier Auswertungsstände; Metadatum, kein Teil des fachlichen Ergebnisses.

    Wird ausschließlich aus input_snapshot und result_snapshot gebildet und ist
    damit auch gegenüber gespeicherten Ständen anderer Katalogversionen bestimmbar.
    """

    changed_inputs: tuple[str, ...]
    recorded_answers: tuple[str, ...]
    recorded_evidence: tuple[str, ...]
    removed_evidence: tuple[str, ...]
    deactivated_answers: tuple[str, ...]
    reactivated_answers: tuple[str, ...]
    applicability_changes: tuple[tuple[str, str | None, str | None], ...]
    gap_status_changes: tuple[tuple[str, str | None, str | None], ...]

    @property
    def empty(self) -> bool:
        return not any(getattr(self, f.name) for f in dataclasses.fields(self))


@dataclass(frozen=True)
class DecisionSummary:
    area: str
    status: str
    outcome: str | None
    mdr_class: str | None
    applicable_from: str | None
    missing_input: tuple[str, str] | None


@dataclass(frozen=True)
class GroupCounts:
    key: str
    label: LocalizedText | None
    counts: ResultCounts


@dataclass(frozen=True)
class AssessmentSummary:
    assessment_id: str
    schema_version: str
    catalog_versions: CatalogVersionSet
    profile: ProductProfile
    decisions: tuple[DecisionSummary, ...]
    counts: ResultCounts
    by_theme: tuple[GroupCounts, ...]
    by_lifecycle: tuple[GroupCounts, ...]
    results: tuple[RRResult, ...]


@dataclass(frozen=True)
class Assessment:
    """Kanonische Bewertung; fachlicher Inhalt ohne METADATA-Felder bestimmt den Fingerprint."""

    assessment_id: str = field(metadata=METADATA)
    revision: int = field(metadata=METADATA)
    created_at: str = field(metadata=METADATA)
    state: AssessmentState = field(metadata=METADATA)
    language: Language = field(metadata=METADATA)
    catalog_versions: CatalogVersionSet
    profile: ProductProfile
    answers: tuple[GapAssessment, ...]
    evidence: tuple[EvidenceReference, ...]
    engine_runs: tuple[EngineRun, ...]
    decision_results: tuple[DecisionResult, ...]
    results: tuple[RRResult, ...]
    counts: ResultCounts
    last_change: AssessmentChange | None = field(metadata=METADATA)
    fingerprint: str = field(metadata=METADATA)

    @property
    def schema_version(self) -> str:
        """Das Ergebnisschema ist DATA_MODEL.yaml; seine Version ist Teil des CatalogVersionSet."""
        return self.catalog_versions.data_model_version

    def result(self, requirement_id: str) -> RRResult:
        for result in self.results:
            if result.requirement_id == requirement_id:
                return result
        raise KeyError(requirement_id)



def count_results(results: Iterable[RRResult]) -> ResultCounts:
    items = list(results)
    applicability = Counter(r.applicability.applicability.value for r in items)
    gap = Counter(r.gap.status.value for r in items)
    return ResultCounts(
        total=len(items),
        applicability=MappingProxyType({s.value: applicability[s.value] for s in Applicability}),
        gap_status=MappingProxyType({s.value: gap[s.value] for s in GapResultStatus}),
        gaps=sum(1 for r in items if r.gap.is_gap),
        measure_review_required=sum(
            1 for r in items if r.applicability.applicability is Applicability.APPLICABLE
            and r.measure.status is MeasureMappingStatus.REVIEW_REQUIRED),
        answers_review_required=sum(
            1 for r in items if r.gap.answer_state is AnswerState.REACTIVATED_REVIEW_REQUIRED),
    )


def input_snapshot(source: Assessment | AssessmentInput) -> dict[str, Any]:
    """Kanonische Eingaben: Profil, Bewertungen je RR (ohne assessed_at), Nachweisreferenzen je ID."""
    return {
        "profile": dict(source.profile.answers),
        "answers": {a.requirement_id: canonical(a) for a in source.answers},
        "evidence": {e.evidence_id: canonical(e) for e in source.evidence},
    }


def result_snapshot(assessment: Assessment) -> dict[str, Any]:
    """Katalogunabhängige Ergebnissicht aus Codes und Kennungen (lesbar ohne Katalogtexte)."""
    return {
        "decisions": [{
            "area": d.area, "status": d.status.value, "outcome": d.outcome,
            "mdr_class": d.mdr_class, "applicable_from": d.applicable_from,
            "missing_input": None if d.missing_input is None
            else [d.missing_input.rule_id, d.missing_input.input_key],
            "rule_ids": [e.rule_id for e in d.executions],
        } for d in assessment.decision_results],
        "requirements": [{
            "requirement_id": r.requirement_id,
            "applicability": r.applicability.applicability.value,
            "reason_code": r.applicability.reason_code,
            "block": r.applicability.block,
            "evaluated_predicates": [[p.predicate_key, p.value.value]
                                     for p in r.applicability.evaluated_predicates],
            "relevant_inputs": [[key, value] for key, value in r.applicability.relevant_inputs],
            "supporting_rule_ids": list(r.applicability.supporting_rule_ids),
            "theme_cluster": r.theme_cluster,
            "lifecycle_phases": [phase.code for phase in r.lifecycle_phases],
            "gap_status": r.gap.status.value,
            "gap_reason": r.gap.reason.value,
            "gap": r.gap.is_gap,
            "answer_state": None if r.gap.answer_state is None else r.gap.answer_state.value,
            "evidence_state": r.gap.evidence.state.value,
            "evidence_ids": list(r.gap.evidence.evidence_ids),
            "measure_status": r.measure.status.value,
            "measures": [m.measure_key for m in r.measure.measures],
        } for r in assessment.results],
        "counts": canonical(assessment.counts),
    }


def compute_change(before_inputs: Mapping[str, Any], before_results: Mapping[str, Any],
                   after_inputs: Mapping[str, Any],
                   after_results: Mapping[str, Any]) -> AssessmentChange:
    """Differenz zweier Stände aus input_snapshot/result_snapshot."""
    def changed(old: Mapping[str, Any], new: Mapping[str, Any], ignore: str | None = None):
        strip = (lambda v: {k: x for k, x in v.items() if k != ignore}) if ignore else (lambda v: v)
        return tuple(sorted(key for key in new
                            if key not in old or strip(old[key]) != strip(new[key])))

    def by_rr(results: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
        return {r["requirement_id"]: r for r in results["requirements"]}

    old_rr, new_rr = by_rr(before_results), by_rr(after_results)

    def transitions(field_name: str) -> tuple[tuple[str, str | None, str | None], ...]:
        return tuple((rr, old_rr.get(rr, {}).get(field_name), new_rr.get(rr, {}).get(field_name))
                     for rr in sorted(old_rr.keys() | new_rr.keys())
                     if old_rr.get(rr, {}).get(field_name) != new_rr.get(rr, {}).get(field_name))

    states = transitions("answer_state")
    old_profile, new_profile = before_inputs["profile"], after_inputs["profile"]
    return AssessmentChange(
        changed_inputs=tuple(sorted(key for key in old_profile.keys() | new_profile.keys()
                                    if old_profile.get(key, _MISSING)
                                    != new_profile.get(key, _MISSING))),
        recorded_answers=changed(before_inputs["answers"], after_inputs["answers"], "stale"),
        recorded_evidence=changed(before_inputs["evidence"], after_inputs["evidence"]),
        removed_evidence=tuple(sorted(set(before_inputs["evidence"]) - set(after_inputs["evidence"]))),
        deactivated_answers=tuple(rr for rr, old, new in states
                                  if new == AnswerState.INACTIVE.value and old is not None),
        reactivated_answers=tuple(rr for rr, old, new in states
                                  if old == AnswerState.INACTIVE.value and new is not None),
        applicability_changes=transitions("applicability"),
        gap_status_changes=transitions("gap_status"),
    )


def canonical_uuid(label: str, value: Any) -> str:
    """Kennung in kanonischer UUID-Form; alles andere wird abgewiesen."""
    try:
        valid = isinstance(value, str) and str(uuid.UUID(value)) == value
    except (TypeError, ValueError, AttributeError):
        valid = False
    if not valid:
        raise InvalidInputError(label, value, "must be a UUID in canonical form")
    return value


@dataclass(frozen=True)
class _CatalogView:
    title: LocalizedText
    requirement_text: LocalizedText
    theme_cluster: str
    lifecycle_phases: tuple[LifecyclePhase, ...]
    measure: MeasureMapping


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


class AssessmentService:
    """Erzeugt und berechnet Bewertungen deterministisch gegen die geladenen Kataloge."""

    def __init__(self, repository: CatalogRepository) -> None:
        self._repository = repository
        self._rules = RuleEngine(repository)
        self._applicability = ApplicabilityEngine(repository)
        self._gaps = GapEngine()
        self._evidence = EvidenceService()
        self._entry_keys = {entry: self._rules.input_keys(entry)
                            for entry in repository.entry_points}
        self._profile_keys = frozenset(repository.applicability["profile_inputs"])
        requirements = RequirementService(repository)
        self._views = {rr_id: self._catalog_view(requirements, rr_id)
                       for rr_id in repository.requirement_ids}

    @staticmethod
    def _catalog_view(service: RequirementService, rr_id: str) -> _CatalogView:
        de, en = service.view(rr_id, Language.DE), service.view(rr_id, Language.EN)
        try:
            status = MeasureMappingStatus(de.measure_status)
        except ValueError as exc:
            raise CatalogValidationError(
                [f"RR_MEASURE: {rr_id}: unknown mapping status '{de.measure_status}'"]) from exc
        measures = tuple(
            PlannedMeasure(
                measure_key=m_de.measure_key,
                label=LocalizedText(m_de.label, m_en.label),
                evidence_types=tuple(PlannedEvidenceType(key, LocalizedText(label_de, label_en))
                                     for (key, label_de), (_, label_en)
                                     in zip(m_de.evidence_types, m_en.evidence_types)))
            for m_de, m_en in zip(de.measures, en.measures))
        if (status is MeasureMappingStatus.MAPPED) != bool(measures):
            raise CatalogValidationError(
                [f"RR_MEASURE: {rr_id}: status {status.value} inconsistent with measures"])
        return _CatalogView(
            title=LocalizedText(de.title, en.title),
            requirement_text=LocalizedText(de.text, en.text),
            theme_cluster=de.theme_cluster,
            lifecycle_phases=tuple(LifecyclePhase(code, LocalizedText(label_de, label_en))
                                   for (code, label_de), (_, label_en)
                                   in zip(de.lifecycle_phases, en.lifecycle_phases)),
            measure=MeasureMapping(status, measures),
        )

    def summarize(self, assessment: Assessment) -> AssessmentSummary:
        """Ergebnissicht für Darstellung und Bericht; Gruppen nach Themencluster und Lebenszyklusphase.

        Eine RR mit mehreren Lebenszyklusphasen zählt in jeder ihrer Phasen.
        """
        themes: dict[str, list[RRResult]] = {}
        phases: dict[str, list[RRResult]] = {}
        for result in assessment.results:
            themes.setdefault(result.theme_cluster, []).append(result)
            for phase in result.lifecycle_phases:
                phases.setdefault(phase.code, []).append(result)
        return AssessmentSummary(
            assessment_id=assessment.assessment_id,
            schema_version=assessment.schema_version,
            catalog_versions=assessment.catalog_versions,
            profile=assessment.profile,
            decisions=tuple(
                DecisionSummary(d.area, d.status.value, d.outcome, d.mdr_class, d.applicable_from,
                                None if d.missing_input is None
                                else (d.missing_input.rule_id, d.missing_input.input_key))
                for d in assessment.decision_results),
            counts=assessment.counts,
            by_theme=tuple(GroupCounts(key, None, count_results(items))
                           for key, items in themes.items()),
            by_lifecycle=tuple(
                GroupCounts(phase, LocalizedText(self._repository.phase_label(phase, Language.DE),
                                                 self._repository.phase_label(phase, Language.EN)),
                            count_results(phases[phase]))
                for phase in self._repository.lifecycle_phases if phase in phases),
            results=assessment.results,
        )

    # Eingaben -------------------------------------------------------------

    def _split(self, profile: ProductProfile) -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
        """Flache Produkteingaben den Einstiegspunkten bzw. den Applicability-Eingaben zuordnen."""
        rule_inputs: dict[str, dict[str, Any]] = {}
        profile_inputs: dict[str, Any] = {}
        for key, value in profile.answers:
            if key in self._profile_keys:
                profile_inputs[key] = value
                continue
            entries = [entry for entry, keys in self._entry_keys.items() if key in keys]
            if not entries:
                raise InvalidInputError(key, value, "unknown product profile input key")
            for entry in entries:
                rule_inputs.setdefault(entry, {})[key] = value
        ordered = {entry: rule_inputs[entry] for entry in self._entry_keys if entry in rule_inputs}
        return ordered, profile_inputs

    # Auswertung -----------------------------------------------------------

    def create(self, data: AssessmentInput, *, assessment_id: str | None = None,
               created_at: str | None = None, language: Language = Language.DE,
               revision: int = 1, state: AssessmentState = AssessmentState.DRAFT) -> Assessment:
        """Bewertung gegen die geladenen Katalogversionen anlegen bzw. aus Eingaben wiederherstellen."""
        if not isinstance(data, AssessmentInput):
            raise InvalidInputError("assessment_input", data, "must be an AssessmentInput")
        if not isinstance(language, Language):
            raise InvalidInputError("language", language, "must be a Language")
        if not isinstance(state, AssessmentState):
            raise InvalidInputError("state", state, "must be an AssessmentState")
        if not isinstance(revision, int) or isinstance(revision, bool) or revision < 1:
            raise InvalidInputError("revision", revision, "must be a positive integer")
        assessment_id = canonical_uuid("assessment_id", assessment_id or str(uuid.uuid4()))
        evaluated = self._evaluate(data.profile, data.answers, data.evidence)
        return self._assessment(assessment_id, revision, created_at or _now(), state, language,
                                evaluated, None)

    def recalculate(self, assessment: Assessment, *, profile: ProductProfile | None = None,
                    answers: Iterable[GapAssessment] = (),
                    evidence: Iterable[EvidenceReference] = (),
                    remove_evidence: Iterable[str] = ()) -> Assessment:
        """Eingaben ändern und vollständig neu auswerten (SR-040).

        profile ersetzt das Produktprofil; answers und evidence werden je RR bzw.
        evidence_id ergänzt oder ersetzt, remove_evidence entfernt Referenzen.
        Bewertungen werden nie verworfen: nicht anwendbare RR führen sie als
        INACTIVE und markieren sie als veraltet. Die übergebene Bewertung bleibt
        unverändert; bei Fehlern entsteht keine neue.
        """
        if assessment.catalog_versions != self._repository.versions:
            raise CatalogVersionMismatchError(assessment.catalog_versions, self._repository.versions)
        if assessment.state is not AssessmentState.DRAFT:
            raise InvalidInputError("state", assessment.state.value, "only DRAFT can be recalculated")
        new_profile = assessment.profile if profile is None else profile
        if not isinstance(new_profile, ProductProfile):
            raise InvalidInputError("profile", new_profile, "must be a ProductProfile")
        merged_answers = {a.requirement_id: a for a in assessment.answers}
        merged_answers.update({getattr(a, "requirement_id", None): a for a in answers})
        merged_evidence = {e.evidence_id: e for e in assessment.evidence}
        merged_evidence.update({getattr(e, "evidence_id", None): e for e in evidence})
        for evidence_id in remove_evidence:
            if evidence_id not in merged_evidence:
                raise InvalidInputError("remove_evidence", evidence_id, "unknown evidence reference")
            del merged_evidence[evidence_id]
        evaluated = self._evaluate(new_profile, merged_answers.values(), merged_evidence.values())
        updated = self._assessment(assessment.assessment_id, assessment.revision,
                                   assessment.created_at, assessment.state, assessment.language,
                                   evaluated, None)
        change = compute_change(input_snapshot(assessment), result_snapshot(assessment),
                                input_snapshot(updated), result_snapshot(updated))
        return dataclasses.replace(updated, last_change=change)

    def _evaluate(self, profile: ProductProfile, answers: Iterable[Any],
                  evidence: Iterable[Any]) -> dict[str, Any]:
        """Vollständige, zustandslose Auswertung eines Eingabestands; fail-closed."""
        if not isinstance(profile, ProductProfile):
            raise InvalidInputError("profile", profile, "must be a ProductProfile")
        register = self._evidence.register(evidence)
        for reference in register.values():
            if reference.measure_key is not None:
                try:
                    self._repository.measure(reference.measure_key)
                except KeyError as exc:
                    raise InvalidInputError(f"evidence[{reference.evidence_id}].measure_key",
                                            reference.measure_key, "unknown measure") from exc
        rule_inputs, profile_inputs = self._split(profile)
        runs = tuple(self._rules.evaluate(entry, inputs) for entry, inputs in rule_inputs.items())
        decisions = [result for run in runs for result in run.decision_results]
        applicability = self._applicability.evaluate(decisions, profile_inputs)
        if [r.requirement_id for r in applicability.requirements] != list(self._views):
            raise UnexpectedEndStateError("APPLICABILITY_ENGINE",
                                          "applicability does not cover exactly the RR catalog")
        plans = {rr_id: MeasurePlan(view.measure.status,
                                    tuple(m.measure_key for m in view.measure.measures))
                 for rr_id, view in self._views.items()}
        states = {r.requirement_id: r.applicability for r in applicability.requirements}
        answer_list = [dataclasses.replace(a, stale=True)
                       if isinstance(a, GapAssessment) and not a.stale
                       and states.get(a.requirement_id, Applicability.APPLICABLE)
                       is not Applicability.APPLICABLE else a
                       for a in answers]
        gaps = self._gaps.evaluate(applicability.requirements, plans, answer_list, register)
        results = tuple(self._rr_result(requirement, gap, applicability)
                        for requirement, gap in zip(applicability.requirements, gaps))
        return {
            "profile": profile,
            "answers": tuple(sorted(answer_list, key=lambda a: a.requirement_id)),
            "evidence": tuple(register.values()),
            "runs": runs,
            "decisions": applicability.decision_results,
            "results": results,
        }

    def _rr_result(self, requirement: ApplicableRequirement, gap: GapResult,
                   applicability: ApplicabilityResult) -> RRResult:
        if gap.requirement_id != requirement.requirement_id:
            raise UnexpectedEndStateError(requirement.requirement_id, "gap result out of order")
        view = self._views[requirement.requirement_id]
        return RRResult(
            requirement_result_id=str(uuid.uuid5(
                ID_NAMESPACE, f"requirement-result:{requirement.applicable_requirement_id}:"
                              f"{fingerprint(gap)}")),
            requirement_id=requirement.requirement_id,
            title=view.title,
            requirement_text=view.requirement_text,
            theme_cluster=view.theme_cluster,
            lifecycle_phases=view.lifecycle_phases,
            applicability=requirement,
            explanation=self._applicability.explain(applicability, requirement.requirement_id),
            measure=view.measure,
            gap=gap,
        )

    def _assessment(self, assessment_id: str, revision: int, created_at: str,
                    state: AssessmentState, language: Language, evaluated: Mapping[str, Any],
                    change: AssessmentChange | None) -> Assessment:
        counts = count_results(evaluated["results"])
        if counts.total != self._repository.requirement_count or \
                sum(counts.gap_status.values()) != counts.total:
            raise UnexpectedEndStateError("GAP_ENGINE", "not exactly one gap status per RR")
        assessment = Assessment(
            assessment_id=assessment_id,
            revision=revision,
            created_at=created_at,
            state=state,
            language=language,
            catalog_versions=self._repository.versions,
            profile=evaluated["profile"],
            answers=evaluated["answers"],
            evidence=evaluated["evidence"],
            engine_runs=evaluated["runs"],
            decision_results=evaluated["decisions"],
            results=evaluated["results"],
            counts=counts,
            last_change=change,
            fingerprint="",
        )
        return dataclasses.replace(assessment, fingerprint=fingerprint(assessment))


_MISSING = object()
