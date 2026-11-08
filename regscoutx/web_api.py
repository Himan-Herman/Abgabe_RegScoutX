"""APPLICATION_API: JSON-Schnittstelle der Web-Oberfläche zum AssessmentApplicationService (ADR-0007).

Reiner Adapter ohne Fachlogik: Er übersetzt HTTP-Anfragen in Aufrufe des
Anwendungseinstiegs und seiner Sichten und Fehler in stabile, lokalisierbare
Codes. Die Oberfläche greift nie direkt auf Kataloge, Engines oder
Persistenzdateien zu. Kein Netzwerkzugriff nach außen, keine Telemetrie.
"""

from __future__ import annotations

import json
import re
import threading
import uuid
from dataclasses import dataclass, field
from typing import Any, Callable, Mapping

from regscoutx.assessment_application import AssessmentApplicationService
from regscoutx.assessment_service import AssessmentInput, ProductProfile
from regscoutx.assessment_views import AssessmentViews
from regscoutx.catalog_repository import CatalogRepository
from regscoutx.domain import Language, canonical
from regscoutx.errors import (
    AssessmentNotFoundError,
    AssessmentStateError,
    CatalogVersionMismatchError,
    I18nError,
    InvalidInputError,
    PersistenceError,
    RegScoutXError,
    ReportGenerationError,
    UnknownRequirementError,
)
from regscoutx.evidence_service import EvidenceReference
from regscoutx.gap_engine import GapAssessment, GapStatus
from regscoutx.i18n import load_messages
from regscoutx.questionnaire import Questionnaire
from regscoutx.report_service import ReportFormat

JSON = "application/json; charset=utf-8"
UUID = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
RR = r"RR-\d{3}"
LABELLED_ENUMS = ("applicability", "applicability_reason", "gap_result", "gap_reason", "gap_status",
                  "answer_state", "evidence_state", "measure_mapping_status", "assessment_state",
                  "version_status", "revision_origin", "audit_event_type", "decision_area",
                  "decision_status", "tri_state", "report_open_item", "report_format")
EVIDENCE_FIELDS = ("title", "document_identifier", "document_version", "location", "measure_key")


@dataclass
class Response:
    status: int
    body: bytes
    content_type: str = JSON
    headers: dict[str, str] = field(default_factory=dict)


class ApiError(Exception):
    def __init__(self, status: int, code: str, detail: str = "", **extra: Any) -> None:
        super().__init__(detail)
        self.status, self.code, self.detail, self.extra = status, code, detail, extra


def _json(status: int, data: Any) -> Response:
    return Response(status, json.dumps(data, ensure_ascii=False, default=str).encode("utf-8"))


def _language(value: str | None) -> Language:
    try:
        return Language(value or "de")
    except ValueError as exc:
        raise ApiError(400, "UNSUPPORTED_LANGUAGE", str(value)) from exc


def _stored_counts(counts: Mapping[str, Any] | None) -> dict[str, int] | None:
    """Gespeicherte Summen einer Revision in derselben flachen Form wie im Überblick."""
    if counts is None:
        return None
    applicability, gap = counts["applicability"], counts["gap_status"]
    return {"total": counts["total"], "applicable": applicability["APPLICABLE"],
            "not_applicable": applicability["NOT_APPLICABLE"],
            "unresolved": applicability["APPLICABILITY_UNRESOLVED"],
            "fulfilled": gap["FULFILLED"], "partially_fulfilled": gap["PARTIALLY_FULFILLED"],
            "not_fulfilled": gap["NOT_FULFILLED"], "not_assessed": gap["NOT_ASSESSED"],
            "evidence_review_required": gap["EVIDENCE_REVIEW_REQUIRED"], "gaps": counts["gaps"],
            "mapping_review_required": counts["measure_review_required"],
            "answers_review_required": counts["answers_review_required"]}


def _object(body: Any) -> Mapping[str, Any]:
    if not isinstance(body, Mapping):
        raise ApiError(400, "BAD_REQUEST", "JSON object expected")
    return body


class ApiApplication:
    """Routen der Anwendungs-API; threadsicher über eine Sperre je Instanz."""

    def __init__(self, catalogs: CatalogRepository, service: AssessmentApplicationService) -> None:
        self._catalogs = catalogs
        self._service = service
        self._views = AssessmentViews(catalogs)
        self._questionnaire = Questionnaire(catalogs)
        self._lock = threading.RLock()
        self._bundles: dict[Language, dict[str, Any]] = {}
        a = rf"/api/assessments/(?P<aid>{UUID})"
        self._routes: list[tuple[str, re.Pattern[str], Callable[..., Response]]] = [
            ("GET", re.compile(r"/api/meta"), self.meta),
            ("GET", re.compile(r"/api/i18n/(?P<lang>[a-z]{2})"), self.i18n),
            ("GET", re.compile(r"/api/measures"), self.measures),
            ("GET", re.compile(r"/api/assessments"), self.list_assessments),
            ("POST", re.compile(r"/api/assessments"), self.create),
            ("GET", re.compile(a), self.overview),
            ("POST", re.compile(a + r"/open"), self.open),
            ("GET", re.compile(a + r"/questionnaire"), self.questionnaire),
            ("PATCH", re.compile(a + r"/profile"), self.patch_profile),
            ("GET", re.compile(a + r"/requirements"), self.requirements),
            ("GET", re.compile(a + rf"/requirements/(?P<rr>{RR})"), self.requirement),
            ("PUT", re.compile(a + rf"/requirements/(?P<rr>{RR})/assessment"), self.set_assessment),
            ("POST", re.compile(a + rf"/requirements/(?P<rr>{RR})/confirm"), self.confirm),
            ("POST", re.compile(a + rf"/requirements/(?P<rr>{RR})/evidence/(?P<eid>{UUID})"),
             self.link),
            ("DELETE", re.compile(a + rf"/requirements/(?P<rr>{RR})/evidence/(?P<eid>{UUID})"),
             self.unlink),
            ("GET", re.compile(a + r"/evidence"), self.evidence),
            ("POST", re.compile(a + r"/evidence"), self.add_evidence),
            ("PUT", re.compile(a + rf"/evidence/(?P<eid>{UUID})"), self.update_evidence),
            ("DELETE", re.compile(a + rf"/evidence/(?P<eid>{UUID})"), self.remove_evidence),
            ("GET", re.compile(a + r"/matrix"), self.matrix),
            ("GET", re.compile(a + r"/report/document"), self.report_document),
            ("GET", re.compile(a + r"/report\.(?P<fmt>pdf|html)"), self.report_file),
            ("GET", re.compile(a + r"/revisions"), self.revisions),
            ("GET", re.compile(a + r"/audit"), self.audit),
            ("POST", re.compile(a + r"/(?P<action>finalise|reopen|rebase|recalculate)"), self.action),
        ]

    # Dispatch ----------------------------------------------------------------

    def handle(self, method: str, path: str, query: Mapping[str, str], body: Any) -> Response:
        try:
            for route_method, pattern, handler in self._routes:
                match = pattern.fullmatch(path)
                if match and route_method == method:
                    with self._lock:
                        return handler(query=query, body=body, **match.groupdict())
            if any(pattern.fullmatch(path) for _, pattern, _ in self._routes):
                raise ApiError(405, "METHOD_NOT_ALLOWED", method)
            raise ApiError(404, "NOT_FOUND", path)
        except ApiError as exc:
            return _json(exc.status, {"error": {"code": exc.code, "detail": exc.detail, **exc.extra}})
        except AssessmentNotFoundError as exc:
            return _json(404, {"error": {"code": "ASSESSMENT_NOT_FOUND", "detail": str(exc)}})
        except UnknownRequirementError as exc:
            return _json(404, {"error": {"code": "REQUIREMENT_NOT_FOUND", "detail": str(exc)}})
        except InvalidInputError as exc:
            return _json(422, {"error": {"code": "INVALID_INPUT", "field": exc.input_key,
                                         "detail": exc.reason}})
        except CatalogVersionMismatchError as exc:
            return _json(409, {"error": {"code": "VERSION_MISMATCH", "detail": str(exc)}})
        except AssessmentStateError as exc:
            code = "VERSION_MISMATCH" if exc.reason.startswith("catalog versions") else "STATE_CONFLICT"
            return _json(409, {"error": {"code": code, "operation": exc.operation,
                                         "detail": exc.reason}})
        except PersistenceError as exc:
            return _json(500, {"error": {"code": "CORRUPTED_ASSESSMENT", "detail": exc.reason}})
        except ReportGenerationError as exc:
            return _json(500, {"error": {"code": "REPORT_FAILED", "detail": exc.reason}})
        except (I18nError, RegScoutXError) as exc:
            return _json(500, {"error": {"code": "APPLICATION_ERROR", "detail": type(exc).__name__}})

    # Allgemein ----------------------------------------------------------------

    def meta(self, **_: Any) -> Response:
        return _json(200, {"catalog_versions": dict(vars(self._catalogs.versions)),
                           "languages": [language.value for language in Language],
                           "requirement_count": self._catalogs.requirement_count,
                           "sources": dict(self._catalogs.source_designations)})

    def i18n(self, lang: str, **_: Any) -> Response:
        language = _language(lang)
        if language not in self._bundles:
            enums = {name: {code: self._catalogs.enum_label(name, code, language)
                            for code in self._catalogs.enum_codes(name)} for name in LABELLED_ENUMS}
            self._bundles[language] = {
                "language": language.value,
                "messages": dict(load_messages(language)),
                "enums": enums,
                "themes": {t: self._catalogs.theme_label(t, language)
                           for t in self._catalogs.theme_clusters},
                "phases": {p: self._catalogs.phase_label(p, language)
                           for p in self._catalogs.lifecycle_phases},
                "theme_order": list(self._catalogs.theme_clusters),
                "phase_order": list(self._catalogs.lifecycle_phases),
            }
        return _json(200, self._bundles[language])

    def measures(self, **_: Any) -> Response:
        keys = sorted({m for rr in self._catalogs.requirement_ids
                       for m in self._catalogs.measure_mapping(rr)["measures"]})
        return _json(200, [{"measure_key": key, "label": dict(self._catalogs.measure(key)["label"]),
                            "evidence_types": [
                                {"key": e, "label": dict(self._catalogs.evidence_type(e)["label"])}
                                for e in self._catalogs.measure(key)["evidence_types"]]}
                           for key in keys])

    # Bewertungen ----------------------------------------------------------------

    def _overview(self, aid: str, opened=None) -> dict[str, Any]:
        opened = opened or self._service.read(aid)
        model = self._service.report_model(aid)
        questionnaire = (self._questionnaire.build(opened.assessment)
                         if opened.assessment is not None else None)
        return self._views.overview(opened, model, questionnaire, self._service.audit_log(aid))

    def list_assessments(self, **_: Any) -> Response:
        items = []
        for aid in self._service.assessment_ids():
            try:
                revisions = self._service.revisions(aid)
            except PersistenceError:
                # Eine beschädigte Datei macht die Liste nicht unbrauchbar; sie wird einzeln gemeldet.
                items.append({"assessment_id": aid, "corrupted": True, "updated_at": ""})
                continue
            current = revisions[-1]
            items.append({"assessment_id": aid, "corrupted": False, "revision": current.revision,
                          "revision_count": len(revisions), "state": current.state.value,
                          "version_status": self._service.check_versions(aid).value,
                          "created_at": revisions[0].created_at, "updated_at": current.updated_at,
                          "counts": _stored_counts(current.results.get("counts")),
                          "decisions": [{k: d[k] for k in ("area", "status", "outcome", "mdr_class")}
                                        for d in current.results.get("decisions", [])]})
        items.sort(key=lambda item: item["updated_at"], reverse=True)
        return _json(200, items)

    def create(self, body: Any, **_: Any) -> Response:
        data = _object(body or {})
        profile = data.get("profile", {})
        if set(data) - {"profile"}:
            raise ApiError(400, "BAD_REQUEST", "unknown fields")
        opened = self._service.create(AssessmentInput(ProductProfile.of(profile)))
        return _json(201, self._overview(opened.assessment_id))

    def overview(self, aid: str, **_: Any) -> Response:
        return _json(200, self._overview(aid))

    def open(self, aid: str, **_: Any) -> Response:
        opened = self._service.open(aid)
        return _json(200, self._overview(aid, opened))

    def questionnaire(self, aid: str, **_: Any) -> Response:
        opened = self._service.read(aid)
        if opened.assessment is None:
            raise ApiError(409, "VERSION_MISMATCH", opened.version_status.value)
        return _json(200, canonical(self._questionnaire.build(opened.assessment)))

    def patch_profile(self, aid: str, body: Any, **_: Any) -> Response:
        data = _object(body)
        if set(data) != {"key", "value"} or not isinstance(data["key"], str):
            raise ApiError(400, "BAD_REQUEST", "key and value expected")
        opened = self._service.read(aid)
        profile = dict(opened.stored.inputs.profile.answers)
        if data["value"] is None:
            profile.pop(data["key"], None)
        else:
            profile[data["key"]] = data["value"]
        updated = self._service.update_profile(aid, profile)
        return _json(200, {"overview": self._overview(aid, updated),
                           "questionnaire": canonical(self._questionnaire.build(updated.assessment)),
                           "change": canonical(updated.assessment.last_change)})

    # Anforderungen ----------------------------------------------------------------

    def requirements(self, aid: str, **_: Any) -> Response:
        model = self._service.report_model(aid)
        return _json(200, {"texts_available": model.catalog_texts_available,
                           "items": [self._views.requirement_row(r) for r in model.requirements]})

    def _detail(self, aid: str, rr: str) -> dict[str, Any]:
        self._catalogs.requirement(rr)
        model = self._service.report_model(aid)
        entry = next(r for r in model.requirements if r.requirement_id == rr)
        answer = next((a for a in self._service.revisions(aid)[-1].inputs.answers
                       if a.requirement_id == rr), None)
        answer_data = None if answer is None else {
            "status": answer.status.value, "justification": answer.justification,
            "evidence_ids": list(answer.evidence_ids), "stale": answer.stale}
        return self._views.requirement_detail(model, entry, answer_data)

    def requirement(self, aid: str, rr: str, **_: Any) -> Response:
        return _json(200, self._detail(aid, rr))

    def set_assessment(self, aid: str, rr: str, body: Any, **_: Any) -> Response:
        data = _object(body)
        if not set(data) <= {"status", "justification"} or "status" not in data:
            raise ApiError(400, "BAD_REQUEST", "status and optional justification expected")
        try:
            status = GapStatus(data["status"])
        except ValueError as exc:
            raise ApiError(422, "INVALID_INPUT", "status", field="status") from exc
        previous = next((a for a in self._service.revisions(aid)[-1].inputs.answers
                         if a.requirement_id == rr), None)
        justification = data.get("justification")
        if isinstance(justification, str) and not justification.strip():
            justification = None
        self._service.set_gap_assessment(aid, GapAssessment(
            rr, status, justification, previous.evidence_ids if previous else ()))
        return _json(200, self._detail(aid, rr))

    def confirm(self, aid: str, rr: str, **_: Any) -> Response:
        self._service.confirm_gap_assessment(aid, rr)
        return _json(200, self._detail(aid, rr))

    def link(self, aid: str, rr: str, eid: str, **_: Any) -> Response:
        self._service.link_evidence(aid, rr, eid)
        return _json(200, self._detail(aid, rr))

    def unlink(self, aid: str, rr: str, eid: str, **_: Any) -> Response:
        self._service.unlink_evidence(aid, rr, eid)
        return _json(200, self._detail(aid, rr))

    # Nachweise ----------------------------------------------------------------

    def evidence(self, aid: str, **_: Any) -> Response:
        model = self._service.report_model(aid)
        return _json(200, {"items": canonical(model.evidence), "measures": canonical(model.measures),
                           "mapping_review_required": model.counts.mapping_review_required})

    @staticmethod
    def _reference(evidence_id: str, body: Any) -> EvidenceReference:
        data = _object(body)
        if not set(data) <= set(EVIDENCE_FIELDS):
            raise ApiError(400, "BAD_REQUEST", "unknown evidence fields")
        values = {name: (data.get(name) or None) if name not in ("title", "document_identifier")
                  else data.get(name) for name in EVIDENCE_FIELDS}
        return EvidenceReference(evidence_id, **values)

    def add_evidence(self, aid: str, body: Any, **_: Any) -> Response:
        reference = self._reference(str(uuid.uuid4()), body)
        self._service.add_evidence(aid, reference)
        return _json(201, canonical(reference))

    def update_evidence(self, aid: str, eid: str, body: Any, **_: Any) -> Response:
        reference = self._reference(eid, body)
        self._service.update_evidence(aid, reference)
        return _json(200, canonical(reference))

    def remove_evidence(self, aid: str, eid: str, **_: Any) -> Response:
        self._service.remove_evidence(aid, eid)
        return _json(200, {"removed": eid})

    # Auswertung, Bericht, Revisionen ------------------------------------------

    def matrix(self, aid: str, **_: Any) -> Response:
        return _json(200, self._views.matrix(self._service.report_model(aid)))

    @staticmethod
    def _revision(query: Mapping[str, str]) -> int | None:
        value = query.get("revision")
        if value is None:
            return None
        if not value.isdigit():
            raise ApiError(400, "BAD_REQUEST", "revision")
        return int(value)

    def report_document(self, aid: str, query: Mapping[str, str], **_: Any) -> Response:
        document = self._service.report_document(aid, _language(query.get("lang")),
                                                 self._revision(query))
        return _json(200, canonical(document))

    def report_file(self, aid: str, fmt: str, query: Mapping[str, str], **_: Any) -> Response:
        artifact = self._service.create_report(
            aid, language=_language(query.get("lang")),
            report_format=ReportFormat.PDF if fmt == "pdf" else ReportFormat.HTML,
            revision=self._revision(query))
        return Response(200, artifact.content, artifact.media_type, {
            "Content-Disposition": f'attachment; filename="{artifact.filename}"',
            "X-RegScoutX-Content-Hash": artifact.content_hash})

    def revisions(self, aid: str, **_: Any) -> Response:
        current_versions = dict(vars(self._catalogs.versions))
        return _json(200, [{"revision": r.revision, "state": r.state.value, "origin": r.origin.value,
                            "based_on": r.based_on, "created_at": r.created_at,
                            "updated_at": r.updated_at, "fingerprint": r.fingerprint,
                            "catalog_versions": dict(r.catalog_versions),
                            "same_catalog_versions": dict(r.catalog_versions) == current_versions,
                            "counts": _stored_counts(r.results.get("counts")), "change": r.change}
                           for r in self._service.revisions(aid)])

    def audit(self, aid: str, **_: Any) -> Response:
        return _json(200, [{"sequence": e.sequence, "revision": e.revision,
                            "occurred_at": e.occurred_at, "event_type": e.event_type.value,
                            "subject_id": e.subject_id, "details": dict(e.details)}
                           for e in self._service.audit_log(aid).events])

    def action(self, aid: str, action: str, **_: Any) -> Response:
        opened = {"finalise": self._service.finalise, "reopen": self._service.reopen,
                  "rebase": self._service.rebase, "recalculate": self._service.recalculate}[action](aid)
        return _json(200, self._overview(aid, opened))
