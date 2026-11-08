"""Katalogbasierte Traceability: Verweisintegrität und abgeleitete Matrixansicht.

Die Verknüpfungen stehen ausschließlich in den führenden Katalogen (siehe
docs/05-traceability/TRACEABILITY_MODEL.md). Dieses Werkzeug liest sie, prüft,
dass jedes Verweisziel vergeben ist, und erzeugt bei Bedarf eine Matrixansicht.
Keine Aussage über fachliche Richtigkeit; Werkzeugbasis nach ADR-0001.
"""

from __future__ import annotations

import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import validate_rr_applicability as applicability
import validate_rr_catalog as rr
import validate_rr_measures as measures
import validate_rul_catalog as rul
import validate_sr_catalog as sr
import validate_standards_mapping as standards
import validate_test_catalog as tests



@dataclass(frozen=True)
class Link:
    """Eine Entwurfszeit-Verknüpfung vom Nachfolger zum Vorgänger."""

    source: str
    kind: str
    target: str


@dataclass(frozen=True)
class Artifacts:
    rr_catalog: dict[str, Any]
    rul_catalog: dict[str, Any]
    sr_catalog: dict[str, Any]
    reference: sr.SrReferenceData
    applicability: dict[str, Any]
    standards_mapping: dict[str, Any]
    measure_catalog: dict[str, Any] = field(default_factory=dict)
    tc_catalog: dict[str, Any] = field(default_factory=dict)
    ev_index: dict[str, Any] = field(default_factory=dict)


def load_artifacts(repo_root: Path = rr.REPO_ROOT) -> Artifacts:
    return Artifacts(
        rr_catalog=rr.load_catalog(repo_root / rr.CATALOG_PATH),
        rul_catalog=rr.load_catalog(repo_root / rul.CATALOG_PATH),
        sr_catalog=rr.load_catalog(repo_root / sr.CATALOG_PATH),
        reference=sr.load_reference_data(repo_root),
        applicability=rr.load_catalog(repo_root / applicability.MAPPING_PATH),
        standards_mapping=rr.load_catalog(repo_root / standards.MAPPING_PATH),
        measure_catalog=rr.load_catalog(repo_root / measures.CATALOG_PATH),
        tc_catalog=rr.load_catalog(repo_root / tests.TC_CATALOG_PATH),
        ev_index=(rr.load_catalog(repo_root / tests.EV_INDEX_PATH)
                  if (repo_root / tests.EV_INDEX_PATH).is_file() else {}),
    )


def collect_links(artifacts: Artifacts) -> list[Link]:
    """Alle Entwurfszeit-Verknüpfungen aus den Katalogen lesen."""
    links: list[Link] = []
    for entry in artifacts.rr_catalog.get("requirements") or []:
        sources = entry.get("sources") or {}
        for locator in sources.get("primary") or []:
            links.append(Link(entry["id"], "RR_SOURCE_PRIMARY", locator))
        for locator in sources.get("supplementary") or []:
            links.append(Link(entry["id"], "RR_SOURCE_SUPPLEMENTARY", locator))
    for entry in artifacts.rul_catalog.get("rules") or []:
        for locator in entry.get("primary_legal_anchor") or []:
            links.append(Link(entry["id"], "PRIMARY_LEGAL_ANCHOR", locator))
        for locator in entry.get("guidance_anchor") or []:
            links.append(Link(entry["id"], "GUIDANCE_ANCHOR", locator))
        for dependency in entry.get("dependencies") or []:
            links.append(Link(entry["id"], "DEPENDS_ON", dependency))
        produced = []
        for branch in entry.get("branches") or []:
            for name in (branch.get("result"), branch.get("review")):
                if name and name not in produced:
                    produced.append(name)
        for name in produced:
            links.append(Link(entry["id"], "PRODUCES", f"RUL_OUTPUT:{name}"))
    for entry in artifacts.sr_catalog.get("requirements") or []:
        for reference in entry.get("derived_from") or []:
            links.append(Link(entry["id"], "DERIVED_FROM", reference))
        for module in entry.get("allocated_modules") or []:
            links.append(Link(entry["id"], "ALLOCATED_TO", module))
    mapping = artifacts.applicability or {}
    for rr_id, entry in (mapping.get("requirements") or {}).items():
        links.append(Link(rr_id, "APPLICABILITY_BLOCK", f"BLOCK:{entry['block']}"))
        for predicate in entry.get("local") or []:
            links.append(Link(rr_id, "LOCAL_CONDITION", f"PREDICATE:{predicate}"))
    for key, block in (mapping.get("blocks") or {}).items():
        for predicate in block.get("scope") or []:
            links.append(Link(f"BLOCK:{key}", "BLOCK_SCOPE", f"PREDICATE:{predicate}"))
    for key, spec in (mapping.get("predicates") or {}).items():
        source = f"PREDICATE:{key}"
        links.append(Link(source, "CONDITION_SOURCE", f"EVIDENCE:{spec['source_of_condition'].split()[0]}"))
        for part in spec.get("of") or []:
            links.append(Link(source, "PREDICATE_PART", f"PREDICATE:{part}"))
        for item in (*spec.get("true_if", ()), *spec.get("false_if", ())):
            links.append(Link(source, "DECISION_OUTCOME", f"RUL_OUTPUT:{item['outcome']}"))
        if spec.get("input"):
            links.append(Link(source, "PROFILE_INPUT", f"INPUT:{spec['input']}"))
        for locator in spec.get("missing_primary_law") or []:
            links.append(Link(source, "MISSING_PRIMARY_LAW", locator))
    for relation in (artifacts.standards_mapping or {}).get("relations") or []:
        if relation["kind"] == "SOURCE_SUPPORT":
            links.append(Link(relation["rr"], "SOURCE_SUPPORT", relation["locator"]))
        else:
            links.append(Link(relation["from"], "NORMATIVE_DEPENDENCY", relation["to"]))
    for rr_id, mapping in (artifacts.measure_catalog.get("requirements") or {}).items():
        for key in mapping.get("measures") or []:
            links.append(Link(rr_id, "RR_MEASURE", f"MEASURE:{key}"))
    for key, spec in (artifacts.measure_catalog.get("measures") or {}).items():
        for evidence_type in spec.get("evidence_types") or []:
            links.append(Link(f"MEASURE:{key}", "MEASURE_EVIDENCE_TYPE",
                              f"EVIDENCE_TYPE:{evidence_type}"))
    for case in artifacts.tc_catalog.get("test_cases") or []:
        for sr_id in case.get("verifies_sr") or []:
            links.append(Link(case["id"], "TC_VERIFIES_SR", sr_id))
        for rule_id in case.get("verifies_rul") or []:
            links.append(Link(case["id"], "VERIFIES", rule_id))
        for item in case.get("covers_rr") or []:
            links.append(Link(case["id"], "TC_COVERS_RR", item))
    for entry in artifacts.ev_index.get("evidence") or []:
        for tc_id in entry.get("test_cases") or []:
            links.append(Link(entry["id"], "EV_OF_TC", tc_id))
    return links


def check_integrity(artifacts: Artifacts, links: list[Link]) -> list[str]:
    """Jedes Verweisziel muss vergeben bzw. bekannt sein."""
    data = artifacts.reference
    rul_ids = {entry.get("id") for entry in artifacts.rul_catalog.get("rules") or []}
    rr_ids = {entry.get("id") for entry in artifacts.rr_catalog.get("requirements") or []}
    sr_ids = {entry.get("id") for entry in artifacts.sr_catalog.get("requirements") or []}
    tc_ids = {case.get("id") for case in artifacts.tc_catalog.get("test_cases") or []}
    measure_catalog = artifacts.measure_catalog or {}
    mapping = artifacts.applicability or {}
    known = (
        {f"BLOCK:{key}" for key in mapping.get("blocks") or {}}
        | {f"PREDICATE:{key}" for key in mapping.get("predicates") or {}}
        | {f"RUL_OUTPUT:{key}" for key in artifacts.rul_catalog.get("outputs") or {}}
        | {f"INPUT:{key}" for key in mapping.get("profile_inputs") or {}}
        | {f"MEASURE:{key}" for key in measure_catalog.get("measures") or {}}
        | {f"EVIDENCE_TYPE:{key}" for key in measure_catalog.get("evidence_types") or {}}
        | {f"EVIDENCE:{path.name}" for path in
           (rr.REPO_ROOT / applicability.REGULATORY_DIR).glob("*.md")}
    )
    errors: list[str] = []
    for link in links:
        if link.kind in ("APPLICABILITY_BLOCK", "LOCAL_CONDITION", "BLOCK_SCOPE",
                         "CONDITION_SOURCE", "PREDICATE_PART", "DECISION_OUTCOME",
                         "PROFILE_INPUT", "PRODUCES", "RR_MEASURE", "MEASURE_EVIDENCE_TYPE"):
            if link.target not in known:
                errors.append(f"{link.source}: {link.kind} references unknown '{link.target}'")
        elif link.kind == "DERIVED_FROM":
            sr.validate_derivation(link.target, link.source, data, errors)
        elif link.kind == "ALLOCATED_TO":
            if link.target not in data.modules:
                errors.append(f"{link.source}: unknown architecture module '{link.target}'")
        elif link.kind == "TC_VERIFIES_SR":
            if link.target not in sr_ids:
                errors.append(f"{link.source}: TC_VERIFIES_SR references unknown SR '{link.target}'")
        elif link.kind == "TC_COVERS_RR":
            if link.target not in rr_ids and link.target not in known:
                errors.append(f"{link.source}: TC_COVERS_RR references unknown '{link.target}'")
        elif link.kind == "EV_OF_TC":
            if link.target not in tc_ids:
                errors.append(f"{link.source}: EV_OF_TC references unknown TC '{link.target}'")
        elif link.kind == "NORMATIVE_DEPENDENCY":
            if link.target not in rr_ids and link.target not in data.source_ids:
                errors.append(f"{link.source}: NORMATIVE_DEPENDENCY references unknown "
                              f"'{link.target}'")
        elif link.kind in ("DEPENDS_ON", "VERIFIES"):
            if link.target not in rul_ids:
                errors.append(f"{link.source}: {link.kind} references unknown rule '{link.target}'")
        else:
            head = link.target.partition("#")[0] if isinstance(link.target, str) else None
            if head not in data.source_ids:
                errors.append(f"{link.source}: {link.kind} references unknown source "
                              f"'{link.target}'")
    return errors


def summary(artifacts: Artifacts, links: list[Link]) -> list[str]:
    kinds = Counter(link.kind for link in links)
    rul_ids = [entry["id"] for entry in artifacts.rul_catalog.get("rules") or []]
    verified = {link.target for link in links if link.kind == "VERIFIES"}
    allocated = Counter(link.target for link in links if link.kind == "ALLOCATED_TO")
    lines = [f"links: {len(links)}"]
    lines += [f"  {kind}: {count}" for kind, count in sorted(kinds.items())]
    lines.append(f"RUL verified by test cases: {len(verified)} of {len(rul_ids)}")
    sr_ids = [entry["id"] for entry in artifacts.sr_catalog.get("requirements") or []]
    sr_verified = {link.target for link in links if link.kind == "TC_VERIFIES_SR"}
    lines.append(f"SR verified by test cases: {len(sr_verified)} of {len(sr_ids)}")
    rr_entries = artifacts.rr_catalog.get("requirements") or []
    measure_catalog = artifacts.measure_catalog or {}
    mappings = measure_catalog.get("requirements") or {}
    statuses = Counter(mapping.get("status") for mapping in mappings.values())
    lines.append("RR measure mapping: " + ", ".join(f"{key} {value}"
                                                    for key, value in sorted(statuses.items())))
    bases = Counter(mapping.get("mapping_basis") for mapping in mappings.values() if mapping.get("mapping_basis"))
    if bases:
        lines.append("RR measure mapping basis: " + ", ".join(f"{key} {value}"
                                                              for key, value in sorted(bases.items())))
    complete = sum(
        1 for entry in rr_entries
        if (entry.get("sources") or {}).get("primary") and entry.get("lifecycle_phases")
        and (mappings.get(entry["id"]) or {}).get("measures")
        and all((measure_catalog.get("measures") or {}).get(key, {}).get("evidence_types")
                for key in mappings[entry["id"]]["measures"]))
    lines.append(f"RR with source, lifecycle phase, measure and evidence type: {complete} of {len(rr_entries)}")
    lines.append("SR per architecture module: "
                 + ", ".join(f"{module} {allocated[module]}"
                             for module in sorted(artifacts.reference.modules)))
    return lines


def markdown(artifacts: Artifacts, links: list[Link]) -> str:
    """Abgeleitete Matrixansicht; wird nicht versioniert."""
    by_source: dict[str, dict[str, list[str]]] = {}
    for link in links:
        by_source.setdefault(link.source, {}).setdefault(link.kind, []).append(link.target)
    verified_by: dict[str, list[str]] = {}
    for link in links:
        if link.kind in ("VERIFIES", "TC_VERIFIES_SR", "TC_COVERS_RR"):
            verified_by.setdefault(link.target, []).append(link.source)
    evidence_of = {}
    for link in links:
        if link.kind == "EV_OF_TC":
            evidence_of.setdefault(link.target, []).append(link.source)
    measures = artifacts.measure_catalog or {}
    blocks = {rr_id: entry["block"] for rr_id, entry in
              ((artifacts.applicability or {}).get("requirements") or {}).items()}

    out = ["# Traceability-Matrix (abgeleitet, nicht manuell pflegen)", "",
           f"RR_CATALOG {artifacts.rr_catalog.get('version')} · "
           f"RUL_CATALOG {artifacts.rul_catalog.get('version')} · "
           f"SR_CATALOG {artifacts.sr_catalog.get('version')} · "
           f"RR_MEASURE {measures.get('version')} · "
           f"TC_CATALOG {artifacts.tc_catalog.get('version')}", "",
           "## SR", "", "| SR | derived_from | allocated_modules | verifiziert durch |",
           "| --- | --- | --- | --- |"]
    for entry in artifacts.sr_catalog.get("requirements") or []:
        row = by_source.get(entry["id"], {})
        out.append(f"| {entry['id']} | {', '.join(row.get('DERIVED_FROM', []))} | "
                   f"{', '.join(row.get('ALLOCATED_TO', []))} | "
                   f"{', '.join(verified_by.get(entry['id'], [])) or '—'} |")
    out += ["", "## RUL", "", "| RUL | Primary Legal Anchor | Guidance Anchor | verifiziert durch |",
            "| --- | --- | --- | --- |"]
    for entry in artifacts.rul_catalog.get("rules") or []:
        row = by_source.get(entry["id"], {})
        out.append(f"| {entry['id']} | {', '.join(row.get('PRIMARY_LEGAL_ANCHOR', []))} | "
                   f"{', '.join(row.get('GUIDANCE_ANCHOR', []))} | "
                   f"{', '.join(verified_by.get(entry['id'], [])) or '—'} |")
    out += ["", "## RR", "", "| RR | primary | supplementary | Lebenszyklusphasen | Maßnahme "
            "(Status) | Nachweisart | TC |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for entry in artifacts.rr_catalog.get("requirements") or []:
        row = by_source.get(entry["id"], {})
        mapping = (measures.get("requirements") or {}).get(entry["id"]) or {}
        keys = mapping.get("measures") or []
        types = [t for key in keys for t in measures["measures"][key]["evidence_types"]]
        tcs = sorted(set(verified_by.get(entry["id"], [])
                         + verified_by.get(f"BLOCK:{blocks.get(entry['id'])}", [])))
        out.append(f"| {entry['id']} | {', '.join(row.get('RR_SOURCE_PRIMARY', []))} | "
                   f"{', '.join(row.get('RR_SOURCE_SUPPLEMENTARY', [])) or '—'} | "
                   f"{', '.join(entry.get('lifecycle_phases') or [])} | "
                   f"{', '.join(keys) or '—'} ({mapping.get('status', '—')}"
                   f"{', ' + mapping['mapping_basis'] if mapping.get('mapping_basis') else ''}) | "
                   f"{', '.join(types) or '—'} | {', '.join(tcs) or '—'} |")
    out += ["", "## TC", "", "| TC | SR | RUL | RR/RR-Gruppe | EV |", "| --- | --- | --- | --- | --- |"]
    for case in artifacts.tc_catalog.get("test_cases") or []:
        row = by_source.get(case["id"], {})
        out.append(f"| {case['id']} | {', '.join(row.get('TC_VERIFIES_SR', [])) or '—'} | "
                   f"{', '.join(row.get('VERIFIES', [])) or '—'} | "
                   f"{', '.join(row.get('TC_COVERS_RR', [])) or '—'} | "
                   f"{', '.join(evidence_of.get(case['id'], [])) or '—'} |")
    return "\n".join(out) + "\n"


def main(argv: list[str]) -> int:
    if not rr.is_supported_python():
        print("ERROR: unsupported Python version", file=sys.stderr)
        return 1
    try:
        artifacts = load_artifacts()
    except (rr.ReferenceDataError, rr.CatalogLoadError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    links = collect_links(artifacts)
    errors = check_integrity(artifacts, links)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Traceability check: FAIL ({len(errors)} error(s))", file=sys.stderr)
        return 1
    if "--markdown" in argv:
        sys.stdout.write(markdown(artifacts, links))
        return 0
    print("Traceability check: PASS")
    for line in summary(artifacts, links):
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
