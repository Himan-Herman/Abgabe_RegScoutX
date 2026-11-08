"""In-Memory-Domainobjekte der Regelauswertung nach docs/04-architecture/DATA_MODEL.yaml."""

from __future__ import annotations

import hashlib
import json
import uuid
from dataclasses import dataclass, fields, is_dataclass
from enum import Enum
from typing import Any, Mapping

from regscoutx.errors import InvalidInputError, MissingInputError


# Fester Namensraum für reproduzierbare IDs aller Engines: gleiche Eingaben ergeben gleiche IDs.
ID_NAMESPACE = uuid.UUID("5f0c1d3e-7a52-4c1b-9b0e-2f8a6d4e9c11")

# Feld-Metadatum für nicht fachliche Angaben (z. B. Zeitstempel), die kein Fingerprint enthält.
METADATA = {"fingerprint": False}


class Language(Enum):
    DE = "de"
    EN = "en"


class DecisionStatus(Enum):
    DECIDED = "DECIDED"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    INCOMPLETE = "INCOMPLETE"
    NOT_EVALUATED = "NOT_EVALUATED"


@dataclass(frozen=True)
class CatalogVersionSet:
    sources_version: str
    rr_catalog_version: str
    rul_catalog_version: str
    data_model_version: str
    rr_applicability_version: str
    rr_measure_version: str


@dataclass(frozen=True)
class RuleExecution:
    execution_id: str
    decision_result_id: str
    sequence: int
    rule_id: str
    input_key: str
    received_value: Any
    derived_input: bool
    matched_condition: Any
    output: str | None
    next_rule: str | None
    review: str | None
    basis: str | None
    primary_legal_anchor: tuple[str, ...]
    guidance_anchor: tuple[str, ...]


@dataclass(frozen=True)
class ReviewItem:
    """Offener Prüfpunkt; die Ursache wird über den Katalog aufgelöst, nicht kopiert."""

    rule_id: str
    output: str
    matched_condition: Any


@dataclass(frozen=True)
class MissingInput:
    rule_id: str
    input_key: str


@dataclass(frozen=True)
class DecisionResult:
    decision_result_id: str
    area: str
    status: DecisionStatus
    outcome: str | None
    mdr_class: str | None
    class_candidates: tuple[tuple[str, str], ...]
    reviews: tuple[ReviewItem, ...]
    missing_input: MissingInput | None
    executions: tuple[RuleExecution, ...]
    applicable_from: str | None = None
    compliance_flags: tuple[str, ...] = ()


# Applicability-Domainobjekte liegen im gemeinsamen Kern, damit GAP_ENGINE sie ohne
# Abhängigkeit vom APPLICABILITY_ENGINE lesen kann (ARCHITECTURE.md Abschnitt 4).

class TriState(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"
    UNKNOWN = "UNKNOWN"


class Applicability(Enum):
    APPLICABLE = "APPLICABLE"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    APPLICABILITY_UNRESOLVED = "APPLICABILITY_UNRESOLVED"


@dataclass(frozen=True)
class EvaluatedPredicate:
    predicate_key: str
    value: TriState


@dataclass(frozen=True)
class ApplicableRequirement:
    applicable_requirement_id: str
    requirement_id: str
    applicability: Applicability
    reason_code: str
    block: str | None
    evaluated_predicates: tuple[EvaluatedPredicate, ...]
    supporting_rule_ids: tuple[str, ...]
    relevant_inputs: tuple[tuple[str, Any], ...]
    source_of_applicability: str
    determined_by: tuple[str, ...]


@dataclass(frozen=True)
class EngineRun:
    """Reproduzierbares Protokoll einer Engine-Ausführung ab einer Einstiegsregel."""

    run_id: str
    entry_rule: str
    catalog_versions: CatalogVersionSet
    input_snapshot: tuple[tuple[str, Any], ...]
    rule_path: tuple[str, ...]
    decision_results: tuple[DecisionResult, ...]
    missing_input: MissingInput | None

    @property
    def complete(self) -> bool:
        return self.missing_input is None

    @property
    def final(self) -> DecisionResult:
        return self.decision_results[-1]

    def require_complete(self) -> EngineRun:
        """Fail-closed-Variante für Aufrufer, die ein vollständiges Ergebnis benötigen."""
        if self.missing_input is not None:
            raise MissingInputError(self.missing_input.rule_id, self.missing_input.input_key)
        return self


@dataclass(frozen=True)
class LocalizedText:
    """Zweisprachiger Katalogtext; die Auswahl der Sprache ist Sache der Darstellung."""

    de: str
    en: str


def canonical(value: Any) -> Any:
    """JSON-fähige, reihenfolgestabile Form eines Domainobjekts ohne METADATA-Felder."""
    if is_dataclass(value) and not isinstance(value, type):
        return {field.name: canonical(getattr(value, field.name)) for field in fields(value)
                if field.metadata.get("fingerprint", True)}
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Mapping):
        return {str(key): canonical(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [canonical(item) for item in value]
    return value


def fingerprint(value: Any) -> str:
    """SHA-256 über die kanonische fachliche Form; Metadaten verändern den Wert nicht."""
    text = json.dumps(canonical(value), sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def checked_fields(label: str, data: Any, required: tuple[str, ...],
                   optional: tuple[str, ...] = ()) -> dict[str, Any]:
    """Maschinenlesbare Eingabe gegen erlaubte Felder prüfen (SR-034); unbekannte Felder abweisen."""
    if not isinstance(data, Mapping):
        raise InvalidInputError(label, data, "must be a mapping")
    unknown = sorted(set(data) - set(required) - set(optional), key=str)
    if unknown:
        raise InvalidInputError(label, unknown, "unknown field(s)")
    missing = [name for name in required if name not in data]
    if missing:
        raise InvalidInputError(label, missing, "missing required field(s)")
    return dict(data)
