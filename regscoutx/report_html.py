"""REPORTING: semantisches, eigenständiges HTML aus einem ReportDocument.

Setzt Blöcke nur um; keine Texte, keine Inhalte, kein Katalog- oder
Persistenzzugriff. Jeder Text wird escaped. Keine Skripte, keine externen
Ressourcen, keine Links außer Sprungmarken. Farben, Typografie und Abstände
kommen aus tokens.json; Light/Dark/System über prefers-color-scheme und
data-theme, Druck über ein eigenes Farbschema.
"""

from __future__ import annotations

import json
from html import escape
from pathlib import Path
from typing import Any, Mapping

from regscoutx.report_document import (
    Chips,
    Distribution,
    Fields,
    Group,
    Heading,
    Para,
    ReportDocument,
    Spine,
    Table,
)

RESOURCES = Path(__file__).resolve().parent / "resources" / "report"


def load_tokens() -> Mapping[str, Any]:
    return json.loads((RESOURCES / "tokens.json").read_text(encoding="utf-8"))


def _e(text: Any) -> str:
    return escape(str(text), quote=True)


def _variables(colors: Mapping[str, str]) -> str:
    return "".join(f"--color-{name.replace('_', '-')}:{value};" for name, value in colors.items())


def token_css(tokens: Mapping[str, Any]) -> str:
    """CSS-Variablen aus den Tokens; Typo- und Abstandsgrößen relativ zur Grundschrift (rem)."""
    body = tokens["type"]["body"]
    rem = lambda pt: f"{pt / body:.4f}rem"  # noqa: E731
    px = lambda pt: f"{max(1, round(pt * 4 / 3))}px"  # noqa: E731
    fonts = tokens["font"]
    base = (f'--font-sans:"{fonts["sans"]}",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;'
            f'--font-mono:"{fonts["mono"]}",ui-monospace,"SFMono-Regular",Menlo,monospace;'
            f'--type-line-height:{tokens["type"]["line_height"]};'
            f'--type-measure:{tokens["type"]["measure_ch"]}ch;'
            + "".join(f"--type-{k}:{rem(v)};" for k, v in tokens["type"].items()
                      if k not in ("line_height", "measure_ch"))
            + "".join(f"--space-{k}:{rem(v)};" for k, v in tokens["space"].items())
            + "".join(f"--radius-{k}:{px(v)};" for k, v in tokens["radius"].items())
            + "".join(f"--border-{k}:{px(v)};" for k, v in tokens["border"].items()))
    colors = tokens["color"]
    return (f"@font-face{{font-family:\"{fonts['sans']}\";src:local(\"{fonts['sans']}\");}}"
            f"@font-face{{font-family:\"{fonts['mono']}\";src:local(\"{fonts['mono']}\");}}"
            f":root{{color-scheme:light dark;{base}{_variables(colors['light'])}}}"
            f"@media (prefers-color-scheme:dark){{:root:not([data-theme=\"light\"])"
            f"{{{_variables(colors['dark'])}}}}}"
            f":root[data-theme=\"dark\"]{{{_variables(colors['dark'])}}}"
            f"@media print{{:root{{color-scheme:light;{_variables(colors['print'])}}}}}")


class HtmlRenderer:

    def __init__(self, tokens: Mapping[str, Any] | None = None) -> None:
        self._tokens = tokens or load_tokens()
        self._css = token_css(self._tokens) + (RESOURCES / "report.css").read_text(encoding="utf-8")

    def render(self, document: ReportDocument) -> str:
        parts = [
            "<!DOCTYPE html>",
            f'<html lang="{_e(document.language)}">',
            "<head>",
            '<meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1">',
            '<meta name="color-scheme" content="light dark">',
            '<meta name="robots" content="noindex">',
            f'<meta name="regscoutx-content-hash" content="{_e(document.content_hash)}">',
            f"<title>{_e(document.title)}</title>",
            f"<style>{self._css}</style>",
            "</head>",
            "<body>",
            f'<a class="skip-link" href="#{_e(document.sections[0].anchor)}">'
            f"{_e(document.sections[0].title)}</a>",
            '<main class="report">',
            '<header class="deck">',
            f'<p class="deck__brand">{_e(document.running_header)}</p>',
            f"<h1>{_e(document.title)}</h1>",
            f'<p class="deck__subtitle">{_e(document.subtitle)}</p>',
        ]
        parts += [f'<p class="banner" role="note">{_e(text)}</p>' for text in document.banners]
        parts.append(self._fields(document.cover))
        parts.append("</header>")
        parts.append(f'<nav class="toc" aria-labelledby="toc-title"><h2 id="toc-title">'
                     f"{_e(document.contents_title)}</h2><ol>")
        parts += [f'<li><a href="#{_e(s.anchor)}">{_e(s.title)}</a></li>' for s in document.sections]
        parts.append("</ol></nav>")
        for section in document.sections:
            parts.append(f'<section id="{_e(section.anchor)}" aria-labelledby="{_e(section.anchor)}-h">')
            parts.append(f'<h2 id="{_e(section.anchor)}-h">{_e(section.title)}</h2>')
            parts += [self._block(block) for block in section.blocks]
            parts.append("</section>")
        parts += ["</main>", "</body>", "</html>"]
        return "\n".join(parts) + "\n"

    def _block(self, block: Any) -> str:
        if isinstance(block, Heading):
            anchor = f' id="{_e(block.anchor)}"' if block.anchor else ""
            return f"<h{block.level}{anchor}>{_e(block.text)}</h{block.level}>"
        if isinstance(block, Para):
            return f'<p class="p--{_e(block.style)}">{_e(block.text)}</p>'
        if isinstance(block, Fields):
            return self._fields(block)
        if isinstance(block, Chips):
            items = "".join(f'<li class="chip"><span class="chip__label">{_e(c.label)}</span>'
                            f'<span class="{self._tone(c.tone)}">{_e(c.value)}</span></li>'
                            for c in block.items)
            return f'<ul class="chips">{items}</ul>'
        if isinstance(block, Table):
            return self._table(block)
        if isinstance(block, Spine):
            items = "".join(f'<li><span class="spine__stage">{_e(stage)}</span>'
                            f'<span class="spine__value">{_e(value)}</span></li>'
                            for stage, value in block.stages)
            return f'<ol class="spine" aria-label="{_e(block.caption)}">{items}</ol>'
        if isinstance(block, Distribution):
            return self._distribution(block)
        if isinstance(block, Group):
            inner = "".join(self._block(b) for b in block.blocks)
            return f'<article class="{_e(block.kind)}">{inner}</article>'
        raise TypeError(f"unsupported report block {type(block).__name__}")

    @staticmethod
    def _tone(tone: str | None) -> str:
        return f"tone tone--{_e(tone)}" if tone else ""

    def _fields(self, fields: Fields) -> str:
        rows = "".join(f"<dt>{_e(label)}</dt><dd{' class=\"mono\"' if mono else ''}>{_e(value)}</dd>"
                       for label, value, mono in fields.rows)
        return f'<dl class="fields">{rows}</dl>'

    def _table(self, table: Table) -> str:
        head = "".join(f'<th scope="col"{" class=\"num\"" if i in table.numeric else ""}>{_e(h)}</th>'
                       for i, h in enumerate(table.headers))
        body = []
        for row in table.rows:
            cells = []
            for i, (text, tone) in enumerate(row):
                classes = [c for c in ("num" if i in table.numeric else "",
                                       "mono" if i in table.mono else "",
                                       self._tone(tone)) if c]
                cls = f' class="{" ".join(classes)}"' if classes else ""
                tag = "th" if i == 0 else "td"
                scope = ' scope="row"' if i == 0 else ""
                cells.append(f"<{tag}{scope}{cls}>{_e(text)}</{tag}>")
            body.append(f"<tr>{''.join(cells)}</tr>")
        if not body and table.empty:
            body.append(f'<tr><td class="empty" colspan="{len(table.headers)}">{_e(table.empty)}</td></tr>')
        return (f'<div class="table-wrap" role="region" tabindex="0" aria-label="{_e(table.caption)}">'
                f"<table><caption>{_e(table.caption)}</caption><thead><tr>{head}</tr></thead>"
                f"<tbody>{''.join(body)}</tbody></table></div>")

    def _distribution(self, block: Distribution) -> str:
        segments = "".join(
            f'<span class="distribution__segment--{_e(tone)}" style="flex:{count} 0 0"></span>'
            for _, count, tone in block.items if count)
        legend = "".join(f'<li><span class="tone tone--{_e(tone)}">{_e(text)}</span></li>'
                         for (_, _, tone), text in zip(block.items, block.legend))
        return (f'<figure class="distribution"><figcaption>{_e(block.caption)}</figcaption>'
                f'<div class="distribution__bar" aria-hidden="true">{segments}</div>'
                f'<ul class="distribution__legend">{legend}</ul></figure>')
