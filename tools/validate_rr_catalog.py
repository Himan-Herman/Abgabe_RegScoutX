"""Formale Strukturprüfung des regulatorischen Anforderungskatalogs.

Der Validator prüft ausschließlich formale und strukturelle Konsistenz von
docs/03-regulatory/RR_CATALOG.yaml. Er trifft keine Aussage über regulatorische
Richtigkeit; siehe tools/README.md und ADR-0001.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent

CATALOG_PATH = Path("docs/03-regulatory/RR_CATALOG.yaml")
VOCABULARY_PATH = Path("docs/03-regulatory/CONTROLLED_VOCABULARY.md")
SOURCES_PATH = Path("docs/03-regulatory/SOURCES.md")
CONVENTIONS_PATH = Path("docs/00-project/DOCUMENTATION_CONVENTIONS.md")

ROOT_FIELDS = ("version", "requirements", "change_history")
RR_FIELDS = (
    "id",
    "status",
    "title",
    "requirement_text",
    "sources",
    "theme_cluster",
    "lifecycle_phases",
    "uncertainty",
    "replaces",
    "replaced_by",
)
LANGUAGE_KEYS = ("de", "en")
SOURCE_KEYS = ("primary", "supplementary")

RR_ID_PATTERN = re.compile(r"^RR-\d{3}$")
VERSION_PATTERN = re.compile(r"^\d+\.\d+$")
SRC_ID_PATTERN = re.compile(r"^SRC-\d{3}$")

THEME_HEADING_PATTERN = re.compile(r"^### 1\.\d+\s+(.+?)\s*$", re.MULTILINE)
PHASE_HEADING_PATTERN = re.compile(r"^### 3\.\d+\s+(.+?)\s*$", re.MULTILINE)
SRC_HEADING_PATTERN = re.compile(r"^## (SRC-\d{3})(?:\s|$)", re.MULTILINE)
INLINE_CODE_PATTERN = re.compile(r"`([^`]+)`")
# Die Vokabularzeile muss vollständig aus Inline-Code-Werten bestehen, damit
# beliebige Prosa mit Inline-Code nicht als Statusvokabular durchgeht.
STATUS_LINE_PATTERN = re.compile(r"^`[^`]+`(?:\s*·\s*`[^`]+`)*$")

STATUS_MARKER = "Jedes Element führt einen Status aus folgendem Vokabular:"

MINIMUM_PYTHON = (3, 12)


class ReferenceDataError(Exception):
    """Führende Referenzdatei ist nicht lesbar oder nicht interpretierbar."""


class CatalogLoadError(Exception):
    """Katalogdatei ist nicht lesbar oder nicht als YAML parsebar."""


@dataclass(frozen=True)
class ReferenceData:
    """Aus den führenden Dokumenten ausgelesene zulässige Werte."""

    theme_clusters: frozenset[str]
    lifecycle_phases: frozenset[str]
    source_ids: frozenset[str]
    status_values: frozenset[str]


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ReferenceDataError(f"cannot read {path}: {exc}") from exc


def _unique(values: list[str], *, label: str, origin: str) -> frozenset[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    if duplicates:
        raise ReferenceDataError(
            f"duplicate {label} in {origin}: {', '.join(sorted(duplicates))}"
        )
    return frozenset(seen)


def parse_controlled_vocabulary(text: str) -> tuple[frozenset[str], frozenset[str]]:
    """Themencluster und Lebenszyklusphasen aus CONTROLLED_VOCABULARY.md lesen."""
    themes = [m.strip() for m in THEME_HEADING_PATTERN.findall(text)]
    phases = [m.strip() for m in PHASE_HEADING_PATTERN.findall(text)]
    if not themes:
        raise ReferenceDataError(
            "no theme cluster headings ('### 1.x <value>') found in controlled vocabulary"
        )
    if not phases:
        raise ReferenceDataError(
            "no lifecycle phase headings ('### 3.x <value>') found in controlled vocabulary"
        )
    return (
        _unique(themes, label="theme cluster", origin="controlled vocabulary"),
        _unique(phases, label="lifecycle phase", origin="controlled vocabulary"),
    )


def parse_source_ids(text: str) -> frozenset[str]:
    """Vergebene SRC-IDs ausschließlich aus den führenden Quellenüberschriften lesen."""
    ids = SRC_HEADING_PATTERN.findall(text)
    if not ids:
        raise ReferenceDataError(
            "no source headings ('## SRC-NNN ...') found in source register"
        )
    return _unique(ids, label="source id", origin="source register")


def parse_status_vocabulary(text: str) -> frozenset[str]:
    """Statusvokabular aus DOCUMENTATION_CONVENTIONS.md lesen."""
    marker_index = text.find(STATUS_MARKER)
    if marker_index == -1:
        raise ReferenceDataError("status vocabulary marker not found in conventions")
    remainder = text[marker_index + len(STATUS_MARKER) :]
    # Das Vokabular steht in der ersten nichtleeren Zeile nach dem Marker.
    for line in remainder.splitlines():
        candidate = line.strip()
        if not candidate:
            continue
        if not STATUS_LINE_PATTERN.fullmatch(candidate):
            raise ReferenceDataError(
                "status vocabulary line does not consist solely of inline-code values "
                f"separated by '·': {candidate!r}"
            )
        values = [value.strip() for value in INLINE_CODE_PATTERN.findall(candidate)]
        values = [value for value in values if value]
        if not values:
            raise ReferenceDataError("no status values found after status vocabulary marker")
        return _unique(values, label="status value", origin="conventions")
    raise ReferenceDataError("no status values found after status vocabulary marker")


def load_reference_data(repo_root: Path = REPO_ROOT) -> ReferenceData:
    """Alle zulässigen Werte aus den führenden Dokumenten laden (fail-closed)."""
    themes, phases = parse_controlled_vocabulary(_read_text(repo_root / VOCABULARY_PATH))
    return ReferenceData(
        theme_clusters=themes,
        lifecycle_phases=phases,
        source_ids=parse_source_ids(_read_text(repo_root / SOURCES_PATH)),
        status_values=parse_status_vocabulary(_read_text(repo_root / CONVENTIONS_PATH)),
    )


class _UniqueKeyLoader(yaml.SafeLoader):
    """SafeLoader, der doppelte Mapping-Schlüssel meldet statt sie zu überschreiben."""


def _construct_mapping_without_duplicates(loader: _UniqueKeyLoader, node: yaml.MappingNode,
                                          deep: bool = False) -> dict[Any, Any]:
    loader.flatten_mapping(node)
    seen: set[Any] = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in seen
        except TypeError:
            # Nicht hashbare Schlüssel meldet der SafeConstructor unten selbst.
            continue
        if duplicate:
            mark = key_node.start_mark
            raise CatalogLoadError(
                f"duplicate YAML mapping key '{key}' "
                f"at line {mark.line + 1}, column {mark.column + 1}"
            )
        seen.add(key)
    return yaml.SafeLoader.construct_mapping(loader, node, deep=deep)


_UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_mapping_without_duplicates,
)


def load_catalog_text(text: str, origin: str = "<text>") -> Any:
    """YAML-Text mit der Loader-Logik des Validators parsen."""
    try:
        return yaml.load(text, Loader=_UniqueKeyLoader)
    except yaml.YAMLError as exc:
        raise CatalogLoadError(f"cannot parse {origin} as YAML: {exc}") from exc


def load_catalog(path: Path) -> Any:
    """Katalog laden; nicht parsebares YAML führt zum kontrollierten Abbruch."""
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise CatalogLoadError(f"cannot read {path}: {exc}") from exc
    return load_catalog_text(raw, origin=str(path))


def _validate_root(catalog: Any, errors: list[str]) -> bool:
    if not isinstance(catalog, dict):
        errors.append("root: catalog must be a mapping")
        return False
    missing = [field for field in ROOT_FIELDS if field not in catalog]
    unexpected = sorted(set(catalog) - set(ROOT_FIELDS))
    for field in missing:
        errors.append(f"root: missing field '{field}'")
    for field in unexpected:
        errors.append(f"root: unexpected field '{field}'")

    version = catalog.get("version")
    if not isinstance(version, str):
        errors.append("root: version must be a string in MAJOR.MINOR form")
    elif not VERSION_PATTERN.fullmatch(version):
        errors.append(f"root: version must match MAJOR.MINOR, found '{version}'")

    if not isinstance(catalog.get("requirements"), list):
        errors.append("root: requirements must be a list")
    history = catalog.get("change_history")
    if not isinstance(history, list):
        errors.append("root: change_history must be a list")
    elif not history:
        errors.append("root: change_history must not be empty")
    return isinstance(catalog.get("requirements"), list)


def _validate_text_pair(entry: dict[str, Any], field: str, label: str, errors: list[str]) -> None:
    value = entry.get(field)
    if not isinstance(value, dict):
        errors.append(f"{label}: {field} must be a mapping with keys 'de' and 'en'")
        return
    for key in LANGUAGE_KEYS:
        if key not in value:
            errors.append(f"{label}: {field} missing key '{key}'")
    for key in sorted(set(value) - set(LANGUAGE_KEYS)):
        errors.append(f"{label}: {field} unexpected key '{key}'")
    for key in LANGUAGE_KEYS:
        if key not in value:
            continue
        text = value[key]
        if not isinstance(text, str):
            errors.append(f"{label}: {field}.{key} must be a string")
        elif not text.strip():
            errors.append(f"{label}: {field}.{key} must not be empty")


def _validate_locator(locator: Any, field: str, label: str, reference: ReferenceData,
                      errors: list[str]) -> None:
    if not isinstance(locator, str):
        errors.append(f"{label}: {field} entries must be strings")
        return
    if "@" in locator:
        errors.append(f"{label}: locator contains '@': '{locator}'")
        return
    head, separator, rest = locator.partition("#")
    if not separator:
        errors.append(f"{label}: locator must contain '#': '{locator}'")
        return
    if not SRC_ID_PATTERN.fullmatch(head):
        errors.append(f"{label}: locator must start with a single SRC-NNN id: '{locator}'")
        return
    if not rest.strip():
        errors.append(f"{label}: locator must name a position after '#': '{locator}'")
    if head not in reference.source_ids:
        errors.append(f"{label}: unknown source id '{head}' in locator '{locator}'")


def _validate_sources(entry: dict[str, Any], label: str, reference: ReferenceData,
                      errors: list[str]) -> None:
    sources = entry.get("sources")
    if not isinstance(sources, dict):
        errors.append(f"{label}: sources must be a mapping with keys 'primary' and 'supplementary'")
        return
    for key in SOURCE_KEYS:
        if key not in sources:
            errors.append(f"{label}: sources missing key '{key}'")
    for key in sorted(set(sources) - set(SOURCE_KEYS)):
        errors.append(f"{label}: sources unexpected key '{key}'")

    for key in SOURCE_KEYS:
        if key not in sources:
            continue
        if not isinstance(sources[key], list):
            errors.append(f"{label}: sources.{key} must be a list")
            continue
        for locator in sources[key]:
            _validate_locator(locator, f"sources.{key}", label, reference, errors)

    primary = sources.get("primary")
    if isinstance(primary, list) and not primary:
        errors.append(f"{label}: sources.primary must not be empty")

    supplementary = sources.get("supplementary")
    if isinstance(primary, list) and isinstance(supplementary, list):
        overlap = sorted(
            {item for item in primary if isinstance(item, str)}
            & {item for item in supplementary if isinstance(item, str)}
        )
        for locator in overlap:
            errors.append(
                f"{label}: locator '{locator}' appears in both sources.primary "
                "and sources.supplementary"
            )


def _validate_replacement_lists(entry: dict[str, Any], label: str, own_id: str | None,
                                known_ids: set[str], errors: list[str]) -> None:
    for field in ("replaces", "replaced_by"):
        value = entry.get(field)
        if not isinstance(value, list):
            errors.append(f"{label}: {field} must be a list")
            continue
        for item in value:
            if not isinstance(item, str):
                errors.append(f"{label}: {field} entries must be strings")
                continue
            if not RR_ID_PATTERN.fullmatch(item):
                errors.append(f"{label}: {field} entry '{item}' is not a valid RR id")
                continue
            if own_id is not None and item == own_id:
                errors.append(f"{label}: self-reference in {field}")
                continue
            if item not in known_ids:
                errors.append(f"{label}: {field} references unknown RR id '{item}'")


def _validate_replacement_symmetry(entries: dict[str, dict[str, Any]], errors: list[str]) -> None:
    for rr_id, entry in entries.items():
        for item in entry.get("replaced_by", []) or []:
            counterpart = entries.get(item) if isinstance(item, str) else None
            if counterpart is None:
                continue
            if rr_id not in (counterpart.get("replaces") or []):
                errors.append(
                    f"{rr_id}: inconsistent replacement relation — "
                    f"{item}.replaces does not contain {rr_id}"
                )
        for item in entry.get("replaces", []) or []:
            counterpart = entries.get(item) if isinstance(item, str) else None
            if counterpart is None:
                continue
            if rr_id not in (counterpart.get("replaced_by") or []):
                errors.append(
                    f"{rr_id}: inconsistent replacement relation — "
                    f"{item}.replaced_by does not contain {rr_id}"
                )


def _validate_requirement(entry: Any, index: int, reference: ReferenceData,
                          errors: list[str]) -> str | None:
    label = f"requirements[{index}]"
    if not isinstance(entry, dict):
        errors.append(f"{label}: requirement must be a mapping")
        return None

    raw_id = entry.get("id")
    if isinstance(raw_id, str) and RR_ID_PATTERN.fullmatch(raw_id):
        label = raw_id
    elif not isinstance(raw_id, str):
        errors.append(f"{label}: id must be a string")
    else:
        errors.append(f"{label}: id '{raw_id}' does not match RR-NNN")

    for field in RR_FIELDS:
        if field not in entry:
            errors.append(f"{label}: missing field '{field}'")
    for field in sorted(set(entry) - set(RR_FIELDS)):
        errors.append(f"{label}: unexpected field '{field}'")

    status = entry.get("status")
    if not isinstance(status, str):
        errors.append(f"{label}: status must be a string")
    elif status not in reference.status_values:
        errors.append(f"{label}: unknown status '{status}'")

    _validate_text_pair(entry, "title", label, errors)
    _validate_text_pair(entry, "requirement_text", label, errors)
    _validate_sources(entry, label, reference, errors)

    theme = entry.get("theme_cluster")
    if not isinstance(theme, str):
        errors.append(f"{label}: theme_cluster must be a single string value")
    elif theme not in reference.theme_clusters:
        errors.append(f"{label}: unknown theme cluster '{theme}'")

    phases = entry.get("lifecycle_phases")
    if not isinstance(phases, list):
        errors.append(f"{label}: lifecycle_phases must be a list")
    elif not phases:
        errors.append(f"{label}: lifecycle_phases must not be empty")
    else:
        for phase in phases:
            if not isinstance(phase, str):
                errors.append(f"{label}: lifecycle_phases entries must be strings")
            elif phase not in reference.lifecycle_phases:
                errors.append(f"{label}: unknown lifecycle phase '{phase}'")

    uncertainty = entry.get("uncertainty")
    if uncertainty is None:
        pass
    elif not isinstance(uncertainty, str) or isinstance(uncertainty, bool):
        errors.append(f"{label}: uncertainty must be null or a non-empty string")
    elif not uncertainty.strip():
        errors.append(f"{label}: uncertainty must be null or a non-empty string")

    return label if isinstance(raw_id, str) and RR_ID_PATTERN.fullmatch(raw_id) else None


def _validate_change_history(catalog: dict[str, Any], errors: list[str]) -> None:
    history = catalog.get("change_history")
    if not isinstance(history, list) or not history:
        return

    seen: set[str] = set()
    for index, item in enumerate(history):
        label = f"change_history[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{label}: entry must be a mapping")
            continue
        version = item.get("version")
        if "version" not in item:
            errors.append(f"{label}: missing field 'version'")
        elif not isinstance(version, str):
            errors.append(f"{label}: version must be a string in MAJOR.MINOR form")
        elif not VERSION_PATTERN.fullmatch(version):
            errors.append(f"{label}: version must match MAJOR.MINOR, found '{version}'")
        elif version in seen:
            errors.append(f"{label}: duplicate change_history version '{version}'")
        else:
            seen.add(version)

        change = item.get("change")
        if "change" not in item:
            errors.append(f"{label}: missing field 'change'")
        elif not isinstance(change, str):
            errors.append(f"{label}: change must be a string")
        elif not change.strip():
            errors.append(f"{label}: change must not be empty")

    last = history[-1]
    if isinstance(last, dict) and isinstance(last.get("version"), str):
        if catalog.get("version") != last["version"]:
            errors.append(
                f"root: version '{catalog.get('version')}' does not match last "
                f"change_history version '{last['version']}'"
            )


def validate_catalog(catalog: Any, reference: ReferenceData) -> list[str]:
    """Bereits geladenes Katalogobjekt prüfen und alle Befunde sammeln."""
    errors: list[str] = []
    requirements_ok = _validate_root(catalog, errors)
    if not isinstance(catalog, dict):
        return errors

    _validate_change_history(catalog, errors)
    if not requirements_ok:
        return errors

    requirements = catalog["requirements"]
    seen_ids: set[str] = set()
    valid_ids: list[str] = []
    for index, entry in enumerate(requirements):
        rr_id = _validate_requirement(entry, index, reference, errors)
        if rr_id is None:
            continue
        if rr_id in seen_ids:
            errors.append(f"{rr_id}: duplicate RR id")
        seen_ids.add(rr_id)
        valid_ids.append(rr_id)

    # Ersetzungsbeziehungen erst prüfen, wenn alle IDs des Katalogs bekannt sind.
    entries_by_id: dict[str, dict[str, Any]] = {}
    for index, entry in enumerate(requirements):
        if not isinstance(entry, dict):
            continue
        rr_id = entry.get("id")
        label = rr_id if isinstance(rr_id, str) else f"requirements[{index}]"
        own_id = rr_id if isinstance(rr_id, str) else None
        _validate_replacement_lists(entry, label, own_id, set(valid_ids), errors)
        if isinstance(rr_id, str) and rr_id not in entries_by_id:
            entries_by_id[rr_id] = entry

    _validate_replacement_symmetry(entries_by_id, errors)
    return errors


def validate_repository(repo_root: Path = REPO_ROOT) -> list[str]:
    """Katalog und Referenzdaten aus dem Repository laden und prüfen."""
    reference = load_reference_data(repo_root)
    catalog = load_catalog(repo_root / CATALOG_PATH)
    return validate_catalog(catalog, reference)


def is_supported_python(version_info: tuple[int, ...] = sys.version_info) -> bool:
    """Prüfen, ob die laufende Python-Version die ADR-Untergrenze erfüllt."""
    return tuple(version_info[:2]) >= MINIMUM_PYTHON


def main() -> int:
    if not is_supported_python():
        running = ".".join(str(part) for part in sys.version_info[:3])
        minimum = ".".join(str(part) for part in MINIMUM_PYTHON)
        print(
            f"ERROR: Python >= {minimum} is required; running Python {running}",
            file=sys.stderr,
        )
        return 1

    try:
        errors = validate_repository()
    except (ReferenceDataError, CatalogLoadError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"RR catalog validation: FAIL ({len(errors)} error(s))", file=sys.stderr)
        return 1

    catalog = load_catalog(REPO_ROOT / CATALOG_PATH)
    print("RR catalog validation: PASS")
    print(f"version: {catalog['version']}")
    print(f"requirements: {len(catalog['requirements'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
