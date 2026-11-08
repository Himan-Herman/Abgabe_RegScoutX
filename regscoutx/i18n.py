"""I18N: zentrale Auflösung sichtbarer Texte in Deutsch und Englisch (SR-026, SR-027).

Drei Quellen, keine Duplikate:
- UI- und Berichtstexte mit stabilen, semantischen Schlüsseln aus
  regscoutx/resources/i18n/<sprache>.json;
- Bezeichnungen fachlicher Codes aus enum_labels in DATA_MODEL.yaml;
- Themencluster und Lebenszyklusphasen aus CONTROLLED_VOCABULARY.md.
Regulatorische Katalogtexte (RR, RUL, RR_MEASURE) werden nicht hierher kopiert.
Fehlende Schlüssel oder Parameter sind Fehler; es gibt keinen stillen Fallback
in eine andere Sprache.
"""

from __future__ import annotations

import json
import string
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from regscoutx.catalog_repository import CatalogRepository
from regscoutx.domain import Language
from regscoutx.errors import I18nError

RESOURCES = Path(__file__).resolve().parent / "resources" / "i18n"


def load_messages(language: Language) -> Mapping[str, str]:
    path = RESOURCES / f"{language.value}.json"
    try:
        messages = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise I18nError(language.value, f"cannot read {path.name}") from exc
    if not isinstance(messages, dict) or not all(
            isinstance(k, str) and isinstance(v, str) and v.strip() for k, v in messages.items()):
        raise I18nError(language.value, "messages must map keys to non-empty strings")
    return MappingProxyType(messages)


def placeholders(template: str) -> frozenset[str]:
    return frozenset(name for _, name, _, _ in string.Formatter().parse(template) if name)


class Translator:
    """Texte einer Sprache; Codes bleiben sprachneutral."""

    def __init__(self, catalogs: CatalogRepository, language: Language) -> None:
        if not isinstance(language, Language):
            raise I18nError(language, "unsupported language")
        self._catalogs = catalogs
        self.language = language
        self._messages = load_messages(language)

    def text(self, key: str, /, **params: Any) -> str:
        template = self._messages.get(key)
        if template is None:
            raise I18nError(self.language.value, f"missing key '{key}'")
        if placeholders(template) != set(params):
            raise I18nError(self.language.value, f"parameters {sorted(params)} do not match '{key}'")
        return template.format(**params)

    def code(self, enum_name: str, code: str) -> str:
        try:
            return self._catalogs.enum_label(enum_name, code, self.language)
        except KeyError as exc:
            raise I18nError(self.language.value, f"missing label {enum_name}.{code}") from exc

    def phase(self, code: str) -> str:
        return self._catalogs.phase_label(code, self.language)

    def theme(self, code: str) -> str:
        return self._catalogs.theme_label(code, self.language)

    def number(self, value: int) -> str:
        grouped = f"{value:,}"
        return grouped.replace(",", self.text("format.thousands_separator"))

    def percent(self, part: int, total: int) -> str:
        if total == 0:
            return self.text("value.not_available")
        value = f"{100 * part / total:.1f}".replace(".", self.text("format.decimal_separator"))
        return self.text("format.percent", value=value)

    def date(self, iso_date: str) -> str:
        year, month, day = iso_date[:10].split("-")
        return self.text("format.date", year=year, month=month, day=day)

    def value(self, value: Any) -> str:
        if value is True:
            return self.text("value.true")
        if value is False:
            return self.text("value.false")
        if value is None:
            return self.text("value.not_available")
        return str(value)
