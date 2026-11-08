"""REPORTING: druckoptimierter PDF-Bericht (A4) aus demselben ReportDocument wie der HTML-Bericht.

Technologie: ReportLab (ADR-0006), lokal und ohne Netzzugriff. Der Renderer setzt
nur Blöcke um und enthält keine Texte oder Inhalte. Schriften (IBM Plex, SIL OFL
1.1) werden aus regscoutx/resources/fonts eingebettet. Jeder Text wird für das
Paragraph-Markup von ReportLab escaped. Das Druck-Farbschema stammt aus
tokens.json; ein Dark Mode wird im PDF nicht verwendet.
"""

from __future__ import annotations

import io
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping
from xml.sax.saxutils import escape

from reportlab.graphics.shapes import Drawing, Rect
from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.platypus import (
    BaseDocTemplate,
    CondPageBreak,
    Frame,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table as RLTable,
    TableStyle,
)

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
from regscoutx.report_html import load_tokens

FONTS = Path(__file__).resolve().parent / "resources" / "fonts"
SANS, SANS_BOLD, SANS_ITALIC, MONO = ("RegScoutXSans", "RegScoutXSans-Bold", "RegScoutXSans-Italic",
                                      "RegScoutXMono")


@dataclass(frozen=True)
class PdfResult:
    data: bytes
    pages: int
    headings: tuple[tuple[int, str, int], ...]  # (Ebene, Text, Seite)


def _x(text: Any) -> str:
    return escape(str(text))


def _hex(color: Any) -> str:
    return "#" + color.hexval()[2:]


def register_fonts(tokens: Mapping[str, Any]) -> None:
    files = tokens["font"]["files"]
    for name, key in ((SANS, "sans"), (SANS_BOLD, "sans_bold"), (SANS_ITALIC, "sans_italic"),
                      (MONO, "mono")):
        if name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(name, str(FONTS / files[key])))
    pdfmetrics.registerFontFamily(SANS, normal=SANS, bold=SANS_BOLD, italic=SANS_ITALIC,
                                  boldItalic=SANS_BOLD)


class _NumberedCanvas(pdfcanvas.Canvas):
    """Zweiphasige Seitenzählung für „Seite x von y“."""

    footer: tuple[str, str, Any, float] = ("", "", colors.black, 8)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._states: list[dict[str, Any]] = []

    def showPage(self) -> None:  # noqa: N802 (ReportLab-API)
        self._states.append(dict(self.__dict__))
        self._startPage()

    def save(self) -> None:
        total = len(self._states)
        for state in self._states:
            self.__dict__.update(state)
            template, header, color, size = self.footer
            width, _ = self._pagesize
            self.setFont(SANS, size)
            self.setFillColor(color)
            self.drawRightString(width - 18 * mm, 11 * mm,
                                 template % {"page": self._pageNumber, "pages": total})
            super().showPage()
        super().save()


class _Doc(BaseDocTemplate):

    def __init__(self, buffer: io.BytesIO, **kwargs: Any) -> None:
        super().__init__(buffer, **kwargs)
        self.headings: list[tuple[int, str, int]] = []

    def afterFlowable(self, flowable: Any) -> None:  # noqa: N802 (ReportLab-API)
        level = getattr(flowable, "_regscoutx_level", None)
        if level is not None:
            text = flowable._regscoutx_text
            key = f"h{len(self.headings)}"
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(text, key, level=level - 2, closed=level > 2)
            self.headings.append((level, text, self.page))


class PdfRenderer:

    def __init__(self, tokens: Mapping[str, Any] | None = None) -> None:
        self._tokens = tokens or load_tokens()
        register_fonts(self._tokens)
        self._c = {name: colors.HexColor(value) for name, value in self._tokens["color"]["print"].items()}
        self._s = self._styles()

    def _tone(self, tone: str | None) -> Any:
        return self._c[f"tone_{tone}"] if tone else self._c["text_primary"]

    def _styles(self) -> dict[str, ParagraphStyle]:
        t, sp, c = self._tokens["type"], self._tokens["space"], self._c
        lead = t["line_height"]

        def style(name: str, size: float, **kw: Any) -> ParagraphStyle:
            base = dict(fontName=SANS, fontSize=size, leading=size * lead,
                        textColor=c["text_primary"], spaceAfter=sp["s"])
            base.update(kw)
            return ParagraphStyle(name, **base)

        return {
            "title": style("title", t["title"], fontName=SANS_BOLD, leading=t["title"] * 1.15,
                           spaceAfter=sp["xs"]),
            "subtitle": style("subtitle", t["subtitle"], textColor=c["text_secondary"],
                              spaceAfter=sp["l"]),
            "brand": style("brand", t["small"], textColor=c["accent"], spaceAfter=sp["xs"]),
            "h2": style("h2", t["h2"], fontName=SANS_BOLD, spaceBefore=sp["l"], spaceAfter=sp["m"],
                        keepWithNext=1),
            "h3": style("h3", t["h3"], fontName=SANS_BOLD, spaceBefore=sp["m"], spaceAfter=sp["s"],
                        keepWithNext=1),
            "h4": style("h4", t["h4"], fontName=SANS_BOLD, spaceBefore=sp["xs"], spaceAfter=sp["xs"],
                        keepWithNext=1),
            "body": style("body", t["body"]),
            "lead": style("lead", t["body"], textColor=c["text_secondary"]),
            "note": style("note", t["small"], textColor=c["text_muted"]),
            "warning": style("warning", t["body"], backColor=c["warning_surface"],
                             borderColor=c["warning_border"], borderWidth=0, borderPadding=sp["s"],
                             leftIndent=sp["s"], spaceBefore=sp["s"], spaceAfter=sp["m"]),
            "requirement": style("requirement", t["requirement"], leftIndent=sp["m"],
                                 spaceAfter=sp["s"]),
            "label": style("label", t["small"], textColor=c["text_muted"], spaceAfter=0),
            "cell": style("cell", t["small"], spaceAfter=0),
            "cell_num": style("cell_num", t["small"], spaceAfter=0, alignment=TA_RIGHT),
            "cell_head": style("cell_head", t["small"], fontName=SANS_BOLD,
                               textColor=c["text_secondary"], spaceAfter=0),
            "cell_head_num": style("cell_head_num", t["small"], fontName=SANS_BOLD,
                                   textColor=c["text_secondary"], spaceAfter=0, alignment=TA_RIGHT),
            "mono": style("mono", t["mono"], fontName=MONO, spaceAfter=0, wordWrap="CJK"),
            "caption": style("caption", t["small"], fontName=SANS_BOLD, textColor=c["text_secondary"],
                             spaceAfter=sp["xs"], keepWithNext=1),
        }

    # Seite ---------------------------------------------------------------

    def _page(self, document: ReportDocument):
        c, t = self._c, self._tokens["type"]

        def draw(canv: Any, doc: Any) -> None:
            width, height = A4
            canv.saveState()
            canv.setFont(SANS, t["small"])
            canv.setFillColor(c["text_muted"])
            canv.drawString(doc.leftMargin, height - 12 * mm, document.running_header)
            canv.setStrokeColor(c["divider"])
            canv.setLineWidth(self._tokens["border"]["hairline"])
            canv.line(doc.leftMargin, height - 14 * mm, width - doc.rightMargin, height - 14 * mm)
            canv.line(doc.leftMargin, 15 * mm, width - doc.rightMargin, 15 * mm)
            canv.drawString(doc.leftMargin, 11 * mm, document.title)
            canv.restoreState()
        return draw

    # Blöcke --------------------------------------------------------------

    def _p(self, text: Any, style: str = "body", color: Any = None) -> Paragraph:
        markup = _x(text)
        if color is not None:
            markup = f'<font color="{_hex(color)}">{markup}</font>'
        return Paragraph(markup, self._s[style])

    def _heading(self, level: int, text: str) -> Paragraph:
        paragraph = self._p(text, f"h{min(level, 4)}")
        paragraph._regscoutx_level = level
        paragraph._regscoutx_text = text
        return paragraph

    def _fields(self, fields: Fields, width: float) -> RLTable:
        rows = [[self._p(label, "label"), self._p(value, "mono" if mono else "cell")]
                for label, value, mono in fields.rows]
        table = RLTable(rows, colWidths=[width * 0.28, width * 0.72], hAlign="LEFT")
        table.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), self._tokens["space"]["s"]),
            ("TOPPADDING", (0, 0), (-1, -1), 1.5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
        ]))
        return table

    def _chips(self, chips: Chips) -> Paragraph:
        muted = _hex(self._c["text_muted"])
        parts = [f'<font color="{muted}">{_x(c.label)}</font> '
                 f'<font name="{SANS_BOLD}" color="{_hex(self._tone(c.tone))}">{_x(c.value)}</font>'
                 for c in chips.items]
        return Paragraph("&nbsp;&nbsp;·&nbsp;&nbsp;".join(parts), self._s["cell"])

    def _table(self, block: Table, width: float) -> list[Any]:
        total = sum(block.widths)
        widths = [width * w / total for w in block.widths]
        head = [Paragraph(_x(h), self._s["cell_head_num" if i in block.numeric else "cell_head"])
                for i, h in enumerate(block.headers)]
        rows = [head]
        for row in block.rows:
            cells = []
            for i, (text, tone) in enumerate(row):
                style = "mono" if i in block.mono else ("cell_num" if i in block.numeric else "cell")
                color = self._tone(tone) if tone else None
                cells.append(self._p(text, style, color))
            rows.append(cells)
        if len(rows) == 1 and block.empty:
            rows.append([self._p(block.empty, "note")] + [""] * (len(block.headers) - 1))
        table = RLTable(rows, colWidths=widths, repeatRows=1, hAlign="LEFT")
        commands = [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("BACKGROUND", (0, 0), (-1, 0), self._c["surface_muted"]),
            ("LINEBELOW", (0, 0), (-1, 0), self._tokens["border"]["rule"], self._c["border"]),
            ("LINEBELOW", (0, 1), (-1, -1), self._tokens["border"]["hairline"], self._c["divider"]),
            ("BOX", (0, 0), (-1, -1), self._tokens["border"]["hairline"], self._c["border"]),
            ("LEFTPADDING", (0, 0), (-1, -1), 3),
            ("RIGHTPADDING", (0, 0), (-1, -1), 3),
            ("TOPPADDING", (0, 0), (-1, -1), 2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ]
        if len(rows) == 2 and block.empty and not block.rows:
            commands.append(("SPAN", (0, 1), (-1, 1)))
        table.setStyle(TableStyle(commands))
        return [self._p(block.caption, "caption"), table, Spacer(1, self._tokens["space"]["m"])]

    def _spine(self, block: Spine, width: float) -> list[Any]:
        cells = [[Paragraph(f'<font color="{_hex(self._c["text_muted"])}" size="'
                            f'{self._tokens["type"]["small"]}">{_x(stage)}</font><br/>'
                            f'<font name="{SANS_BOLD}">{_x(value)}</font>', self._s["cell"])
                  for stage, value in block.stages]]
        table = RLTable(cells, colWidths=[width / len(block.stages)] * len(block.stages))
        table.setStyle(TableStyle([
            ("LINEABOVE", (0, 0), (-1, 0), self._tokens["border"]["accent"], self._c["accent"]),
            ("BACKGROUND", (0, 0), (-1, -1), self._c["surface_muted"]),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LINEAFTER", (0, 0), (-2, 0), 2, colors.white),
        ]))
        return [self._p(block.caption, "caption"), table, Spacer(1, self._tokens["space"]["m"])]

    def _distribution(self, block: Distribution, width: float) -> list[Any]:
        height = 9
        drawing = Drawing(width, height)
        x = 0.0
        for _, count, tone in block.items:
            if not count or not block.total:
                continue
            segment = width * count / block.total
            drawing.add(Rect(x, 0, segment, height, fillColor=self._tone(tone), strokeColor=None))
            x += segment
        drawing.add(Rect(0, 0, width, height, fillColor=None, strokeColor=self._c["border"],
                         strokeWidth=self._tokens["border"]["hairline"]))
        legend = "&nbsp;&nbsp;·&nbsp;&nbsp;".join(
            f'<font color="{_hex(self._tone(tone))}">{_x(text)}</font>'
            for (_, _, tone), text in zip(block.items, block.legend))
        return [self._p(block.caption, "caption"), drawing, Spacer(1, 3),
                Paragraph(legend, self._s["note"])]

    def _flow(self, block: Any, width: float) -> list[Any]:
        if isinstance(block, Heading):
            return [self._heading(block.level, block.text)]
        if isinstance(block, Para):
            return [self._p(block.text, block.style)]
        if isinstance(block, Fields):
            return [self._fields(block, width), Spacer(1, self._tokens["space"]["s"])]
        if isinstance(block, Chips):
            return [self._chips(block), Spacer(1, self._tokens["space"]["xs"])]
        if isinstance(block, Table):
            return self._table(block, width)
        if isinstance(block, Spine):
            return self._spine(block, width)
        if isinstance(block, Distribution):
            return self._distribution(block, width)
        if isinstance(block, Group):
            inner = [f for b in block.blocks for f in self._flow(b, width)]
            return [KeepTogether(inner), Spacer(1, self._tokens["space"]["m"])]
        raise TypeError(f"unsupported report block {type(block).__name__}")

    def render(self, document: ReportDocument) -> PdfResult:
        margins = self._tokens["page"]["margin_mm"]
        buffer = io.BytesIO()
        doc = _Doc(buffer, pagesize=A4, leftMargin=margins["left"] * mm,
                   rightMargin=margins["right"] * mm, topMargin=margins["top"] * mm,
                   bottomMargin=margins["bottom"] * mm, title=document.title,
                   subject=document.subtitle, author="RegScoutX", creator="RegScoutX",
                   invariant=1)
        frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        doc.addPageTemplates([PageTemplate(id="page", frames=[frame], onPage=self._page(document))])
        width = doc.width
        story: list[Any] = [
            self._p(document.title, "title"),
            self._p(document.subtitle, "subtitle"),
        ]
        story += [self._p(text, "warning") for text in document.banners]
        story += [self._fields(document.cover, width), Spacer(1, self._tokens["space"]["l"]),
                  self._p(document.contents_title, "caption")]
        story += [self._p(section.title, "cell") for section in document.sections]
        for section in document.sections:
            story.append(CondPageBreak(60 * mm))
            story.append(self._heading(2, section.title))
            for block in section.blocks:
                story.extend(self._flow(block, width))
        canvas_class = type("ReportCanvas", (_NumberedCanvas,), {"footer": (
            document.page_template, document.running_header, self._c["text_muted"],
            self._tokens["type"]["small"])})
        doc.build(story, canvasmaker=canvas_class)
        data = buffer.getvalue()
        pages = doc.page
        return PdfResult(data, pages, tuple(doc.headings))
