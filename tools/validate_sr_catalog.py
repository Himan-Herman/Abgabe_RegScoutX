"""Formale Strukturprüfung des Systemanforderungskatalogs (SR).

Prüft docs/02-requirements/SR_CATALOG.yaml nach
docs/02-requirements/SYSTEM_REQUIREMENTS.md. Keine Aussage über fachliche
Richtigkeit; Werkzeugbasis nach ADR-0001.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import validate_rr_catalog as rr
import validate_rul_catalog as rul

CATALOG_PATH = Path("docs/02-requirements/SR_CATALOG.yaml")
METHOD_PATH = Path("docs/02-requirements/SYSTEM_REQUIREMENTS.md")
ARCHITECTURE_PATH = Path("docs/04-architecture/ARCHITECTURE.md")
EXPOSE_PATH = Path("docs/00-project/EXPOSE_SCOPE.md")
EXPOSE_PREFIX = "EXPOSE_SCOPE.md#"
STATE_OF_THE_ART_PATH = Path("docs/01-research/STATE_OF_THE_ART.md")
STATE_OF_THE_ART_PREFIX = "STATE_OF_THE_ART.md#"

ROOT_FIELDS = ("version", "requirements", "change_history")
SR_FIELDS = (
    "id",
    "status",
    "group",
    "title",
    "statement",
    "acceptance_criterion",
    "verification_method",
    "derived_from",
    "allocated_modules",
    "rationale",
    "replaces",
    "replaced_by",
)
SR_ID_PATTERN = re.compile(r"^SR-\d{3}$")
HEADING_PATTERN = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
DESIGN_IMPLICATION_PATTERN = re.compile(r"^\| (DI-\d{3}) \|", re.MULTILINE)

GROUP_MARKER = "Zulässige SR-Gruppen:"
VERIFICATION_MARKER = "Zulässige Verifikationsmethoden:"
MODULE_MARKER = "Zulässige Architekturmodule:"


@dataclass(frozen=True)
class SrReferenceData:
    """Zulässige Werte und bekannte Verweisziele für SR."""

    status_values: frozenset[str]
    groups: frozenset[str]
    verification_methods: frozenset[str]
    modules: frozenset[str]
    source_ids: frozenset[str]
    rr_ids: frozenset[str]
    expose_anchors: frozenset[str]
    design_implications: frozenset[str]


def heading_anchor(heading: str) -> str:
    """Anker einer Markdown-Überschrift nach der üblichen Slug-Bildung."""
    slug = heading.strip().lower()
    slug = re.sub(r"[^\w\- ]", "", slug)
    return slug.replace(" ", "-")


def parse_anchors(text: str) -> frozenset[str]:
    anchors = [heading_anchor(heading) for heading in HEADING_PATTERN.findall(text)]
    if not anchors:
        raise rr.ReferenceDataError("no headings found in exposé")
    return frozenset(anchors)


def parse_design_implications(text: str) -> frozenset[str]:
    """Kennungen der Design Implications (DI-NNN) aus STATE_OF_THE_ART.md lesen."""
    identifiers = DESIGN_IMPLICATION_PATTERN.findall(text)
    if not identifiers:
        raise rr.ReferenceDataError("no design implications found in state of the art")
    return frozenset(identifiers)


def load_reference_data(repo_root: Path = rr.REPO_ROOT) -> SrReferenceData:
    """Zulässige Werte aus den führenden Dokumenten laden (fail-closed)."""
    method = rr._read_text(repo_root / METHOD_PATH)
    architecture = rr._read_text(repo_root / ARCHITECTURE_PATH)
    rr_catalog = rr.load_catalog(repo_root / rr.CATALOG_PATH)
    rr_ids = [entry.get("id") for entry in rr_catalog.get("requirements", [])
              if isinstance(entry, dict)]
    if not rr_ids:
        raise rr.ReferenceDataError("no RR ids found in RR catalog")
    return SrReferenceData(
        status_values=rr.parse_status_vocabulary(rr._read_text(repo_root / rr.CONVENTIONS_PATH)),
        groups=rul.parse_marked_vocabulary(method, GROUP_MARKER, "SR group"),
        verification_methods=rul.parse_marked_vocabulary(
            method, VERIFICATION_MARKER, "verification method"),
        modules=rul.parse_marked_vocabulary(architecture, MODULE_MARKER, "architecture module"),
        source_ids=rr.parse_source_ids(rr._read_text(repo_root / rr.SOURCES_PATH)),
        rr_ids=frozenset(rr_ids),
        expose_anchors=parse_anchors(rr._read_text(repo_root / EXPOSE_PATH)),
        design_implications=parse_design_implications(
            rr._read_text(repo_root / STATE_OF_THE_ART_PATH)),
    )


def reference_kind(reference: str) -> str:
    """Art eines Herkunftsverweises: EXPOSE, STATE_OF_THE_ART, RR, SRC oder UNKNOWN."""
    if reference.startswith(EXPOSE_PREFIX):
        return "EXPOSE"
    if reference.startswith(STATE_OF_THE_ART_PREFIX):
        return "STATE_OF_THE_ART"
    if rr.RR_ID_PATTERN.fullmatch(reference):
        return "RR"
    if reference.startswith("SRC-"):
        return "SRC"
    return "UNKNOWN"


def validate_derivation(reference: Any, label: str, data: SrReferenceData,
                        errors: list[str]) -> None:
    """Einen derived_from-Verweis gegen die bekannten Ziele prüfen."""
    if not isinstance(reference, str):
        errors.append(f"{label}: derived_from entries must be strings")
        return
    kind = reference_kind(reference)
    if kind == "EXPOSE":
        anchor = reference[len(EXPOSE_PREFIX):]
        if anchor not in data.expose_anchors:
            errors.append(f"{label}: unknown exposé section '{reference}'")
    elif kind == "STATE_OF_THE_ART":
        if reference[len(STATE_OF_THE_ART_PREFIX):] not in data.design_implications:
            errors.append(f"{label}: unknown design implication '{reference}'")
    elif kind == "RR":
        if reference not in data.rr_ids:
            errors.append(f"{label}: unknown RR id '{reference}'")
    elif kind == "SRC":
        locator_reference = rr.ReferenceData(frozenset(), frozenset(), data.source_ids,
                                             data.status_values)
        rr._validate_locator(reference, "derived_from", label, locator_reference, errors)
    else:
        errors.append(f"{label}: derived_from must reference the exposé, a design "
                      f"implication, an RR or an SRC locator, found '{reference}'")


def _validate_requirement(entry: Any, index: int, data: SrReferenceData,
                          errors: list[str]) -> str | None:
    label = f"requirements[{index}]"
    if not isinstance(entry, dict):
        errors.append(f"{label}: requirement must be a mapping")
        return None
    raw_id = entry.get("id")
    valid_id = isinstance(raw_id, str) and SR_ID_PATTERN.fullmatch(raw_id) is not None
    if valid_id:
        label = raw_id
    else:
        errors.append(f"{label}: id must match SR-NNN")
    for field in SR_FIELDS:
        if field not in entry:
            errors.append(f"{label}: missing field '{field}'")
    for field in sorted(set(entry) - set(SR_FIELDS)):
        errors.append(f"{label}: unexpected field '{field}'")

    if entry.get("status") not in data.status_values:
        errors.append(f"{label}: unknown status '{entry.get('status')}'")
    if entry.get("group") not in data.groups:
        errors.append(f"{label}: unknown group '{entry.get('group')}'")
    if entry.get("verification_method") not in data.verification_methods:
        errors.append(f"{label}: unknown verification method '{entry.get('verification_method')}'")
    for field in ("title", "statement", "acceptance_criterion"):
        rr._validate_text_pair(entry, field, label, errors)
    if not isinstance(entry.get("rationale"), str) or not entry["rationale"].strip():
        errors.append(f"{label}: rationale must be a non-empty string")

    derived = entry.get("derived_from")
    if not isinstance(derived, list) or not derived:
        errors.append(f"{label}: derived_from must be a non-empty list")
    else:
        for reference in derived:
            validate_derivation(reference, label, data, errors)

    modules = entry.get("allocated_modules")
    if not isinstance(modules, list) or not modules:
        errors.append(f"{label}: allocated_modules must be a non-empty list")
    else:
        for module in modules:
            if module not in data.modules:
                errors.append(f"{label}: unknown architecture module '{module}'")
        if len(set(modules)) != len(modules):
            errors.append(f"{label}: allocated_modules must be unique")
    return raw_id if valid_id else None


def validate_catalog(catalog: Any, data: SrReferenceData) -> list[str]:
    """Bereits geladenes SR-Katalogobjekt prüfen und alle Befunde sammeln."""
    errors: list[str] = []
    if not isinstance(catalog, dict):
        return ["root: catalog must be a mapping"]
    for field in ROOT_FIELDS:
        if field not in catalog:
            errors.append(f"root: missing field '{field}'")
    for field in sorted(set(catalog) - set(ROOT_FIELDS)):
        errors.append(f"root: unexpected field '{field}'")
    version = catalog.get("version")
    if not isinstance(version, str) or not rr.VERSION_PATTERN.fullmatch(version):
        errors.append("root: version must be a string in MAJOR.MINOR form")
    rr._validate_change_history(catalog, errors)
    requirements = catalog.get("requirements")
    if not isinstance(requirements, list):
        errors.append("root: requirements must be a list")
        return errors

    entries: dict[str, dict[str, Any]] = {}
    for index, entry in enumerate(requirements):
        sr_id = _validate_requirement(entry, index, data, errors)
        if sr_id is None:
            continue
        if sr_id in entries:
            errors.append(f"{sr_id}: duplicate SR id")
            continue
        entries[sr_id] = entry
    ids = list(entries)
    if ids != sorted(ids):
        errors.append("requirements: SR ids must appear in ascending order")
    rul._validate_replacements(entries, errors)
    return errors


def validate_repository(repo_root: Path = rr.REPO_ROOT) -> list[str]:
    data = load_reference_data(repo_root)
    return validate_catalog(rr.load_catalog(repo_root / CATALOG_PATH), data)


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
        print(f"SR catalog validation: FAIL ({len(errors)} error(s))", file=sys.stderr)
        return 1
    catalog = rr.load_catalog(rr.REPO_ROOT / CATALOG_PATH)
    print("SR catalog validation: PASS")
    print(f"version: {catalog['version']}")
    print(f"requirements: {len(catalog['requirements'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
