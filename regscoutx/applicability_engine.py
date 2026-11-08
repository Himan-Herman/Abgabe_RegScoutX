"""APPLICABILITY_ENGINE: deterministische Anwendbarkeit der RR aus Entscheidungsergebnissen und Eingaben.

Grundlage ist ausschließlich die technische Zuordnung RR_APPLICABILITY.yaml:
übergeordneter Bereich (Block) und lokale Bedingungen je RR als Prädikate über
DecisionResults des RULE_ENGINE und kontrollierte Applicability-Eingaben.
Anforderungstexte werden nicht ausgewertet. Die Prädikatlogik ist dreiwertig
(TRUE, FALSE, UNKNOWN); alles Ungeklärte führt fail-closed zu
APPLICABILITY_UNRESOLVED.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from regscoutx.catalog_repository import CatalogRepository
from regscoutx.domain import (
    ID_NAMESPACE,
    ApplicableRequirement,
    Applicability,
    CatalogVersionSet,
    DecisionResult,
    DecisionStatus,
    EvaluatedPredicate,
    TriState,
)
from regscoutx.errors import InvalidInputError, UnexpectedEndStateError


@dataclass(frozen=True)
class ApplicabilityResult:
    catalog_versions: CatalogVersionSet
    decision_results: tuple[DecisionResult, ...]
    requirements: tuple[ApplicableRequirement, ...]

    def by_id(self, requirement_id: str) -> ApplicableRequirement:
        for requirement in self.requirements:
            if requirement.requirement_id == requirement_id:
                return requirement
        raise KeyError(requirement_id)

    def counts(self) -> dict[str, int]:
        counts = {status.value: 0 for status in Applicability}
        for requirement in self.requirements:
            counts[requirement.applicability.value] += 1
        return counts


@dataclass(frozen=True)
class DecisionTrace:
    """Herangezogenes Entscheidungsergebnis mit seinem Regelpfad."""

    decision_result_id: str
    area: str
    status: str
    outcome: str | None
    rule_ids: tuple[str, ...]


@dataclass(frozen=True)
class ApplicabilityExplanation:
    """Herleitung der Anwendbarkeit einer RR (SR-042) aus der bestehenden Trace-Struktur."""

    requirement_id: str
    applicability: Applicability
    reason_code: str
    block: str | None
    evaluated_predicates: tuple[EvaluatedPredicate, ...]
    relevant_inputs: tuple[tuple[str, Any], ...]
    decisions: tuple[DecisionTrace, ...]
    supporting_rule_ids: tuple[str, ...]
    primary_sources: tuple[str, ...]
    supplementary_sources: tuple[str, ...]
    source_of_applicability: str


@dataclass
class _Trace:
    areas: set[str]
    inputs: dict[str, Any]
    inactive_reason: str | None = None


def _all_of(values: list[TriState]) -> TriState:
    if TriState.FALSE in values:
        return TriState.FALSE
    return TriState.TRUE if all(v is TriState.TRUE for v in values) else TriState.UNKNOWN


def _any_of(values: list[TriState]) -> TriState:
    if TriState.TRUE in values:
        return TriState.TRUE
    return TriState.FALSE if values and all(v is TriState.FALSE for v in values) else TriState.UNKNOWN


class ApplicabilityEngine:
    """Bestimmt je RR APPLICABLE, NOT_APPLICABLE oder APPLICABILITY_UNRESOLVED."""

    def __init__(self, repository: CatalogRepository) -> None:
        self._repository = repository
        self._mapping = repository.applicability

    def _validate_inputs(self, inputs: Mapping[str, Any]) -> dict[str, Any]:
        if not isinstance(inputs, Mapping):
            raise InvalidInputError("<inputs>", inputs, "inputs must be a mapping")
        definitions = self._mapping["profile_inputs"]
        for key, value in inputs.items():
            spec = definitions.get(key)
            if spec is None:
                raise InvalidInputError(key, value, "unknown applicability input key")
            if not any(type(value) is type(allowed) and value == allowed
                       for allowed in spec["allowed_values"]):
                raise InvalidInputError(
                    key, value, f"value not in allowed_values {list(spec['allowed_values'])}")
        return dict(inputs)

    def _decided(self, results: Mapping[str, DecisionResult], area: str) -> DecisionResult | None:
        result = results.get(area)
        return result if result is not None and result.status is DecisionStatus.DECIDED else None

    def _predicate(self, key: str, results: Mapping[str, DecisionResult],
                   inputs: Mapping[str, Any], trace: _Trace,
                   memo: dict[str, tuple[TriState, _Trace]]) -> TriState:
        if key in memo:
            value, cached = memo[key]
            trace.areas.update(cached.areas)
            trace.inputs.update(cached.inputs)
            trace.inactive_reason = trace.inactive_reason or cached.inactive_reason
            return value
        own = _Trace(set(), {})
        value = self._evaluate_predicate(key, results, inputs, own, memo)
        memo[key] = (value, own)
        trace.areas.update(own.areas)
        trace.inputs.update(own.inputs)
        trace.inactive_reason = trace.inactive_reason or own.inactive_reason
        return value

    def _evaluate_predicate(self, key: str, results: Mapping[str, DecisionResult],
                            inputs: Mapping[str, Any], trace: _Trace,
                            memo: dict[str, tuple[TriState, _Trace]]) -> TriState:
        spec = self._mapping["predicates"][key]
        kind = spec["kind"]
        if kind == "DECISION_OUTCOME":
            trace.areas.update(item["area"] for item in (*spec["true_if"], *spec["false_if"]))
            value = TriState.UNKNOWN
            for item in spec["true_if"]:
                decided = self._decided(results, item["area"])
                if decided is not None and decided.outcome == item["outcome"]:
                    value = TriState.TRUE
            if value is TriState.UNKNOWN:
                for item in spec["false_if"]:
                    decided = self._decided(results, item["area"])
                    if decided is not None and decided.outcome == item["outcome"]:
                        value = TriState.FALSE
                        trace.inactive_reason = item.get("reason_code")
        elif kind == "MDR_CLASS":
            trace.areas.add(spec["area"])
            decided = self._decided(results, spec["area"])
            if decided is None or decided.mdr_class is None:
                value = TriState.UNKNOWN
            else:
                value = TriState.TRUE if decided.mdr_class in spec["classes"] else TriState.FALSE
        elif kind == "PROFILE_INPUT":
            name = spec["input"]
            if name not in inputs:
                value = TriState.UNKNOWN
            else:
                trace.inputs[name] = inputs[name]
                if inputs[name] in spec.get("unknown_values", ()):
                    value = TriState.UNKNOWN
                else:
                    value = TriState.TRUE if inputs[name] in spec["true_values"] else TriState.FALSE
        elif kind in ("ALL_OF", "ANY_OF"):
            parts = [self._predicate(part, results, inputs, trace, memo) for part in spec["of"]]
            value = _all_of(parts) if kind == "ALL_OF" else _any_of(parts)
        elif kind == "NOT_MODELLED":
            if spec["area"] is not None:
                trace.areas.add(spec["area"])
            value = TriState.UNKNOWN
        else:
            raise UnexpectedEndStateError(key, f"unsupported predicate kind '{kind}'")
        return value

    def explain(self, result: ApplicabilityResult, requirement_id: str) -> ApplicabilityExplanation:
        """Herleitung einer RR-Anwendbarkeit für jeden Zustand (SR-042); keine neue Bewertung."""
        requirement = result.by_id(requirement_id)
        sources = self._repository.requirement(requirement_id)["sources"]
        by_id = {decision.decision_result_id: decision for decision in result.decision_results}
        decisions = tuple(
            DecisionTrace(decision.decision_result_id, decision.area, decision.status.value,
                          decision.outcome,
                          tuple(execution.rule_id for execution in decision.executions))
            for decision in (by_id[item] for item in requirement.determined_by))
        return ApplicabilityExplanation(
            requirement_id=requirement_id,
            applicability=requirement.applicability,
            reason_code=requirement.reason_code,
            block=requirement.block,
            evaluated_predicates=requirement.evaluated_predicates,
            relevant_inputs=requirement.relevant_inputs,
            decisions=decisions,
            supporting_rule_ids=requirement.supporting_rule_ids,
            primary_sources=tuple(sources["primary"]),
            supplementary_sources=tuple(sources["supplementary"]),
            source_of_applicability=requirement.source_of_applicability,
        )

    def _not_evaluated(self, area: str, versions: CatalogVersionSet) -> DecisionResult:
        result_id = str(uuid.uuid5(ID_NAMESPACE, f"not-evaluated:{area}:{vars(versions)}"))
        return DecisionResult(
            decision_result_id=result_id, area=area, status=DecisionStatus.NOT_EVALUATED,
            outcome=None, mdr_class=None, class_candidates=(), reviews=(), missing_input=None,
            executions=())

    def evaluate(self, decision_results: Sequence[DecisionResult],
                 inputs: Mapping[str, Any]) -> ApplicabilityResult:
        """Anwendbarkeit aller RR des Katalogs bestimmen."""
        valid_inputs = self._validate_inputs(inputs)
        versions = self._repository.versions
        results: dict[str, DecisionResult] = {}
        for result in decision_results:
            if result.area in results:
                raise InvalidInputError("decision_results", result.area,
                                        "more than one DecisionResult per area")
            results[result.area] = result
        referenced_areas = self._referenced_areas()
        for area in sorted(referenced_areas - set(results)):
            results[area] = self._not_evaluated(area, versions)

        memo: dict[str, tuple[TriState, _Trace]] = {}
        requirements = tuple(
            self._requirement(rr_id, results, valid_inputs, memo)
            for rr_id in self._repository.requirement_ids)
        return ApplicabilityResult(versions, tuple(results.values()), requirements)

    def _referenced_areas(self) -> set[str]:
        areas: set[str] = set()
        for spec in self._mapping["predicates"].values():
            if spec.get("area") is not None:
                areas.add(spec["area"])
            for item in (*spec.get("true_if", ()), *spec.get("false_if", ())):
                areas.add(item["area"])
        return areas

    def _requirement(self, rr_id: str, results: Mapping[str, DecisionResult],
                     inputs: Mapping[str, Any],
                     memo: dict[str, tuple[TriState, _Trace]]) -> ApplicableRequirement:
        entry = self._mapping["requirements"].get(rr_id)
        trace = _Trace(set(), {})
        evaluated: list[EvaluatedPredicate] = []

        def check(keys: Sequence[str]) -> TriState:
            values = []
            for key in keys:
                value = self._predicate(key, results, inputs, trace, memo)
                evaluated.append(EvaluatedPredicate(key, value))
                values.append(value)
            return _all_of(values)

        block = None
        if entry is None:
            status, reason, source = Applicability.APPLICABILITY_UNRESOLVED, "NO_MAPPING", "—"
        else:
            block = entry["block"]
            source = f"RR_APPLICABILITY.yaml#{rr_id} · {entry['evidence']}"
            status, reason = self._decide(entry, check)
            if reason == "SCOPE_INACTIVE" and trace.inactive_reason:
                reason = trace.inactive_reason

        determined = [results[area] for area in sorted(trace.areas) if area in results]
        rule_ids = sorted({e.rule_id for result in determined for e in result.executions})
        return ApplicableRequirement(
            applicable_requirement_id=str(uuid.uuid5(ID_NAMESPACE, f"applicability:{rr_id}:"
                                                     f"{sorted(inputs.items())}:"
                                                     f"{[r.decision_result_id for r in determined]}")),
            requirement_id=rr_id,
            applicability=status,
            reason_code=reason,
            block=block,
            evaluated_predicates=tuple(evaluated),
            supporting_rule_ids=tuple(rule_ids),
            relevant_inputs=tuple(sorted(trace.inputs.items())),
            source_of_applicability=source,
            determined_by=tuple(r.decision_result_id for r in determined),
        )

    def _decide(self, entry: Mapping[str, Any], check) -> tuple[Applicability, str]:
        scope = check(self._mapping["blocks"][entry["block"]]["scope"])
        if scope is TriState.FALSE:
            return Applicability.NOT_APPLICABLE, "SCOPE_INACTIVE"
        if scope is TriState.UNKNOWN:
            return Applicability.APPLICABILITY_UNRESOLVED, "SCOPE_UNRESOLVED"
        if entry["conditionality"] == "NOT_STATED":
            return Applicability.APPLICABILITY_UNRESOLVED, "CONDITIONALITY_NOT_DOCUMENTED"
        local = check(entry["local"]) if entry["local"] else TriState.TRUE
        if local is TriState.FALSE:
            return Applicability.NOT_APPLICABLE, "LOCAL_CONDITION_NOT_MET"
        if entry.get("local_not_modelled"):
            return Applicability.APPLICABILITY_UNRESOLVED, "LOCAL_CONDITION_NOT_MODELLED"
        if local is TriState.UNKNOWN:
            return Applicability.APPLICABILITY_UNRESOLVED, "LOCAL_CONDITION_UNRESOLVED"
        return (Applicability.APPLICABLE,
                "LOCAL_CONDITIONS_MET" if entry["local"] else "SCOPE_ACTIVE")
