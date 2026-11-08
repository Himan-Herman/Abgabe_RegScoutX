"""Anwendungseinstieg des ASSESSMENT_SERVICE: Lebenszyklus, Revisionen, Versionsabgleich und Audit.

Einziger Zugang späterer Adapter (API, Oberfläche) zu Bewertungen. Orchestriert
AssessmentService (Auswertung), EvidenceService (Nachweisreferenzen), AUDIT_LOG
und eine AssessmentRepository-Schnittstelle; keine regulatorische Logik.

Semantik (ARCHITECTURE.md Abschnitt 8, ADR-0005):
- Eine Bewertung besteht aus fortlaufenden Revisionen; nur die letzte ist
  änderbar und nur im Zustand DRAFT. FINALISED ist unveränderlich; reopen
  erzeugt eine neue DRAFT-Revision.
- Beim Öffnen wird das CatalogVersionSet der letzten Revision mit dem geladenen
  verglichen: MATCH erlaubt alle Operationen; MISMATCH und
  INCOMPLETE_VERSION_INFO erlauben nur Lesen des gespeicherten Stands und werden
  protokolliert; eine Neubewertung mit dem aktuellen Stand ist nur bei MISMATCH
  und nur als neue Revision (rebase) möglich.
- Jede Änderung wertet vollständig neu aus und wird im nur anhängenden
  Audit-Protokoll mit Codes, Schlüsseln und Kennungen (ohne Freitexte) erfasst.
"""

from __future__ import annotations

import dataclasses
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Callable, Mapping

from regscoutx.assessment_codec import (
    VERSION_FIELDS,
    RevisionOrigin,
    StoredRevision,
    event_record,
    parse_event,
    parse_revision,
    revision_record,
    with_state,
)
from regscoutx.assessment_repository import FORMAT, FORMAT_VERSION, AssessmentRepository
from regscoutx.assessment_service import (
    Assessment,
    AssessmentChange,
    AssessmentInput,
    AssessmentService,
    AssessmentState,
    AssessmentSummary,
    ProductProfile,
    compute_change,
    input_snapshot,
    result_snapshot,
)
from regscoutx.audit_log import AuditEventType, AuditLog
from regscoutx.catalog_repository import CatalogRepository
from regscoutx.domain import Applicability, Language
from regscoutx.errors import (
    AssessmentStateError,
    InvalidInputError,
    PersistenceError,
    ReportGenerationError,
)
from regscoutx.evidence_service import EvidenceReference, EvidenceService
from regscoutx.gap_engine import GapAssessment, GapStatus
from regscoutx.report_model import (
    AnswerSource,
    DecisionSource,
    EvidenceSource,
    ReportModel,
    ReportSource,
    RequirementSource,
    RevisionSource,
)
from regscoutx.report_document import ReportDocument
from regscoutx.report_service import ReportArtifact, ReportFormat, ReportService

Event = tuple[AuditEventType, str | None, Mapping[str, Any]]


class VersionStatus(Enum):
    MATCH = "MATCH"
    MISMATCH = "MISMATCH"
    INCOMPLETE_VERSION_INFO = "INCOMPLETE_VERSION_INFO"


@dataclass(frozen=True)
class OpenedAssessment:
    """Geöffnete Bewertung: gespeicherte letzte Revision, Versionsabgleich und – nur bei MATCH – Auswertung."""

    assessment_id: str
    stored: StoredRevision
    revision_count: int
    version_status: VersionStatus
    assessment: Assessment | None

    @property
    def state(self) -> AssessmentState:
        return self.stored.state

    @property
    def writable(self) -> bool:
        return self.version_status is VersionStatus.MATCH and self.state is AssessmentState.DRAFT


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _change_details(change: AssessmentChange | None) -> dict[str, Any]:
    if change is None:
        return {}
    return {"changed_inputs": list(change.changed_inputs),
            "applicability_changes": len(change.applicability_changes),
            "gap_status_changes": len(change.gap_status_changes),
            "deactivated_answers": list(change.deactivated_answers),
            "reactivated_answers": list(change.reactivated_answers),
            "removed_evidence": list(change.removed_evidence)}


class AssessmentApplicationService:

    def __init__(self, catalogs: CatalogRepository, store: AssessmentRepository,
                 clock: Callable[[], str] = _utc_now) -> None:
        self._catalogs = catalogs
        self._store = store
        self._clock = clock
        self._service = AssessmentService(catalogs)
        self._evidence = EvidenceService()
        self._reports = ReportService(catalogs)

    # Laden und Versionsabgleich -------------------------------------------

    def _document(self, assessment_id: str) -> tuple[Mapping[str, Any], tuple[StoredRevision, ...],
                                                     AuditLog]:
        document = self._store.load(assessment_id)
        revisions = tuple(parse_revision(assessment_id, r) for r in document["revisions"])
        log = AuditLog(tuple(parse_event(assessment_id, e) for e in document["audit"]))
        return document, revisions, log

    def _version_status(self, revision: StoredRevision) -> VersionStatus:
        stored = revision.catalog_versions
        if set(stored) != set(VERSION_FIELDS) or any(
                not isinstance(value, str) or not value for value in stored.values()):
            return VersionStatus.INCOMPLETE_VERSION_INFO
        if dict(stored) == dict(vars(self._catalogs.versions)):
            return VersionStatus.MATCH
        return VersionStatus.MISMATCH

    def _restore(self, assessment_id: str, revision: StoredRevision) -> Assessment:
        """Auswertung aus den gespeicherten Eingaben; Abweichung vom gespeicherten Ergebnis ist fail-closed."""
        assessment = self._service.create(
            revision.inputs, assessment_id=assessment_id, created_at=revision.created_at,
            language=revision.language, revision=revision.revision, state=revision.state)
        if assessment.fingerprint != revision.fingerprint or \
                result_snapshot(assessment) != dict(revision.results):
            raise PersistenceError(assessment_id, f"revision {revision.revision} does not reproduce "
                                                  "its stored result")
        return assessment

    def check_versions(self, assessment_id: str) -> VersionStatus:
        _, revisions, _ = self._document(assessment_id)
        return self._version_status(revisions[-1])

    def read(self, assessment_id: str) -> OpenedAssessment:
        """Wie open, aber ohne Audit-Eintrag; für wiederholte Abfragen einer bereits geöffneten Bewertung."""
        _, revisions, _ = self._document(assessment_id)
        current = revisions[-1]
        status = self._version_status(current)
        assessment = self._restore(assessment_id, current) if status is VersionStatus.MATCH else None
        return OpenedAssessment(assessment_id, current, len(revisions), status, assessment)

    def assessment_ids(self) -> tuple[str, ...]:
        return self._store.assessment_ids()

    def open(self, assessment_id: str) -> OpenedAssessment:
        """Bewertung öffnen; eine Versionsabweichung wird protokolliert, nie still übernommen (SR-037)."""
        document, revisions, log = self._document(assessment_id)
        current = revisions[-1]
        status = self._version_status(current)
        if status is VersionStatus.MATCH:
            return OpenedAssessment(assessment_id, current, len(revisions), status,
                                    self._restore(assessment_id, current))
        log = log.append(assessment_id, current.revision, self._clock(),
                         AuditEventType.CATALOG_VERSION_MISMATCH_DETECTED, None,
                         self._catalogs.versions,
                         {"version_status": status.value,
                          "stored": dict(current.catalog_versions),
                          "loaded": dict(vars(self._catalogs.versions))})
        self._save(document, document["revisions"], log)
        return OpenedAssessment(assessment_id, current, len(revisions), status, None)

    def revisions(self, assessment_id: str) -> tuple[StoredRevision, ...]:
        return self._document(assessment_id)[1]

    def audit_log(self, assessment_id: str) -> AuditLog:
        return self._document(assessment_id)[2]

    def summary(self, assessment_id: str) -> AssessmentSummary:
        opened = self.open(assessment_id)
        if opened.assessment is None:
            raise AssessmentStateError(assessment_id, "summary", opened.version_status.value)
        return self._service.summarize(opened.assessment)

    def evidence(self, assessment_id: str, *, requirement_id: str | None = None,
                 measure_key: str | None = None) -> tuple[EvidenceReference, ...]:
        """Nachweisreferenzen der letzten Revision, optional nach RR bzw. Maßnahme gefiltert."""
        inputs = self.revisions(assessment_id)[-1].inputs
        register = self._evidence.register(inputs.evidence)
        items = (self._evidence.by_measure(register, measure_key) if measure_key is not None
                 else tuple(register.values()))
        if requirement_id is not None:
            linked = {e for a in inputs.answers if a.requirement_id == requirement_id
                      for e in a.evidence_ids}
            items = tuple(item for item in items if item.evidence_id in linked)
        return items

    # Schreiben ------------------------------------------------------------

    def _save(self, document: Mapping[str, Any], revisions: list[Any], log: AuditLog) -> None:
        self._store.save({
            "format": FORMAT, "format_version": FORMAT_VERSION,
            "assessment_id": document["assessment_id"], "created_at": document["created_at"],
            "revisions": list(revisions), "audit": [event_record(e) for e in log.events],
        })

    def _append(self, log: AuditLog, assessment: Assessment, now: str,
                events: list[Event]) -> AuditLog:
        for event_type, subject, details in events:
            log = log.append(assessment.assessment_id, assessment.revision, now, event_type,
                             subject, self._catalogs.versions, details)
        return log

    @staticmethod
    def _evaluation_events(assessment: Assessment) -> list[Event]:
        return ([(AuditEventType.RULES_EXECUTED, run.entry_rule, {"rule_path": list(run.rule_path)})
                 for run in assessment.engine_runs]
                + [(AuditEventType.APPLICABILITY_DETERMINED, None,
                    dict(assessment.counts.applicability))])

    def create(self, data: AssessmentInput, *, language: Language = Language.DE,
               assessment_id: str | None = None) -> OpenedAssessment:
        now = self._clock()
        assessment = self._service.create(data, assessment_id=assessment_id, created_at=now,
                                          language=language)
        if self._store.exists(assessment.assessment_id):
            raise InvalidInputError("assessment_id", assessment.assessment_id, "already exists")
        events: list[Event] = [
            (AuditEventType.ASSESSMENT_CREATED, assessment.assessment_id, {}),
            (AuditEventType.REVISION_CREATED, "1", {"origin": RevisionOrigin.CREATED.value}),
        ]
        events += [(AuditEventType.INPUT_RECORDED, key, {"after": value})
                   for key, value in assessment.profile.answers]
        events += [(AuditEventType.EVIDENCE_LINKED, e.evidence_id, {"measure_key": e.measure_key})
                   for e in assessment.evidence]
        events += [(AuditEventType.GAP_STATUS_SET, a.requirement_id, {"status": a.status.value})
                   for a in assessment.answers]
        events += self._evaluation_events(assessment)
        log = self._append(AuditLog(), assessment, now, events)
        record = revision_record(assessment, RevisionOrigin.CREATED, None, now, None)
        self._save({"assessment_id": assessment.assessment_id, "created_at": now}, [record], log)
        return OpenedAssessment(assessment.assessment_id, parse_revision(assessment.assessment_id,
                                                                         record),
                                1, VersionStatus.MATCH, assessment)

    def _writable(self, assessment_id: str, operation: str):
        document, revisions, log = self._document(assessment_id)
        current = revisions[-1]
        status = self._version_status(current)
        if status is not VersionStatus.MATCH:
            raise AssessmentStateError(assessment_id, operation, f"catalog versions {status.value}")
        if current.state is not AssessmentState.DRAFT:
            raise AssessmentStateError(assessment_id, operation,
                                       f"revision {current.revision} is {current.state.value}")
        return document, revisions, log, self._restore(assessment_id, current)

    def _mutate(self, assessment_id: str, operation: str,
                apply: Callable[[Assessment], tuple[Assessment, list[Event]]]) -> OpenedAssessment:
        document, revisions, log, current = self._writable(assessment_id, operation)
        updated, events = apply(current)
        now = self._clock()
        events += self._evaluation_events(updated)
        events.append((AuditEventType.ASSESSMENT_RECALCULATED, None,
                       _change_details(updated.last_change)))
        log = self._append(log, updated, now, events)
        stored = revisions[-1]
        record = revision_record(updated, stored.origin, stored.based_on, now, updated.last_change)
        self._save(document, [*document["revisions"][:-1], record], log)
        return OpenedAssessment(assessment_id, parse_revision(assessment_id, record),
                                len(revisions), VersionStatus.MATCH, updated)

    def update_profile(self, assessment_id: str, profile: Mapping[str, Any]) -> OpenedAssessment:
        new_profile = ProductProfile.of(profile)

        def apply(current: Assessment):
            updated = self._service.recalculate(current, profile=new_profile)
            old, new = current.profile.as_dict(), new_profile.as_dict()
            return updated, [(AuditEventType.INPUT_RECORDED, key,
                              {"before": old.get(key), "after": new.get(key)})
                             for key in updated.last_change.changed_inputs]
        return self._mutate(assessment_id, "update_profile", apply)

    def recalculate(self, assessment_id: str) -> OpenedAssessment:
        return self._mutate(assessment_id, "recalculate",
                            lambda current: (self._service.recalculate(current), []))

    def _answer_event(self, current: Assessment, answer: GapAssessment, reason: str) -> Event:
        previous = next((a for a in current.answers if a.requirement_id == answer.requirement_id),
                        None)
        event_type = (AuditEventType.GAP_STATUS_SET if previous is None
                      else AuditEventType.GAP_STATUS_CHANGED)
        return (event_type, answer.requirement_id,
                {"reason": reason, "status_before": None if previous is None
                 else previous.status.value, "status_after": answer.status.value,
                 "evidence_count": len(answer.evidence_ids)})

    def set_gap_assessment(self, assessment_id: str, answer: GapAssessment) -> OpenedAssessment:
        """Erfüllungsbewertung einer RR setzen oder ändern; stale setzt ausschließlich das System."""
        if not isinstance(answer, GapAssessment) or answer.stale is not False:
            raise InvalidInputError("answer", answer, "must be a GapAssessment with stale=False")

        def apply(current: Assessment):
            event = self._answer_event(current, answer, "SET")
            return self._service.recalculate(current, answers=(answer,)), [event]
        return self._mutate(assessment_id, "set_gap_assessment", apply)

    def confirm_gap_assessment(self, assessment_id: str, requirement_id: str) -> OpenedAssessment:
        """Wieder anwendbare, veraltete Bewertung bewusst bestätigen (REACTIVATED_REVIEW_REQUIRED → ACTIVE)."""
        def apply(current: Assessment):
            answer = next((a for a in current.answers if a.requirement_id == requirement_id), None)
            if answer is None or not answer.stale:
                raise InvalidInputError("requirement_id", requirement_id,
                                        "no stale gap assessment to confirm")
            if current.result(requirement_id).applicability.applicability is not \
                    Applicability.APPLICABLE:
                raise InvalidInputError("requirement_id", requirement_id,
                                        "requirement is not applicable; nothing to confirm")
            confirmed = dataclasses.replace(answer, stale=False)
            event = self._answer_event(current, confirmed, "CONFIRMED")
            return self._service.recalculate(current, answers=(confirmed,)), [event]
        return self._mutate(assessment_id, "confirm_gap_assessment", apply)

    def add_evidence(self, assessment_id: str, reference: EvidenceReference) -> OpenedAssessment:
        def apply(current: Assessment):
            register = self._evidence.register(current.evidence)
            self._evidence.add(register, reference)
            return (self._service.recalculate(current, evidence=(reference,)),
                    [(AuditEventType.EVIDENCE_LINKED, reference.evidence_id,
                      {"measure_key": reference.measure_key})])
        return self._mutate(assessment_id, "add_evidence", apply)

    def update_evidence(self, assessment_id: str, reference: EvidenceReference) -> OpenedAssessment:
        def apply(current: Assessment):
            register = self._evidence.register(current.evidence)
            before = self._evidence.get(register, getattr(reference, "evidence_id", None))
            self._evidence.update(register, reference)
            return (self._service.recalculate(current, evidence=(reference,)),
                    [(AuditEventType.EVIDENCE_UPDATED, reference.evidence_id,
                      {"fields": list(self._evidence.changed_fields(before, reference))})])
        return self._mutate(assessment_id, "update_evidence", apply)

    def remove_evidence(self, assessment_id: str, evidence_id: str) -> OpenedAssessment:
        def apply(current: Assessment):
            users = [a.requirement_id for a in current.answers if evidence_id in a.evidence_ids]
            self._evidence.remove(self._evidence.register(current.evidence), evidence_id, users)
            return (self._service.recalculate(current, remove_evidence=(evidence_id,)),
                    [(AuditEventType.EVIDENCE_REMOVED, evidence_id, {})])
        return self._mutate(assessment_id, "remove_evidence", apply)

    def _relink(self, assessment_id: str, requirement_id: str, evidence_id: str,
                link: bool) -> OpenedAssessment:
        operation = "link_evidence" if link else "unlink_evidence"

        def apply(current: Assessment):
            self._evidence.get(self._evidence.register(current.evidence), evidence_id)
            answer = next((a for a in current.answers if a.requirement_id == requirement_id),
                          None) or GapAssessment(requirement_id, GapStatus.NOT_ASSESSED)
            present = evidence_id in answer.evidence_ids
            if present is link:
                raise InvalidInputError("evidence_id", evidence_id,
                                        "already linked" if link else "not linked")
            ids = (answer.evidence_ids + (evidence_id,) if link
                   else tuple(e for e in answer.evidence_ids if e != evidence_id))
            updated_answer = dataclasses.replace(answer, evidence_ids=ids)
            event = self._answer_event(current, updated_answer,
                                       "EVIDENCE_LINKED" if link else "EVIDENCE_UNLINKED")
            return self._service.recalculate(current, answers=(updated_answer,)), [event]
        return self._mutate(assessment_id, operation, apply)

    def link_evidence(self, assessment_id: str, requirement_id: str,
                      evidence_id: str) -> OpenedAssessment:
        """Nachweisreferenz einer RR zuordnen (über deren GapAssessment; ohne Bewertung NOT_ASSESSED)."""
        return self._relink(assessment_id, requirement_id, evidence_id, True)

    def unlink_evidence(self, assessment_id: str, requirement_id: str,
                        evidence_id: str) -> OpenedAssessment:
        return self._relink(assessment_id, requirement_id, evidence_id, False)

    # Lebenszyklus und Revisionen ------------------------------------------

    def finalise(self, assessment_id: str) -> OpenedAssessment:
        """DRAFT → FINALISED; nicht bei unbestätigten reaktivierten Bewertungen."""
        document, revisions, log, current = self._writable(assessment_id, "finalise")
        if current.counts.answers_review_required:
            raise AssessmentStateError(assessment_id, "finalise",
                                       f"{current.counts.answers_review_required} reactivated "
                                       "gap assessment(s) need confirmation")
        now = self._clock()
        finalised = dataclasses.replace(current, state=AssessmentState.FINALISED)
        record = with_state(document["revisions"][-1], AssessmentState.FINALISED, now)
        log = self._append(log, finalised, now, [(AuditEventType.ASSESSMENT_FINALISED, None,
                                                  {"fingerprint": current.fingerprint})])
        self._save(document, [*document["revisions"][:-1], record], log)
        return OpenedAssessment(assessment_id, parse_revision(assessment_id, record),
                                len(revisions), VersionStatus.MATCH, finalised)

    def _new_revision(self, assessment_id: str, document: Mapping[str, Any],
                      revisions: tuple[StoredRevision, ...], log: AuditLog,
                      origin: RevisionOrigin, events: list[Event]) -> OpenedAssessment:
        previous = revisions[-1]
        now = self._clock()
        assessment = self._service.create(previous.inputs, assessment_id=assessment_id,
                                          created_at=now, language=previous.language,
                                          revision=previous.revision + 1)
        change = compute_change(previous.input_snapshot, previous.results,
                                input_snapshot(assessment), result_snapshot(assessment))
        assessment = dataclasses.replace(assessment, last_change=change)
        events = [*events, (AuditEventType.REVISION_CREATED, str(assessment.revision),
                            {"origin": origin.value, "based_on": previous.revision})]
        events += self._evaluation_events(assessment)
        events.append((AuditEventType.ASSESSMENT_RECALCULATED, None, _change_details(change)))
        log = self._append(log, assessment, now, events)
        record = revision_record(assessment, origin, previous.revision, now, change)
        self._save(document, [*document["revisions"], record], log)
        return OpenedAssessment(assessment_id, parse_revision(assessment_id, record),
                                len(revisions) + 1, VersionStatus.MATCH, assessment)

    def reopen(self, assessment_id: str) -> OpenedAssessment:
        """FINALISED bleibt unverändert; es entsteht eine neue DRAFT-Revision mit denselben Eingaben."""
        document, revisions, log = self._document(assessment_id)
        current = revisions[-1]
        status = self._version_status(current)
        if status is not VersionStatus.MATCH:
            raise AssessmentStateError(assessment_id, "reopen", f"catalog versions {status.value}")
        if current.state is not AssessmentState.FINALISED:
            raise AssessmentStateError(assessment_id, "reopen", "only FINALISED can be reopened")
        self._restore(assessment_id, current)
        return self._new_revision(assessment_id, document, revisions, log, RevisionOrigin.REOPENED,
                                  [(AuditEventType.ASSESSMENT_REOPENED, str(current.revision), {})])

    def rebase(self, assessment_id: str) -> OpenedAssessment:
        """Bewusste Neubewertung mit dem aktuellen Katalogstand als neue Revision (nur bei MISMATCH).

        Die bisherige Revision bleibt unverändert lesbar; regulatorische
        Entscheidungen werden nicht migriert, sondern vollständig neu bestimmt.
        """
        document, revisions, log = self._document(assessment_id)
        status = self._version_status(revisions[-1])
        if status is not VersionStatus.MISMATCH:
            raise AssessmentStateError(assessment_id, "rebase", f"catalog versions {status.value}")
        return self._new_revision(assessment_id, document, revisions, log,
                                  RevisionOrigin.CATALOG_REBASE, [])

    # Bericht --------------------------------------------------------------

    @staticmethod
    def _report_source(assessment_id: str, revision: StoredRevision,
                       revisions: tuple[StoredRevision, ...], status: VersionStatus,
                       assessment: Assessment | None) -> ReportSource:
        """Gespeicherte Revision als reine Werte; Zusatzangaben nur aus der verifizierten Auswertung (MATCH)."""
        results = revision.results
        reviews = determined = None
        if assessment is not None:
            reviews = [tuple((r.rule_id, r.output, r.matched_condition) for r in d.reviews)
                       for d in assessment.decision_results]
            determined = [tuple(d.area for d in r.explanation.decisions) for r in assessment.results]
        return ReportSource(
            assessment_id=assessment_id, revision=revision.revision, revision_count=len(revisions),
            state=revision.state.value, origin=revision.origin.value, based_on=revision.based_on,
            created_at=revision.created_at, updated_at=revision.updated_at,
            catalog_versions=tuple(revision.catalog_versions.items()),
            version_status=status.value, fingerprint=revision.fingerprint,
            profile=revision.inputs.profile.answers,
            answers=tuple(AnswerSource(a.requirement_id, a.status.value, a.justification,
                                       a.evidence_ids, a.stale) for a in revision.inputs.answers),
            evidence=tuple(EvidenceSource(e.evidence_id, e.title, e.document_identifier,
                                          e.document_version, e.location, e.measure_key)
                           for e in revision.inputs.evidence),
            decisions=tuple(DecisionSource(
                d["area"], d["status"], d["outcome"], d["mdr_class"], d["applicable_from"],
                None if d["missing_input"] is None else tuple(d["missing_input"]),
                tuple(d["rule_ids"]), None if reviews is None else reviews[i])
                for i, d in enumerate(results["decisions"])),
            requirements=tuple(RequirementSource(
                requirement_id=r["requirement_id"], applicability=r["applicability"],
                reason_code=r["reason_code"], block=r["block"],
                evaluated_predicates=tuple(tuple(p) for p in r["evaluated_predicates"]),
                relevant_inputs=tuple(tuple(i) for i in r["relevant_inputs"]),
                supporting_rule_ids=tuple(r["supporting_rule_ids"]),
                determined_by_areas=None if determined is None else determined[i],
                theme=r["theme_cluster"], lifecycle=tuple(r["lifecycle_phases"]),
                gap_status=r["gap_status"], gap_reason=r["gap_reason"], is_gap=r["gap"],
                answer_state=r["answer_state"], evidence_state=r["evidence_state"],
                evidence_ids=tuple(r["evidence_ids"]), measure_status=r["measure_status"],
                measures=tuple(r["measures"]))
                for i, r in enumerate(results["requirements"])),
            counts=results["counts"],
            revisions=tuple(RevisionSource(r.revision, r.state.value, r.origin.value, r.based_on,
                                           r.created_at, r.updated_at,
                                           tuple(r.catalog_versions.items()))
                            for r in revisions),
        )

    def _report_input(self, assessment_id: str, revision: int | None):
        document, revisions, log = self._document(assessment_id)
        number = len(revisions) if revision is None else revision
        if not isinstance(number, int) or isinstance(number, bool) or not 1 <= number <= len(revisions):
            raise InvalidInputError("revision", revision, "unknown revision")
        stored = revisions[number - 1]
        status = self._version_status(stored)
        assessment = self._restore(assessment_id, stored) if status is VersionStatus.MATCH else None
        source = self._report_source(assessment_id, stored, revisions, status, assessment)
        return document, log, number, status, source

    def report_model(self, assessment_id: str, revision: int | None = None) -> ReportModel:
        """Sprachneutrales Berichtsmodell einer gespeicherten Revision (lesend, ohne Audit)."""
        return self._reports.model(self._report_input(assessment_id, revision)[4])

    def report_document(self, assessment_id: str, language: Language,
                        revision: int | None = None) -> ReportDocument:
        """Formatneutrales Berichtsdokument für die Web-Ansicht (lesend, ohne Audit; keine zweite Berichtslogik)."""
        model = self.report_model(assessment_id, revision)
        return self._reports.document(model, language, self._clock())

    def create_report(self, assessment_id: str, *, language: Language = Language.DE,
                      report_format: ReportFormat = ReportFormat.HTML,
                      revision: int | None = None) -> ReportArtifact:
        """Bericht einer gespeicherten Revision (Standard: letzte) erzeugen und REPORT_CREATED protokollieren.

        Der Bericht berechnet nichts neu. Bei MATCH wird die Revision vorher gegen
        eine Neuauswertung geprüft; bei MISMATCH oder unvollständigen Versionsangaben
        entsteht ein als historisch gekennzeichneter Bericht aus den gespeicherten
        Codes. Ein Fehler bei der Erzeugung ändert weder Bewertung noch Audit.
        """
        if not isinstance(language, Language):
            raise InvalidInputError("language", language, "must be a Language")
        if not isinstance(report_format, ReportFormat):
            raise InvalidInputError("report_format", report_format, "must be a ReportFormat")
        document, log, number, status, source = self._report_input(assessment_id, revision)
        generated_at = self._clock()
        try:
            artifact = self._reports.render(source, language, report_format, generated_at)
        except Exception as exc:  # jede Renderer-Ausnahme wird kontrolliert gemeldet (SR-036)
            raise ReportGenerationError(assessment_id, number, f"{type(exc).__name__}: {exc}") from exc
        log = log.append(assessment_id, number, generated_at, AuditEventType.REPORT_CREATED,
                         artifact.report_id, self._catalogs.versions,
                         {"language": language.value, "format": report_format.value,
                          "report_schema_version": artifact.report_schema_version,
                          "content_hash": artifact.content_hash,
                          "version_status": status.value})
        self._save(document, document["revisions"], log)
        return artifact
