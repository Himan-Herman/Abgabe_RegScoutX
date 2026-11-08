"""GAP_ENGINE: genau ein Gap-Status je RR aus Anwendbarkeit und strukturierter Erfüllungsbewertung.

Anwendbarkeit und Erfüllung bleiben getrennt: NOT_APPLICABLE und
APPLICABILITY_UNRESOLVED stammen ausschließlich aus dem APPLICABILITY_ENGINE;
Erfüllungsstatus stammen ausschließlich aus einer GapAssessment des Nutzers
(SR-013). Eine als veraltet (stale) markierte Bewertung fließt erst nach bewusster
Bestätigung wieder ein. Fehlende Bewertung ergibt NOT_ASSESSED, fehlende Nachweisreferenz bei
behaupteter (teilweiser) Erfüllung EVIDENCE_REVIEW_REQUIRED (Nachweislücke,
SR-015) – beides ist keine regulatorische Aussage „nicht erfüllt“. Begründungen
und Dokumentangaben werden nicht ausgewertet; keine Textheuristik, keine KI.
Die vorgesehenen Maßnahmen je RR (RR_MEASURE) erhält die Engine als Werte vom
Aufrufer; sie liest keine Kataloge.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Iterable, Mapping, Sequence

from regscoutx.domain import (
    ID_NAMESPACE,
    METADATA,
    Applicability,
    ApplicableRequirement,
    checked_fields,
    fingerprint,
)
from regscoutx.errors import InvalidInputError, UnexpectedEndStateError
from regscoutx.evidence_service import EvidenceReference

ANSWER_REQUIRED = ("requirement_id", "status")
ANSWER_OPTIONAL = ("justification", "evidence_ids", "assessed_at")


class GapStatus(Enum):
    """Erfüllungsstatus nach DATA_MODEL gap_status; NOT_APPLICABLE ist nicht vom Nutzer setzbar."""

    FULFILLED = "FULFILLED"
    PARTIALLY_FULFILLED = "PARTIALLY_FULFILLED"
    NOT_FULFILLED = "NOT_FULFILLED"
    NOT_ASSESSED = "NOT_ASSESSED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


ASSERTED = (GapStatus.FULFILLED, GapStatus.PARTIALLY_FULFILLED, GapStatus.NOT_FULFILLED)
NEEDS_EVIDENCE = (GapStatus.FULFILLED, GapStatus.PARTIALLY_FULFILLED)


class GapResultStatus(Enum):
    """Abgeleiteter Ergebnisstatus je RR (DATA_MODEL gap_result)."""

    NOT_APPLICABLE = "NOT_APPLICABLE"
    APPLICABILITY_UNRESOLVED = "APPLICABILITY_UNRESOLVED"
    NOT_ASSESSED = "NOT_ASSESSED"
    FULFILLED = "FULFILLED"
    PARTIALLY_FULFILLED = "PARTIALLY_FULFILLED"
    NOT_FULFILLED = "NOT_FULFILLED"
    EVIDENCE_REVIEW_REQUIRED = "EVIDENCE_REVIEW_REQUIRED"


GAP_STATUSES = (GapResultStatus.PARTIALLY_FULFILLED, GapResultStatus.NOT_FULFILLED,
                GapResultStatus.EVIDENCE_REVIEW_REQUIRED)


class GapReason(Enum):
    """Nicht-regulatorischer Begründungscode des Ergebnisstatus (DATA_MODEL gap_reason)."""

    RR_NOT_APPLICABLE = "RR_NOT_APPLICABLE"
    RR_APPLICABILITY_UNRESOLVED = "RR_APPLICABILITY_UNRESOLVED"
    NO_ANSWER = "NO_ANSWER"
    ANSWER_NOT_ASSESSED = "ANSWER_NOT_ASSESSED"
    ANSWER_NOT_FULFILLED = "ANSWER_NOT_FULFILLED"
    ANSWER_WITH_EVIDENCE = "ANSWER_WITH_EVIDENCE"
    ANSWER_WITHOUT_EVIDENCE = "ANSWER_WITHOUT_EVIDENCE"
    ANSWER_REVIEW_REQUIRED = "ANSWER_REVIEW_REQUIRED"


class AnswerState(Enum):
    """ACTIVE: bestätigt und wirksam; INACTIVE: RR nicht anwendbar; REACTIVATED_REVIEW_REQUIRED: RR wieder anwendbar, Bestätigung ausstehend."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    REACTIVATED_REVIEW_REQUIRED = "REACTIVATED_REVIEW_REQUIRED"


class EvidenceState(Enum):
    NOT_CONSIDERED = "NOT_CONSIDERED"
    NO_EVIDENCE_REFERENCED = "NO_EVIDENCE_REFERENCED"
    EVIDENCE_REFERENCED = "EVIDENCE_REFERENCED"


class MeasureMappingStatus(Enum):
    """Mapping-Status einer RR im RR_MEASURE_CATALOG."""

    MAPPED = "MAPPED"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"


@dataclass(frozen=True)
class GapAssessment:
    """Strukturierte Erfüllungsbewertung einer RR durch den Nutzer; an die RR, nicht an eine Auswertung gebunden.

    stale wird vom ASSESSMENT_SERVICE gesetzt, sobald die RR in einer Auswertung
    nicht anwendbar ist, und nur durch Bestätigung oder neue Bewertung aufgehoben.
    """

    requirement_id: str
    status: GapStatus
    justification: str | None = None
    evidence_ids: tuple[str, ...] = ()
    assessed_at: str | None = field(default=None, compare=False, metadata=METADATA)
    stale: bool = False

    @property
    def gap_assessment_id(self) -> str:
        return str(uuid.uuid5(ID_NAMESPACE, f"gap-assessment:{fingerprint(self)}"))

    @classmethod
    def from_mapping(cls, data: Any) -> GapAssessment:
        values = checked_fields("answer", data, ANSWER_REQUIRED, ANSWER_OPTIONAL)
        try:
            values["status"] = GapStatus(values["status"])
        except ValueError as exc:
            raise InvalidInputError("answer.status", values["status"],
                                    f"value must be one of {[s.value for s in GapStatus]}") from exc
        evidence_ids = values.get("evidence_ids", ())
        if not isinstance(evidence_ids, (list, tuple)):
            raise InvalidInputError("answer.evidence_ids", evidence_ids, "must be a list")
        values["evidence_ids"] = tuple(evidence_ids)
        return cls(**values)


@dataclass(frozen=True)
class MeasurePlan:
    """Vorgesehene Maßnahmen einer RR aus RR_MEASURE (vom Aufrufer übergeben)."""

    status: MeasureMappingStatus
    measure_keys: tuple[str, ...]


@dataclass(frozen=True)
class EvidenceResult:
    state: EvidenceState
    evidence_ids: tuple[str, ...]
    measures_with_evidence: tuple[str, ...]
    measures_without_evidence: tuple[str, ...]


@dataclass(frozen=True)
class GapResult:
    requirement_id: str
    applicable_requirement_id: str
    applicability: Applicability
    status: GapResultStatus
    reason: GapReason
    is_gap: bool
    answer: GapAssessment | None
    answer_state: AnswerState | None
    evidence: EvidenceResult
    measure_status: MeasureMappingStatus


def _derive(applicability: Applicability, answer: GapAssessment | None,
            has_evidence: bool) -> tuple[GapResultStatus, GapReason]:
    """Einzige Ableitungstabelle des Gap-Status (docs/04-architecture/ARCHITECTURE.md Abschnitt 8)."""
    if applicability is Applicability.NOT_APPLICABLE:
        return GapResultStatus.NOT_APPLICABLE, GapReason.RR_NOT_APPLICABLE
    if applicability is Applicability.APPLICABILITY_UNRESOLVED:
        return GapResultStatus.APPLICABILITY_UNRESOLVED, GapReason.RR_APPLICABILITY_UNRESOLVED
    if answer is not None and answer.stale:
        return GapResultStatus.NOT_ASSESSED, GapReason.ANSWER_REVIEW_REQUIRED
    if answer is None:
        return GapResultStatus.NOT_ASSESSED, GapReason.NO_ANSWER
    if answer.status is GapStatus.NOT_ASSESSED:
        return GapResultStatus.NOT_ASSESSED, GapReason.ANSWER_NOT_ASSESSED
    if answer.status is GapStatus.NOT_FULFILLED:
        return GapResultStatus.NOT_FULFILLED, GapReason.ANSWER_NOT_FULFILLED
    if not has_evidence:
        return GapResultStatus.EVIDENCE_REVIEW_REQUIRED, GapReason.ANSWER_WITHOUT_EVIDENCE
    return GapResultStatus(answer.status.value), GapReason.ANSWER_WITH_EVIDENCE


class GapEngine:
    """Validiert Erfüllungsbewertungen und leitet je RR genau einen Gap-Status ab."""

    def validate(self, answers: Iterable[Any], requirement_ids: Iterable[str],
                 evidence: Mapping[str, EvidenceReference],
                 plans: Mapping[str, MeasurePlan]) -> dict[str, GapAssessment]:
        known = set(requirement_ids)
        valid: dict[str, GapAssessment] = {}
        for answer in answers:
            if not isinstance(answer, GapAssessment):
                raise InvalidInputError("answers", answer, "must be a GapAssessment")
            rr_id = answer.requirement_id
            label = f"answers[{rr_id}]"
            if rr_id not in known:
                raise InvalidInputError(label, rr_id, "unknown requirement")
            if rr_id in valid:
                raise InvalidInputError(label, rr_id, "more than one answer per requirement")
            if not isinstance(answer.status, GapStatus) or answer.status is GapStatus.NOT_APPLICABLE:
                raise InvalidInputError(f"{label}.status", answer.status,
                                        "NOT_APPLICABLE is derived from applicability only")
            justification = answer.justification
            if answer.status in ASSERTED and (not isinstance(justification, str)
                                              or not justification.strip()):
                raise InvalidInputError(f"{label}.justification", justification,
                                        f"required for {answer.status.value}")
            if justification is not None and not isinstance(justification, str):
                raise InvalidInputError(f"{label}.justification", justification, "must be a string")
            if answer.assessed_at is not None:
                try:
                    datetime.fromisoformat(answer.assessed_at)
                except (TypeError, ValueError) as exc:
                    raise InvalidInputError(f"{label}.assessed_at", answer.assessed_at,
                                            "must be an ISO date-time") from exc
            if not isinstance(answer.stale, bool):
                raise InvalidInputError(f"{label}.stale", answer.stale, "must be a boolean")
            if not isinstance(answer.evidence_ids, tuple) or \
                    len(set(answer.evidence_ids)) != len(answer.evidence_ids):
                raise InvalidInputError(f"{label}.evidence_ids", answer.evidence_ids,
                                        "must be a tuple of unique evidence ids")
            for evidence_id in answer.evidence_ids:
                if evidence_id not in evidence:
                    raise InvalidInputError(f"{label}.evidence_ids", evidence_id,
                                            "unknown evidence reference")
                measure_key = evidence[evidence_id].measure_key
                if measure_key is not None and measure_key not in plans[rr_id].measure_keys:
                    raise InvalidInputError(f"{label}.evidence_ids", evidence_id,
                                            f"measure_key '{measure_key}' is not a planned "
                                            f"measure of {rr_id}")
            valid[rr_id] = answer
        return valid

    def evaluate(self, requirements: Sequence[ApplicableRequirement],
                 plans: Mapping[str, MeasurePlan], answers: Iterable[Any],
                 evidence: Mapping[str, EvidenceReference]) -> tuple[GapResult, ...]:
        """Je ApplicableRequirement genau ein GapResult in Katalogreihenfolge."""
        ids = [requirement.requirement_id for requirement in requirements]
        missing = [rr_id for rr_id in ids if rr_id not in plans]
        if missing:
            raise UnexpectedEndStateError(missing[0], "no measure mapping for requirement")
        valid = self.validate(answers, ids, evidence, plans)
        return tuple(self._result(requirement, plans[requirement.requirement_id],
                                  valid.get(requirement.requirement_id), evidence)
                     for requirement in requirements)

    @staticmethod
    def _result(requirement: ApplicableRequirement, plan: MeasurePlan,
                answer: GapAssessment | None,
                evidence: Mapping[str, EvidenceReference]) -> GapResult:
        active = requirement.applicability is Applicability.APPLICABLE
        used = answer if active else None
        effective = used is not None and not used.stale
        evidence_ids = used.evidence_ids if effective else ()
        status, reason = _derive(requirement.applicability, used, bool(evidence_ids))
        covered = {evidence[item].measure_key for item in evidence_ids}
        if not active or (used is not None and used.stale):
            evidence_result = EvidenceResult(EvidenceState.NOT_CONSIDERED, (), (), ())
        else:
            evidence_result = EvidenceResult(
                state=(EvidenceState.EVIDENCE_REFERENCED if evidence_ids
                       else EvidenceState.NO_EVIDENCE_REFERENCED),
                evidence_ids=evidence_ids,
                measures_with_evidence=tuple(key for key in plan.measure_keys if key in covered),
                measures_without_evidence=tuple(key for key in plan.measure_keys
                                                if key not in covered),
            )
        return GapResult(
            requirement_id=requirement.requirement_id,
            applicable_requirement_id=requirement.applicable_requirement_id,
            applicability=requirement.applicability,
            status=status,
            reason=reason,
            is_gap=status in GAP_STATUSES,
            answer=answer,
            answer_state=_answer_state(answer, active),
            evidence=evidence_result,
            measure_status=plan.status,
        )


def _answer_state(answer: GapAssessment | None, active: bool) -> AnswerState | None:
    if answer is None:
        return None
    if not active:
        return AnswerState.INACTIVE
    return AnswerState.REACTIVATED_REVIEW_REQUIRED if answer.stale else AnswerState.ACTIVE
