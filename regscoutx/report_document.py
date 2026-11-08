"""REPORTING: formatneutraler Berichtsaufbau aus ReportModel und Translator.

Einzige Stelle, an der Gliederung, Reihenfolge und sichtbare Texte des Berichts
festgelegt werden. HTML- und PDF-Renderer setzen die Blöcke nur um und enthalten
keine eigenen Texte oder Inhalte. Alle Texte stammen aus dem Translator (zentrale
Sprachressourcen, DATA_MODEL-Bezeichnungen, Vokabular) oder aus den DE/EN-Feldern
der Kataloge im ReportModel.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from regscoutx.domain import LocalizedText
from regscoutx.i18n import Translator
from regscoutx.report_model import (
    GAP_STATUSES,
    Counts,
    DecisionEntry,
    ReportModel,
    RequirementEntry,
)

Cell = tuple[str, str | None]  # (Text, Tonalität)

GAP_TONES = {"FULFILLED": "fulfilled", "PARTIALLY_FULFILLED": "partial",
             "NOT_FULFILLED": "not_fulfilled", "NOT_ASSESSED": "not_assessed",
             "EVIDENCE_REVIEW_REQUIRED": "review", "NOT_APPLICABLE": "not_applicable",
             "APPLICABILITY_UNRESOLVED": "unresolved"}
APPLICABILITY_TONES = {"APPLICABLE": "applicable", "NOT_APPLICABLE": "not_applicable",
                       "APPLICABILITY_UNRESOLVED": "unresolved"}
ASSESSED_GAP_STATUSES = ("FULFILLED", "PARTIALLY_FULFILLED", "NOT_FULFILLED",
                         "EVIDENCE_REVIEW_REQUIRED", "NOT_ASSESSED")
VERSION_KEYS = ("sources_version", "rr_catalog_version", "rul_catalog_version",
                "data_model_version", "rr_applicability_version", "rr_measure_version")


@dataclass(frozen=True)
class Heading:
    level: int
    text: str
    anchor: str | None = None


@dataclass(frozen=True)
class Para:
    text: str
    style: str = "body"


@dataclass(frozen=True)
class Chip:
    label: str
    value: str
    tone: str | None


@dataclass(frozen=True)
class Chips:
    items: tuple[Chip, ...]


@dataclass(frozen=True)
class Fields:
    rows: tuple[tuple[str, str, bool], ...]  # (Bezeichnung, Wert, technisch/monospace)


@dataclass(frozen=True)
class Table:
    caption: str
    headers: tuple[str, ...]
    rows: tuple[tuple[Cell, ...], ...]
    widths: tuple[float, ...]
    numeric: tuple[int, ...] = ()
    mono: tuple[int, ...] = ()
    empty: str | None = None


@dataclass(frozen=True)
class Spine:
    caption: str
    stages: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class Distribution:
    caption: str
    items: tuple[tuple[str, int, str], ...]
    total: int
    legend: tuple[str, ...]


@dataclass(frozen=True)
class Group:
    kind: str
    blocks: tuple[Any, ...]


@dataclass(frozen=True)
class Section:
    anchor: str
    title: str
    blocks: tuple[Any, ...]


@dataclass(frozen=True)
class ReportDocument:
    language: str
    title: str
    subtitle: str
    banners: tuple[str, ...]
    cover: Fields
    running_header: str
    page_template: str
    contents_title: str
    sections: tuple[Section, ...]
    content_hash: str


class ReportComposer:
    """Setzt ein ReportModel in einer Sprache zu Abschnitten und Blöcken zusammen."""

    def __init__(self, translator: Translator) -> None:
        self._t = translator
        self._lang = translator.language.value

    # Hilfen ---------------------------------------------------------------

    def text(self, key: str, /, **params: Any) -> str:
        return self._t.text(key, **params)

    def local(self, value: LocalizedText | None) -> str | None:
        return None if value is None else getattr(value, self._lang)

    def unavailable(self) -> str:
        return self.text("value.catalog_text_unavailable")

    def join(self, items: list[str] | tuple[str, ...]) -> str:
        return self.text("format.list_separator").join(items) if items else self.text("value.none")

    def num(self, value: int) -> str:
        return self._t.number(value)

    # Aufbau ---------------------------------------------------------------

    def compose(self, model: ReportModel, generated_at: str) -> ReportDocument:
        meta = model.metadata
        content_hash = model.content_hash(self._t.language)
        sections = (
            self._identification(model, generated_at, content_hash),
            self._versions(model),
            self._profile(model),
            self._classification(model),
            self._summary(model),
            self._gap_summary(model),
            self._groups("by_theme", model.by_theme, self._t.theme),
            self._groups("by_lifecycle", model.by_lifecycle, self._t.phase),
            self._requirements(model),
            self._measures(model),
            self._open_points(model),
            self._method(),
            self._disclaimer(),
            self._revisions(model),
        )
        numbered = tuple(Section(s.anchor, self.text("report.section_number", number=str(i),
                                                      title=s.title), s.blocks)
                         for i, s in enumerate(sections, start=1))
        banners = []
        if meta.historical:
            banners.append(self.text("banner.historical",
                                     status=self._t.code("version_status", meta.version_status)))
            banners.append(self.text("banner.catalog_texts_unavailable"))
        if meta.superseded:
            banners.append(self.text("banner.superseded", revision=str(meta.revision),
                                     latest=str(meta.revision_count)))
        return ReportDocument(
            language=self._lang,
            title=self.text("report.title"),
            subtitle=self.text("report.subtitle"),
            banners=tuple(banners),
            cover=Fields((
                (self.text("field.assessment_id"), meta.assessment_id, True),
                (self.text("field.revision"), self.text("value.revision_of", revision=str(meta.revision),
                                                        count=str(meta.revision_count)), False),
                (self.text("field.state"), self._t.code("assessment_state", meta.state), False),
                (self.text("field.version_status"),
                 self._t.code("version_status", meta.version_status), False),
                (self.text("field.language"), self.text(f"language.{self._lang}"), False),
                (self.text("field.generated_at"), generated_at, True),
            )),
            running_header=self.text("report.running_header", assessment_id=meta.assessment_id,
                                     revision=str(meta.revision)),
            page_template=self.text("report.page", page="%(page)s", pages="%(pages)s"),
            contents_title=self.text("report.contents"),
            sections=numbered,
            content_hash=content_hash,
        )

    def _identification(self, model: ReportModel, generated_at: str, content_hash: str) -> Section:
        meta = model.metadata
        based_on = self.text("value.none") if meta.based_on is None else str(meta.based_on)
        return Section("identification", self.text("section.identification"), (
            Fields((
                (self.text("field.assessment_id"), meta.assessment_id, True),
                (self.text("field.revision"), self.text("value.revision_of", revision=str(meta.revision),
                                                        count=str(meta.revision_count)), False),
                (self.text("field.state"), self._t.code("assessment_state", meta.state), False),
                (self.text("field.origin"), self._t.code("revision_origin", meta.origin), False),
                (self.text("field.based_on"), based_on, False),
                (self.text("field.revision_created_at"), meta.created_at, True),
                (self.text("field.revision_updated_at"), meta.updated_at, True),
                (self.text("field.assessment_fingerprint"), meta.assessment_fingerprint, True),
                (self.text("field.report_schema_version"), meta.report_schema_version, True),
                (self.text("field.content_hash"), content_hash, True),
                (self.text("field.language"), self.text(f"language.{self._lang}"), False),
                (self.text("field.generated_at"), generated_at, True),
            )),
            Para(self.text("identification.note"), "note"),
        ))

    def _versions(self, model: ReportModel) -> Section:
        meta = model.metadata
        versions = dict(meta.catalog_versions)
        keys = list(VERSION_KEYS) + sorted(set(versions) - set(VERSION_KEYS))
        rows = tuple(((self.text(f"catalog.{key}") if key in VERSION_KEYS else key, None),
                      (self._t.value(versions.get(key)), None)) for key in keys)
        blocks: list[Any] = [
            Table(self.text("versions.caption"), (self.text("col.catalog"), self.text("col.version")),
                  rows, (3, 1), mono=(1,)),
            Para(self.text("versions.status", status=self._t.code("version_status",
                                                                   meta.version_status)),
                 "warning" if meta.historical else "note"),
        ]
        return Section("versions", self.text("section.versions"), tuple(blocks))

    def _profile(self, model: ReportModel) -> Section:
        rows = []
        for entry in model.profile:
            question = self.local(entry.question) or self.unavailable()
            value = self.local(entry.value_label) or self._t.value(entry.value)
            rows.append(((question, None), (entry.key, None), (value, None)))
        return Section("profile", self.text("section.profile"), (
            Para(self.text("profile.lead", count=self.num(len(model.profile))), "lead"),
            Table(self.text("profile.caption"),
                  (self.text("col.question"), self.text("col.input_key"), self.text("col.value")),
                  tuple(rows), (5, 2.2, 2.2), mono=(1,), empty=self.text("empty.profile")),
        ))

    def _decision_label(self, decision: DecisionEntry) -> str:
        if decision.outcome is None:
            return self.text("value.none")
        return self.local(decision.outcome_label) or decision.outcome

    def _classification(self, model: ReportModel) -> Section:
        rows = []
        for decision in model.decisions:
            detail = []
            if decision.mdr_class is not None:
                detail.append(self.text("classification.mdr_class", mdr_class=decision.mdr_class))
            if decision.applicable_from is not None:
                detail.append(self.text("classification.applicable_from",
                                        date=self._t.date(decision.applicable_from)))
            rows.append(((self._t.code("decision_area", decision.area), None),
                         (self._t.code("decision_status", decision.status),
                          "applicable" if decision.status == "DECIDED" else "review"),
                         (self._decision_label(decision), None),
                         (self.join(detail) if detail else self.text("value.none"), None)))
        blocks: list[Any] = [
            Para(self.text("classification.lead"), "lead"),
            Table(self.text("classification.caption"),
                  (self.text("col.area"), self.text("col.status"), self.text("col.outcome"),
                   self.text("col.detail")), tuple(rows), (2.2, 1.6, 4, 2),
                  empty=self.text("empty.decisions")),
        ]
        for decision in model.decisions:
            items: list[Any] = [Heading(3, self._t.code("decision_area", decision.area))]
            rule_rows = tuple(((rule.rule_id, None),
                               (self.join(rule.primary_legal_anchor) if rule.primary_legal_anchor
                                is not None else self.unavailable(), None),
                               (self.join(rule.guidance_anchor) if rule.guidance_anchor is not None
                                else self.unavailable(), None))
                              for rule in decision.rules)
            items.append(Table(self.text("classification.rules_caption"),
                               (self.text("col.rule"), self.text("col.primary_legal_anchor"),
                                self.text("col.guidance_anchor")),
                               rule_rows, (1.2, 4, 4), mono=(0, 1, 2),
                               empty=self.text("empty.rules")))
            if decision.missing_input is not None:
                rule_id, key = decision.missing_input
                items.append(Para(self.text("classification.missing_input", rule=rule_id, key=key,
                                            question=self.local(decision.missing_question)
                                            or self.unavailable()), "warning"))
            for review in decision.reviews or ():
                items.append(Para(self.text("classification.review", rule=review.rule_id,
                                            cause=self.local(review.cause) or self.unavailable()),
                                  "warning"))
            blocks.append(Group("decision", tuple(items)))
        return Section("classification", self.text("section.classification"), tuple(blocks))

    def _count_rows(self, counts: Counts) -> tuple[tuple[Cell, ...], ...]:
        figures = (
            ("figure.total", counts.total, None), ("figure.applicable", counts.applicable, "applicable"),
            ("figure.not_applicable", counts.not_applicable, "not_applicable"),
            ("figure.unresolved", counts.unresolved, "unresolved"),
            ("figure.fulfilled", counts.fulfilled, "fulfilled"),
            ("figure.partially_fulfilled", counts.partially_fulfilled, "partial"),
            ("figure.not_fulfilled", counts.not_fulfilled, "not_fulfilled"),
            ("figure.not_assessed", counts.not_assessed, "not_assessed"),
            ("figure.evidence_review_required", counts.evidence_review_required, "review"),
            ("figure.gaps", counts.gaps, "not_fulfilled"),
            ("figure.mapping_review_required", counts.mapping_review_required, "review"),
            ("figure.answers_review_required", counts.answers_review_required, "review"),
        )
        return tuple(((self.text(key), tone), (self.num(value), None)) for key, value, tone in figures)

    def _summary(self, model: ReportModel) -> Section:
        counts = model.counts
        stages = tuple((self.text(f"spine.{stage.stage.lower()}"),
                        self.num(stage.value) if stage.total is None
                        else self.text("value.part_of_total", part=self.num(stage.value),
                                       total=self.num(stage.total)))
                       for stage in model.spine)
        return Section("summary", self.text("section.summary"), (
            Para(self.text("summary.lead", total=self.num(counts.total),
                           applicable=self.num(counts.applicable),
                           unresolved=self.num(counts.unresolved),
                           not_applicable=self.num(counts.not_applicable),
                           gaps=self.num(counts.gaps), not_assessed=self.num(counts.not_assessed)),
                 "lead"),
            Spine(self.text("spine.caption"), stages),
            Table(self.text("summary.caption"), (self.text("col.figure"), self.text("col.count")),
                  self._count_rows(counts), (5, 1.2), numeric=(1,)),
            Para(self.text("summary.note"), "note"),
        ))

    def _gap_summary(self, model: ReportModel) -> Section:
        counts = model.counts
        values = {"FULFILLED": counts.fulfilled, "PARTIALLY_FULFILLED": counts.partially_fulfilled,
                  "NOT_FULFILLED": counts.not_fulfilled, "NOT_ASSESSED": counts.not_assessed,
                  "EVIDENCE_REVIEW_REQUIRED": counts.evidence_review_required,
                  "NOT_APPLICABLE": counts.not_applicable,
                  "APPLICABILITY_UNRESOLVED": counts.unresolved}
        items = tuple((self._t.code("gap_result", status), values[status], GAP_TONES[status])
                      for status in ASSESSED_GAP_STATUSES)
        rows = tuple(((self._t.code("gap_result", status), GAP_TONES[status]),
                      (self.num(values[status]), None),
                      (self._t.percent(values[status], counts.applicable)
                       if status in ASSESSED_GAP_STATUSES else self.text("value.not_applicable_share"),
                       None))
                     for status in GAP_STATUSES)
        return Section("gap_summary", self.text("section.gap_summary"), (
            Para(self.text("gap_summary.lead"), "lead"),
            Distribution(self.text("gap_summary.distribution_caption"), items, counts.applicable,
                         tuple(self.text("value.label_count", label=label, count=self.num(count))
                               for label, count, _ in items)),
            Table(self.text("gap_summary.caption"),
                  (self.text("col.gap_status"), self.text("col.count"),
                   self.text("col.share_of_applicable")), rows, (4, 1.2, 1.6), numeric=(1, 2)),
            Para(self.text("gap_summary.note"), "note"),
        ))

    def _group_table(self, anchor: str, kind: str, groups, label, fields: tuple[str, ...]) -> Table:
        headers = (self.text(f"col.{anchor}"),) + tuple(self.text(f"col.short.{f}") for f in fields)
        rows = tuple(((label(g.key), None),) + tuple((self.num(getattr(g.counts, f)), None)
                                                     for f in fields) for g in groups)
        return Table(self.text(f"groups.{kind}_caption", group=self.text(f"col.{anchor}")), headers,
                     rows, (3.2,) + (1.1,) * len(fields), numeric=tuple(range(1, len(fields) + 1)),
                     empty=self.text("empty.groups"))

    def _groups(self, anchor: str, groups, label) -> Section:
        return Section(anchor, self.text(f"section.{anchor}"), (
            Para(self.text(f"{anchor}.lead"), "lead"),
            self._group_table(anchor, "applicability", groups, label,
                              ("total", "applicable", "not_applicable", "unresolved")),
            self._group_table(anchor, "gap", groups, label,
                              ("fulfilled", "partially_fulfilled", "not_fulfilled",
                               "evidence_review_required", "not_assessed", "gaps")),
        ))

    def _evidence_text(self, model: ReportModel, evidence_id: str) -> str:
        entry = next((e for e in model.evidence if e.evidence_id == evidence_id), None)
        if entry is None:
            return evidence_id
        details = [entry.document_identifier] + [v for v in (entry.document_version, entry.location)
                                                 if v]
        return self.text("evidence.reference", title=entry.title, details=self.join(details),
                         evidence_id=entry.evidence_id)

    def _requirement(self, model: ReportModel, entry: RequirementEntry) -> Group:
        texts = model.catalog_texts_available
        title = self.local(entry.title)
        heading = (self.text("requirement.heading", requirement_id=entry.requirement_id, title=title)
                   if title else entry.requirement_id)
        chips = [Chip(self.text("chip.applicability"),
                      self._t.code("applicability", entry.applicability),
                      APPLICABILITY_TONES[entry.applicability]),
                 Chip(self.text("chip.gap_status"), self._t.code("gap_result", entry.gap_status),
                      GAP_TONES[entry.gap_status])]
        if entry.answer_state is not None:
            chips.append(Chip(self.text("chip.answer_state"),
                              self._t.code("answer_state", entry.answer_state),
                              "review" if entry.answer_state == "REACTIVATED_REVIEW_REQUIRED"
                              else None))
        chips.append(Chip(self.text("chip.measure_mapping"),
                          self._t.code("measure_mapping_status", entry.measure_status),
                          "review" if entry.measure_status == "REVIEW_REQUIRED" else None))
        reason = self._t.code("applicability_reason", entry.reason_code)
        block = self.local(entry.block_description)
        trace_inputs = [self.text("trace.input", key=k, value=self._t.value(v))
                        for k, v in entry.relevant_inputs]
        trace_conditions = [self.text("trace.condition", key=k, value=self._t.code("tri_state", v))
                            for k, v in entry.evaluated_predicates]
        areas = (self.join([self._t.code("decision_area", a) for a in entry.determined_by_areas])
                 if entry.determined_by_areas is not None else self.unavailable())
        measures = ([self.text("measure.reference", label=self.local(m.label) or m.measure_key,
                               key=m.measure_key) for m in entry.measures]
                    if texts or not entry.measures else [m.measure_key for m in entry.measures])
        expected = [self.local(label) or key for m in entry.measures for key, label in m.evidence_types]
        answer = (self.text("value.none") if entry.answer_status is None
                  else self._t.code("gap_status", entry.answer_status))
        rows = [
            (self.text("field.theme"), self._t.theme(entry.theme), False),
            (self.text("field.lifecycle"), self.join([self._t.phase(p) for p in entry.lifecycle]), False),
            (self.text("field.primary_sources"),
             self.join(entry.primary_sources) if entry.primary_sources is not None
             else self.unavailable(), True),
            (self.text("field.supplementary_sources"),
             self.join(entry.supplementary_sources) if entry.supplementary_sources is not None
             else self.unavailable(), True),
            (self.text("field.applicability_reason"),
             self.text("value.reason_with_block", reason=reason, block=block) if block else reason,
             False),
            (self.text("field.trace_inputs"), self.join(trace_inputs), True),
            (self.text("field.trace_conditions"), self.join(trace_conditions), True),
            (self.text("field.trace_rules"), self.join(entry.supporting_rule_ids), True),
            (self.text("field.trace_decisions"), areas, False),
            (self.text("field.gap_reason"), self._t.code("gap_reason", entry.gap_reason), False),
            (self.text("field.user_assessment"), answer, False),
        ]
        if entry.justification:
            rows.append((self.text("field.justification"), entry.justification, False))
        rows += [
            (self.text("field.measures"),
             self.join(measures) if entry.measures else self.text("measure.open"), False),
            (self.text("field.expected_evidence"),
             self.join(expected) if expected else (self.unavailable() if entry.measures and not texts
                                                   else self.text("value.none")), False),
            (self.text("field.evidence_references"),
             self.join([self._evidence_text(model, e) for e in entry.evidence_ids]), False),
            (self.text("field.open_items"),
             self.join([self._t.code("report_open_item", i) for i in entry.open_items]), False),
        ]
        blocks: list[Any] = [Heading(4, heading, f"rr-{entry.requirement_id}"), Chips(tuple(chips))]
        blocks.append(Para(self.local(entry.text), "requirement") if entry.text
                      else Para(self.unavailable(), "note"))
        blocks.append(Fields(tuple(rows)))
        return Group("requirement", tuple(blocks))

    def _requirements(self, model: ReportModel) -> Section:
        blocks: list[Any] = [Para(self.text("requirements.lead"), "lead")]
        detailed = [r for r in model.requirements if r.applicability != "NOT_APPLICABLE"]
        themes = [g.key for g in model.by_theme]
        for theme in themes:
            entries = [r for r in detailed if r.theme == theme]
            if not entries:
                continue
            blocks.append(Heading(3, self.text("requirements.theme_heading", theme=self._t.theme(theme),
                                               count=self.num(len(entries)))))
            blocks.extend(self._requirement(model, r) for r in entries)
        if not detailed:
            blocks.append(Para(self.text("empty.detailed_requirements"), "note"))
        not_applicable = [r for r in model.requirements if r.applicability == "NOT_APPLICABLE"]
        rows = tuple(((r.requirement_id, None), (self.local(r.title) or self.unavailable(), None),
                      (self._t.theme(r.theme), None),
                      (self._t.code("applicability_reason", r.reason_code), "not_applicable"),
                      (self.join([self._t.code("decision_area", a) for a in r.determined_by_areas])
                       if r.determined_by_areas is not None else self.unavailable(), None))
                     for r in not_applicable)
        blocks.append(Heading(3, self.text("requirements.not_applicable_heading",
                                           count=self.num(len(not_applicable)))))
        blocks.append(Table(self.text("requirements.not_applicable_caption"),
                            (self.text("col.requirement"), self.text("col.title"),
                             self.text("col.theme"), self.text("col.reason"),
                             self.text("col.determined_by")),
                            rows, (1.1, 4, 2, 2.6, 2), mono=(0,),
                            empty=self.text("empty.not_applicable")))
        return Section("requirements", self.text("section.requirements"), tuple(blocks))

    def _measures(self, model: ReportModel) -> Section:
        texts = model.catalog_texts_available
        measure_rows = tuple((
            (self.local(m.measure.label) or m.measure.measure_key, None),
            (self.join([self.local(label) or key for key, label in m.measure.evidence_types])
             if texts else self.unavailable(), None),
            (self.num(m.planned), None), (self.num(m.with_evidence), None))
            for m in model.measures)
        evidence_rows = tuple((
            (e.title, None), (e.document_identifier, None),
            (e.document_version or self.text("value.none"), None),
            (e.location or self.text("value.none"), None),
            (e.measure_key or self.text("value.none"), None),
            (self.join(e.requirement_ids), None)) for e in model.evidence)
        return Section("measures", self.text("section.measures"), (
            Para(self.text("measures.lead"), "lead"),
            Table(self.text("measures.caption"),
                  (self.text("col.measure"), self.text("col.expected_evidence"),
                   self.text("col.planned"), self.text("col.with_evidence")),
                  measure_rows, (3.2, 3.2, 1.2, 1.4), numeric=(2, 3),
                  empty=self.text("empty.measures")),
            Para(self.text("measures.mapping_review",
                           count=self.num(model.counts.mapping_review_required)), "note"),
            Heading(3, self.text("measures.evidence_heading")),
            Table(self.text("measures.evidence_caption"),
                  (self.text("col.title"), self.text("col.document"), self.text("col.document_version"),
                   self.text("col.location"), self.text("col.measure_key"),
                   self.text("col.requirements")),
                  evidence_rows, (3, 2, 1, 2, 2, 2), mono=(1, 4, 5),
                  empty=self.text("empty.evidence")),
            Para(self.text("measures.separation_note"), "note"),
        ))

    def _open_points(self, model: ReportModel) -> Section:
        review = model.review
        blocks: list[Any] = [Para(self.text("open_points.lead"), "lead")]
        if model.metadata.historical:
            blocks.append(Para(self.text("banner.historical", status=self._t.code(
                "version_status", model.metadata.version_status)), "warning"))
        blocks.append(Table(
            self.text("open_points.review_caption"),
            (self.text("col.area"), self.text("col.rule"), self.text("col.outcome"),
             self.text("col.cause")),
            tuple(((self._t.code("decision_area", area), None), (r.rule_id, None), (r.output, None),
                   (self.local(r.cause) or self.unavailable(), "review"))
                  for area, r in review.review_decisions),
            (2, 1.2, 2.6, 4), mono=(1, 2), empty=self.text("empty.review_decisions")))
        blocks.append(Table(
            self.text("open_points.incomplete_caption"),
            (self.text("col.area"), self.text("col.rule"), self.text("col.input_key"),
             self.text("col.question")),
            tuple(((self._t.code("decision_area", d.area), None), (d.missing_input[0], None),
                   (d.missing_input[1], None),
                   (self.local(d.missing_question) or self.unavailable(), "review"))
                  for d in review.incomplete_decisions),
            (2, 1.2, 2.4, 4.2), mono=(1, 2), empty=self.text("empty.incomplete_decisions")))
        blocks.append(Table(
            self.text("open_points.unresolved_caption"),
            (self.text("col.reason"), self.text("col.count")),
            tuple(((self._t.code("applicability_reason", reason), "unresolved"), (self.num(count), None))
                  for reason, count in review.unresolved_by_reason),
            (5, 1.2), numeric=(1,), empty=self.text("empty.unresolved")))
        blocks.append(Fields((
            (self.text("figure.not_assessed"), self.num(review.not_assessed), False),
            (self.text("figure.answers_review_required"), self.join(review.reactivated), True),
            (self.text("figure.evidence_review_required"),
             self.join(review.evidence_review_required), True),
            (self.text("figure.mapping_review_required"), self.num(review.mapping_review_required),
             False),
        )))
        return Section("open_points", self.text("section.open_points"), tuple(blocks))

    def _method(self) -> Section:
        return Section("method", self.text("section.method"), tuple(
            Para(self.text(f"method.p{i}"), "body") for i in range(1, 6)))

    def _disclaimer(self) -> Section:
        return Section("disclaimer", self.text("section.disclaimer"), tuple(
            Para(self.text(f"disclaimer.p{i}"), "body") for i in range(1, 4)))

    def _revisions(self, model: ReportModel) -> Section:
        current = dict(model.metadata.catalog_versions)
        rows = tuple((
            (str(r.revision), "applicable" if r.revision == model.metadata.revision else None),
            (self._t.code("assessment_state", r.state), None),
            (self._t.code("revision_origin", r.origin), None),
            (self.text("value.none") if r.based_on is None else str(r.based_on), None),
            (r.created_at, None), (r.updated_at, None),
            (self.text("revisions.same_versions") if dict(r.catalog_versions) == current
             else self.text("revisions.other_versions"), None)) for r in model.revisions)
        return Section("revisions", self.text("section.revisions"), (
            Para(self.text("revisions.lead", revision=str(model.metadata.revision)), "lead"),
            Table(self.text("revisions.caption"),
                  (self.text("col.revision"), self.text("col.state"), self.text("col.origin"),
                   self.text("col.based_on"), self.text("col.created_at"), self.text("col.updated_at"),
                   self.text("col.catalog_versions")),
                  rows, (1, 1.3, 1.9, 0.8, 2.7, 2.7, 1.6), mono=(4, 5)),
        ))
