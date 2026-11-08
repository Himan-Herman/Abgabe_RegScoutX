"""Formale Strukturprüfung des fachlichen Datenmodells.

Prüft docs/04-architecture/DATA_MODEL.yaml auf auflösbare Typen, Enums,
Entitäts- und Katalogverweise. Keine Aussage über fachliche Angemessenheit;
Werkzeugbasis nach ADR-0001.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import validate_rr_catalog as rr

MODEL_PATH = Path("docs/04-architecture/DATA_MODEL.yaml")

ROOT_FIELDS = ("version", "description", "catalog_ref_kinds", "enums", "enum_labels",
               "value_objects", "entities", "change_history")
SCALAR_TYPES = frozenset({"uuid", "string", "text", "integer", "boolean", "date", "datetime",
                          "version", "scalar"})
ATTRIBUTE_FIELDS = frozenset({"type", "required"})
ENTITY_FIELDS = ("description", "identifier", "attributes", "invariants")
VALUE_OBJECT_FIELDS = ("description", "attributes")


def resolve_type(type_name: Any, model: dict[str, Any]) -> str | None:
    """Fehlermeldung für einen nicht auflösbaren Attributtyp, sonst None."""
    if not isinstance(type_name, str) or not type_name:
        return "type must be a non-empty string"
    if type_name.startswith("list:"):
        return resolve_type(type_name[len("list:"):], model)
    if type_name in SCALAR_TYPES:
        return None
    kind, _, target = type_name.partition(":")
    if kind == "enum":
        return None if target in (model.get("enums") or {}) else f"unknown enum '{target}'"
    if kind == "ref":
        return None if target in (model.get("entities") or {}) else f"unknown entity '{target}'"
    if kind == "value":
        return (None if target in (model.get("value_objects") or {})
                else f"unknown value object '{target}'")
    if kind == "catalog_ref":
        return (None if target in (model.get("catalog_ref_kinds") or [])
                else f"unknown catalog reference kind '{target}'")
    return f"unknown type '{type_name}'"


def _validate_attributes(owner: str, attributes: Any, model: dict[str, Any],
                         errors: list[str]) -> None:
    if not isinstance(attributes, dict) or not attributes:
        errors.append(f"{owner}: attributes must be a non-empty mapping")
        return
    for name, spec in attributes.items():
        label = f"{owner}.{name}"
        if not isinstance(spec, dict):
            errors.append(f"{label}: attribute must be a mapping")
            continue
        for field in sorted(ATTRIBUTE_FIELDS - set(spec)):
            errors.append(f"{label}: missing field '{field}'")
        for field in sorted(set(spec) - ATTRIBUTE_FIELDS):
            errors.append(f"{label}: unexpected field '{field}'")
        if not isinstance(spec.get("required"), bool):
            errors.append(f"{label}: required must be a boolean")
        problem = resolve_type(spec.get("type"), model)
        if problem:
            errors.append(f"{label}: {problem}")


def _validate_block(kind: str, block: Any, fields: tuple[str, ...], model: dict[str, Any],
                    errors: list[str]) -> None:
    if not isinstance(block, dict) or not block:
        errors.append(f"root: {kind} must be a non-empty mapping")
        return
    for name, spec in block.items():
        if not isinstance(spec, dict):
            errors.append(f"{kind}.{name}: must be a mapping")
            continue
        for field in fields:
            if field not in spec:
                errors.append(f"{kind}.{name}: missing field '{field}'")
        for field in sorted(set(spec) - set(fields)):
            errors.append(f"{kind}.{name}: unexpected field '{field}'")
        _validate_attributes(f"{kind}.{name}", spec.get("attributes"), model, errors)
        if kind == "entities":
            identifier = spec.get("identifier")
            attributes = spec.get("attributes") or {}
            if identifier not in attributes:
                errors.append(f"entities.{name}: identifier '{identifier}' is not an attribute")
            elif attributes[identifier].get("type") != "uuid" or \
                    attributes[identifier].get("required") is not True:
                errors.append(f"entities.{name}: identifier must be a required uuid")
            invariants = spec.get("invariants")
            if not isinstance(invariants, list) or not all(
                    isinstance(item, str) and item.strip() for item in invariants):
                errors.append(f"entities.{name}: invariants must be a list of strings")


def validate_model(model: Any) -> list[str]:
    """Bereits geladenes Datenmodell prüfen und alle Befunde sammeln."""
    errors: list[str] = []
    if not isinstance(model, dict):
        return ["root: data model must be a mapping"]
    for field in ROOT_FIELDS:
        if field not in model:
            errors.append(f"root: missing field '{field}'")
    for field in sorted(set(model) - set(ROOT_FIELDS)):
        errors.append(f"root: unexpected field '{field}'")
    version = model.get("version")
    if not isinstance(version, str) or not rr.VERSION_PATTERN.fullmatch(version):
        errors.append("root: version must be a string in MAJOR.MINOR form")
    rr._validate_change_history(model, errors)

    enums = model.get("enums")
    if not isinstance(enums, dict) or not enums:
        errors.append("root: enums must be a non-empty mapping")
        enums = {}
    for name, values in enums.items():
        if (not isinstance(values, list) or not values
                or len(set(map(str, values))) != len(values)):
            errors.append(f"enums.{name}: must be a non-empty list of unique values")
    for name, labels in (model.get("enum_labels") or {}).items():
        if name not in enums:
            errors.append(f"enum_labels.{name}: unknown enum")
            continue
        if not isinstance(labels, dict) or set(labels) != set(enums[name]):
            errors.append(f"enum_labels.{name}: labels must cover exactly the enum values")
            continue
        for value in labels:
            rr._validate_text_pair(labels, value, f"enum_labels.{name}", errors)

    _validate_block("value_objects", model.get("value_objects"), VALUE_OBJECT_FIELDS,
                    model, errors)
    _validate_block("entities", model.get("entities"), ENTITY_FIELDS, model, errors)
    return errors


def validate_repository(repo_root: Path = rr.REPO_ROOT) -> list[str]:
    return validate_model(rr.load_catalog(repo_root / MODEL_PATH))


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
        print(f"Data model validation: FAIL ({len(errors)} error(s))", file=sys.stderr)
        return 1
    model = rr.load_catalog(rr.REPO_ROOT / MODEL_PATH)
    print("Data model validation: PASS")
    print(f"version: {model['version']}")
    print(f"entities: {len(model['entities'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
