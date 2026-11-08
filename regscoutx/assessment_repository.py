"""ASSESSMENT_REPOSITORY: Speicherschnittstelle für Bewertungsdokumente (ADR-0005).

Die Schnittstelle kennt nur das versionierte, JSON-fähige Bewertungsdokument
(docs/04-architecture/PERSISTENCE_FORMAT.md), keine Domainobjekte. Sie prüft vor
jedem Schreiben die Anhängeregel: vorhandene Revisionen und Audit-Einträge
dürfen nicht verändert oder entfernt werden; nur die letzte Revision darf im
Zustand DRAFT ersetzt werden. Implementierungen liefern nur Lesen und
atomisches Schreiben.
"""

from __future__ import annotations

import uuid
from abc import ABC, abstractmethod
from typing import Any, Mapping

from regscoutx.errors import AssessmentNotFoundError, InvalidInputError, PersistenceError

FORMAT = "regscoutx.assessment"
FORMAT_VERSION = "1.0"
DOCUMENT_FIELDS = ("format", "format_version", "assessment_id", "created_at", "revisions", "audit")
DRAFT = "DRAFT"


def checked_assessment_id(assessment_id: Any) -> str:
    """Nur kanonische UUIDs; verhindert Pfadangaben und beliebige Dateinamen."""
    try:
        valid = isinstance(assessment_id, str) and str(uuid.UUID(assessment_id)) == assessment_id
    except (TypeError, ValueError, AttributeError):
        valid = False
    if not valid:
        raise InvalidInputError("assessment_id", assessment_id, "must be a UUID in canonical form")
    return assessment_id


def check_envelope(document: Any, assessment_id: str) -> Mapping[str, Any]:
    """Hülle eines Dokuments prüfen; jede Abweichung ist ein Persistenzfehler (fail-closed)."""
    if not isinstance(document, Mapping) or set(document) != set(DOCUMENT_FIELDS):
        raise PersistenceError(assessment_id, "document does not match the persistence schema")
    if document["format"] != FORMAT or document["format_version"] != FORMAT_VERSION:
        raise PersistenceError(assessment_id, f"unsupported format "
                                              f"{document['format']!r} {document['format_version']!r}")
    if document["assessment_id"] != assessment_id:
        raise PersistenceError(assessment_id, "assessment_id does not match the storage key")
    revisions, audit = document["revisions"], document["audit"]
    if not isinstance(revisions, list) or not revisions or not isinstance(audit, list):
        raise PersistenceError(assessment_id, "revisions and audit must be lists")
    numbers = [r.get("revision") if isinstance(r, Mapping) else None for r in revisions]
    if numbers != list(range(1, len(revisions) + 1)):
        raise PersistenceError(assessment_id, "revisions must be numbered consecutively from 1")
    sequences = [e.get("sequence") if isinstance(e, Mapping) else None for e in audit]
    if sequences != list(range(1, len(audit) + 1)):
        raise PersistenceError(assessment_id, "audit events must be numbered consecutively from 1")
    return document


def check_append_only(stored: Mapping[str, Any], new: Mapping[str, Any]) -> None:
    """Anhängeregel zwischen gespeichertem und neuem Dokument."""
    assessment_id = new["assessment_id"]
    old_revisions, new_revisions = stored["revisions"], new["revisions"]
    if stored["created_at"] != new["created_at"]:
        raise PersistenceError(assessment_id, "created_at must not change")
    if len(new_revisions) < len(old_revisions):
        raise PersistenceError(assessment_id, "revisions must not be removed")
    replaceable = (len(new_revisions) == len(old_revisions)
                   and old_revisions[-1].get("state") == DRAFT)
    frozen = old_revisions[:-1] if replaceable else old_revisions
    if list(new_revisions[:len(frozen)]) != list(frozen):
        raise PersistenceError(assessment_id, "stored revisions must not be modified")
    if list(new["audit"][:len(stored["audit"])]) != list(stored["audit"]):
        raise PersistenceError(assessment_id, "audit events must not be modified or removed")


class AssessmentRepository(ABC):
    """Austauschbarer Speicher für Bewertungsdokumente."""

    def save(self, document: Mapping[str, Any]) -> None:
        assessment_id = checked_assessment_id(
            document.get("assessment_id") if isinstance(document, Mapping) else None)
        check_envelope(document, assessment_id)
        if self.exists(assessment_id):
            check_append_only(self.load(assessment_id), document)
        self._write(assessment_id, document)

    def load(self, assessment_id: str) -> Mapping[str, Any]:
        checked_assessment_id(assessment_id)
        if not self.exists(assessment_id):
            raise AssessmentNotFoundError(assessment_id)
        return check_envelope(self._read(assessment_id), assessment_id)

    @abstractmethod
    def exists(self, assessment_id: str) -> bool:
        """Ob zu der (bereits geprüften) Kennung ein Dokument existiert."""

    @abstractmethod
    def assessment_ids(self) -> tuple[str, ...]:
        """Kennungen aller gespeicherten Bewertungen, sortiert."""

    @abstractmethod
    def _read(self, assessment_id: str) -> Any:
        """Dokument lesen; unlesbare Daten als PersistenceError."""

    @abstractmethod
    def _write(self, assessment_id: str, document: Mapping[str, Any]) -> None:
        """Dokument atomisch schreiben."""
