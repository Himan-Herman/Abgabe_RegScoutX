"""Formale Strukturprüfung des Maßnahmenkatalogs (RR_MEASURE, SR-043).

Prüft docs/03-regulatory/RR_MEASURE_CATALOG.yaml gegen den RR-Katalog und das
Datenmodell: Schema, gültige Nachweisarten, Mapping-Status, Mapping-Basis,
Zuordnungsregel, Wortlautanker und Begründung für jede RR, referenzielle
Gültigkeit der measure_keys, keine verwaisten Maßnahmen oder Nachweisarten und
Reproduzierbarkeit der regelbasierten Zuordnung (TRIGGER) aus den trigger_pattern.
Adjudizierte Zuordnungen (ADJ-*) haben Vorrang vor der regelbasierten Zuordnung
und müssen die Maßnahme ihrer Regel tragen. Keine Aussage über die fachliche
Angemessenheit einer Maßnahme; Werkzeugbasis nach ADR-0001.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import validate_rr_catalog as rr

CATALOG_PATH = Path("docs/03-regulatory/RR_MEASURE_CATALOG.yaml")
DATA_MODEL_PATH = Path("docs/04-architecture/DATA_MODEL.yaml")

ROOT_FIELDS = ("version", "rr_catalog_version", "description", "mapping_bases", "explicit_evidence_terms",
               "adjudication_rules", "evidence_types", "measures", "requirements", "change_history")
TEXT_FIELDS = ("label", "description")
RULE_FIELDS = ("measure", "label", "description")
MEASURE_FIELDS = ("label", "evidence_types", "trigger_pattern")
MAPPING_FIELDS = ("status", "measures", "basis", "mapping_basis", "mapping_rule", "rationale")
MAPPING_STATUS = ("MAPPED", "REVIEW_REQUIRED")
MAPPING_BASES = ("SOURCE_EXPLICIT", "PROJECT_DERIVED")
TRIGGER_RULE = "TRIGGER"
CATALOG_REF_KIND = "RR_MEASURE"


def _check_fields(label: str, entry: Any, fields: tuple[str, ...], errors: list[str]) -> bool:
    if not isinstance(entry, dict):
        errors.append(f"{label}: must be a mapping")
        return False
    for field in fields:
        if field not in entry:
            errors.append(f"{label}: missing field '{field}'")
    for field in sorted(set(entry) - set(fields)):
        errors.append(f"{label}: unexpected field '{field}'")
    return set(fields) <= set(entry)


def _check_texts(label: str, entry: Any, fields: tuple[str, ...], errors: list[str]) -> bool:
    if not _check_fields(label, entry, fields, errors):
        return False
    for field in TEXT_FIELDS:
        rr._validate_text_pair(entry, field, label, errors)
    return True


def classify(text: str, patterns: list[tuple[str, re.Pattern[str]]]) -> tuple[str | None, str | None]:
    """Erste passende Maßnahme in Katalogreihenfolge und der gefundene Wortlaut."""
    for key, pattern in patterns:
        match = pattern.search(text)
        if match:
            return key, match.group(0)
    return None, None


def mapping_basis_of(wording: str, explicit: re.Pattern[str]) -> str:
    """Mapping-Basis einer regelbasierten Zuordnung aus ihrem Wortlaut."""
    return "SOURCE_EXPLICIT" if explicit.search(wording) else "PROJECT_DERIVED"


def _validate_mapping(label: str, mapping: dict[str, Any], text: str, measures: dict[str, Any],
                      rules: dict[str, Any], patterns: list[tuple[str, re.Pattern[str]]] | None,
                      explicit: re.Pattern[str] | None, errors: list[str]) -> None:
    status, keys, basis = mapping["status"], mapping["measures"], mapping["basis"]
    kind, rule, rationale = mapping["mapping_basis"], mapping["mapping_rule"], mapping["rationale"]
    if status not in MAPPING_STATUS:
        errors.append(f"{label}: unknown status '{status}'")
        return
    if not isinstance(keys, list) or any(key not in measures for key in keys):
        errors.append(f"{label}: measures must reference known measure_keys")
        return
    if not isinstance(rationale, str) or not rationale.strip():
        errors.append(f"{label}: rationale must be a non-empty string")
    if status == "REVIEW_REQUIRED":
        if keys or basis is not None or kind is not None or rule is not None:
            errors.append(f"{label}: REVIEW_REQUIRED must have no measures and basis, mapping_basis and "
                          "mapping_rule null")
        return
    if not keys:
        errors.append(f"{label}: MAPPED requires at least one measure")
    if not isinstance(basis, str) or not basis or basis not in text:
        errors.append(f"{label}: basis must be wording contained in the requirement text")
        return
    if kind not in MAPPING_BASES:
        errors.append(f"{label}: unknown mapping_basis '{kind}'")
        return
    if explicit is not None and kind == "SOURCE_EXPLICIT" and not explicit.search(basis):
        errors.append(f"{label}: SOURCE_EXPLICIT requires basis wording that names an evidence artefact "
                      "(explicit_evidence_terms)")
    if rule == TRIGGER_RULE:
        if patterns is None or explicit is None:
            return
        expected, term = classify(text, patterns)
        if expected is None or keys != [expected] or basis != term:
            errors.append(f"{label}: mapping does not reproduce from trigger_pattern "
                          f"(expected {expected!r} / {term!r})")
        elif kind != mapping_basis_of(term, explicit):
            errors.append(f"{label}: mapping_basis of a TRIGGER mapping must follow from its wording")
    elif rule in rules:
        if keys != [rules[rule].get("measure")]:
            errors.append(f"{label}: measures must be the measure of adjudication rule '{rule}'")
    else:
        errors.append(f"{label}: unknown mapping_rule '{rule}'")


def validate_catalog(catalog: Any, rr_catalog: dict[str, Any],
                     data_model: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not _check_fields("root", catalog, ROOT_FIELDS, errors):
        return errors
    if not isinstance(catalog["version"], str) or not rr.VERSION_PATTERN.fullmatch(
            catalog["version"]):
        errors.append("root: version must be a string in MAJOR.MINOR form")
    rr._validate_change_history(catalog, errors)
    if catalog["rr_catalog_version"] != rr_catalog.get("version"):
        errors.append("root: rr_catalog_version does not match RR catalog version "
                      f"'{rr_catalog.get('version')}'; impact review required")
    if CATALOG_REF_KIND not in (data_model.get("catalog_ref_kinds") or []):
        errors.append(f"root: data model does not declare catalog reference kind "
                      f"'{CATALOG_REF_KIND}'")
    if not isinstance(catalog["description"], str) or not catalog["description"].strip():
        errors.append("root: description must be a non-empty string")

    bases = catalog["mapping_bases"] or {}
    if sorted(bases) != sorted(MAPPING_BASES):
        errors.append(f"root: mapping_bases must be exactly {list(MAPPING_BASES)}")
    for key, spec in bases.items():
        _check_texts(f"mapping_bases.{key}", spec, TEXT_FIELDS, errors)
    explicit: re.Pattern[str] | None = None
    try:
        explicit = re.compile(catalog["explicit_evidence_terms"])
    except (re.error, TypeError) as exc:
        errors.append(f"root: explicit_evidence_terms does not compile: {exc}")

    evidence_types = catalog["evidence_types"] or {}
    for key, spec in evidence_types.items():
        _check_texts(f"evidence_types.{key}", spec, TEXT_FIELDS, errors)

    patterns: list[tuple[str, re.Pattern[str]]] | None = []
    measures = catalog["measures"] or {}
    for key, spec in measures.items():
        label = f"measures.{key}"
        if not _check_fields(label, spec, MEASURE_FIELDS, errors):
            patterns = None
            continue
        rr._validate_text_pair(spec, "label", label, errors)
        types = spec["evidence_types"]
        if not isinstance(types, list) or not types or any(t not in evidence_types for t in types):
            errors.append(f"{label}: evidence_types must be a non-empty list of known evidence types")
        if spec["trigger_pattern"] is None:
            continue
        try:
            if patterns is not None:
                patterns.append((key, re.compile(spec["trigger_pattern"])))
        except (re.error, TypeError) as exc:
            errors.append(f"{label}: trigger_pattern does not compile: {exc}")
            patterns = None
    unused = set(evidence_types) - {t for spec in measures.values() if isinstance(spec, dict)
                                    for t in spec.get("evidence_types") or []}
    for key in sorted(unused):
        errors.append(f"evidence_types.{key}: evidence type is not used by any measure")

    rules = catalog["adjudication_rules"] or {}
    for key, spec in rules.items():
        label = f"adjudication_rules.{key}"
        if key == TRIGGER_RULE:
            errors.append(f"{label}: '{TRIGGER_RULE}' is reserved for rule-based mappings")
        if _check_texts(label, spec, RULE_FIELDS, errors) and spec["measure"] not in measures:
            errors.append(f"{label}: measure must be a known measure_key")

    mappings = catalog["requirements"] or {}
    entries = {entry["id"]: entry for entry in rr_catalog.get("requirements") or []}
    for rr_id in entries:
        if rr_id not in mappings:
            errors.append(f"requirements: no mapping status for '{rr_id}'")
    for rr_id in sorted(set(mappings) - set(entries)):
        errors.append(f"requirements: unknown RR id '{rr_id}'")
    for rr_id, mapping in mappings.items():
        label = f"requirements.{rr_id}"
        if rr_id in entries and _check_fields(label, mapping, MAPPING_FIELDS, errors):
            _validate_mapping(label, mapping, entries[rr_id]["requirement_text"]["de"], measures, rules,
                              patterns, explicit, errors)
    used = {key for mapping in mappings.values() if isinstance(mapping, dict)
            for key in mapping.get("measures") or []}
    for key in sorted(set(measures) - used):
        errors.append(f"measures.{key}: measure is not assigned to any RR")
    used_rules = {mapping.get("mapping_rule") for mapping in mappings.values() if isinstance(mapping, dict)}
    for key in sorted(set(rules) - used_rules):
        errors.append(f"adjudication_rules.{key}: rule is not used by any RR")
    return errors


def validate_repository(repo_root: Path = rr.REPO_ROOT) -> list[str]:
    return validate_catalog(
        rr.load_catalog(repo_root / CATALOG_PATH),
        rr.load_catalog(repo_root / rr.CATALOG_PATH),
        rr.load_catalog(repo_root / DATA_MODEL_PATH),
    )


def summary(catalog: dict[str, Any], rr_catalog: dict[str, Any]) -> list[str]:
    """Kennzahlen des Katalogs: Status, Mapping-Basis, Regelart und Verteilungen."""
    entries = {entry["id"]: entry for entry in rr_catalog["requirements"]}
    patterns = [(key, re.compile(spec["trigger_pattern"])) for key, spec in catalog["measures"].items()
                if spec["trigger_pattern"] is not None]
    mappings = catalog["requirements"]
    status = Counter(m["status"] for m in mappings.values())
    kind = Counter(m["mapping_basis"] for m in mappings.values() if m["status"] == "MAPPED")
    rule = Counter("TRIGGER" if m["mapping_rule"] == TRIGGER_RULE else "ADJ" for m in mappings.values()
                   if m["status"] == "MAPPED")
    overrides = sum(1 for rr_id, m in mappings.items() if m["mapping_rule"] not in (None, TRIGGER_RULE)
                    and classify(entries[rr_id]["requirement_text"]["de"], patterns)[0] is not None)
    lines = [f"version: {catalog['version']}",
             f"measures: {len(catalog['measures'])}; evidence types: {len(catalog['evidence_types'])}; "
             f"adjudication rules: {len(catalog['adjudication_rules'])}",
             "requirements: " + " ".join(f"{k}={v}" for k, v in sorted(status.items())),
             "mapping basis: " + " ".join(f"{k}={v}" for k, v in sorted(kind.items())),
             "mapping rule: " + " ".join(f"{k}={v}" for k, v in sorted(rule.items()))
             + f" (adjudication overriding a trigger match: {overrides})"]

    def table(title: str, keys_of) -> None:
        counts: Counter = Counter()
        for rr_id, m in mappings.items():
            for key in keys_of(entries[rr_id]):
                counts[(key, m["mapping_basis"] or m["status"])] += 1
        lines.append(f"{title}:")
        for key in sorted({k for k, _ in counts}):
            row = " ".join(f"{b}={counts[(key, b)]}" for b in (*MAPPING_BASES, "REVIEW_REQUIRED")
                           if counts[(key, b)])
            lines.append(f"  {key}: {row}")

    table("by theme", lambda e: [e["theme_cluster"]])
    table("by primary source", lambda e: sorted({s.split("#")[0] for s in e["sources"]["primary"]}))
    table("by lifecycle phase", lambda e: e["lifecycle_phases"])
    return lines


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
        print(f"RR measure catalog validation: FAIL ({len(errors)} error(s))", file=sys.stderr)
        return 1
    print("RR measure catalog validation: PASS")
    for line in summary(rr.load_catalog(rr.REPO_ROOT / CATALOG_PATH),
                        rr.load_catalog(rr.REPO_ROOT / rr.CATALOG_PATH)):
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
