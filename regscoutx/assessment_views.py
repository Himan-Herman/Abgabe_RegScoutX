"""ASSESSMENT_SERVICE: JSON-fähige Sichten für Oberfläche und Anwendungs-API.

Die Sichten verdichten ausschließlich gespeicherte Ergebnisse (ReportModel aus D3,
gespeicherte Revision, Audit) und berechnen keine Entscheidung, Anwendbarkeit
oder Gap-Status neu. Neu sind nur Zählungen und Zustände für Navigation und
Visualisierung: Regulatory Spine, Zustand je Applicability-Block und die
Compliance-Matrix (Themencluster × Lebenszyklusphase).
"""

from __future__ import annotations

from collections import Counter
from typing import Any, Iterable, Mapping

from regscoutx.assessment_application import OpenedAssessment, VersionStatus
from regscoutx.audit_log import AuditEventType, AuditLog
from regscoutx.catalog_repository import CatalogRepository
from regscoutx.domain import canonical
from regscoutx.questionnaire import SEGMENT_AREAS, QuestionnaireView
from regscoutx.report_model import ReportModel, RequirementEntry

INACTIVE_REASONS = {"SCOPE_INACTIVE", "SCOPE_NOT_YET_APPLICABLE", "SCOPE_LEGACY_TRANSITION"}
UNRESOLVED_SCOPE = {"SCOPE_UNRESOLVED"}
CELL_FIELDS = ("total", "applicable", "not_applicable", "unresolved", "fulfilled",
               "partially_fulfilled", "not_fulfilled", "not_assessed", "evidence_review_required",
               "gaps")


def _pair(value: Mapping[str, str] | None) -> dict[str, str] | None:
    return None if value is None else {"de": value["de"], "en": value["en"]}


def cell(entries: Iterable[RequirementEntry]) -> dict[str, int]:
    items = list(entries)
    applicability = Counter(e.applicability for e in items)
    gap = Counter(e.gap_status for e in items)
    return {"total": len(items), "applicable": applicability["APPLICABLE"],
            "not_applicable": applicability["NOT_APPLICABLE"],
            "unresolved": applicability["APPLICABILITY_UNRESOLVED"],
            "fulfilled": gap["FULFILLED"], "partially_fulfilled": gap["PARTIALLY_FULFILLED"],
            "not_fulfilled": gap["NOT_FULFILLED"], "not_assessed": gap["NOT_ASSESSED"],
            "evidence_review_required": gap["EVIDENCE_REVIEW_REQUIRED"],
            "gaps": sum(1 for e in items if e.is_gap)}


class AssessmentViews:

    def __init__(self, catalogs: CatalogRepository) -> None:
        self._catalogs = catalogs
        self._mapping = catalogs.applicability

    # Überblick --------------------------------------------------------------

    def blocks(self, model: ReportModel) -> list[dict[str, Any]]:
        members: dict[str, list[RequirementEntry]] = {}
        for entry in model.requirements:
            if entry.block is not None:
                members.setdefault(entry.block, []).append(entry)
        result = []
        for block, spec in self._mapping["blocks"].items():
            entries = members.get(block, [])
            reasons = Counter(e.reason_code for e in entries)
            if entries and set(reasons) <= INACTIVE_REASONS:
                state = "INACTIVE"
            elif entries and set(reasons) <= UNRESOLVED_SCOPE:
                state = "UNRESOLVED"
            else:
                state = "ACTIVE"
            result.append({"block": block, "description": _pair(spec["description"]), "state": state,
                           "counts": cell(entries), "reasons": dict(sorted(reasons.items()))})
        return result

    def spine(self, opened: OpenedAssessment, model: ReportModel,
              questionnaire: QuestionnaireView | None, log: AuditLog) -> list[dict[str, Any]]:
        c = model.counts
        blocked = opened.version_status is not VersionStatus.MATCH
        open_questions = sum(s.open for s in questionnaire.segments) if questionnaire else 0
        answered = sum(s.answered for s in questionnaire.segments) if questionnaire else 0
        decisions = {d.area: d.status for d in model.decisions}
        # Einordnung folgt den Fragebogen-Segmenten mit Entscheidungsbereichen: ein nicht
        # erforderliches Segment (z. B. Klassifizierung ohne MDSW-Qualifizierung) gilt nicht als offen.
        decision_segments = [s.status for s in questionnaire.segments
                             if s.segment in SEGMENT_AREAS] if questionnaire else []
        classification = ("ATTENTION" if "REVIEW" in decision_segments
                          else "OPEN" if not decision_segments or {"OPEN", "WAITING"} & set(decision_segments)
                          else "COMPLETE")
        reports = sum(1 for e in log.events if e.event_type is AuditEventType.REPORT_CREATED
                      and e.revision == opened.stored.revision)
        with_evidence = sum(1 for r in model.requirements if r.evidence_ids)
        stages = [
            ("PROFILE", "OPEN" if open_questions else "COMPLETE", answered, answered + open_questions),
            ("APPLICABILITY", "ATTENTION" if c.unresolved else "COMPLETE", c.applicable, c.total),
            ("CLASSIFICATION", classification,
             sum(1 for s in decisions.values() if s == "DECIDED"), len(decisions)),
            ("REQUIREMENTS", "COMPLETE", c.applicable + c.unresolved, c.total),
            # Ohne anwendbare Anforderungen ist Gap-Bewertung und Evidenz nicht abgeschlossen, sondern offen.
            ("GAP", "OPEN" if c.not_assessed or not c.applicable
             else ("ATTENTION" if c.gaps else "COMPLETE"),
             c.applicable - c.not_assessed, c.applicable),
            ("EVIDENCE", "OPEN" if not c.applicable else (
                "ATTENTION" if c.evidence_review_required or c.answers_review_required
                or c.mapping_review_required else "COMPLETE"), with_evidence, c.applicable),
            ("REPORT", "COMPLETE" if reports else "OPEN", reports, None),
        ]
        return [{"stage": stage, "state": "BLOCKED" if blocked and stage != "REPORT" else state,
                 "value": value, "total": total} for stage, state, value, total in stages]

    def overview(self, opened: OpenedAssessment, model: ReportModel,
                 questionnaire: QuestionnaireView | None, log: AuditLog) -> dict[str, Any]:
        stored = opened.stored
        return {
            "assessment_id": opened.assessment_id,
            "revision": stored.revision,
            "revision_count": opened.revision_count,
            "state": stored.state.value,
            "origin": stored.origin.value,
            "version_status": opened.version_status.value,
            "writable": opened.writable,
            "created_at": stored.created_at,
            "updated_at": stored.updated_at,
            "fingerprint": stored.fingerprint,
            "catalog_versions": dict(stored.catalog_versions),
            "loaded_catalog_versions": dict(vars(self._catalogs.versions)),
            "counts": canonical(model.counts),
            "decisions": canonical(model.decisions),
            "blocks": self.blocks(model),
            "spine": self.spine(opened, model, questionnaire, log),
            "last_change": canonical(opened.assessment.last_change) if opened.assessment else None,
        }

    # Anforderungen -----------------------------------------------------------

    @staticmethod
    def requirement_row(entry: RequirementEntry) -> dict[str, Any]:
        return {"requirement_id": entry.requirement_id, "title": canonical(entry.title),
                "theme": entry.theme, "lifecycle": list(entry.lifecycle),
                "applicability": entry.applicability, "reason_code": entry.reason_code,
                "block": entry.block, "gap_status": entry.gap_status, "gap_reason": entry.gap_reason,
                "is_gap": entry.is_gap, "answer_state": entry.answer_state,
                "answer_status": entry.answer_status, "evidence_state": entry.evidence_state,
                "evidence_count": len(entry.evidence_ids), "measure_status": entry.measure_status,
                "measures": [m.measure_key for m in entry.measures],
                "primary_sources": list(entry.primary_sources or ()),
                "open_items": list(entry.open_items)}

    def requirement_detail(self, model: ReportModel, entry: RequirementEntry,
                           answer: Mapping[str, Any] | None) -> dict[str, Any]:
        predicates = self._mapping["predicates"]
        decisions = {d.area: d for d in model.decisions}
        areas = entry.determined_by_areas or ()
        evidence = {e.evidence_id: e for e in model.evidence}
        return {
            **canonical(entry),
            "answer": answer,
            "predicates": [{"key": key, "value": value,
                            "description": _pair(predicates[key].get("description"))
                            if key in predicates else None}
                           for key, value in entry.evaluated_predicates],
            "decisions": [canonical(decisions[a]) for a in areas if a in decisions],
            "evidence": [canonical(evidence[e]) for e in entry.evidence_ids if e in evidence],
            "texts_available": model.catalog_texts_available,
            "catalog_versions": dict(model.metadata.catalog_versions),
        }

    # Matrix ------------------------------------------------------------------

    def matrix(self, model: ReportModel) -> dict[str, Any]:
        themes = [g.key for g in model.by_theme]
        phases = [g.key for g in model.by_lifecycle]
        cells = []
        for theme in themes:
            for phase in phases:
                entries = [r for r in model.requirements if r.theme == theme and phase in r.lifecycle]
                cells.append({"theme": theme, "phase": phase, **cell(entries)})
        return {"themes": themes, "phases": phases, "cells": cells,
                "theme_totals": {g.key: canonical(g.counts) for g in model.by_theme},
                "phase_totals": {g.key: canonical(g.counts) for g in model.by_lifecycle}}
