"""CATALOG_REPOSITORY: zentrale, schreibgeschützte Laufzeitsicht auf die versionierten Kataloge.

Lädt SOURCES, RR_CATALOG, RUL_CATALOG, SR_CATALOG, DATA_MODEL, die Applicability-
Zuordnung und den Maßnahmenkatalog (RR_MEASURE) genau einmal,
prüft sie vorher fail-closed mit den bestehenden Validatoren und stellt sie
unveränderlich bereit. Regulatorische Inhalte werden nicht verändert.
"""

from __future__ import annotations

import re
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from regscoutx import _validation
from regscoutx.domain import CatalogVersionSet, Language
from regscoutx.errors import (
    CatalogValidationError,
    UnknownOutputError,
    UnknownRequirementError,
    UnknownRuleError,
)

SOURCES_VERSION_PATTERN = re.compile(r"^Version (\d+\.\d+) ·", re.MULTILINE)
PHASE_LABEL_PATTERN = re.compile(r"^### 3\.\d+\s+(.+?)\s*\n\*English: (.+?)\*\s*$", re.MULTILINE)
SOURCE_HEADING_PATTERN = re.compile(r"^## (SRC-\d{3}) · (.+?)\s*$", re.MULTILINE)
THEME_LABEL_PATTERN = re.compile(r"^### 1\.\d+\s+(.+?)\s*\n\*English: (.+?)\*\s*$", re.MULTILINE)


def _parse_labels(pattern: re.Pattern[str], text: str, name: str) -> dict[str, dict[str, str]]:
    labels = {de.strip(): {"de": de.strip(), "en": en.strip()} for de, en in pattern.findall(text)}
    if not labels:
        raise CatalogValidationError([f"no {name} labels found in controlled vocabulary"])
    return labels


def parse_phase_labels(text: str) -> dict[str, dict[str, str]]:
    """DE/EN-Bezeichnungen der Lebenszyklusphasen aus CONTROLLED_VOCABULARY.md."""
    return _parse_labels(PHASE_LABEL_PATTERN, text, "lifecycle phase")


def parse_theme_labels(text: str) -> dict[str, dict[str, str]]:
    """DE/EN-Bezeichnungen der Themencluster aus CONTROLLED_VOCABULARY.md."""
    return _parse_labels(THEME_LABEL_PATTERN, text, "theme cluster")


def freeze(value: Any) -> Any:
    """Verschachtelte Katalogdaten unveränderlich machen."""
    if isinstance(value, dict):
        return MappingProxyType({key: freeze(item) for key, item in value.items()})
    if isinstance(value, list):
        return tuple(freeze(item) for item in value)
    return value


class CatalogRepository:
    """Schreibgeschützte Kataloge mit ID-Auflösung; unbekannte IDs werden abgelehnt."""

    def __init__(self, rul_catalog: Mapping[str, Any], rr_catalog: Mapping[str, Any],
                 sr_catalog: Mapping[str, Any], applicability: Mapping[str, Any],
                 versions: CatalogVersionSet, measure_catalog: Mapping[str, Any] | None = None,
                 phase_labels: Mapping[str, Mapping[str, str]] | None = None,
                 theme_labels: Mapping[str, Mapping[str, str]] | None = None,
                 enum_labels: Mapping[str, Mapping[str, Mapping[str, str]]] | None = None,
                 source_designations: Mapping[str, str] | None = None) -> None:
        self._versions = versions
        self._source_designations = freeze(dict(source_designations or {}))
        self._measures = freeze(dict(measure_catalog or {"evidence_types": {}, "measures": {},
                                                         "requirements": {}}))
        self._phase_labels = freeze(dict(phase_labels or {}))
        self._theme_labels = freeze(dict(theme_labels or {}))
        self._enum_labels = freeze(dict(enum_labels or {}))
        self._applicability = freeze(dict(applicability))
        self._rul = freeze(dict(rul_catalog))
        # Ersetzte Regeln bleiben im Katalog für die Herkunft erhalten, sind
        # aber kein ausführbarer Einstieg in die aktuelle Laufzeitsicht.
        self._rules = MappingProxyType({rule["id"]: rule for rule in self._rul["rules"]
                                       if rule["status"] == "aktiv"})
        self._requirements = MappingProxyType(
            {entry["id"]: entry for entry in freeze(rr_catalog["requirements"])})
        self._system_requirements = MappingProxyType(
            {entry["id"]: entry for entry in freeze(sr_catalog["requirements"])})

    @classmethod
    def load(cls, repo_root: Path | None = None) -> CatalogRepository:
        """Alle Kataloge validieren und laden; jeder Befund bricht das Laden ab."""
        root = Path(repo_root) if repo_root is not None else _validation.REPO_ROOT
        try:
            errors = _validation.validation_errors(root)
            if errors:
                raise CatalogValidationError(errors)
            catalogs = {name: _validation.load_yaml(root / path)
                        for name, path in _validation.PATHS.items() if name != "sources"}
            sources_text = (root / _validation.PATHS["sources"]).read_text(encoding="utf-8")
            vocabulary = (root / _validation.VOCABULARY_PATH).read_text(encoding="utf-8")
            phase_labels = parse_phase_labels(vocabulary)
            theme_labels = parse_theme_labels(vocabulary)
        except _validation.LOAD_ERRORS as exc:
            raise CatalogValidationError([str(exc)]) from exc
        except OSError as exc:
            raise CatalogValidationError([f"cannot read catalog: {exc}"]) from exc
        match = SOURCES_VERSION_PATTERN.search(sources_text)
        if match is None:
            raise CatalogValidationError(["source register version not found"])
        versions = CatalogVersionSet(
            sources_version=match.group(1),
            rr_catalog_version=catalogs["rr"]["version"],
            rul_catalog_version=catalogs["rul"]["version"],
            data_model_version=catalogs["data_model"]["version"],
            rr_applicability_version=catalogs["rr_applicability"]["version"],
            rr_measure_version=catalogs["rr_measure"]["version"],
        )
        return cls(catalogs["rul"], catalogs["rr"], catalogs["sr"],
                   catalogs["rr_applicability"], versions, catalogs["rr_measure"], phase_labels,
                   theme_labels, catalogs["data_model"]["enum_labels"],
                   dict(SOURCE_HEADING_PATTERN.findall(sources_text)))

    @property
    def versions(self) -> CatalogVersionSet:
        return self._versions

    @property
    def entry_points(self) -> tuple[str, ...]:
        return self._rul["entry_points"]

    @property
    def class_order(self) -> tuple[str, ...]:
        return self._rul["class_order"]

    @property
    def rule_ids(self) -> tuple[str, ...]:
        return tuple(self._rules)

    def has_rule(self, rule_id: Any) -> bool:
        return isinstance(rule_id, str) and rule_id in self._rules

    def rule(self, rule_id: Any) -> Mapping[str, Any]:
        if not self.has_rule(rule_id):
            raise UnknownRuleError(rule_id)
        return self._rules[rule_id]

    def output(self, name: Any) -> Mapping[str, Any]:
        outputs = self._rul["outputs"]
        if not isinstance(name, str) or name not in outputs:
            raise UnknownOutputError(name)
        return outputs[name]

    def requirement(self, requirement_id: Any) -> Mapping[str, Any]:
        if not isinstance(requirement_id, str) or requirement_id not in self._requirements:
            raise UnknownRequirementError(requirement_id)
        return self._requirements[requirement_id]

    @property
    def requirement_count(self) -> int:
        return len(self._requirements)

    @property
    def requirement_ids(self) -> tuple[str, ...]:
        return tuple(self._requirements)

    @property
    def applicability(self) -> Mapping[str, Any]:
        """Technische Applicability-Zuordnung der RR (RR_APPLICABILITY.yaml), schreibgeschützt."""
        return self._applicability

    @property
    def measure_catalog_version(self) -> str | None:
        return self._measures.get("version")

    def measure_mapping(self, requirement_id: Any) -> Mapping[str, Any]:
        """Mapping-Status und vorgesehene Maßnahmen einer RR (RR_MEASURE_CATALOG.yaml)."""
        self.requirement(requirement_id)
        mapping = self._measures["requirements"].get(requirement_id)
        if mapping is None:
            raise UnknownRequirementError(requirement_id)
        return mapping

    def measure(self, measure_key: str) -> Mapping[str, Any]:
        return self._measures["measures"][measure_key]

    def evidence_type(self, evidence_type_key: str) -> Mapping[str, Any]:
        return self._measures["evidence_types"][evidence_type_key]

    @property
    def lifecycle_phases(self) -> tuple[str, ...]:
        """Kontrollierte Lebenszyklusphasen in Vokabularreihenfolge."""
        return tuple(self._phase_labels)

    @property
    def theme_clusters(self) -> tuple[str, ...]:
        """Kontrollierte Themencluster in Vokabularreihenfolge."""
        return tuple(self._theme_labels)

    def theme_label(self, theme: str, language: Language) -> str:
        return self._theme_labels[theme][language.value]

    def enum_label(self, enum_name: str, code: str, language: Language) -> str:
        """Zentrale DE/EN-Bezeichnung eines Codes aus enum_labels in DATA_MODEL.yaml."""
        return self._enum_labels[enum_name][code][language.value]

    @property
    def labelled_enums(self) -> tuple[str, ...]:
        return tuple(self._enum_labels)

    def enum_codes(self, enum_name: str) -> tuple[str, ...]:
        """Codes eines bezeichneten Enums in der Reihenfolge von DATA_MODEL.yaml."""
        return tuple(self._enum_labels[enum_name])

    @property
    def source_designations(self) -> Mapping[str, str]:
        """Kurzbezeichnung je SRC-ID aus den Überschriften des Quellenregisters (unübersetzt)."""
        return self._source_designations

    def phase_label(self, phase: str, language: Language) -> str:
        """Bezeichnung einer kontrollierten Lebenszyklusphase in der gewünschten Sprache."""
        return self._phase_labels[phase][language.value]

    def system_requirement(self, sr_id: Any) -> Mapping[str, Any]:
        if not isinstance(sr_id, str) or sr_id not in self._system_requirements:
            raise UnknownRequirementError(sr_id)
        return self._system_requirements[sr_id]

    def question(self, rule_id: str, language: Language) -> str:
        """Nutzerfrage einer Regel in der gewünschten Sprache aus dem Katalog."""
        return self.rule(rule_id)["question"][language.value]

    def output_label(self, name: str, language: Language) -> str:
        return self.output(name)["label"][language.value]

    def review_cause(self, rule_id: str, matched_condition: Any, language: Language) -> str:
        """Dokumentierte Ursache eines Review-Ausgangs aus dem Katalog."""
        for branch in self.rule(rule_id)["branches"]:
            if branch["when"] == matched_condition and type(branch["when"]) is type(matched_condition):
                return branch["review_cause"][language.value]
        raise UnknownOutputError(f"{rule_id}:{matched_condition!r}")
