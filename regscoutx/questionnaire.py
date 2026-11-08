"""ASSESSMENT_SERVICE: adaptiver, segmentierter Fragebogen aus Katalog und Regelpfaden.

Die Oberfläche erhält hier – nicht aus eigener Logik – welche Fragen gestellt
werden, warum eine Folgefrage erscheint (DI-004), welche Werte, Formate und
Folgen vor der Eingabe gelten (DI-006) und den semantischen Fortschritt je
Segment (DI-001). Grundlage sind ausschließlich der RUL-Katalog (Folgeregeln je
Zweig), die Applicability-Zuordnung und die gespeicherte Auswertung. Es wird
keine Entscheidung getroffen oder vorweggenommen.

Segmentierung: RUL-Fragen nach Regelkategorie; Applicability-Eingaben nach den
Blöcken, die sie auswerten. Eine Applicability-Eingabe wird gefragt, sobald eine
Anforderung ein Prädikat mit dieser Eingabe tatsächlich auswertet (d. h. ihr
übergeordneter Bereich nicht inaktiv ist).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from regscoutx.assessment_service import Assessment
from regscoutx.catalog_repository import CatalogRepository
from regscoutx.domain import LocalizedText
from regscoutx.rule_engine import RuleEngine

WIZARD_ENTRIES = ("RUL-001", "RUL-027")
RULE_SEGMENTS = {"QUALIFICATION": "qualification", "BOUNDARY": "qualification",
                 "CLASSIFICATION": "classification", "AI_ACT_APPLICABILITY": "ai_act"}
# Segment einer Applicability-Eingabe: zuerst nach dokumentierter Herkunft (source_of_condition),
# für Normeingaben nach dem Normblock, der sie auswertet.
SOURCE_SEGMENTS = (("RR_EXTRACTION_MDR", "mdr_context"), ("RR_EXTRACTION_SRC_009", "eifu"))
BLOCK_SEGMENTS = (("NORM_SRC_005", "qms"),
                  ("NORM_SRC_007", "software_lifecycle"), ("NORM_SRC_008", "usability"),
                  ("SRC009_", "eifu"), ("MDR_", "mdr_context"))
SEGMENT_ORDER = ("qualification", "classification", "ai_act", "mdr_context", "eifu", "qms",
                 "software_lifecycle", "usability")
SEGMENT_AREAS = {"qualification": ("QUALIFICATION", "BOUNDARY"),
                 "classification": ("CLASSIFICATION",), "ai_act": ("AI_ACT_APPLICABILITY",)}
SEGMENT_ENTRIES = {"qualification": "RUL-001", "classification": "RUL-001", "ai_act": "RUL-027"}


@dataclass(frozen=True)
class Option:
    value: Any
    label: LocalizedText | None
    consequence_kind: str | None  # RESULT | REVIEW | NEXT
    consequence: LocalizedText | None


@dataclass(frozen=True)
class Reason:
    kind: str  # ENTRY | FOLLOWS | REQUIRED_BY
    rule_id: str | None
    question: LocalizedText | None
    answer: Any
    answer_label: LocalizedText | None
    blocks: tuple[tuple[str, LocalizedText, int], ...]


@dataclass(frozen=True)
class Question:
    key: str
    source: str  # RUL | PROFILE
    rule_id: str | None
    segment: str
    text: LocalizedText
    input_type: str  # boolean | enum | date
    options: tuple[Option, ...]
    date_thresholds: tuple[str, ...]
    answer: Any
    answered: bool
    reason: Reason


@dataclass(frozen=True)
class Segment:
    segment: str
    status: str  # COMPLETE | OPEN | REVIEW | NOT_REQUIRED | WAITING
    answered: int
    open: int
    outcome: str | None
    outcome_label: LocalizedText | None
    questions: tuple[Question, ...]


@dataclass(frozen=True)
class QuestionnaireView:
    segments: tuple[Segment, ...]
    stale: tuple[Question, ...]
    next_question: str | None


def _pair(value: Mapping[str, str] | None) -> LocalizedText | None:
    return None if value is None else LocalizedText(value["de"], value["en"])


class Questionnaire:

    def __init__(self, catalogs: CatalogRepository) -> None:
        self._catalogs = catalogs
        self._rules = RuleEngine(catalogs)
        self._entry_keys = {entry: self._rules.input_keys(entry) for entry in WIZARD_ENTRIES}
        self._input_rules: dict[str, Mapping[str, Any]] = {}
        for rule_id in catalogs.rule_ids:
            rule = catalogs.rule(rule_id)
            if rule["input_type"] != "derived":
                self._input_rules.setdefault(rule["input_key"], rule)
        mapping = catalogs.applicability
        self._profile = mapping["profile_inputs"]
        self._predicates = mapping["predicates"]
        self._blocks = mapping["blocks"]
        self._pred_inputs: dict[str, frozenset[str]] = {}
        self._input_blocks: dict[str, set[str]] = {}
        for block, spec in self._blocks.items():
            for predicate in spec["scope"]:
                for key in self._inputs(predicate):
                    self._input_blocks.setdefault(key, set()).add(block)
        for entry in mapping["requirements"].values():
            for predicate in entry["local"] or ():
                for key in self._inputs(predicate):
                    self._input_blocks.setdefault(key, set()).add(entry["block"])

    def _inputs(self, predicate: str) -> frozenset[str]:
        if predicate not in self._pred_inputs:
            spec = self._predicates[predicate]
            if spec["kind"] == "PROFILE_INPUT":
                value = frozenset({spec["input"]})
            elif spec["kind"] in ("ALL_OF", "ANY_OF"):
                value = frozenset().union(*(self._inputs(part) for part in spec["of"]))
            else:
                value = frozenset()
            self._pred_inputs[predicate] = value
        return self._pred_inputs[predicate]

    def _profile_segment(self, key: str) -> str:
        source = self._profile[key].get("source_of_condition") or ""
        for prefix, segment in SOURCE_SEGMENTS:
            if source.startswith(prefix):
                return segment
        blocks = self._input_blocks.get(key, set())
        for prefix, segment in BLOCK_SEGMENTS:
            if any(block.startswith(prefix) for block in blocks):
                return segment
        return "mdr_context"

    # Fragen -----------------------------------------------------------------

    def _rule_options(self, rule: Mapping[str, Any]) -> tuple[Option, ...]:
        labels = rule.get("value_labels") or {}
        options = []
        for value in rule["allowed_values"]:
            branch = next((b for b in rule["branches"]
                           if not isinstance(b["when"], Mapping) and type(b["when"]) is type(value)
                           and b["when"] == value), None)
            kind = consequence = None
            if branch is not None:
                if branch.get("result"):
                    output = self._catalogs.output(branch["result"])
                    kind = "REVIEW" if output["type"] == "REVIEW" else "RESULT"
                    consequence = _pair(output["label"])
                elif branch.get("review"):
                    kind, consequence = "REVIEW", _pair(self._catalogs.output(branch["review"])["label"])
                elif branch.get("next"):
                    kind, consequence = "NEXT", _pair(self._catalogs.rule(branch["next"])["title"])
            label = labels.get(value) if isinstance(value, str) else None
            options.append(Option(value, _pair(label), kind, consequence))
        return tuple(options)

    @staticmethod
    def _thresholds(rule: Mapping[str, Any]) -> tuple[str, ...]:
        dates = set()
        for branch in rule["branches"]:
            for condition in (branch["when"], branch.get("date_condition")):
                if isinstance(condition, Mapping):
                    dates |= {v for k, v in condition.items() if k in ("before", "on_or_after")}
        return tuple(sorted(dates))

    def _label(self, rule: Mapping[str, Any], value: Any) -> LocalizedText | None:
        labels = rule.get("value_labels") or {}
        return _pair(labels.get(value)) if isinstance(value, str) else None

    def _rule_question(self, key: str, answer: Any, answered: bool, reason: Reason,
                       rule_id: str | None = None) -> Question:
        # Gemeinsame Eingaben können je Rechtsweg andere Stichtage erläutern.
        # Für erreichte/offene Fragen gilt daher der konkrete Regelknoten.
        rule = self._catalogs.rule(rule_id) if rule_id is not None else self._input_rules[key]
        return Question(key=key, source="RUL", rule_id=rule["id"],
                        segment=RULE_SEGMENTS.get(rule["category"], "qualification"),
                        text=_pair(rule["question"]), input_type=rule["input_type"],
                        options=() if rule["input_type"] == "date" else self._rule_options(rule),
                        date_thresholds=self._thresholds(rule), answer=answer, answered=answered,
                        reason=reason)

    def _profile_question(self, key: str, answer: Any, answered: bool, reason: Reason) -> Question:
        spec = self._profile[key]
        labels = spec.get("value_labels") or {}
        options = tuple(Option(v, _pair(labels.get(v)) if isinstance(v, str) else None, None, None)
                        for v in spec["allowed_values"])
        return Question(key=key, source="PROFILE", rule_id=None, segment=self._profile_segment(key),
                        text=_pair(spec["question"]), input_type=spec["input_type"],
                        options=options, date_thresholds=(), answer=answer, answered=answered,
                        reason=reason)

    def _rule_questions(self, profile: Mapping[str, Any]) -> tuple[list[Question], set[str], set[str]]:
        questions: list[Question] = []
        used: set[str] = set()
        complete: set[str] = set()
        for entry in WIZARD_ENTRIES:
            inputs = {k: v for k, v in profile.items() if k in self._entry_keys[entry]}
            run = self._rules.evaluate(entry, inputs)
            previous: tuple[Mapping[str, Any], Any] | None = None

            def reason() -> Reason:
                if previous is None:
                    return Reason("ENTRY", None, None, None, None, ())
                rule, value = previous
                return Reason("FOLLOWS", rule["id"], _pair(rule["question"]), value,
                              self._label(rule, value), ())

            for decision in run.decision_results:
                for execution in decision.executions:
                    rule = self._catalogs.rule(execution.rule_id)
                    if execution.derived_input:
                        continue
                    questions.append(self._rule_question(execution.input_key, execution.received_value,
                                                         True, reason(), execution.rule_id))
                    used.add(execution.input_key)
                    condition = execution.matched_condition
                    if isinstance(condition, tuple) and len(condition) == 3:
                        other = condition[1]
                        questions.append(self._rule_question(other, profile.get(other), True, reason()))
                        used.add(other)
                    previous = (rule, execution.received_value)
            if run.missing_input is not None:
                key = run.missing_input.input_key
                questions.append(self._rule_question(key, None, False, reason(), run.missing_input.rule_id))
                used.add(key)
            else:
                complete.add(entry)
        return questions, used, complete

    def build(self, assessment: Assessment) -> QuestionnaireView:
        profile = dict(assessment.profile.answers)
        questions, used, complete = self._rule_questions(profile)
        demand: dict[str, dict[str, int]] = {}
        for result in assessment.results:
            for predicate in result.applicability.evaluated_predicates:
                for key in self._inputs(predicate.predicate_key):
                    block = result.applicability.block
                    counts = demand.setdefault(key, {})
                    counts[block] = counts.get(block, 0) + 1
        for key in self._profile:
            if key not in demand:
                continue
            blocks = tuple((block, _pair(self._blocks[block]["description"]), count)
                           for block, count in sorted(demand[key].items()))
            questions.append(self._profile_question(key, profile.get(key), key in profile,
                                                    Reason("REQUIRED_BY", None, None, None, None,
                                                           blocks)))
            used.add(key)
        stale = tuple(
            (self._rule_question(key, value, True, Reason("ENTRY", None, None, None, None, ()))
             if key in self._input_rules else
             self._profile_question(key, value, True, Reason("ENTRY", None, None, None, None, ())))
            for key, value in profile.items() if key not in used)
        decisions = {d.area: d for d in assessment.decision_results}
        segments = []
        for segment in SEGMENT_ORDER:
            items = tuple(q for q in questions if q.segment == segment)
            open_count = sum(1 for q in items if not q.answered)
            outcome = label = None
            status = "COMPLETE" if items and not open_count else ("OPEN" if open_count else "WAITING")
            for area in SEGMENT_AREAS.get(segment, ()):
                decision = decisions.get(area)
                if decision is None or decision.status.value == "NOT_EVALUATED":
                    continue
                if decision.status.value == "REVIEW_REQUIRED":
                    status = "REVIEW"
                if decision.outcome is not None:
                    outcome = decision.outcome
                    label = LocalizedText(
                        *(self._catalogs.output(decision.outcome)["label"][lang] for lang in ("de", "en")))
            if segment in SEGMENT_ENTRIES and not items and SEGMENT_ENTRIES[segment] in complete:
                status = "NOT_REQUIRED"
            segments.append(Segment(segment, status, sum(1 for q in items if q.answered), open_count,
                                    outcome, label, items))
        next_question = next((q.key for s in segments for q in s.questions if not q.answered), None)
        return QuestionnaireView(tuple(segments), stale, next_question)
