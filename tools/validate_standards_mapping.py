"""Formale Strukturprüfung der Zuordnung der Normkandidaten zu RR.

Prüft docs/03-regulatory/RR_STANDARDS_MAPPING_SRC_005_008.yaml gegen RR-Katalog
und Quellenregister: vollständige und eindeutige Kandidatenzuordnung,
Kandidatenzahl je Quelle, Merge-Gruppen, Lokatoren und Beziehungen zu
bestehenden RR. Keine Aussage über die fachliche Richtigkeit einer
Deduplizierungsentscheidung; Werkzeugbasis nach ADR-0001.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import validate_rr_catalog as rr

MAPPING_PATH = Path("docs/03-regulatory/RR_STANDARDS_MAPPING_SRC_005_008.yaml")
REGULATORY_DIR = Path("docs/03-regulatory")

ROOT_FIELDS = ("version", "rr_catalog_version", "description", "evidence", "sources", "merges",
               "candidates", "relations", "change_history")
CANDIDATE_FIELDS = ("temp_id", "source", "locator", "split_of", "decision", "rr")
MERGE_FIELDS = ("rr", "candidates")
DECISIONS = ("NEW_UNIQUE_RR", "CROSS_NORM_MERGE", "EXISTING_RR_SUPPORT", "CROSSWALK_ONLY")
RELATION_FIELDS = {
    "SOURCE_SUPPORT": ("kind", "candidate", "rr", "locator", "note"),
    "NORMATIVE_DEPENDENCY": ("kind", "candidate", "from", "to", "note"),
}


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


def _locator_ok(locator: Any, source_ids: frozenset[str]) -> bool:
    if not isinstance(locator, str):
        return False
    head, separator, rest = locator.partition("#")
    return bool(separator) and head in source_ids and bool(rest.strip())


def validate_mapping(mapping: Any, rr_catalog: dict[str, Any], source_ids: frozenset[str],
                     repo_root: Path = rr.REPO_ROOT) -> list[str]:
    errors: list[str] = []
    if not _check_fields("root", mapping, ROOT_FIELDS, errors):
        return errors
    if not isinstance(mapping["version"], str) or not rr.VERSION_PATTERN.fullmatch(
            mapping["version"]):
        errors.append("root: version must be a string in MAJOR.MINOR form")
    rr._validate_change_history(mapping, errors)
    if mapping["rr_catalog_version"] != rr_catalog.get("version"):
        errors.append("root: rr_catalog_version does not match RR catalog version "
                      f"'{rr_catalog.get('version')}'; impact review required")
    evidence = mapping["evidence"]
    if not isinstance(evidence, str) or not (repo_root / REGULATORY_DIR / evidence).is_file():
        errors.append("root: evidence must name an existing evidence file")

    entries = {entry["id"]: entry for entry in rr_catalog.get("requirements") or []}
    sources = mapping["sources"]
    if not isinstance(sources, dict) or not sources or any(
            key not in source_ids or not isinstance(value, int) for key, value in sources.items()):
        errors.append("root: sources must map registered SRC ids to candidate counts")
        sources = {}

    candidates: dict[str, dict[str, Any]] = {}
    counts: dict[str, int] = {}
    produced: dict[str, str] = {}
    for index, entry in enumerate(mapping["candidates"] or []):
        label = f"candidates[{index}]"
        if not _check_fields(label, entry, CANDIDATE_FIELDS, errors):
            continue
        temp_id = entry["temp_id"]
        label = f"candidates.{temp_id}"
        if temp_id in candidates:
            errors.append(f"{label}: duplicate temp_id")
        candidates[temp_id] = entry
        source = entry["source"]
        if source not in sources:
            errors.append(f"{label}: source '{source}' is not listed in sources")
        counts[source] = counts.get(source, 0) + 1
        locator = entry["locator"]
        if not _locator_ok(locator, source_ids) or locator.partition("#")[0] != source:
            errors.append(f"{label}: locator '{locator}' must be a locator of {source}")
        if entry["decision"] not in DECISIONS:
            errors.append(f"{label}: unknown decision '{entry['decision']}'")
            continue
        targets = entry["rr"]
        if not isinstance(targets, list) or not targets or any(t not in entries for t in targets):
            errors.append(f"{label}: rr must be a non-empty list of catalogued RR ids")
            continue
        if entry["decision"] == "NEW_UNIQUE_RR":
            if len(targets) != 1:
                errors.append(f"{label}: NEW_UNIQUE_RR must map to exactly one RR")
                continue
            target = targets[0]
            if target in produced:
                errors.append(f"{label}: {target} is already produced by {produced[target]}")
            produced[target] = temp_id
            if entries[target]["sources"]["primary"] != [locator]:
                errors.append(f"{label}: primary source of {target} must be exactly '{locator}'")
    for source, expected in sources.items():
        if counts.get(source, 0) != expected:
            errors.append(f"sources.{source}: {counts.get(source, 0)} candidates, "
                          f"expected {expected}")

    merged: set[str] = set()
    for key, spec in (mapping["merges"] or {}).items():
        label = f"merges.{key}"
        if not _check_fields(label, spec, MERGE_FIELDS, errors):
            continue
        target = spec["rr"]
        if target not in entries:
            errors.append(f"{label}: unknown RR '{target}'")
            continue
        if target in produced:
            errors.append(f"{label}: {target} is already produced by {produced[target]}")
        produced[target] = key
        members = spec["candidates"]
        if not isinstance(members, list) or len(members) < 2:
            errors.append(f"{label}: a merge needs at least two candidates")
            continue
        if len({candidates[m]["source"] for m in members if m in candidates}) < 2:
            errors.append(f"{label}: a cross-norm merge needs candidates of different sources")
        sources_of_rr = [*entries[target]["sources"]["primary"],
                         *entries[target]["sources"]["supplementary"]]
        for member in members:
            candidate = candidates.get(member)
            if candidate is None:
                errors.append(f"{label}: unknown candidate '{member}'")
                continue
            merged.add(member)
            if candidate["decision"] != "CROSS_NORM_MERGE" or candidate["rr"] != [target]:
                errors.append(f"{label}: candidate '{member}' must be CROSS_NORM_MERGE to {target}")
            if candidate["locator"] not in sources_of_rr:
                errors.append(f"{label}: locator '{candidate['locator']}' of '{member}' "
                              f"is not a source of {target}")
    for temp_id, entry in candidates.items():
        if entry.get("decision") == "CROSS_NORM_MERGE" and temp_id not in merged:
            errors.append(f"candidates.{temp_id}: CROSS_NORM_MERGE without merge group")

    standard_rr = sorted(rr_id for rr_id, entry in entries.items()
                         if entry["sources"]["primary"][0].partition("#")[0] in sources)
    for rr_id in standard_rr:
        if rr_id not in produced:
            errors.append(f"{rr_id}: primary source is a mapped standard but no candidate maps to it")

    related: set[str] = set()
    for index, relation in enumerate(mapping["relations"] or []):
        kind = relation.get("kind") if isinstance(relation, dict) else None
        label = f"relations[{index}]"
        if kind not in RELATION_FIELDS:
            errors.append(f"{label}: unknown relation kind '{kind}'")
            continue
        if not _check_fields(label, relation, RELATION_FIELDS[kind], errors):
            continue
        member = relation["candidate"]
        if member is not None:
            candidate = candidates.get(member)
            if candidate is None or candidate["decision"] not in (
                    "EXISTING_RR_SUPPORT", "CROSSWALK_ONLY"):
                errors.append(f"{label}: candidate must be an EXISTING_RR_SUPPORT or "
                              "CROSSWALK_ONLY candidate")
            else:
                related.add(member)
        if kind == "SOURCE_SUPPORT":
            if relation["rr"] not in entries:
                errors.append(f"{label}: unknown RR '{relation['rr']}'")
            elif member in candidates and relation["rr"] not in candidates[member]["rr"]:
                errors.append(f"{label}: {relation['rr']} is not a target of '{member}'")
            if not _locator_ok(relation["locator"], source_ids):
                errors.append(f"{label}: invalid locator '{relation['locator']}'")
        else:
            origin, target = relation["from"], relation["to"]
            if origin not in source_ids and not _locator_ok(origin, source_ids):
                errors.append(f"{label}: 'from' must be a SRC id or locator")
            if target not in entries and target not in source_ids:
                errors.append(f"{label}: 'to' must be a catalogued RR id or SRC id")
            elif member in candidates and target not in candidates[member]["rr"]:
                errors.append(f"{label}: {target} is not a target of '{member}'")
        if not isinstance(relation["note"], str) or not relation["note"].strip():
            errors.append(f"{label}: note must be a non-empty string")
    for temp_id, entry in candidates.items():
        if entry.get("decision") in ("EXISTING_RR_SUPPORT", "CROSSWALK_ONLY") \
                and temp_id not in related:
            errors.append(f"candidates.{temp_id}: {entry['decision']} without relation")
    return errors


def validate_repository(repo_root: Path = rr.REPO_ROOT) -> list[str]:
    return validate_mapping(
        rr.load_catalog(repo_root / MAPPING_PATH),
        rr.load_catalog(repo_root / rr.CATALOG_PATH),
        rr.load_reference_data(repo_root).source_ids,
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
        print(f"Standards mapping validation: FAIL ({len(errors)} error(s))", file=sys.stderr)
        return 1
    mapping = rr.load_catalog(rr.REPO_ROOT / MAPPING_PATH)
    decisions: dict[str, int] = {}
    for entry in mapping["candidates"]:
        decisions[entry["decision"]] = decisions.get(entry["decision"], 0) + 1
    produced = {entry["rr"][0] for entry in mapping["candidates"]
                if entry["decision"] == "NEW_UNIQUE_RR"}
    produced |= {spec["rr"] for spec in mapping["merges"].values()}
    print("Standards mapping validation: PASS")
    print(f"version: {mapping['version']}")
    print(f"candidates: {len(mapping['candidates'])} "
          + " ".join(f"{key}={value}" for key, value in sorted(decisions.items())))
    print(f"merges: {len(mapping['merges'])}; new RR: {len(produced)}; "
          f"relations: {len(mapping['relations'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
