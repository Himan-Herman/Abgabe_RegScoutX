"""Formale Strukturprüfung der technischen RR-Applicability-Zuordnung.

Prüft docs/03-regulatory/RR_APPLICABILITY.yaml gegen RR-Katalog, RUL-Katalog
und Datenmodell: vollständige RR-Abdeckung, auflösbare Blöcke, Prädikate,
Eingaben, Ausgabecodes und Evidenzverweise, zyklenfreie Prädikate. Keine
Aussage über die fachliche Richtigkeit einer Bedingung; Werkzeugbasis nach
ADR-0001.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import validate_rr_catalog as rr

MAPPING_PATH = Path("docs/03-regulatory/RR_APPLICABILITY.yaml")
REGULATORY_DIR = Path("docs/03-regulatory")
DATA_MODEL_PATH = Path("docs/04-architecture/DATA_MODEL.yaml")
RUL_CATALOG_PATH = Path("docs/03-regulatory/RUL_CATALOG.yaml")

ROOT_FIELDS = ("version", "rr_catalog_version", "rul_catalog_version", "description",
               "profile_inputs", "predicates", "blocks", "requirements", "change_history")
INPUT_FIELDS = ("input_type", "allowed_values", "value_labels", "question", "source_of_condition")
BLOCK_FIELDS = ("description", "scope", "source_of_condition")
REQUIREMENT_FIELDS = ("block", "conditionality", "local", "local_not_modelled", "evidence")
CONDITIONALITY = ("REGULAR", "CONDITIONAL", "NOT_STATED")
PREDICATE_FIELDS = {
    "DECISION_OUTCOME": ("true_if", "false_if"),
    "MDR_CLASS": ("area", "classes"),
    "PROFILE_INPUT": ("input", "true_values"),
    "ALL_OF": ("of",),
    "ANY_OF": ("of",),
    "NOT_MODELLED": ("area", "reason", "missing_primary_law"),
}
COMMON_PREDICATE_FIELDS = ("kind", "description", "source_of_condition")
# Optionale Felder: Eingabewerte, bei denen das Prädikat fail-closed UNKNOWN ergibt.
OPTIONAL_PREDICATE_FIELDS = {"PROFILE_INPUT": ("unknown_values",)}


def _evidence_exists(reference: Any, repo_root: Path) -> bool:
    """Der erste Token eines Evidenzverweises muss eine vorhandene Datei in docs/03-regulatory sein."""
    if not isinstance(reference, str) or not reference.strip():
        return False
    return (repo_root / REGULATORY_DIR / reference.split()[0]).is_file()


def _check_fields(label: str, entry: Any, fields: tuple[str, ...], errors: list[str]) -> bool:
    if not isinstance(entry, dict):
        errors.append(f"{label}: must be a mapping")
        return False
    for field in fields:
        if field not in entry:
            errors.append(f"{label}: missing field '{field}'")
    for field in sorted(set(entry) - set(fields)):
        errors.append(f"{label}: unexpected field '{field}'")
    return True


def validate_mapping(mapping: Any, rr_catalog: dict[str, Any], rul_catalog: dict[str, Any],
                     data_model: dict[str, Any], repo_root: Path = rr.REPO_ROOT) -> list[str]:
    errors: list[str] = []
    if not _check_fields("root", mapping, ROOT_FIELDS, errors):
        return errors
    if not isinstance(mapping.get("version"), str) or not rr.VERSION_PATTERN.fullmatch(
            mapping["version"]):
        errors.append("root: version must be a string in MAJOR.MINOR form")
    rr._validate_change_history(mapping, errors)
    if mapping.get("rr_catalog_version") != rr_catalog.get("version"):
        errors.append("root: rr_catalog_version does not match RR catalog version "
                      f"'{rr_catalog.get('version')}'; impact review required")
    if mapping.get("rul_catalog_version") != rul_catalog.get("version"):
        errors.append("root: rul_catalog_version does not match RUL catalog version "
                      f"'{rul_catalog.get('version')}'; impact review required")

    areas = set(data_model["enums"]["decision_area"])
    reasons = set(data_model["enums"]["applicability_reason"])
    outputs = set(rul_catalog["outputs"])
    classes = set(rul_catalog["class_order"])
    inputs = mapping.get("profile_inputs") or {}
    predicates = mapping.get("predicates") or {}
    blocks = mapping.get("blocks") or {}

    for key, spec in inputs.items():
        label = f"profile_inputs.{key}"
        if not _check_fields(label, spec, INPUT_FIELDS, errors):
            continue
        allowed = spec.get("allowed_values")
        if spec.get("input_type") == "boolean":
            if allowed != [True, False] and allowed != [False, True]:
                errors.append(f"{label}: boolean input must allow exactly true and false")
            if spec.get("value_labels") is not None:
                errors.append(f"{label}: value_labels must be null for boolean inputs")
        elif spec.get("input_type") == "enum":
            labels = spec.get("value_labels")
            if not isinstance(allowed, list) or not allowed or not isinstance(labels, dict) \
                    or set(labels) != set(allowed):
                errors.append(f"{label}: enum value_labels must cover exactly the allowed values")
            else:
                for value in allowed:
                    rr._validate_text_pair(labels, value, f"{label}.value_labels", errors)
        else:
            errors.append(f"{label}: input_type must be boolean or enum")
        rr._validate_text_pair(spec, "question", label, errors)
        if not _evidence_exists(spec.get("source_of_condition"), repo_root):
            errors.append(f"{label}: source_of_condition must name an existing evidence file")

    for key, spec in predicates.items():
        label = f"predicates.{key}"
        kind = spec.get("kind") if isinstance(spec, dict) else None
        if kind not in PREDICATE_FIELDS:
            errors.append(f"{label}: unknown predicate kind '{kind}'")
            continue
        fields = COMMON_PREDICATE_FIELDS + PREDICATE_FIELDS[kind]
        optional = tuple(field for field in OPTIONAL_PREDICATE_FIELDS.get(kind, ())
                         if field in spec)
        if not _check_fields(label, spec, fields + optional, errors):
            continue
        rr._validate_text_pair(spec, "description", label, errors)
        if not _evidence_exists(spec.get("source_of_condition"), repo_root):
            errors.append(f"{label}: source_of_condition must name an existing evidence file")
        if kind == "DECISION_OUTCOME":
            if not spec["true_if"]:
                errors.append(f"{label}: true_if must not be empty")
            for item in (*spec["true_if"], *spec["false_if"]):
                if not isinstance(item, dict) or item.get("area") not in areas \
                        or item.get("outcome") not in outputs:
                    errors.append(f"{label}: condition {item!r} needs a known area and RUL output")
                elif set(item) - {"area", "outcome", "reason_code"}:
                    errors.append(f"{label}: condition {item!r} has unexpected fields")
            for item in spec["true_if"]:
                if isinstance(item, dict) and "reason_code" in item:
                    errors.append(f"{label}: reason_code is only allowed in false_if")
            for item in spec["false_if"]:
                if isinstance(item, dict) and "reason_code" in item \
                        and item["reason_code"] not in reasons:
                    errors.append(f"{label}: unknown reason_code '{item['reason_code']}'")
        elif kind == "MDR_CLASS":
            if spec["area"] not in areas:
                errors.append(f"{label}: unknown area '{spec['area']}'")
            if not spec["classes"] or not set(spec["classes"]) <= classes:
                errors.append(f"{label}: classes must be a non-empty subset of the RUL class_order")
        elif kind == "PROFILE_INPUT":
            definition = inputs.get(spec["input"])
            if definition is None:
                errors.append(f"{label}: unknown profile input '{spec['input']}'")
            elif not spec["true_values"] or any(
                    value not in definition["allowed_values"] for value in spec["true_values"]):
                errors.append(f"{label}: true_values must be allowed values of '{spec['input']}'")
            elif "unknown_values" in spec and (
                    not spec["unknown_values"]
                    or any(value not in definition["allowed_values"]
                           for value in spec["unknown_values"])
                    or any(value in spec["true_values"] for value in spec["unknown_values"])):
                errors.append(f"{label}: unknown_values must be allowed values of "
                              f"'{spec['input']}' disjoint from true_values")
        elif kind in ("ALL_OF", "ANY_OF"):
            if not spec["of"] or any(part not in predicates for part in spec["of"]):
                errors.append(f"{label}: 'of' must reference known predicates")
        elif kind == "NOT_MODELLED":
            if spec["area"] is not None and spec["area"] not in areas:
                errors.append(f"{label}: unknown area '{spec['area']}'")
            rr._validate_text_pair(spec, "reason", label, errors)
            if not isinstance(spec["missing_primary_law"], list):
                errors.append(f"{label}: missing_primary_law must be a list")

    visiting: set[str] = set()
    done: set[str] = set()

    def visit(key: str) -> None:
        if key in done or key not in predicates or not isinstance(predicates[key], dict):
            return
        if key in visiting:
            errors.append(f"predicates.{key}: cyclic predicate reference")
            return
        visiting.add(key)
        for part in predicates[key].get("of") or []:
            visit(part)
        visiting.discard(key)
        done.add(key)

    for key in predicates:
        visit(key)

    for key, spec in blocks.items():
        label = f"blocks.{key}"
        if not _check_fields(label, spec, BLOCK_FIELDS, errors):
            continue
        rr._validate_text_pair(spec, "description", label, errors)
        if not spec["scope"] or any(part not in predicates for part in spec["scope"]):
            errors.append(f"{label}: scope must reference known predicates")
        if not _evidence_exists(spec.get("source_of_condition"), repo_root):
            errors.append(f"{label}: source_of_condition must name an existing evidence file")

    requirements = mapping.get("requirements") or {}
    catalog_ids = [entry["id"] for entry in rr_catalog["requirements"]]
    for rr_id in catalog_ids:
        if rr_id not in requirements:
            errors.append(f"requirements: no mapping for '{rr_id}'")
    for rr_id in sorted(set(requirements) - set(catalog_ids)):
        errors.append(f"requirements: unknown RR id '{rr_id}'")
    used_blocks: set[str] = set()
    for rr_id, entry in requirements.items():
        label = f"requirements.{rr_id}"
        if not _check_fields(label, entry, REQUIREMENT_FIELDS, errors):
            continue
        used_blocks.add(entry["block"])
        if entry["block"] not in blocks:
            errors.append(f"{label}: unknown block '{entry['block']}'")
        if entry["conditionality"] not in CONDITIONALITY:
            errors.append(f"{label}: unknown conditionality '{entry['conditionality']}'")
        local = entry["local"]
        if not isinstance(local, list) or any(part not in predicates for part in local):
            errors.append(f"{label}: local must be a list of known predicates")
        not_modelled = entry["local_not_modelled"]
        if not_modelled is not None:
            rr._validate_text_pair(entry, "local_not_modelled", label, errors)
        if entry["conditionality"] == "REGULAR" and (local or not_modelled is not None):
            errors.append(f"{label}: a regular requirement must not have local conditions")
        if not _evidence_exists(entry.get("evidence"), repo_root):
            errors.append(f"{label}: evidence must name an existing evidence file")
    for key in sorted(set(blocks) - used_blocks):
        errors.append(f"blocks.{key}: block is not used by any requirement")
    return errors


def validate_repository(repo_root: Path = rr.REPO_ROOT) -> list[str]:
    return validate_mapping(
        rr.load_catalog(repo_root / MAPPING_PATH),
        rr.load_catalog(repo_root / rr.CATALOG_PATH),
        rr.load_catalog(repo_root / RUL_CATALOG_PATH),
        rr.load_catalog(repo_root / DATA_MODEL_PATH),
        repo_root,
    )


def main() -> int:
    if not rr.is_supported_python():
        print("ERROR: unsupported Python version", file=sys.stderr)
        return 1
    try:
        errors = validate_repository()
    except rr.CatalogLoadError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"RR applicability validation: FAIL ({len(errors)} error(s))", file=sys.stderr)
        return 1
    mapping = rr.load_catalog(rr.REPO_ROOT / MAPPING_PATH)
    counts: dict[str, int] = {}
    for entry in mapping["requirements"].values():
        counts[entry["conditionality"]] = counts.get(entry["conditionality"], 0) + 1
    print("RR applicability validation: PASS")
    print(f"version: {mapping['version']}")
    print(f"requirements: {len(mapping['requirements'])} "
          + " ".join(f"{key}={value}" for key, value in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
