"""AUDIT_LOG: nur anhängendes Ereignisprotokoll einer Bewertung (SR-032, SR-040).

Unveränderlich: append liefert ein neues Protokoll mit allen bisherigen
Einträgen; Einträge werden nie geändert oder entfernt. details enthält nur
Codes, Schlüssel und Kennungen, keine Freitexte oder Dokumentangaben.
Zeitpunkte sind Metadaten und gehen in keinen fachlichen Fingerprint ein.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from enum import Enum
from types import MappingProxyType
from typing import Any, Mapping

from regscoutx.domain import ID_NAMESPACE, CatalogVersionSet


class AuditEventType(Enum):
    ASSESSMENT_CREATED = "ASSESSMENT_CREATED"
    INPUT_RECORDED = "INPUT_RECORDED"
    RULES_EXECUTED = "RULES_EXECUTED"
    APPLICABILITY_DETERMINED = "APPLICABILITY_DETERMINED"
    GAP_STATUS_SET = "GAP_STATUS_SET"
    EVIDENCE_LINKED = "EVIDENCE_LINKED"
    REPORT_CREATED = "REPORT_CREATED"
    ASSESSMENT_FINALISED = "ASSESSMENT_FINALISED"
    CATALOG_VERSION_MISMATCH_DETECTED = "CATALOG_VERSION_MISMATCH_DETECTED"
    GAP_STATUS_CHANGED = "GAP_STATUS_CHANGED"
    EVIDENCE_UPDATED = "EVIDENCE_UPDATED"
    EVIDENCE_REMOVED = "EVIDENCE_REMOVED"
    ASSESSMENT_RECALCULATED = "ASSESSMENT_RECALCULATED"
    ASSESSMENT_REOPENED = "ASSESSMENT_REOPENED"
    REVISION_CREATED = "REVISION_CREATED"


@dataclass(frozen=True)
class AuditEvent:
    event_id: str
    assessment_id: str
    revision: int
    sequence: int
    occurred_at: str
    event_type: AuditEventType
    subject_id: str | None
    details: Mapping[str, Any]
    catalog_versions: CatalogVersionSet


@dataclass(frozen=True)
class AuditLog:
    events: tuple[AuditEvent, ...] = ()

    def append(self, assessment_id: str, revision: int, occurred_at: str,
               event_type: AuditEventType, subject_id: str | None,
               catalog_versions: CatalogVersionSet,
               details: Mapping[str, Any] | None = None) -> AuditLog:
        sequence = len(self.events) + 1
        event = AuditEvent(
            event_id=str(uuid.uuid5(ID_NAMESPACE, f"audit:{assessment_id}:{sequence}")),
            assessment_id=assessment_id,
            revision=revision,
            sequence=sequence,
            occurred_at=occurred_at,
            event_type=event_type,
            subject_id=subject_id,
            details=MappingProxyType(dict(details or {})),
            catalog_versions=catalog_versions,
        )
        return AuditLog(self.events + (event,))
