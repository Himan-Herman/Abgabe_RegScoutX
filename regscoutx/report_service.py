"""REPORTING: Fassade ReportSource → ReportModel → ReportDocument → HTML bzw. PDF.

Der ASSESSMENT_SERVICE ruft ausschließlich diese Fassade auf; Renderer greifen
weder auf Kataloge noch auf Engines oder Persistenz zu. HTML und PDF entstehen
aus demselben Dokument, der Inhaltshash ist formatunabhängig.
"""

from __future__ import annotations

import re
import uuid
from dataclasses import dataclass
from enum import Enum

from regscoutx.catalog_repository import CatalogRepository
from regscoutx.domain import ID_NAMESPACE, Language
from regscoutx.i18n import Translator
from regscoutx.report_document import ReportComposer, ReportDocument
from regscoutx.report_html import HtmlRenderer
from regscoutx.report_model import REPORT_SCHEMA_VERSION, ReportBuilder, ReportModel, ReportSource

SAFE_ID = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")


class ReportFormat(Enum):
    HTML = "HTML"
    PDF = "PDF"


MEDIA_TYPES = {ReportFormat.HTML: "text/html; charset=utf-8", ReportFormat.PDF: "application/pdf"}


@dataclass(frozen=True)
class ReportArtifact:
    report_id: str
    assessment_id: str
    revision: int
    language: Language
    format: ReportFormat
    report_schema_version: str
    version_status: str
    content_hash: str
    generated_at: str
    media_type: str
    filename: str
    content: bytes
    pages: int | None


class ReportService:

    def __init__(self, catalogs: CatalogRepository) -> None:
        self._catalogs = catalogs
        self._builder = ReportBuilder(catalogs)
        self._html = HtmlRenderer()
        self._pdf = None

    def model(self, source: ReportSource) -> ReportModel:
        return self._builder.build(source)

    def document(self, model: ReportModel, language: Language, generated_at: str) -> ReportDocument:
        return ReportComposer(Translator(self._catalogs, language)).compose(model, generated_at)

    def render(self, source: ReportSource, language: Language, report_format: ReportFormat,
               generated_at: str) -> ReportArtifact:
        if not SAFE_ID.fullmatch(source.assessment_id):
            raise ValueError("assessment_id is not a canonical UUID")
        model = self.model(source)
        document = self.document(model, language, generated_at)
        pages = None
        if report_format is ReportFormat.HTML:
            content = self._html.render(document).encode("utf-8")
        elif report_format is ReportFormat.PDF:
            if self._pdf is None:
                from regscoutx.report_pdf import PdfRenderer
                self._pdf = PdfRenderer()
            result = self._pdf.render(document)
            content, pages = result.data, result.pages
        else:
            raise ValueError(f"unsupported report format {report_format!r}")
        extension = report_format.value.lower()
        return ReportArtifact(
            report_id=str(uuid.uuid5(ID_NAMESPACE, f"report:{document.content_hash}:{extension}")),
            assessment_id=source.assessment_id, revision=source.revision, language=language,
            format=report_format, report_schema_version=REPORT_SCHEMA_VERSION,
            version_status=source.version_status, content_hash=document.content_hash,
            generated_at=generated_at, media_type=MEDIA_TYPES[report_format],
            filename=f"regscoutx-report_{source.assessment_id}_r{source.revision}_"
                     f"{language.value}.{extension}",
            content=content, pages=pages)
