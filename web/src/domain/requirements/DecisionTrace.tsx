/**
 * Decision Trace (Signature Component): Herleitung einer Anforderung als geordnete Kette
 * Eingabe → Prädikat → Regel/Entscheidung → Anwendbarkeit → Anforderung → Gap-Status →
 * Maßnahme → Nachweis. Jeder Schritt zeigt die gespeicherten Codes mit Bezeichnung.
 */

import type { ReactNode } from "react";
import type { RequirementDetail } from "../../core/api/types";
import { useI18n } from "../../core/i18n/i18n";
import { Glyph, type GlyphName } from "../../core/primitives/Glyph";
import { StatusTag } from "../../core/primitives/primitives";
import { looks } from "../assessment/status";

function Stage({ index, glyph, title, children, empty }:
  { index: number; glyph: GlyphName; title: string; children?: ReactNode; empty?: string | null }) {
  return (
    <li className="rx-trace__stage">
      <span className="rx-trace__node" aria-hidden="true"><Glyph name={glyph} size="sm" /></span>
      <div className="rx-trace__content">
        <p className="rx-trace__title"><span className="rx-trace__index rx-num">{index}</span> {title}</p>
        {empty ? <p className="rx-meta">{empty}</p> : children}
      </div>
    </li>
  );
}

export function DecisionTrace({ detail }: { detail: RequirementDetail }) {
  const i18n = useI18n();
  const value = (raw: string | boolean) => typeof raw === "boolean" ? i18n.t(raw ? "ui.value.yes" : "ui.value.no") : raw;
  const rules = [...new Set([...detail.supporting_rule_ids, ...detail.decisions.flatMap((d) => d.rules.map((r) => r.rule_id))])];
  return (
    <ol className="rx-trace" role="list" aria-label={i18n.t("ui.trace.title")}>
      <Stage index={1} glyph="profile" title={i18n.t("ui.trace.input")}
        empty={detail.relevant_inputs.length === 0 ? i18n.t("ui.trace.no_inputs") : null}>
        <ul className="rx-trace__items" role="list">
          {detail.relevant_inputs.map(([key, raw]) => (
            <li key={key}><span className="rx-code">{key}</span> = <strong>{value(raw)}</strong></li>
          ))}
        </ul>
      </Stage>
      <Stage index={2} glyph="classification" title={i18n.t("ui.trace.predicate")}
        empty={detail.predicates.length === 0 ? i18n.t("ui.trace.no_predicates") : null}>
        <ul className="rx-trace__items" role="list">
          {detail.predicates.map((predicate) => (
            <li key={predicate.key}>
              <span className="rx-code">{predicate.key}</span>{" "}
              <StatusTag tone={predicate.value === "TRUE" ? "applicable" : predicate.value === "FALSE" ? "not_applicable" : "unresolved"}
                glyph={predicate.value === "TRUE" ? "check" : predicate.value === "FALSE" ? "not_applicable" : "unresolved"} variant="plain">
                {i18n.code("tri_state", predicate.value)}
              </StatusTag>
              {predicate.description && <p className="rx-body-sm rx-muted">{i18n.local(predicate.description)}</p>}
            </li>
          ))}
        </ul>
      </Stage>
      <Stage index={3} glyph="trace" title={i18n.t("ui.trace.rule")}
        empty={detail.decisions.length === 0 && rules.length === 0 ? i18n.t("ui.trace.no_rules") : null}>
        <ul className="rx-trace__items" role="list">
          {detail.decisions.map((decision) => (
            <li key={decision.area}>
              {i18n.code("decision_area", decision.area)}:{" "}
              <StatusTag {...looks.decision(decision.status)} variant="plain">{i18n.code("decision_status", decision.status)}</StatusTag>
              {decision.outcome && <> · {i18n.local(decision.outcome_label) ?? decision.outcome}</>}
            </li>
          ))}
          {rules.length > 0 && <li className="rx-meta">{i18n.t("field.trace_rules")}: <span className="rx-code">{rules.join(", ")}</span></li>}
        </ul>
      </Stage>
      <Stage index={4} glyph="applicable" title={i18n.t("ui.trace.applicability")}>
        <StatusTag {...looks.applicability(detail.applicability)}>{i18n.code("applicability", detail.applicability)}</StatusTag>
        <p className="rx-body-sm">{i18n.code("applicability_reason", detail.reason_code)}</p>
        {detail.block_description && <p className="rx-meta">{i18n.local(detail.block_description)} · <span className="rx-code">{detail.block}</span></p>}
      </Stage>
      <Stage index={5} glyph="requirements" title={i18n.t("ui.trace.requirement")}>
        <p><span className="rx-code">{detail.requirement_id}</span> {i18n.local(detail.title) ?? ""}</p>
      </Stage>
      <Stage index={6} glyph="gap" title={i18n.t("ui.trace.gap")}>
        <StatusTag {...looks.gap(detail.gap_status)}>{i18n.code("gap_result", detail.gap_status)}</StatusTag>
        <p className="rx-body-sm">{i18n.code("gap_reason", detail.gap_reason)}</p>
      </Stage>
      <Stage index={7} glyph="list" title={i18n.t("ui.trace.measure")}
        empty={detail.measures.length === 0 ? i18n.code("measure_mapping_status", detail.measure_status) : null}>
        <ul className="rx-trace__items" role="list">
          {detail.measures.map((measure) => (
            <li key={measure.measure_key}>{i18n.local(measure.label) ?? measure.measure_key} <span className="rx-code">{measure.measure_key}</span></li>
          ))}
        </ul>
      </Stage>
      <Stage index={8} glyph="evidence" title={i18n.t("ui.trace.evidence")}
        empty={detail.evidence.length === 0 ? i18n.code("evidence_state", detail.evidence_state) : null}>
        <ul className="rx-trace__items" role="list">
          {detail.evidence.map((item) => (
            <li key={item.evidence_id}>{item.title} <span className="rx-code">{item.document_identifier}</span></li>
          ))}
        </ul>
      </Stage>
    </ol>
  );
}
