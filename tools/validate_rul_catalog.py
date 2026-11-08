"""Formale Strukturprüfung des Katalogs der Entscheidungsregeln (RUL).

Der Validator prüft ausschließlich formale und strukturelle Konsistenz von
docs/03-regulatory/RUL_CATALOG.yaml nach docs/03-regulatory/RUL_METHOD.md. Er
trifft keine Aussage über regulatorische Richtigkeit; siehe tools/README.md.
Werkzeugbasis und führende Referenzdateien entsprechen ADR-0001.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import validate_rr_catalog as rr

CATALOG_PATH = Path("docs/03-regulatory/RUL_CATALOG.yaml")
METHOD_PATH = Path("docs/03-regulatory/RUL_METHOD.md")
COVERAGE_PATH = Path("docs/03-regulatory/COVERAGE_PLAN.md")

ROOT_FIELDS = ("version", "entry_points", "class_order", "outputs", "flags", "rules",
               "change_history")
RUL_FIELDS = (
    "id",
    "status",
    "category",
    "title",
    "question",
    "input_key",
    "input_type",
    "allowed_values",
    "value_labels",
    "decision_logic",
    "branches",
    "primary_legal_anchor",
    "guidance_anchor",
    "guidance_detail",
    "guidance_role",
    "rationale",
    "dependencies",
    "replaces",
    "replaced_by",
)
OUTPUT_FIELDS = ("type", "class", "label")
OUTPUT_OPTIONAL_FIELDS = ("aggregates_to", "applicable_from", "flags")
FLAG_FIELDS = ("label", "primary_legal_anchor")
BRANCH_FIELDS = frozenset({"when", "result", "next", "review", "review_cause", "basis",
                           "date_condition"})
DATE_KINDS = ("before", "on_or_after")

RUL_ID_PATTERN = re.compile(r"^RUL-\d{3}$")
LEVEL_ROW_PATTERN = re.compile(r"^\| (A|B) \| (.+?) \|", re.MULTILINE)

CATEGORY_MARKER = "Zulässige Kategorien:"
INPUT_TYPE_MARKER = "Zulässige Eingabetypen:"
GUIDANCE_ROLE_MARKER = "Zulässige Guidance-Rollen:"
OUTPUT_TYPE_MARKER = "Zulässige Ausgabetypen:"
BASIS_MARKER = "Zulässige Basis-Kennzeichnungen:"

REVIEW_TYPE = "REVIEW"
CLASS_CANDIDATE_TYPE = "CLASS_CANDIDATE"


def _is_iso_date(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _date_condition(value: Any) -> tuple[str, str] | None:
    """(Art, Stichtag) einer Datumsbedingung {before: D} bzw. {on_or_after: D}, sonst None."""
    if not isinstance(value, dict):
        return None
    kinds = [kind for kind in DATE_KINDS if kind in value]
    extra = set(value) - set(DATE_KINDS) - {"input_key"}
    if len(kinds) != 1 or extra or not _is_iso_date(value[kinds[0]]):
        return None
    return kinds[0], value[kinds[0]]


def _complementary(first: tuple[str, str] | None, second: tuple[str, str] | None) -> bool:
    return (first is not None and second is not None and first[1] == second[1]
            and {first[0], second[0]} == set(DATE_KINDS))


@dataclass(frozen=True)
class RulReferenceData:
    """Aus den führenden Dokumenten ausgelesene zulässige Werte."""

    source_ids: frozenset[str]
    status_values: frozenset[str]
    level_a_sources: frozenset[str]
    level_b_sources: frozenset[str]
    categories: frozenset[str]
    input_types: frozenset[str]
    guidance_roles: frozenset[str]
    output_types: frozenset[str]
    basis_values: frozenset[str]


def parse_marked_vocabulary(text: str, marker: str, label: str) -> frozenset[str]:
    """Wertezeile nach einem Marker lesen (gleiche Form wie das Statusvokabular)."""
    marker_index = text.find(marker)
    if marker_index == -1:
        raise rr.ReferenceDataError(f"{label} marker not found in RUL method")
    for line in text[marker_index + len(marker) :].splitlines():
        candidate = line.strip()
        if not candidate:
            continue
        if not rr.STATUS_LINE_PATTERN.fullmatch(candidate):
            raise rr.ReferenceDataError(
                f"{label} line does not consist solely of inline-code values: {candidate!r}"
            )
        values = [value.strip() for value in rr.INLINE_CODE_PATTERN.findall(candidate)]
        return rr._unique(values, label=label, origin="RUL method")
    raise rr.ReferenceDataError(f"no {label} values found after marker")


def parse_source_levels(text: str) -> tuple[frozenset[str], frozenset[str]]:
    """Ebene-A- und Ebene-B-Quellen aus der Quellenrollentabelle des Coverage-Plans lesen."""
    levels: dict[str, list[str]] = {}
    for level, cell in LEVEL_ROW_PATTERN.findall(text):
        if level in levels:
            continue
        levels[level] = [value for value in rr.INLINE_CODE_PATTERN.findall(cell)
                         if rr.SRC_ID_PATTERN.fullmatch(value)]
    for level in ("A", "B"):
        if not levels.get(level):
            raise rr.ReferenceDataError(
                f"no level {level} sources found in coverage plan source role table"
            )
    return (
        rr._unique(levels["A"], label="level A source", origin="coverage plan"),
        rr._unique(levels["B"], label="level B source", origin="coverage plan"),
    )


def load_reference_data(repo_root: Path = rr.REPO_ROOT) -> RulReferenceData:
    """Alle zulässigen Werte aus den führenden Dokumenten laden (fail-closed)."""
    method = rr._read_text(repo_root / METHOD_PATH)
    level_a, level_b = parse_source_levels(rr._read_text(repo_root / COVERAGE_PATH))
    return RulReferenceData(
        source_ids=rr.parse_source_ids(rr._read_text(repo_root / rr.SOURCES_PATH)),
        status_values=rr.parse_status_vocabulary(rr._read_text(repo_root / rr.CONVENTIONS_PATH)),
        level_a_sources=level_a,
        level_b_sources=level_b,
        categories=parse_marked_vocabulary(method, CATEGORY_MARKER, "category"),
        input_types=parse_marked_vocabulary(method, INPUT_TYPE_MARKER, "input type"),
        guidance_roles=parse_marked_vocabulary(method, GUIDANCE_ROLE_MARKER, "guidance role"),
        output_types=parse_marked_vocabulary(method, OUTPUT_TYPE_MARKER, "output type"),
        basis_values=parse_marked_vocabulary(method, BASIS_MARKER, "basis"),
    )


def _as_locator_reference(reference: RulReferenceData) -> rr.ReferenceData:
    return rr.ReferenceData(
        theme_clusters=frozenset(),
        lifecycle_phases=frozenset(),
        source_ids=reference.source_ids,
        status_values=reference.status_values,
    )


def _validate_root(catalog: Any, reference: RulReferenceData, errors: list[str]) -> bool:
    if not isinstance(catalog, dict):
        errors.append("root: catalog must be a mapping")
        return False
    for field in ROOT_FIELDS:
        if field not in catalog:
            errors.append(f"root: missing field '{field}'")
    for field in sorted(set(catalog) - set(ROOT_FIELDS)):
        errors.append(f"root: unexpected field '{field}'")

    version = catalog.get("version")
    if not isinstance(version, str) or not rr.VERSION_PATTERN.fullmatch(version):
        errors.append("root: version must be a string in MAJOR.MINOR form")

    class_order = catalog.get("class_order")
    if (not isinstance(class_order, list) or not class_order
            or not all(isinstance(item, str) for item in class_order)
            or len(set(class_order)) != len(class_order)):
        errors.append("root: class_order must be a non-empty list of unique strings")

    flags = catalog.get("flags")
    if not isinstance(flags, dict):
        errors.append("root: flags must be a mapping")
        flags = {}
    for name, spec in flags.items():
        label = f"flags.{name}"
        if not isinstance(spec, dict) or set(spec) != set(FLAG_FIELDS):
            errors.append(f"{label}: flag must have exactly the fields {FLAG_FIELDS}")
            continue
        rr._validate_text_pair(spec, "label", label, errors)
        _validate_anchor_list(spec, "primary_legal_anchor", reference.level_a_sources, "A",
                              label, reference, errors, required=True)
    outputs = catalog.get("outputs")
    if not isinstance(outputs, dict) or not outputs:
        errors.append("root: outputs must be a non-empty mapping")
    else:
        for name, spec in outputs.items():
            _validate_output(name, spec, catalog.get("class_order"), reference, errors)
            if isinstance(spec, dict):
                target = spec.get("aggregates_to")
                if target is not None and target not in outputs:
                    errors.append(f"outputs.{name}: aggregates_to must name a known output")
                if spec.get("applicable_from") is not None and not _is_iso_date(
                        spec["applicable_from"]):
                    errors.append(f"outputs.{name}: applicable_from must be an ISO date")
                for flag in spec.get("flags") or []:
                    if flag not in flags:
                        errors.append(f"outputs.{name}: unknown flag '{flag}'")

    if not isinstance(catalog.get("entry_points"), list) or not catalog.get("entry_points"):
        errors.append("root: entry_points must be a non-empty list")
    if not isinstance(catalog.get("rules"), list):
        errors.append("root: rules must be a list")
        return False
    return True


def _validate_output(name: Any, spec: Any, class_order: Any, reference: RulReferenceData,
                     errors: list[str]) -> None:
    label = f"outputs.{name}"
    if not isinstance(spec, dict):
        errors.append(f"{label}: output must be a mapping")
        return
    for field in OUTPUT_FIELDS:
        if field not in spec:
            errors.append(f"{label}: missing field '{field}'")
    for field in sorted(set(spec) - set(OUTPUT_FIELDS) - set(OUTPUT_OPTIONAL_FIELDS)):
        errors.append(f"{label}: unexpected field '{field}'")
    output_type = spec.get("type")
    if output_type not in reference.output_types:
        errors.append(f"{label}: unknown output type '{output_type}'")
    output_class = spec.get("class")
    if output_type == CLASS_CANDIDATE_TYPE:
        if not isinstance(class_order, list) or output_class not in class_order:
            errors.append(f"{label}: class candidate must name a class from class_order")
    elif output_class is not None:
        errors.append(f"{label}: only class candidates may name a class")
    rr._validate_text_pair(spec, "label", label, errors)


def _validate_anchor_list(entry: dict[str, Any], field: str, allowed: frozenset[str], level: str,
                          label: str, reference: RulReferenceData, errors: list[str],
                          required: bool) -> None:
    anchors = entry.get(field)
    if not isinstance(anchors, list) or (required and not anchors):
        errors.append(f"{label}: {field} must be a {'non-empty ' if required else ''}list")
        return
    locator_reference = _as_locator_reference(reference)
    for locator in anchors:
        rr._validate_locator(locator, field, label, locator_reference, errors)
        if isinstance(locator, str):
            head = locator.partition("#")[0]
            if head in reference.source_ids and head not in allowed:
                errors.append(
                    f"{label}: {field} must reference a level {level} source, found '{locator}'")


def _validate_anchors(entry: dict[str, Any], label: str, reference: RulReferenceData,
                      errors: list[str]) -> None:
    _validate_anchor_list(entry, "primary_legal_anchor", reference.level_a_sources, "A", label,
                          reference, errors, required=True)
    _validate_anchor_list(entry, "guidance_anchor", reference.level_b_sources, "B", label,
                          reference, errors, required=False)
    guidance = entry.get("guidance_anchor")
    role = entry.get("guidance_role")
    if isinstance(guidance, list) and not guidance:
        if role is not None or entry.get("guidance_detail") is not None:
            errors.append(f"{label}: guidance_role and guidance_detail must be null without "
                          "guidance_anchor")
    elif role not in reference.guidance_roles:
        errors.append(f"{label}: unknown guidance role '{role}'")


def _validate_inputs(entry: dict[str, Any], label: str, reference: RulReferenceData,
                     errors: list[str]) -> list[Any]:
    if not isinstance(entry.get("input_key"), str) or not entry["input_key"].strip():
        errors.append(f"{label}: input_key must be a non-empty string")
    input_type = entry.get("input_type")
    if input_type not in reference.input_types:
        errors.append(f"{label}: unknown input type '{input_type}'")
    allowed = entry.get("allowed_values")
    if input_type == "date":
        if not isinstance(allowed, list) or not all(isinstance(v, str) and not _is_iso_date(v)
                                                    for v in allowed):
            errors.append(f"{label}: date allowed_values must list non-date tokens only")
            return []
    elif not isinstance(allowed, list) or not allowed:
        errors.append(f"{label}: allowed_values must be a non-empty list")
        return []
    if len({repr(value) for value in allowed}) != len(allowed):
        errors.append(f"{label}: allowed_values must be unique")
    if input_type == "boolean" and sorted(allowed) != [False, True]:
        errors.append(f"{label}: boolean input must allow exactly true and false")

    labels = entry.get("value_labels")
    if input_type == "enum":
        if not isinstance(labels, dict) or set(labels) != set(allowed):
            errors.append(f"{label}: enum value_labels must cover exactly the allowed values")
        else:
            for value in allowed:
                rr._validate_text_pair(labels, value, f"{label}.value_labels", errors)
    elif labels is not None:
        errors.append(f"{label}: value_labels must be null for non-enum inputs")
    return allowed


def _validate_branches(entry: dict[str, Any], label: str, allowed: list[Any],
                       outputs: dict[str, Any], reference: RulReferenceData,
                       errors: list[str]) -> list[str]:
    branches = entry.get("branches")
    targets: list[str] = []
    if not isinstance(branches, list) or not branches:
        errors.append(f"{label}: branches must be a non-empty list")
        return targets
    covered: dict[str, list[Any]] = {}
    date_whens: list[tuple[str, str] | None] = []
    for index, branch in enumerate(branches):
        blabel = f"{label}.branches[{index}]"
        if not isinstance(branch, dict):
            errors.append(f"{blabel}: branch must be a mapping")
            continue
        for field in sorted(set(branch) - BRANCH_FIELDS):
            errors.append(f"{blabel}: unexpected field '{field}'")
        condition = branch.get("date_condition")
        if condition is not None and (_date_condition(condition) is None
                                      or not isinstance(condition.get("input_key"), str)):
            errors.append(f"{blabel}: date_condition needs input_key and one ISO before/on_or_after")
        if "when" not in branch:
            errors.append(f"{blabel}: missing field 'when'")
        elif isinstance(branch["when"], dict):
            if entry.get("input_type") != "date" or _date_condition(branch["when"]) is None \
                    or "input_key" in branch["when"]:
                errors.append(f"{blabel}: date 'when' needs a date input and one ISO "
                              "before/on_or_after")
            date_whens.append(_date_condition(branch["when"]))
        else:
            covered.setdefault(repr(branch["when"]), []).append(condition)
            if not any(type(branch["when"]) is type(v) and branch["when"] == v for v in allowed):
                errors.append(f"{blabel}: 'when' value {branch['when']!r} is not an allowed value")
        result = branch.get("result")
        target = branch.get("next")
        if result is None and target is None:
            errors.append(f"{blabel}: branch needs 'result' and/or 'next'")
        if result is not None and result not in outputs:
            errors.append(f"{blabel}: unknown output '{result}'")
        if target is not None:
            if not isinstance(target, str) or not RUL_ID_PATTERN.fullmatch(target):
                errors.append(f"{blabel}: next must be a RUL id")
            else:
                targets.append(target)
        review = branch.get("review")
        if review is not None:
            spec = outputs.get(review)
            if not isinstance(spec, dict) or spec.get("type") != REVIEW_TYPE:
                errors.append(f"{blabel}: review must name an output of type {REVIEW_TYPE}")
        result_is_review = isinstance(outputs.get(result), dict) and \
            outputs[result].get("type") == REVIEW_TYPE
        if review is not None or result_is_review:
            if "review_cause" not in branch:
                errors.append(f"{blabel}: review outcome requires review_cause")
            else:
                rr._validate_text_pair(branch, "review_cause", blabel, errors)
        elif "review_cause" in branch:
            errors.append(f"{blabel}: review_cause without review outcome")
        basis = branch.get("basis")
        if basis is not None and basis not in reference.basis_values:
            errors.append(f"{blabel}: unknown basis '{basis}'")
    exact = sorted(covered) == sorted(map(repr, allowed))
    for conditions in covered.values():
        single = len(conditions) == 1 and conditions[0] is None
        pair = len(conditions) == 2 and _complementary(
            _date_condition(conditions[0]), _date_condition(conditions[1])) \
            and conditions[0].get("input_key") == conditions[1].get("input_key")
        exact = exact and (single or pair)
    if not exact:
        errors.append(f"{label}: branches must cover each allowed value exactly once")
    if entry.get("input_type") == "date":
        if len(date_whens) != 2 or not _complementary(date_whens[0], date_whens[1]):
            errors.append(f"{label}: date input needs exactly two complementary date branches")
    elif date_whens:
        errors.append(f"{label}: date branches require input_type date")
    return targets


def _validate_rule(entry: Any, index: int, outputs: dict[str, Any], reference: RulReferenceData,
                   errors: list[str]) -> tuple[str | None, list[str]]:
    label = f"rules[{index}]"
    if not isinstance(entry, dict):
        errors.append(f"{label}: rule must be a mapping")
        return None, []
    raw_id = entry.get("id")
    valid_id = isinstance(raw_id, str) and RUL_ID_PATTERN.fullmatch(raw_id) is not None
    if valid_id:
        label = raw_id
    else:
        errors.append(f"{label}: id must match RUL-NNN")

    for field in RUL_FIELDS:
        if field not in entry:
            errors.append(f"{label}: missing field '{field}'")
    for field in sorted(set(entry) - set(RUL_FIELDS)):
        errors.append(f"{label}: unexpected field '{field}'")

    if entry.get("status") not in reference.status_values:
        errors.append(f"{label}: unknown status '{entry.get('status')}'")
    if entry.get("category") not in reference.categories:
        errors.append(f"{label}: unknown category '{entry.get('category')}'")
    for field in ("decision_logic", "rationale"):
        if not isinstance(entry.get(field), str) or not entry[field].strip():
            errors.append(f"{label}: {field} must be a non-empty string")
    detail = entry.get("guidance_detail")
    if detail is not None and (not isinstance(detail, str) or not detail.strip()):
        errors.append(f"{label}: guidance_detail must be null or a non-empty string")

    rr._validate_text_pair(entry, "title", label, errors)
    rr._validate_text_pair(entry, "question", label, errors)
    _validate_anchors(entry, label, reference, errors)
    allowed = _validate_inputs(entry, label, reference, errors)
    targets = _validate_branches(entry, label, allowed, outputs, reference, errors)
    return (raw_id if valid_id else None), targets


def _validate_graph(catalog: dict[str, Any], rules: dict[str, dict[str, Any]],
                    edges: dict[str, list[str]], errors: list[str]) -> None:
    known = set(rules)
    for source, targets in edges.items():
        for target in targets:
            if target not in known:
                errors.append(f"{source}: next references unknown rule '{target}'")
            elif rules[source].get("status") == "aktiv" and rules[target].get("status") != "aktiv":
                errors.append(f"{source}: active rule references inactive rule '{target}'")
            elif source not in (rules[target].get("dependencies") or []):
                errors.append(f"{target}: dependencies must contain predecessor '{source}'")
    for rule_id, entry in rules.items():
        dependencies = entry.get("dependencies")
        if not isinstance(dependencies, list):
            errors.append(f"{rule_id}: dependencies must be a list")
            continue
        for item in dependencies:
            if item not in known:
                errors.append(f"{rule_id}: dependencies references unknown rule '{item}'")
            elif item == rule_id:
                errors.append(f"{rule_id}: self-reference in dependencies")

    entry_points = [item for item in catalog.get("entry_points") or [] if isinstance(item, str)]
    for item in entry_points:
        if item not in known:
            errors.append(f"root: entry point '{item}' is not a known rule")
        elif rules[item].get("status") != "aktiv":
            errors.append(f"root: entry point '{item}' is not active")

    visiting: set[str] = set()
    done: set[str] = set()

    def visit(node: str) -> None:
        if node in done or node not in known:
            return
        if node in visiting:
            errors.append(f"{node}: rule graph contains a cycle")
            return
        visiting.add(node)
        for target in edges.get(node, []):
            visit(target)
        visiting.discard(node)
        done.add(node)

    for item in entry_points:
        visit(item)
    active = {rule_id for rule_id, entry in rules.items() if entry.get("status") == "aktiv"}
    for rule_id in sorted(active - done):
        errors.append(f"{rule_id}: rule is not reachable from any entry point")


def _validate_replacements(rules: dict[str, dict[str, Any]], errors: list[str]) -> None:
    for rule_id, entry in rules.items():
        for field, counterpart_field in (("replaces", "replaced_by"), ("replaced_by", "replaces")):
            value = entry.get(field)
            if not isinstance(value, list):
                errors.append(f"{rule_id}: {field} must be a list")
                continue
            for item in value:
                if item == rule_id:
                    errors.append(f"{rule_id}: self-reference in {field}")
                elif item not in rules:
                    errors.append(f"{rule_id}: {field} references unknown rule '{item}'")
                elif rule_id not in (rules[item].get(counterpart_field) or []):
                    errors.append(
                        f"{rule_id}: inconsistent replacement relation with '{item}'"
                    )


def validate_catalog(catalog: Any, reference: RulReferenceData) -> list[str]:
    """Bereits geladenes RUL-Katalogobjekt prüfen und alle Befunde sammeln."""
    errors: list[str] = []
    if not _validate_root(catalog, reference, errors):
        return errors
    rr._validate_change_history(catalog, errors)

    outputs = catalog["outputs"] if isinstance(catalog.get("outputs"), dict) else {}
    rules: dict[str, dict[str, Any]] = {}
    edges: dict[str, list[str]] = {}
    for index, entry in enumerate(catalog["rules"]):
        rule_id, targets = _validate_rule(entry, index, outputs, reference, errors)
        if rule_id is None:
            continue
        if rule_id in rules:
            errors.append(f"{rule_id}: duplicate RUL id")
            continue
        rules[rule_id] = entry
        edges[rule_id] = targets

    ids = [rule_id for rule_id in rules]
    if ids != sorted(ids):
        errors.append("rules: RUL ids must appear in ascending order")
    date_keys = {entry.get("input_key") for entry in rules.values()
                 if entry.get("input_type") == "date"}
    aggregation_targets = {spec.get("aggregates_to") for spec in outputs.values()
                           if isinstance(spec, dict)}
    for rule_id, entry in rules.items():
        for branch in entry.get("branches") or []:
            condition = branch.get("date_condition") if isinstance(branch, dict) else None
            if isinstance(condition, dict) and condition.get("input_key") not in date_keys:
                errors.append(f"{rule_id}: date_condition must reference a date input key")
        allowed = entry.get("allowed_values") or []
        if entry.get("input_type") == "derived" and len(allowed) > 1 and all(
                isinstance(value, str) for value in allowed):
            for value in allowed:
                if value not in aggregation_targets:
                    errors.append(f"{rule_id}: derived value '{value}' is no aggregates_to target")
    _validate_graph(catalog, rules, edges, errors)
    _validate_replacements(rules, errors)
    return errors


def validate_repository(repo_root: Path = rr.REPO_ROOT) -> list[str]:
    """Katalog und Referenzdaten aus dem Repository laden und prüfen."""
    reference = load_reference_data(repo_root)
    catalog = rr.load_catalog(repo_root / CATALOG_PATH)
    return validate_catalog(catalog, reference)


def main() -> int:
    if not rr.is_supported_python():
        running = ".".join(str(part) for part in sys.version_info[:3])
        minimum = ".".join(str(part) for part in rr.MINIMUM_PYTHON)
        print(f"ERROR: Python >= {minimum} is required; running Python {running}",
              file=sys.stderr)
        return 1
    try:
        errors = validate_repository()
    except (rr.ReferenceDataError, rr.CatalogLoadError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"RUL catalog validation: FAIL ({len(errors)} error(s))", file=sys.stderr)
        return 1
    catalog = rr.load_catalog(rr.REPO_ROOT / CATALOG_PATH)
    print("RUL catalog validation: PASS")
    print(f"version: {catalog['version']}")
    print(f"rules: {len(catalog['rules'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
