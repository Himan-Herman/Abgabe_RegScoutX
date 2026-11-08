"""REPORTING: sprachneutrales Berichtsmodell (ReportModel) aus einer gespeicherten Revision.

Eingabe ist eine ReportSource aus reinen Werten, die der ASSESSMENT_SERVICE aus
einer gespeicherten und – bei gleichen Katalogversionen – verifizierten Revision
bildet. Der Builder berechnet keine Entscheidung, Anwendbarkeit oder Gap-Status
neu; er übernimmt gespeicherte Codes, bildet Summen und löst Katalogtexte auf.
Katalogtexte werden nur bei version_status MATCH aufgelöst, damit ein
historischer Stand nie mit Texten eines anderen Katalogstands vermischt wird.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Any, Iterable, Mapping

from regscoutx.catalog_repository import CatalogRepository
from regscoutx.domain import Language, LocalizedText, fingerprint
from regscoutx.errors import UnknownOutputError, UnknownRuleError
from regscoutx.requirement_service import RequirementService

REPORT_SCHEMA_VERSION = "1.0"
MATCH = "MATCH"
APPLICABLE, NOT_APPLICABLE, UNRESOLVED = "APPLICABLE", "NOT_APPLICABLE", "APPLICABILITY_UNRESOLVED"
GAP_STATUSES = ("FULFILLED", "PARTIALLY_FULFILLED", "NOT_FULFILLED", "NOT_ASSESSED",
                "EVIDENCE_REVIEW_REQUIRED", "NOT_APPLICABLE", "APPLICABILITY_UNRESOLVED")
OPEN_ITEMS = ("APPLICABILITY_UNRESOLVED", "ASSESSMENT_PENDING", "CONFIRMATION_REQUIRED",
              "EVIDENCE_REVIEW_REQUIRED", "GAP_TO_CLOSE", "MEASURE_MAPPING_REVIEW")


# Quelle ------------------------------------------------------------------

@dataclass(frozen=True)
class DecisionSource:
    area: str
    status: str
    outcome: str | None
    mdr_class: str | None
    applicable_from: str | None
    missing_input: tuple[str, str] | None
    rule_ids: tuple[str, ...]
    reviews: tuple[tuple[str, str, Any], ...] | None


@dataclass(frozen=True)
class RequirementSource:
    requirement_id: str
    applicability: str
    reason_code: str
    block: str | None
    evaluated_predicates: tuple[tuple[str, str], ...]
    relevant_inputs: tuple[tuple[str, Any], ...]
    supporting_rule_ids: tuple[str, ...]
    determined_by_areas: tuple[str, ...] | None
    theme: str
    lifecycle: tuple[str, ...]
    gap_status: str
    gap_reason: str
    is_gap: bool
    answer_state: str | None
    evidence_state: str
    evidence_ids: tuple[str, ...]
    measure_status: str
    measures: tuple[str, ...]


@dataclass(frozen=True)
class AnswerSource:
    requirement_id: str
    status: str
    justification: str | None
    evidence_ids: tuple[str, ...]
    stale: bool


@dataclass(frozen=True)
class EvidenceSource:
    evidence_id: str
    title: str
    document_identifier: str
    document_version: str | None
    location: str | None
    measure_key: str | None


@dataclass(frozen=True)
class RevisionSource:
    revision: int
    state: str
    origin: str
    based_on: int | None
    created_at: str
    updated_at: str
    catalog_versions: tuple[tuple[str, Any], ...]


@dataclass(frozen=True)
class ReportSource:
    """Gespeicherter Stand genau einer Revision als reine Werte."""

    assessment_id: str
    revision: int
    revision_count: int
    state: str
    origin: str
    based_on: int | None
    created_at: str
    updated_at: str
    catalog_versions: tuple[tuple[str, Any], ...]
    version_status: str
    fingerprint: str
    profile: tuple[tuple[str, Any], ...]
    answers: tuple[AnswerSource, ...]
    evidence: tuple[EvidenceSource, ...]
    decisions: tuple[DecisionSource, ...]
    requirements: tuple[RequirementSource, ...]
    counts: Mapping[str, Any]
    revisions: tuple[RevisionSource, ...]


# Modell ------------------------------------------------------------------

@dataclass(frozen=True)
class ReportMetadata:
    assessment_id: str
    revision: int
    revision_count: int
    superseded: bool
    state: str
    origin: str
    based_on: int | None
    created_at: str
    updated_at: str
    catalog_versions: tuple[tuple[str, Any], ...]
    version_status: str
    historical: bool
    assessment_fingerprint: str
    report_schema_version: str


@dataclass(frozen=True)
class ProfileEntry:
    key: str
    value: Any
    question: LocalizedText | None
    value_label: LocalizedText | None


@dataclass(frozen=True)
class RuleReference:
    rule_id: str
    primary_legal_anchor: tuple[str, ...] | None
    guidance_anchor: tuple[str, ...] | None


@dataclass(frozen=True)
class ReviewEntry:
    rule_id: str
    output: str
    cause: LocalizedText | None


@dataclass(frozen=True)
class DecisionEntry:
    area: str
    status: str
    outcome: str | None
    outcome_label: LocalizedText | None
    mdr_class: str | None
    applicable_from: str | None
    missing_input: tuple[str, str] | None
    missing_question: LocalizedText | None
    rules: tuple[RuleReference, ...]
    reviews: tuple[ReviewEntry, ...] | None


@dataclass(frozen=True)
class Counts:
    total: int
    applicable: int
    not_applicable: int
    unresolved: int
    fulfilled: int
    partially_fulfilled: int
    not_fulfilled: int
    not_assessed: int
    evidence_review_required: int
    gaps: int
    mapping_review_required: int
    answers_review_required: int


@dataclass(frozen=True)
class GroupEntry:
    key: str
    counts: Counts


@dataclass(frozen=True)
class MeasureReference:
    measure_key: str
    label: LocalizedText | None
    evidence_types: tuple[tuple[str, LocalizedText | None], ...]


@dataclass(frozen=True)
class RequirementEntry:
    requirement_id: str
    title: LocalizedText | None
    text: LocalizedText | None
    theme: str
    lifecycle: tuple[str, ...]
    primary_sources: tuple[str, ...] | None
    supplementary_sources: tuple[str, ...] | None
    applicability: str
    reason_code: str
    block: str | None
    block_description: LocalizedText | None
    evaluated_predicates: tuple[tuple[str, str], ...]
    relevant_inputs: tuple[tuple[str, Any], ...]
    supporting_rule_ids: tuple[str, ...]
    determined_by_areas: tuple[str, ...] | None
    gap_status: str
    gap_reason: str
    is_gap: bool
    answer_state: str | None
    answer_status: str | None
    justification: str | None
    evidence_state: str
    evidence_ids: tuple[str, ...]
    measure_status: str
    measures: tuple[MeasureReference, ...]
    open_items: tuple[str, ...]


@dataclass(frozen=True)
class MeasureOverview:
    measure: MeasureReference
    planned: int
    with_evidence: int


@dataclass(frozen=True)
class EvidenceEntry:
    evidence_id: str
    title: str
    document_identifier: str
    document_version: str | None
    location: str | None
    measure_key: str | None
    requirement_ids: tuple[str, ...]


@dataclass(frozen=True)
class SpineStage:
    stage: str
    value: int
    total: int | None


@dataclass(frozen=True)
class ReviewSummary:
    review_decisions: tuple[tuple[str, ReviewEntry], ...]
    incomplete_decisions: tuple[DecisionEntry, ...]
    unresolved_by_reason: tuple[tuple[str, int], ...]
    not_assessed: int
    reactivated: tuple[str, ...]
    evidence_review_required: tuple[str, ...]
    mapping_review_required: int


@dataclass(frozen=True)
class ReportModel:
    metadata: ReportMetadata
    profile: tuple[ProfileEntry, ...]
    decisions: tuple[DecisionEntry, ...]
    counts: Counts
    spine: tuple[SpineStage, ...]
    by_theme: tuple[GroupEntry, ...]
    by_lifecycle: tuple[GroupEntry, ...]
    requirements: tuple[RequirementEntry, ...]
    measures: tuple[MeasureOverview, ...]
    evidence: tuple[EvidenceEntry, ...]
    review: ReviewSummary
    revisions: tuple[RevisionSource, ...]

    @property
    def catalog_texts_available(self) -> bool:
        return not self.metadata.historical

    def content_hash(self, language: Language) -> str:
        """Fachlicher Inhalt je Sprache und Schemaversion; unabhängig von Format und Zeitpunkt."""
        return fingerprint({"model": self, "language": language.value,
                            "report_schema_version": REPORT_SCHEMA_VERSION})


def _counts(entries: Iterable[RequirementSource]) -> Counts:
    items = list(entries)
    applicability = Counter(r.applicability for r in items)
    gap = Counter(r.gap_status for r in items)
    return Counts(
        total=len(items), applicable=applicability[APPLICABLE],
        not_applicable=applicability[NOT_APPLICABLE], unresolved=applicability[UNRESOLVED],
        fulfilled=gap["FULFILLED"], partially_fulfilled=gap["PARTIALLY_FULFILLED"],
        not_fulfilled=gap["NOT_FULFILLED"], not_assessed=gap["NOT_ASSESSED"],
        evidence_review_required=gap["EVIDENCE_REVIEW_REQUIRED"],
        gaps=sum(1 for r in items if r.is_gap),
        mapping_review_required=sum(1 for r in items if r.applicability == APPLICABLE
                                    and r.measure_status == "REVIEW_REQUIRED"),
        answers_review_required=sum(1 for r in items
                                    if r.answer_state == "REACTIVATED_REVIEW_REQUIRED"))


def open_items(requirement: RequirementSource) -> tuple[str, ...]:
    """Offene Punkte als 1:1-Abbildung gespeicherter Zustände (keine neue Bewertung)."""
    items = []
    if requirement.applicability == UNRESOLVED:
        items.append("APPLICABILITY_UNRESOLVED")
    if requirement.applicability == APPLICABLE:
        if requirement.answer_state == "REACTIVATED_REVIEW_REQUIRED":
            items.append("CONFIRMATION_REQUIRED")
        elif requirement.gap_status == "NOT_ASSESSED":
            items.append("ASSESSMENT_PENDING")
        if requirement.gap_status == "EVIDENCE_REVIEW_REQUIRED":
            items.append("EVIDENCE_REVIEW_REQUIRED")
        if requirement.gap_status in ("PARTIALLY_FULFILLED", "NOT_FULFILLED"):
            items.append("GAP_TO_CLOSE")
        if requirement.measure_status == "REVIEW_REQUIRED":
            items.append("MEASURE_MAPPING_REVIEW")
    return tuple(items)


class ReportBuilder:
    """Bildet das ReportModel; Katalogzugriff ausschließlich für Texte und Verweise bei MATCH."""

    def __init__(self, catalogs: CatalogRepository) -> None:
        self._catalogs = catalogs
        self._requirements = RequirementService(catalogs)
        self._input_rules: dict[str, Mapping[str, Any]] = {}
        for rule_id in catalogs.rule_ids:
            rule = catalogs.rule(rule_id)
            self._input_rules.setdefault(rule["input_key"], rule)

    @staticmethod
    def _pair(value: Mapping[str, str] | None) -> LocalizedText | None:
        return None if value is None else LocalizedText(value["de"], value["en"])

    def _question(self, key: str) -> tuple[LocalizedText | None, Mapping[str, Any] | None]:
        spec = self._catalogs.applicability["profile_inputs"].get(key) or self._input_rules.get(key)
        if spec is None:
            return None, None
        return self._pair(spec["question"]), spec.get("value_labels")

    def _profile(self, source: ReportSource, texts: bool) -> tuple[ProfileEntry, ...]:
        entries = []
        for key, value in source.profile:
            question, labels = self._question(key) if texts else (None, None)
            label = labels.get(value) if labels and isinstance(value, str) else None
            entries.append(ProfileEntry(key, value, question, self._pair(label)))
        return tuple(entries)

    def _rule(self, rule_id: str, texts: bool) -> RuleReference:
        if not texts:
            return RuleReference(rule_id, None, None)
        rule = self._catalogs.rule(rule_id)
        return RuleReference(rule_id, tuple(rule["primary_legal_anchor"]),
                             tuple(rule["guidance_anchor"]))

    def _decision(self, decision: DecisionSource, texts: bool) -> DecisionEntry:
        outcome_label = None
        reviews = None
        missing_question = None
        if texts:
            if decision.outcome is not None:
                outcome_label = LocalizedText(
                    self._catalogs.output_label(decision.outcome, Language.DE),
                    self._catalogs.output_label(decision.outcome, Language.EN))
            if decision.missing_input is not None:
                missing_question, _ = self._question(decision.missing_input[1])
        if decision.reviews is not None:
            reviews = tuple(
                ReviewEntry(rule_id, output, LocalizedText(
                    self._catalogs.review_cause(rule_id, condition, Language.DE),
                    self._catalogs.review_cause(rule_id, condition, Language.EN)) if texts else None)
                for rule_id, output, condition in decision.reviews)
        return DecisionEntry(decision.area, decision.status, decision.outcome, outcome_label,
                             decision.mdr_class, decision.applicable_from, decision.missing_input,
                             missing_question, tuple(self._rule(r, texts) for r in decision.rule_ids),
                             reviews)

    def _measure(self, key: str, texts: bool) -> MeasureReference:
        if not texts:
            return MeasureReference(key, None, ())
        measure = self._catalogs.measure(key)
        return MeasureReference(key, self._pair(measure["label"]), tuple(
            (evidence, self._pair(self._catalogs.evidence_type(evidence)["label"]))
            for evidence in measure["evidence_types"]))

    def _requirement(self, source: RequirementSource, answers: Mapping[str, AnswerSource],
                     texts: bool) -> RequirementEntry:
        title = text = primary = supplementary = block_description = None
        if texts:
            de = self._requirements.view(source.requirement_id, Language.DE)
            en = self._requirements.view(source.requirement_id, Language.EN)
            title, text = LocalizedText(de.title, en.title), LocalizedText(de.text, en.text)
            primary, supplementary = de.primary_sources, de.supplementary_sources
            if source.block is not None:
                block_description = self._pair(
                    self._catalogs.applicability["blocks"][source.block]["description"])
        answer = answers.get(source.requirement_id)
        return RequirementEntry(
            requirement_id=source.requirement_id, title=title, text=text, theme=source.theme,
            lifecycle=source.lifecycle, primary_sources=primary, supplementary_sources=supplementary,
            applicability=source.applicability, reason_code=source.reason_code, block=source.block,
            block_description=block_description,
            evaluated_predicates=source.evaluated_predicates,
            relevant_inputs=source.relevant_inputs, supporting_rule_ids=source.supporting_rule_ids,
            determined_by_areas=source.determined_by_areas, gap_status=source.gap_status,
            gap_reason=source.gap_reason, is_gap=source.is_gap, answer_state=source.answer_state,
            answer_status=None if answer is None else answer.status,
            justification=None if answer is None else answer.justification,
            evidence_state=source.evidence_state, evidence_ids=source.evidence_ids,
            measure_status=source.measure_status,
            measures=tuple(self._measure(key, texts) for key in source.measures),
            open_items=open_items(source))

    def build(self, source: ReportSource) -> ReportModel:
        texts = source.version_status == MATCH
        answers = {a.requirement_id: a for a in source.answers}
        try:
            decisions = tuple(self._decision(d, texts) for d in source.decisions)
            requirements = tuple(self._requirement(r, answers, texts) for r in source.requirements)
            measure_keys = sorted({m for r in source.requirements if r.applicability == APPLICABLE
                                   for m in r.measures})
            measures = tuple(self._measure(key, texts) for key in measure_keys)
        except (KeyError, UnknownOutputError, UnknownRuleError) as exc:
            raise ValueError(f"catalog content for report not resolvable: {exc!r}") from exc

        evidence_measure = {e.evidence_id: e.measure_key for e in source.evidence}
        overview = tuple(MeasureOverview(
            measure,
            planned=sum(1 for r in source.requirements
                        if r.applicability == APPLICABLE and measure.measure_key in r.measures),
            with_evidence=sum(1 for r in source.requirements
                              if r.applicability == APPLICABLE and measure.measure_key in r.measures
                              and any(evidence_measure.get(e) == measure.measure_key
                                      for e in r.evidence_ids)))
            for measure in measures)
        linked: dict[str, list[str]] = {}
        for answer in source.answers:
            for evidence_id in answer.evidence_ids:
                linked.setdefault(evidence_id, []).append(answer.requirement_id)
        # Reihenfolge nach Inhalt statt nach vergebener Kennung: gleiche Eingaben ergeben unabhängig
        # von (zufälligen) Nachweiskennungen denselben Bericht (Befund F-2 der Evaluation, Block 6).
        ordered = sorted(source.evidence, key=lambda e: (
            tuple(sorted(linked.get(e.evidence_id, ()))), e.document_identifier, e.title,
            e.document_version or "", e.location or "", e.measure_key or "", e.evidence_id))
        evidence = tuple(EvidenceEntry(e.evidence_id, e.title, e.document_identifier,
                                       e.document_version, e.location, e.measure_key,
                                       tuple(sorted(linked.get(e.evidence_id, ()))))
                         for e in ordered)

        themes = self._catalogs.theme_clusters
        phases = self._catalogs.lifecycle_phases
        present_themes = [t for t in themes if any(r.theme == t for r in source.requirements)]
        present_themes += sorted({r.theme for r in source.requirements} - set(themes))
        present_phases = [p for p in phases if any(p in r.lifecycle for r in source.requirements)]
        present_phases += sorted({p for r in source.requirements for p in r.lifecycle} - set(phases))
        counts = _counts(source.requirements)
        self._check_counts(counts, source.counts)
        unresolved = Counter(r.reason_code for r in source.requirements
                             if r.applicability == UNRESOLVED)
        review = ReviewSummary(
            review_decisions=tuple((d.area, review) for d in decisions for review in d.reviews or ()),
            incomplete_decisions=tuple(d for d in decisions if d.missing_input is not None),
            unresolved_by_reason=tuple(sorted(unresolved.items(), key=lambda i: (-i[1], i[0]))),
            not_assessed=counts.not_assessed,
            reactivated=tuple(r.requirement_id for r in source.requirements
                              if r.answer_state == "REACTIVATED_REVIEW_REQUIRED"),
            evidence_review_required=tuple(r.requirement_id for r in source.requirements
                                           if r.gap_status == "EVIDENCE_REVIEW_REQUIRED"),
            mapping_review_required=counts.mapping_review_required,
        )
        historical = source.version_status != MATCH
        return ReportModel(
            metadata=ReportMetadata(
                assessment_id=source.assessment_id, revision=source.revision,
                revision_count=source.revision_count,
                superseded=source.revision < source.revision_count, state=source.state,
                origin=source.origin, based_on=source.based_on, created_at=source.created_at,
                updated_at=source.updated_at, catalog_versions=source.catalog_versions,
                version_status=source.version_status, historical=historical,
                assessment_fingerprint=source.fingerprint,
                report_schema_version=REPORT_SCHEMA_VERSION),
            profile=self._profile(source, texts),
            decisions=decisions,
            counts=counts,
            spine=(SpineStage("PROFILE", len(source.profile), None),
                   SpineStage("APPLICABILITY", counts.applicable, counts.total),
                   SpineStage("REQUIREMENTS", counts.applicable + counts.unresolved, counts.total),
                   SpineStage("GAP", counts.gaps, counts.applicable),
                   SpineStage("EVIDENCE", sum(1 for r in source.requirements if r.evidence_ids),
                              counts.applicable),
                   SpineStage("REPORT", source.revision, source.revision_count)),
            by_theme=tuple(GroupEntry(t, _counts(r for r in source.requirements if r.theme == t))
                           for t in present_themes),
            by_lifecycle=tuple(GroupEntry(p, _counts(r for r in source.requirements
                                                     if p in r.lifecycle))
                               for p in present_phases),
            requirements=requirements,
            measures=overview,
            evidence=evidence,
            review=review,
            revisions=source.revisions,
        )

    @staticmethod
    def _check_counts(counts: Counts, stored: Mapping[str, Any]) -> None:
        """Gespeicherte Summen müssen den gespeicherten Einzelergebnissen entsprechen (fail-closed)."""
        if not stored:
            return
        expected = (stored["total"], stored["applicability"][APPLICABLE],
                    stored["applicability"][NOT_APPLICABLE], stored["applicability"][UNRESOLVED],
                    stored["gaps"])
        actual = (counts.total, counts.applicable, counts.not_applicable, counts.unresolved,
                  counts.gaps)
        if expected != actual:
            raise ValueError("stored counts do not match stored requirement results")
