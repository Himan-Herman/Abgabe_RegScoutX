"""EVIDENCE_SERVICE: nutzerseitig angegebene Nachweisreferenzen (SR-017, SR-018, SR-034).

Eine EvidenceReference entsteht ausschließlich aus einer Nutzereingabe. Das
Modul erzeugt, ergänzt oder unterstellt keine Nachweise und wertet keine
Dokumentinhalte aus. Vorgesehene Nachweisarten aus RR_MEASURE und
Projektevidenz (EV-NNN) sind eigene Konzepte und hier nicht modelliert.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from types import MappingProxyType
from typing import Any, Iterable, Mapping

from regscoutx.domain import checked_fields
from regscoutx.errors import InvalidInputError

REQUIRED_FIELDS = ("evidence_id", "title", "document_identifier")
OPTIONAL_FIELDS = ("document_version", "location", "measure_key")


@dataclass(frozen=True)
class EvidenceReference:
    """Verweis auf ein Nachweisdokument nach DATA_MODEL.yaml; measure_key verweist auf RR_MEASURE."""

    evidence_id: str
    title: str
    document_identifier: str
    document_version: str | None = None
    location: str | None = None
    measure_key: str | None = None

    @classmethod
    def from_mapping(cls, data: Any) -> EvidenceReference:
        return cls(**checked_fields("evidence", data, REQUIRED_FIELDS, OPTIONAL_FIELDS))


def _text(label: str, value: Any, required: bool) -> None:
    if value is None and not required:
        return
    if not isinstance(value, str) or not value.strip():
        raise InvalidInputError(label, value, "must be a non-empty string")


class EvidenceService:
    """Prüft Nachweisreferenzen und führt sie als schreibgeschütztes Register je Bewertung."""

    def validate(self, reference: Any) -> EvidenceReference:
        if not isinstance(reference, EvidenceReference):
            raise InvalidInputError("evidence", reference, "must be an EvidenceReference")
        label = f"evidence[{reference.evidence_id}]"
        try:
            valid_id = str(uuid.UUID(reference.evidence_id)) == reference.evidence_id
        except (TypeError, ValueError, AttributeError):
            valid_id = False
        if not valid_id:
            raise InvalidInputError(f"{label}.evidence_id", reference.evidence_id,
                                    "must be a UUID in canonical form")
        _text(f"{label}.title", reference.title, True)
        _text(f"{label}.document_identifier", reference.document_identifier, True)
        for name in OPTIONAL_FIELDS:
            _text(f"{label}.{name}", getattr(reference, name), False)
        return reference

    def register(self, references: Iterable[Any]) -> Mapping[str, EvidenceReference]:
        """Register nach evidence_id; doppelte IDs werden abgewiesen."""
        register: dict[str, EvidenceReference] = {}
        for reference in references:
            valid = self.validate(reference)
            if valid.evidence_id in register:
                raise InvalidInputError("evidence", valid.evidence_id, "duplicate evidence_id")
            register[valid.evidence_id] = valid
        return MappingProxyType(dict(sorted(register.items())))

    # Operationen auf einem Register; jede liefert ein neues Register -------

    def add(self, register: Mapping[str, EvidenceReference],
            reference: Any) -> Mapping[str, EvidenceReference]:
        valid = self.validate(reference)
        if valid.evidence_id in register:
            raise InvalidInputError("evidence", valid.evidence_id, "evidence_id already exists")
        return self.register((*register.values(), valid))

    def update(self, register: Mapping[str, EvidenceReference],
               reference: Any) -> Mapping[str, EvidenceReference]:
        valid = self.validate(reference)
        if valid.evidence_id not in register:
            raise InvalidInputError("evidence", valid.evidence_id, "unknown evidence reference")
        return self.register(valid if item.evidence_id == valid.evidence_id else item
                             for item in register.values())

    def remove(self, register: Mapping[str, EvidenceReference], evidence_id: str,
               referenced_by: Iterable[str] = ()) -> Mapping[str, EvidenceReference]:
        """Entfernen nur, wenn keine RR die Referenz nutzt; kein stilles Lösen von Zuordnungen."""
        if evidence_id not in register:
            raise InvalidInputError("evidence", evidence_id, "unknown evidence reference")
        users = sorted(referenced_by)
        if users:
            raise InvalidInputError("evidence", evidence_id, f"still referenced by {users}")
        return self.register(item for item in register.values() if item.evidence_id != evidence_id)

    @staticmethod
    def get(register: Mapping[str, EvidenceReference], evidence_id: str) -> EvidenceReference:
        if evidence_id not in register:
            raise InvalidInputError("evidence", evidence_id, "unknown evidence reference")
        return register[evidence_id]

    @staticmethod
    def by_measure(register: Mapping[str, EvidenceReference],
                   measure_key: str) -> tuple[EvidenceReference, ...]:
        return tuple(item for item in register.values() if item.measure_key == measure_key)

    @staticmethod
    def changed_fields(before: EvidenceReference, after: EvidenceReference) -> tuple[str, ...]:
        """Namen geänderter Felder, ohne deren Inhalte (für das Audit-Protokoll)."""
        return tuple(name for name in (*REQUIRED_FIELDS, *OPTIONAL_FIELDS)
                     if getattr(before, name) != getattr(after, name))
