"""Formale Strukturprüfung des Testfallkatalogs (TC) und des Evidenzindex (EV).

Prüft docs/07-testing/TC_CATALOG.yaml und docs/09-evidence/EV_INDEX.yaml gegen
SR-, RUL-, RR- und Applicability-Katalog: eindeutige, fortlaufende IDs, gültige
Verweise, auflösbare automatisierte Tests und Datenvarianten, Schema der
Referenzfälle, vorhandene Evidenzartefakte und keine verwaisten Testfälle.
Keine Aussage über die fachliche Richtigkeit eines Soll-Ergebnisses;
Werkzeugbasis nach ADR-0001.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import validate_rr_applicability as applicability
import validate_rr_catalog as rr
import validate_rr_measures as measures
import validate_rul_catalog as rul
import validate_sr_catalog as sr

TC_CATALOG_PATH = Path("docs/07-testing/TC_CATALOG.yaml")
EV_INDEX_PATH = Path("docs/09-evidence/EV_INDEX.yaml")
TESTS_DIR = Path("tests")

TC_ROOT_FIELDS = ("version", "catalog_versions", "description", "test_cases", "change_history")
TC_FIELDS = ("id", "status", "title", "purpose", "test_type", "categories", "evaluation_dimensions",
             "preconditions", "inputs", "expected", "verifies_sr", "verifies_rul", "covers_rr",
             "expected_trace", "automation", "data_refs", "golden_case", "golden")
TEST_TYPES = ("AUTOMATED", "VALIDATOR", "MANUAL_REFERENCE")
CATEGORIES = tuple("ABCDEFGHIJKLM")
DIMENSIONS = ("CORRECTNESS", "COMPLETENESS", "REPRODUCIBILITY", "TRACEABILITY", "REGRESSION")
GOLDEN_FIELDS = ("rule_inputs", "profile", "expected_paths", "expected_decisions",
                 "expected_block_states", "expected_requirements", "expected_totals",
                 "expected_scope_totals")
GOLDEN_OPTIONAL = ("expected_missing_input",)
BLOCK_STATES = ("ACTIVE", "INACTIVE", "UNRESOLVED")
APPLICABILITY = ("APPLICABLE", "NOT_APPLICABLE", "APPLICABILITY_UNRESOLVED")

EV_ROOT_FIELDS = ("version", "description", "evidence", "change_history")
EV_FIELDS = ("id", "title", "type", "date", "performed", "artifact", "test_cases", "results",
             "catalog_versions", "assessment")
EV_TYPES = ("AUTOMATED_TEST_RUN", "VALIDATOR_RUN", "MANUAL_REFERENCE")
RESULTS = ("PASS", "FAIL")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TC_ID = re.compile(r"^TC-\d{3}$")
EV_ID = re.compile(r"^EV-\d{3}$")


def _check_fields(label: str, entry: Any, fields: tuple[str, ...], errors: list[str],
                  optional: tuple[str, ...] = ()) -> bool:
    if not isinstance(entry, dict):
        errors.append(f"{label}: must be a mapping")
        return False
    for field in fields:
        if field not in entry:
            errors.append(f"{label}: missing field '{field}'")
    for field in sorted(set(entry) - set(fields) - set(optional)):
        errors.append(f"{label}: unexpected field '{field}'")
    return set(fields) <= set(entry)


def _subset(label: str, values: Any, allowed: Any, name: str, errors: list[str],
            non_empty: bool = False) -> None:
    if not isinstance(values, list) or (non_empty and not values):
        errors.append(f"{label}: {name} must be a{' non-empty' if non_empty else ''} list")
        return
    for value in values:
        if value not in allowed:
            errors.append(f"{label}: unknown {name} entry '{value}'")


def resolve_automation(reference: str, repo_root: Path) -> str | None:
    """Fehlermeldung für einen nicht auflösbaren Testverweis 'pfad[::Klasse::methode]'."""
    path, _, rest = reference.partition("::")
    file = repo_root / path
    if not file.is_file():
        return f"file '{path}' does not exist"
    if not rest:
        return None
    text = file.read_text(encoding="utf-8")
    class_name, _, method = rest.partition("::")
    if not re.search(rf"^class {re.escape(class_name)}\b", text, re.MULTILINE):
        return f"class '{class_name}' not found in '{path}'"
    if method and not re.search(rf"^    def {re.escape(method)}\(", text, re.MULTILINE):
        return f"method '{method}' not found in '{path}'"
    return None


def _validate_golden(label: str, spec: Any, context: dict[str, Any], errors: list[str]) -> None:
    if not _check_fields(f"{label}.golden_case", spec, GOLDEN_FIELDS, errors, GOLDEN_OPTIONAL):
        return
    for entry in spec["rule_inputs"] or {}:
        if entry not in context["entry_points"]:
            errors.append(f"{label}: unknown entry rule '{entry}'")
    for key in spec["profile"] or {}:
        if key not in context["profile_inputs"]:
            errors.append(f"{label}: unknown applicability input '{key}'")
    for entry, path in (spec["expected_paths"] or {}).items():
        if entry not in spec["rule_inputs"] or any(r not in context["rul_ids"] for r in path):
            errors.append(f"{label}: expected_paths must use evaluated entries and known RUL")
    if set(spec["expected_block_states"] or {}) != context["blocks"] or any(
            state not in BLOCK_STATES for state in spec["expected_block_states"].values()):
        errors.append(f"{label}: expected_block_states must cover every block with a known state")
    for rr_id, value in (spec["expected_requirements"] or {}).items():
        if rr_id not in context["rr_ids"] or not isinstance(value, list) or len(value) != 2 \
                or value[0] not in APPLICABILITY or value[1] not in context["reasons"]:
            errors.append(f"{label}: invalid expected requirement '{rr_id}'")
    totals = spec["expected_totals"]
    if totals is not None and (set(totals) != set(APPLICABILITY)
                               or sum(totals.values()) != len(context["rr_ids"])):
        errors.append(f"{label}: expected_totals must cover all applicability states and all RR")
    scope = spec["expected_scope_totals"]
    if not isinstance(scope, dict) or set(scope) != {"inactive", "unresolved"}:
        errors.append(f"{label}: expected_scope_totals needs 'inactive' and 'unresolved'")


def validate_catalogs(tc_catalog: Any, ev_index: Any, context: dict[str, Any],
                      repo_root: Path = rr.REPO_ROOT) -> list[str]:
    errors: list[str] = []
    if not _check_fields("tc_root", tc_catalog, TC_ROOT_FIELDS, errors):
        return errors
    rr._validate_change_history(tc_catalog, errors)
    if tc_catalog["catalog_versions"] != context["catalog_versions"]:
        errors.append("tc_root: catalog_versions do not match the current catalogs; "
                      "impact review required")
    tc_ids: list[str] = []
    referenced_files: set[str] = set()
    for index, case in enumerate(tc_catalog["test_cases"] or []):
        label = f"test_cases[{index}]"
        if not _check_fields(label, case, TC_FIELDS, errors):
            continue
        label = case["id"]
        if not isinstance(label, str) or not TC_ID.fullmatch(label):
            errors.append(f"test_cases[{index}]: id must match TC-NNN")
            continue
        tc_ids.append(label)
        if case["status"] not in context["status_values"]:
            errors.append(f"{label}: unknown status '{case['status']}'")
        for field in ("title", "purpose", "preconditions", "inputs", "expected"):
            rr._validate_text_pair(case, field, label, errors)
        if case["expected_trace"] is not None:
            rr._validate_text_pair(case, "expected_trace", label, errors)
        if case["test_type"] not in TEST_TYPES:
            errors.append(f"{label}: unknown test_type '{case['test_type']}'")
        _subset(label, case["categories"], CATEGORIES, "category", errors, non_empty=True)
        _subset(label, case["evaluation_dimensions"], DIMENSIONS, "evaluation dimension", errors,
                non_empty=True)
        _subset(label, case["verifies_sr"], context["sr_ids"], "SR", errors)
        _subset(label, case["verifies_rul"], context["rul_ids"], "RUL", errors)
        covers = [item for item in case["covers_rr"] or []]
        _subset(label, covers, context["rr_ids"] | {f"BLOCK:{b}" for b in context["blocks"]},
                "RR or RR group", errors)
        if not (case["verifies_sr"] or case["verifies_rul"] or case["covers_rr"]):
            errors.append(f"{label}: a test case must reference at least one SR, RUL or RR")
        automation = case["automation"]
        if not isinstance(automation, list) or (not automation
                                                and case["test_type"] != "MANUAL_REFERENCE"):
            errors.append(f"{label}: automation must list at least one executable test or validator")
            automation = []
        for reference in automation:
            problem = resolve_automation(reference, repo_root)
            if problem:
                errors.append(f"{label}: automation '{reference}': {problem}")
            referenced_files.add(reference.partition("::")[0])
        for reference in case["data_refs"] or []:
            path, _, local_id = reference.partition("#")
            file = repo_root / path
            if not file.is_file():
                errors.append(f"{label}: data_ref file '{path}' does not exist")
                continue
            ids = {item.get("id") for item in rr.load_catalog(file).get("test_cases") or []}
            if local_id not in ids:
                errors.append(f"{label}: data_ref '{reference}' does not resolve")
        if case["golden"] is not (case["golden_case"] is not None):
            errors.append(f"{label}: golden must be true exactly when golden_case is given")
        if case["golden_case"] is not None:
            _validate_golden(label, case["golden_case"], context, errors)
    if tc_ids != [f"TC-{n:03d}" for n in range(1, len(tc_ids) + 1)]:
        errors.append("test_cases: TC ids must be unique and sequential from TC-001")
    for test_file in sorted((repo_root / TESTS_DIR).glob("test_*.py")):
        relative = test_file.relative_to(repo_root).as_posix()
        if relative not in referenced_files:
            errors.append(f"{relative}: automated test file is not referenced by any TC")

    if ev_index is None:
        return errors
    if not _check_fields("ev_root", ev_index, EV_ROOT_FIELDS, errors):
        return errors
    rr._validate_change_history(ev_index, errors)
    ev_ids: list[str] = []
    evidenced: set[str] = set()
    for index, entry in enumerate(ev_index["evidence"] or []):
        label = f"evidence[{index}]"
        if not _check_fields(label, entry, EV_FIELDS, errors):
            continue
        label = entry["id"]
        if not isinstance(label, str) or not EV_ID.fullmatch(label):
            errors.append(f"evidence[{index}]: id must match EV-NNN")
            continue
        ev_ids.append(label)
        rr._validate_text_pair(entry, "title", label, errors)
        rr._validate_text_pair(entry, "performed", label, errors)
        rr._validate_text_pair(entry, "assessment", label, errors)
        if entry["type"] not in EV_TYPES:
            errors.append(f"{label}: unknown type '{entry['type']}'")
        if not isinstance(entry["date"], str) or not DATE_PATTERN.fullmatch(entry["date"]):
            errors.append(f"{label}: date must be YYYY-MM-DD")
        if not isinstance(entry["artifact"], str) or not (repo_root / entry["artifact"]).is_file():
            errors.append(f"{label}: artifact must name an existing file")
        cases = entry["test_cases"]
        _subset(label, cases, set(tc_ids), "TC", errors, non_empty=True)
        results = entry["results"]
        if not isinstance(results, dict) or set(results) != set(cases or []) or any(
                value not in RESULTS for value in results.values()):
            errors.append(f"{label}: results must give PASS or FAIL for exactly its test cases")
        if not isinstance(entry["catalog_versions"], dict) or not entry["catalog_versions"]:
            errors.append(f"{label}: catalog_versions must be a non-empty mapping")
        evidenced |= set(cases or [])
    if ev_ids != [f"EV-{n:03d}" for n in range(1, len(ev_ids) + 1)]:
        errors.append("evidence: EV ids must be unique and sequential from EV-001")
    for tc_id in tc_ids:
        if tc_id not in evidenced:
            errors.append(f"{tc_id}: test case has no evidence (orphaned)")
    return errors


def load_context(repo_root: Path = rr.REPO_ROOT) -> dict[str, Any]:
    rr_catalog = rr.load_catalog(repo_root / rr.CATALOG_PATH)
    rul_catalog = rr.load_catalog(repo_root / rul.CATALOG_PATH)
    sr_catalog = rr.load_catalog(repo_root / sr.CATALOG_PATH)
    mapping = rr.load_catalog(repo_root / applicability.MAPPING_PATH)
    data_model = rr.load_catalog(repo_root / applicability.DATA_MODEL_PATH)
    measure_catalog = rr.load_catalog(repo_root / measures.CATALOG_PATH)
    return {
        "rr_ids": {entry["id"] for entry in rr_catalog["requirements"]},
        "rul_ids": {entry["id"] for entry in rul_catalog["rules"]},
        "sr_ids": {entry["id"] for entry in sr_catalog["requirements"]},
        "entry_points": set(rul_catalog["entry_points"]),
        "blocks": set(mapping["blocks"]),
        "profile_inputs": set(mapping["profile_inputs"]),
        "reasons": set(data_model["enums"]["applicability_reason"]),
        "status_values": rr.parse_status_vocabulary(rr._read_text(repo_root / rr.CONVENTIONS_PATH)),
        "catalog_versions": {
            "rr_catalog": rr_catalog["version"], "rul_catalog": rul_catalog["version"],
            "sr_catalog": sr_catalog["version"], "rr_applicability": mapping["version"],
            "data_model": data_model["version"], "rr_measure": measure_catalog["version"],
        },
    }


def validate_repository(repo_root: Path = rr.REPO_ROOT) -> list[str]:
    ev_path = repo_root / EV_INDEX_PATH
    return validate_catalogs(
        rr.load_catalog(repo_root / TC_CATALOG_PATH),
        rr.load_catalog(ev_path) if ev_path.is_file() else None,
        load_context(repo_root),
        repo_root,
    )


def main() -> int:
    if not rr.is_supported_python():
        print("ERROR: unsupported Python version", file=sys.stderr)
        return 1
    try:
        errors = validate_repository()
    except (rr.ReferenceDataError, rr.CatalogLoadError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Test catalog validation: FAIL ({len(errors)} error(s))", file=sys.stderr)
        return 1
    catalog = rr.load_catalog(rr.REPO_ROOT / TC_CATALOG_PATH)
    cases = catalog["test_cases"]
    types: dict[str, int] = {}
    for case in cases:
        types[case["test_type"]] = types.get(case["test_type"], 0) + 1
    ev_path = rr.REPO_ROOT / EV_INDEX_PATH
    ev_count = len(rr.load_catalog(ev_path)["evidence"]) if ev_path.is_file() else 0
    print("Test catalog validation: PASS")
    print(f"test cases: {len(cases)} " + " ".join(f"{k}={v}" for k, v in sorted(types.items()))
          + f" golden={sum(1 for case in cases if case['golden'])}")
    print(f"evidence: {ev_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
