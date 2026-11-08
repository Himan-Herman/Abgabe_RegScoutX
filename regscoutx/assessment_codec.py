"""Abbildung von Assessment-Revisionen und Audit-Ereignissen auf das Persistenzschema 1.0.

Teil des ASSESSMENT_SERVICE. Das Schema ist in
docs/04-architecture/PERSISTENCE_FORMAT.md beschrieben: nur JSON-Grundtypen,
Codes statt Python-Objekten, eine Prüfsumme je Revision. Eine gespeicherte
Revision enthält die Eingaben (zur verlustfreien Wiederherstellung), den
fachlichen Fingerprint und eine katalogunabhängige Ergebnissicht (lesbar auch
bei abweichenden Katalogversionen).
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from enum import Enum
from types import MappingProxyType
from typing import Any, Mapping

from regscoutx.assessment_service import (
    Assessment,
    AssessmentChange,
    AssessmentInput,
    AssessmentState,
    ProductProfile,
    input_snapshot,
    result_snapshot,
)
from regscoutx.audit_log import AuditEvent, AuditEventType
from regscoutx.domain import CatalogVersionSet, Language, canonical, checked_fields
from regscoutx.errors import InvalidInputError, PersistenceError
from regscoutx.evidence_service import EvidenceReference
from regscoutx.gap_engine import GapAssessment, GapStatus

REVISION_FIELDS = ("revision", "state", "origin", "based_on", "created_at", "updated_at",
                   "language", "catalog_versions", "inputs", "fingerprint", "results", "change",
                   "content_hash")
INPUT_FIELDS = ("profile", "answers", "evidence")
ANSWER_FIELDS = ("requirement_id", "status", "justification", "evidence_ids", "assessed_at", "stale")
EVIDENCE_FIELDS = ("evidence_id", "title", "document_identifier", "document_version", "location",
                   "measure_key")
EVENT_FIELDS = ("event_id", "assessment_id", "revision", "sequence", "occurred_at", "event_type",
                "subject_id", "details", "catalog_versions")
VERSION_FIELDS = tuple(CatalogVersionSet.__dataclass_fields__)


class RevisionOrigin(Enum):
    CREATED = "CREATED"
    REOPENED = "REOPENED"
    CATALOG_REBASE = "CATALOG_REBASE"


@dataclass(frozen=True)
class StoredRevision:
    """Gespeicherte Revision; lesbar ohne Neuauswertung und unabhängig vom geladenen Katalogstand."""

    revision: int
    state: AssessmentState
    origin: RevisionOrigin
    based_on: int | None
    created_at: str
    updated_at: str
    language: Language
    catalog_versions: Mapping[str, Any]
    inputs: AssessmentInput
    fingerprint: str
    results: Mapping[str, Any]
    change: Mapping[str, Any] | None

    @property
    def input_snapshot(self) -> dict[str, Any]:
        return input_snapshot(self.inputs)


def _hash(record: Mapping[str, Any]) -> str:
    body = {key: value for key, value in record.items() if key != "content_hash"}
    text = json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _plain(value: Any) -> Any:
    """In reine JSON-Grundtypen überführen (Tupel zu Listen, Mappings zu dict)."""
    return json.loads(json.dumps(canonical(value), ensure_ascii=False))


def revision_record(assessment: Assessment, origin: RevisionOrigin, based_on: int | None,
                    updated_at: str, change: AssessmentChange | None) -> dict[str, Any]:
    record = {
        "revision": assessment.revision,
        "state": assessment.state.value,
        "origin": origin.value,
        "based_on": based_on,
        "created_at": assessment.created_at,
        "updated_at": updated_at,
        "language": assessment.language.value,
        "catalog_versions": dict(vars(assessment.catalog_versions)),
        "inputs": {
            "profile": dict(assessment.profile.answers),
            "answers": [{"requirement_id": a.requirement_id, "status": a.status.value,
                         "justification": a.justification, "evidence_ids": list(a.evidence_ids),
                         "assessed_at": a.assessed_at, "stale": a.stale}
                        for a in assessment.answers],
            "evidence": [{name: getattr(e, name) for name in EVIDENCE_FIELDS}
                         for e in assessment.evidence],
        },
        "fingerprint": assessment.fingerprint,
        "results": result_snapshot(assessment),
        "change": None if change is None else canonical(change),
        "content_hash": "",
    }
    record = _plain(record)
    record["content_hash"] = _hash(record)
    return record


def with_state(record: Mapping[str, Any], state: AssessmentState, updated_at: str) -> dict[str, Any]:
    """Zustandswechsel einer noch änderbaren Revision (neue Prüfsumme)."""
    changed = {**record, "state": state.value, "updated_at": updated_at}
    changed["content_hash"] = _hash(changed)
    return changed


def _enum(assessment_id: str, enum: type[Enum], value: Any) -> Any:
    try:
        return enum(value)
    except ValueError as exc:
        raise PersistenceError(assessment_id, f"invalid {enum.__name__} '{value}'") from exc


def parse_revision(assessment_id: str, record: Any) -> StoredRevision:
    """Gespeicherte Revision strukturell prüfen; Prüfsummen- oder Schemafehler sind fail-closed."""
    try:
        values = checked_fields("revision", record, REVISION_FIELDS)
        if set(values) != set(REVISION_FIELDS):
            raise PersistenceError(assessment_id, "revision fields incomplete")
        if values["content_hash"] != _hash(values):
            raise PersistenceError(assessment_id, f"revision {values['revision']}: checksum mismatch")
        inputs = checked_fields("inputs", values["inputs"], INPUT_FIELDS)
        answers = tuple(
            GapAssessment(**{**checked_fields("answer", item, ANSWER_FIELDS),
                             "status": _enum(assessment_id, GapStatus, item["status"]),
                             "evidence_ids": tuple(item["evidence_ids"])})
            for item in inputs["answers"])
        evidence = tuple(EvidenceReference(**checked_fields("evidence", item, EVIDENCE_FIELDS))
                         for item in inputs["evidence"])
        versions = values["catalog_versions"]
        if not isinstance(versions, Mapping) or not isinstance(values["results"], Mapping):
            raise PersistenceError(assessment_id, "catalog_versions and results must be objects")
        return StoredRevision(
            revision=values["revision"],
            state=_enum(assessment_id, AssessmentState, values["state"]),
            origin=_enum(assessment_id, RevisionOrigin, values["origin"]),
            based_on=values["based_on"],
            created_at=values["created_at"],
            updated_at=values["updated_at"],
            language=_enum(assessment_id, Language, values["language"]),
            catalog_versions=MappingProxyType(dict(versions)),
            inputs=AssessmentInput(ProductProfile.of(inputs["profile"]), answers, evidence),
            fingerprint=values["fingerprint"],
            results=values["results"],
            change=values["change"],
        )
    except (InvalidInputError, KeyError, TypeError) as exc:
        raise PersistenceError(assessment_id, f"revision does not match the persistence schema: "
                                              f"{type(exc).__name__}") from exc


def event_record(event: AuditEvent) -> dict[str, Any]:
    return _plain({
        "event_id": event.event_id, "assessment_id": event.assessment_id,
        "revision": event.revision, "sequence": event.sequence, "occurred_at": event.occurred_at,
        "event_type": event.event_type.value, "subject_id": event.subject_id,
        "details": event.details, "catalog_versions": vars(event.catalog_versions),
    })


def parse_event(assessment_id: str, record: Any) -> AuditEvent:
    try:
        values = checked_fields("audit_event", record, EVENT_FIELDS)
        if set(values) != set(EVENT_FIELDS) or not isinstance(values["details"], Mapping):
            raise PersistenceError(assessment_id, "audit event fields incomplete")
        return AuditEvent(
            event_id=values["event_id"], assessment_id=values["assessment_id"],
            revision=values["revision"], sequence=values["sequence"],
            occurred_at=values["occurred_at"],
            event_type=_enum(assessment_id, AuditEventType, values["event_type"]),
            subject_id=values["subject_id"],
            details=MappingProxyType(dict(values["details"])),
            catalog_versions=CatalogVersionSet(**values["catalog_versions"]),
        )
    except (InvalidInputError, TypeError) as exc:
        raise PersistenceError(assessment_id, f"audit event does not match the persistence schema: "
                                              f"{type(exc).__name__}") from exc
