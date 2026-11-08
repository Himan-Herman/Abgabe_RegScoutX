"""RULE_ENGINE: deterministische, kataloggetriebene Ausführung der Entscheidungsregeln (RUL).

Die Engine kennt keine regulatorischen Inhalte. Sie folgt ausschließlich den
Zweigen des RUL-Katalogs und wendet die in RUL_METHOD.md festgelegte Semantik
an: Klassenkandidaten werden nach class_order aggregiert, mitgeführte
Review-Ausgänge verhindern eine finale Klasse, fehlende Eingaben führen zu
einem unvollständigen Zustand statt zu einer Annahme. Keine generative KI,
keine Freitextauswertung.
"""

from __future__ import annotations

import json
import uuid
from dataclasses import dataclass, field
from datetime import date
from typing import Any, Mapping

from regscoutx.catalog_repository import CatalogRepository
from regscoutx.domain import (
    ID_NAMESPACE,
    DecisionResult,
    DecisionStatus,
    EngineRun,
    MissingInput,
    ReviewItem,
    RuleExecution,
)
from regscoutx.errors import (
    InvalidInputError,
    InvalidRuleReferenceError,
    RuleCycleError,
    UnexpectedEndStateError,
    UnsupportedDerivationError,
)

CLASS_CANDIDATE = "CLASS_CANDIDATE"
REVIEW = "REVIEW"
DERIVED = "derived"
DATE = "date"
BEFORE = "before"
ON_OR_AFTER = "on_or_after"

def _same(left: Any, right: Any) -> bool:
    """Gleichheit ohne Vermischung von bool und str bzw. int."""
    return type(left) is type(right) and left == right


def _as_date(value: Any) -> date | None:
    """ISO-Datum (JJJJ-MM-TT) als Zeichenkette; sonst None."""
    if not isinstance(value, str):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def _date_matches(condition: Mapping[str, Any], value: date) -> bool:
    """Datumsbedingung {before: D} bzw. {on_or_after: D} auswerten."""
    if BEFORE in condition:
        return value < date.fromisoformat(condition[BEFORE])
    return value >= date.fromisoformat(condition[ON_OR_AFTER])


def _condition_key(condition: Mapping[str, Any]) -> tuple[str, str]:
    kind = BEFORE if BEFORE in condition else ON_OR_AFTER
    return kind, condition[kind]

@dataclass
class _Step:
    rule: Mapping[str, Any]
    value: Any
    derived: bool
    branch: Mapping[str, Any]
    secondary: tuple[str, Any] | None = None


@dataclass
class _Walk:
    steps: list[_Step] = field(default_factory=list)
    missing: MissingInput | None = None


class RuleEngine:
    """Führt Regelpfade ab einer Einstiegsregel aus und protokolliert jeden Regelknoten."""

    def __init__(self, repository: CatalogRepository) -> None:
        self._repository = repository
        self._input_rules: dict[str, list[Mapping[str, Any]]] = {}
        for rule_id in repository.rule_ids:
            rule = repository.rule(rule_id)
            self._input_rules.setdefault(rule["input_key"], []).append(rule)

    # Eingaben -------------------------------------------------------------

    def _validate_inputs(self, inputs: Mapping[str, Any]) -> dict[str, Any]:
        if not isinstance(inputs, Mapping):
            raise InvalidInputError("<inputs>", inputs, "inputs must be a mapping")
        for key, value in inputs.items():
            rules = self._input_rules.get(key)
            if not rules:
                raise InvalidInputError(key, value, "unknown input key")
            for rule in rules:
                if rule["input_type"] == DERIVED:
                    raise InvalidInputError(key, value, "derived input must not be supplied")
                allowed = list(rule["allowed_values"])
                if any(_same(value, token) for token in allowed):
                    continue
                if rule["input_type"] == DATE and _as_date(value) is not None:
                    continue
                expected = "an ISO date or one of " if rule["input_type"] == DATE else ""
                raise InvalidInputError(key, value, f"value must be {expected}{allowed}")
        return dict(inputs)

    # Ableitung ------------------------------------------------------------

    def _derive(self, rule: Mapping[str, Any], walk: _Walk) -> Any:
        """Abgeleitete Eingaben nach zwei generischen, typbasierten Regeln.

        1. Genau ein zulässiger Wert: dieser Wert (der Knoten ist nur über den
           Pfad erreichbar, der ihn impliziert).
        2. Boolesch: true, wenn auf dem Pfad in derselben Kategorie bereits ein
           Klassenkandidat oder ein Review-Ausgang entstanden ist.
        3. Aufzählung: der erste zulässige Wert in Katalogreihenfolge, der als
           aggregates_to eines auf dem Pfad in derselben Kategorie erzeugten
           Ergebnisses auftritt (Aggregation paralleler Routen).
        Jede andere Form wird fail-closed abgelehnt.
        """
        allowed = list(rule["allowed_values"])
        if len(allowed) == 1:
            return allowed[0]
        if all(isinstance(value, str) for value in allowed):
            produced = {self._repository.output(step.branch["result"]).get("aggregates_to")
                        for step in walk.steps
                        if step.rule["category"] == rule["category"] and step.branch.get("result")}
            for value in allowed:
                if value in produced:
                    return value
            raise UnsupportedDerivationError(rule["id"], rule["input_key"])
        if sorted(allowed, key=repr) == [False, True]:
            category = rule["category"]
            for step in walk.steps:
                if step.rule["category"] != category:
                    continue
                result = step.branch.get("result")
                if step.branch.get("review") or (
                        result and self._repository.output(result)["type"] in (CLASS_CANDIDATE, REVIEW)):
                    return True
            return False
        raise UnsupportedDerivationError(rule["id"], rule["input_key"])

    def input_keys(self, entry_rule: str) -> frozenset[str]:
        """Nicht abgeleitete Eingabeschlüssel aller ab entry_rule erreichbaren Regeln.

        Umfasst Datumseingänge aus date_condition; dient der Zuordnung einer
        flachen Produkteingabe zu den Einstiegspunkten.
        """
        keys: set[str] = set()
        pending, seen = [entry_rule], set()
        while pending:
            rule = self._repository.rule(pending.pop())
            if rule["id"] in seen:
                continue
            seen.add(rule["id"])
            if rule["input_type"] != DERIVED:
                keys.add(rule["input_key"])
            for branch in rule["branches"]:
                if branch.get("date_condition"):
                    keys.add(branch["date_condition"]["input_key"])
                if branch.get("next"):
                    pending.append(branch["next"])
        return frozenset(keys)

    # Ausführung -----------------------------------------------------------

    def _walk(self, entry_rule: str, inputs: Mapping[str, Any]) -> _Walk:
        walk = _Walk()
        visited: set[str] = set()
        current: str | None = entry_rule
        while current is not None:
            if current in visited:
                raise RuleCycleError(current)
            visited.add(current)
            rule = self._repository.rule(current)
            key = rule["input_key"]
            derived = rule["input_type"] == DERIVED
            if derived:
                value = self._derive(rule, walk)
            elif key in inputs:
                value = inputs[key]
            else:
                walk.missing = MissingInput(current, key)
                return walk
            matches = self._matching(rule, value)
            secondary = None
            conditioned = [branch for branch in matches if branch.get("date_condition")]
            if conditioned:
                other_key = conditioned[0]["date_condition"]["input_key"]
                if other_key not in inputs:
                    walk.missing = MissingInput(current, other_key)
                    return walk
                other = _as_date(inputs[other_key])
                if other is None:
                    raise InvalidInputError(other_key, inputs[other_key], "an ISO date is required")
                secondary = (other_key, inputs[other_key])
                matches = [branch for branch in matches if not branch.get("date_condition")
                           or _date_matches(branch["date_condition"], other)]
            if len(matches) != 1:
                raise UnexpectedEndStateError(current, f"no unique branch for {value!r}")
            branch = matches[0]
            for name in (branch.get("result"), branch.get("review")):
                if name is not None:
                    self._repository.output(name)
            target = branch.get("next")
            if target is None and branch.get("result") is None:
                raise UnexpectedEndStateError(current, "branch has neither result nor next rule")
            if target is not None and not self._repository.has_rule(target):
                raise InvalidRuleReferenceError(current, target)
            walk.steps.append(_Step(rule, value, derived, branch, secondary))
            current = target
        return walk

    def _matching(self, rule: Mapping[str, Any], value: Any) -> list[Mapping[str, Any]]:
        """Zweige zum Eingabewert; Datumszweige vergleichen ISO-Daten mit before/on_or_after."""
        as_date = _as_date(value) if rule["input_type"] == DATE else None
        matches = []
        for branch in rule["branches"]:
            when = branch["when"]
            if isinstance(when, Mapping):
                if as_date is not None and _date_matches(when, as_date):
                    matches.append(branch)
            elif _same(when, value):
                matches.append(branch)
        return matches

    def evaluate(self, entry_rule: str, inputs: Mapping[str, Any]) -> EngineRun:
        """Regelpfad ab entry_rule deterministisch ausführen.

        Ungültige Eingaben lösen InvalidInputError aus. Fehlt ein
        entscheidungsnotwendiger Wert, endet der Pfad mit dem Status INCOMPLETE.
        """
        self._repository.rule(entry_rule)
        valid_inputs = self._validate_inputs(inputs)
        walk = self._walk(entry_rule, valid_inputs)
        snapshot = tuple(sorted(valid_inputs.items()))
        versions = self._repository.versions
        run_id = str(uuid.uuid5(ID_NAMESPACE, json.dumps(
            [entry_rule, list(map(list, snapshot)), list(vars(versions).values())],
            sort_keys=True)))
        results = self._decision_results(run_id, walk)
        return EngineRun(
            run_id=run_id,
            entry_rule=entry_rule,
            catalog_versions=versions,
            input_snapshot=snapshot,
            rule_path=tuple(step.rule["id"] for step in walk.steps),
            decision_results=results,
            missing_input=walk.missing,
        )

    # Ergebnisbildung ------------------------------------------------------

    def _groups(self, walk: _Walk) -> list[tuple[str, list[_Step]]]:
        groups: list[tuple[str, list[_Step]]] = []
        for step in walk.steps:
            category = step.rule["category"]
            if groups and groups[-1][0] == category:
                groups[-1][1].append(step)
            else:
                groups.append((category, [step]))
        if walk.missing is not None:
            category = self._repository.rule(walk.missing.rule_id)["category"]
            if not groups or groups[-1][0] != category:
                groups.append((category, []))
        return groups

    def _decision_results(self, run_id: str, walk: _Walk) -> tuple[DecisionResult, ...]:
        groups = self._groups(walk)
        results: list[DecisionResult] = []
        sequence = 0
        for index, (area, steps) in enumerate(groups):
            result_id = str(uuid.uuid5(ID_NAMESPACE, f"{run_id}:{index}:{area}"))
            executions = []
            for step in steps:
                sequence += 1
                executions.append(self._execution(result_id, sequence, step))
            is_last = index == len(groups) - 1
            missing = walk.missing if is_last else None
            results.append(self._decision(result_id, area, steps, tuple(executions), missing))
        return tuple(results)

    def _execution(self, result_id: str, sequence: int, step: _Step) -> RuleExecution:
        rule, branch = step.rule, step.branch
        return RuleExecution(
            execution_id=str(uuid.uuid5(ID_NAMESPACE, f"{result_id}:{sequence}")),
            decision_result_id=result_id,
            sequence=sequence,
            rule_id=rule["id"],
            input_key=rule["input_key"],
            received_value=step.value,
            derived_input=step.derived,
            matched_condition=self._describe(branch),
            output=branch.get("result"),
            next_rule=branch.get("next"),
            review=branch.get("review"),
            basis=branch.get("basis"),
            primary_legal_anchor=tuple(rule["primary_legal_anchor"]),
            guidance_anchor=tuple(rule["guidance_anchor"]),
        )

    @staticmethod
    def _describe(branch: Mapping[str, Any]) -> Any:
        """Unveränderliche Beschreibung des gewählten Zweigs für das Protokoll."""
        when = branch["when"]
        described = _condition_key(when) if isinstance(when, Mapping) else when
        if branch.get("date_condition"):
            condition = branch["date_condition"]
            return (described, condition["input_key"], _condition_key(condition))
        return described

    def _decision(self, result_id: str, area: str, steps: list[_Step],
                  executions: tuple[RuleExecution, ...],
                  missing: MissingInput | None) -> DecisionResult:
        candidates: list[tuple[str, str]] = []
        reviews: list[ReviewItem] = []
        flags: list[str] = []
        outcome: str | None = None
        for step in steps:
            result = step.branch.get("result")
            if result is not None:
                outcome = result
                spec = self._repository.output(result)
                if spec["type"] == CLASS_CANDIDATE:
                    candidates.append((step.rule["id"], spec["class"]))
                elif spec["type"] == REVIEW:
                    reviews.append(ReviewItem(step.rule["id"], result, self._describe(step.branch)))
                for flag in spec.get("flags") or ():
                    if flag not in flags:
                        flags.append(flag)
            if step.branch.get("review"):
                reviews.append(ReviewItem(step.rule["id"], step.branch["review"],
                                          self._describe(step.branch)))

        mdr_class = None
        if missing is not None:
            status, outcome = DecisionStatus.INCOMPLETE, None
        elif reviews:
            status, outcome = DecisionStatus.REVIEW_REQUIRED, reviews[-1].output
        else:
            status = DecisionStatus.DECIDED
            if outcome is None:
                raise UnexpectedEndStateError(steps[-1].rule["id"], "area ended without result")
            if candidates and self._repository.output(outcome)["type"] != CLASS_CANDIDATE:
                order = self._repository.class_order
                mdr_class = max((cls for _, cls in candidates), key=order.index)
            elif candidates:
                raise UnexpectedEndStateError(steps[-1].rule["id"],
                                              "classification ended on a class candidate")
        applicable_from = None
        if status is DecisionStatus.DECIDED:
            dates = [spec["applicable_from"] for spec in
                     (self._repository.output(step.branch["result"]) for step in steps
                      if step.branch.get("result"))
                     if spec.get("applicable_from") and spec.get("aggregates_to") == outcome]
            applicable_from = min(dates) if dates else None
        return DecisionResult(
            decision_result_id=result_id,
            area=area,
            status=status,
            outcome=outcome,
            mdr_class=mdr_class,
            class_candidates=tuple(candidates),
            reviews=tuple(reviews),
            missing_input=missing,
            executions=executions,
            applicable_from=applicable_from,
            compliance_flags=tuple(flags),
        )
