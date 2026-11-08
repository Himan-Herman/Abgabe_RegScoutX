/**
 * Anforderungsdetail: Text, Lebenszyklus, Quellen, Erfüllungsbewertung, Evidence Dock,
 * Decision Trace, Maßnahmen und offene Punkte einer RR. Schreibende Aktionen laufen über
 * den Anwendungseinstieg; Status und Gap-Ergebnis bestimmt ausschließlich der Kern.
 */

import { useEffect, useRef, useState } from "react";
import { api } from "../../core/api/client";
import type { EvidenceItem, EvidencePayload, RequirementDetail as Detail } from "../../core/api/types";
import { useResource } from "../../core/api/useResource";
import { useI18n } from "../../core/i18n/i18n";
import { Banner, Button, ChoiceCards, ComboField, Disclosure, Drawer, LoadingState, StatusTag, TextAreaField } from "../../core/primitives/primitives";
import { errorMessage, useAssessment } from "../assessment/AssessmentContext";
import { JUSTIFICATION_REQUIRED, SETTABLE_GAP_STATUS, looks } from "../assessment/status";
import { EvidenceForm, draftOf, type EvidenceDraft } from "../evidence/EvidenceForm";
import { DecisionTrace } from "./DecisionTrace";
import { LifecycleRibbon } from "./LifecycleRibbon";
import { SourceDrawer } from "./SourceDrawer";

function GapForm({ detail, onSaved }: { detail: Detail; onSaved: (next: Detail) => void }) {
  const i18n = useI18n();
  const { run, base, editable, actionError } = useAssessment();
  const [status, setStatus] = useState<string | null>(detail.answer?.status ?? null);
  const [justification, setJustification] = useState(detail.answer?.justification ?? "");
  const [attempted, setAttempted] = useState(false);
  useEffect(() => {
    setStatus(detail.answer?.status ?? null);
    setJustification(detail.answer?.justification ?? "");
    setAttempted(false);
  }, [detail.requirement_id, detail.answer?.status, detail.answer?.justification]);
  const needsJustification = status !== null && JUSTIFICATION_REQUIRED.has(status);
  const serverError = actionError?.code === "INVALID_INPUT" && (actionError.field ?? "").endsWith("justification");
  const localError = attempted && needsJustification && !justification.trim();

  async function save() {
    setAttempted(true);
    if (!status || (needsJustification && !justification.trim())) return;
    const next = await run(() => api.put<Detail>(`${base}/requirements/${detail.requirement_id}/assessment`,
      { status, justification: justification.trim() || null }), i18n.t("ui.gap.saved"));
    if (next) onSaved(next);
  }

  return (
    <div className="rx-stack">
      <ChoiceCards label={i18n.t("field.user_assessment")} value={status} isDisabled={!editable}
        onChange={(value) => setStatus(value)}
        options={SETTABLE_GAP_STATUS.map((code) => ({ value: code, label: i18n.code("gap_status", code),
          description: i18n.t(`ui.gap.hint.${code.toLowerCase()}`) }))} />
      <TextAreaField label={i18n.t("field.justification")} value={justification} onChange={setJustification}
        isRequired={needsJustification} isDisabled={!editable}
        description={i18n.t(needsJustification ? "ui.gap.justification_required" : "ui.gap.justification_optional")}
        errorMessage={localError || serverError ? i18n.t("ui.gap.justification_missing") : null} />
      <div className="rx-cluster">
        <Button variant="primary" onPress={save} isDisabled={!editable || !status}>{i18n.t("ui.gap.save")}</Button>
        {status && (status === "FULFILLED" || status === "PARTIALLY_FULFILLED") && detail.evidence.length === 0 && (
          <p className="rx-meta">{i18n.t("ui.gap.evidence_hint")}</p>
        )}
      </div>
    </div>
  );
}

function EvidenceDock({ detail, onChanged }: { detail: Detail; onChanged: (next: Detail) => void }) {
  const i18n = useI18n();
  const { run, base, editable, actionError } = useAssessment();
  const register = useResource(() => api.get<EvidencePayload>(`${base}/evidence`), [base, detail.evidence.length]);
  const [creating, setCreating] = useState(false);
  const [choice, setChoice] = useState<string | null>(null);
  const linked = new Set(detail.evidence.map((e) => e.evidence_id));
  const available = (register.data?.items ?? []).filter((item) => !linked.has(item.evidence_id));
  const path = `${base}/requirements/${detail.requirement_id}/evidence`;

  async function link(evidenceId: string) {
    const next = await run(() => api.post<Detail>(`${path}/${evidenceId}`), i18n.t("ui.evidence.linked"));
    if (next) { onChanged(next); setChoice(null); }
  }
  async function create(draft: EvidenceDraft) {
    const created = await run(() => api.post<EvidenceItem>(`${base}/evidence`, {
      title: draft.title, document_identifier: draft.document_identifier,
      document_version: draft.document_version || null, location: draft.location || null, measure_key: draft.measure_key,
    }));
    if (!created) return;
    setCreating(false);
    await link(created.evidence_id);
  }

  return (
    <div className="rx-stack">
      {detail.evidence.length === 0 ? <p className="rx-muted rx-body-sm">{i18n.t("ui.evidence.none_linked")}</p> : (
        <ul className="rx-dock" role="list">
          {detail.evidence.map((item) => (
            <li key={item.evidence_id} className="rx-dock__item">
              <div className="rx-dock__text">
                <p className="rx-dock__title">{item.title}</p>
                <p className="rx-meta">
                  <span className="rx-code">{item.document_identifier}</span>
                  {item.document_version && <> · {item.document_version}</>}
                  {item.measure_key && <> · <span className="rx-code">{item.measure_key}</span></>}
                </p>
              </div>
              <Button variant="ghost" isDisabled={!editable} aria-label={i18n.t("ui.evidence.unlink_named", { title: item.title })}
                onPress={async () => {
                  const next = await run(() => api.del<Detail>(`${path}/${item.evidence_id}`), i18n.t("ui.evidence.unlinked"));
                  if (next) onChanged(next);
                }}>{i18n.t("ui.evidence.unlink")}</Button>
            </li>
          ))}
        </ul>
      )}
      {editable && (
        <div className="rx-dock__actions">
          {available.length > 0 && (
            <div className="rx-dock__link">
              <ComboField label={i18n.t("ui.evidence.link_existing")} value={choice} onChange={setChoice}
                emptyText={i18n.t("ui.wizard.no_match")}
                options={available.map((item) => ({ value: item.evidence_id, label: item.title, description: item.document_identifier }))} />
              <Button variant="secondary" isDisabled={!choice} onPress={() => choice && link(choice)}>{i18n.t("ui.evidence.link")}</Button>
            </div>
          )}
          <Button variant="secondary" icon="plus" onPress={() => setCreating(true)}>{i18n.t("ui.evidence.create_and_link")}</Button>
        </div>
      )}
      <Drawer isOpen={creating} onOpenChange={setCreating} title={i18n.t("ui.evidence.create_title")} closeLabel={i18n.t("ui.action.close")}>
        <EvidenceForm initial={draftOf(null)} measures={detail.measures} submitLabel={i18n.t("ui.evidence.create_and_link")}
          onSubmit={create} onCancel={() => setCreating(false)} error={actionError} />
      </Drawer>
    </div>
  );
}

export function RequirementDetail({ requirementId, onUpdated, headingRef }:
  { requirementId: string; onUpdated: (detail: Detail) => void; headingRef?: React.RefObject<HTMLHeadingElement | null> }) {
  const i18n = useI18n();
  const { base, run, editable, refresh, actionError } = useAssessment();
  const detail = useResource(() => api.get<Detail>(`${base}/requirements/${requirementId}`), [base, requirementId]);
  const [sourcesOpen, setSourcesOpen] = useState(false);
  const fallbackRef = useRef<HTMLHeadingElement>(null);
  const ref = headingRef ?? fallbackRef;

  // Nach dem Laden einer neu gewählten Anforderung erhält deren Überschrift den Fokus.
  const loadedId = detail.data?.requirement_id;
  useEffect(() => { if (loadedId) ref.current?.focus(); }, [loadedId, ref]);

  function updated(next: Detail) {
    detail.setData(next);
    onUpdated(next);
    void refresh();
  }

  if (detail.loading && !detail.data) return <LoadingState label={i18n.t("ui.state.loading")} />;
  if (detail.error || !detail.data) {
    return <Banner tone="error" title={errorMessage(i18n.t, i18n.has, detail.error ?? { code: "APPLICATION_ERROR" })} />;
  }
  const d = detail.data;
  const title = i18n.local(d.title);
  const reactivated = d.answer_state === "REACTIVATED_REVIEW_REQUIRED";
  return (
    <article className="rx-detail" aria-labelledby="detail-title">
      <header className="rx-detail__header">
        <p className="rx-code">{d.requirement_id}</p>
        <h2 id="detail-title" ref={ref} tabIndex={-1} className="rx-section-title">{title ?? i18n.t("value.catalog_text_unavailable")}</h2>
        <div className="rx-cluster">
          <StatusTag {...looks.applicability(d.applicability)}>{i18n.code("applicability", d.applicability)}</StatusTag>
          <StatusTag {...looks.gap(d.gap_status)}>{i18n.code("gap_result", d.gap_status)}</StatusTag>
          {d.answer_state && d.answer_state !== "ACTIVE" && (
            <StatusTag {...looks.answer(d.answer_state)}>{i18n.code("answer_state", d.answer_state)}</StatusTag>
          )}
        </div>
        <p className="rx-meta">{i18n.theme(d.theme)}</p>
      </header>

      {!d.texts_available && <Banner tone="info" title={i18n.t("banner.catalog_texts_unavailable")} />}
      {d.text && <p className="rx-detail__text rx-reading">{i18n.local(d.text)}</p>}

      <section className="rx-stack rx-stack--tight" aria-labelledby="lifecycle-title">
        <h3 id="lifecycle-title" className="rx-subsection-title">{i18n.t("field.lifecycle")}</h3>
        <LifecycleRibbon phases={d.lifecycle} />
      </section>

      <section className="rx-cluster rx-cluster--between">
        <p className="rx-body-sm">
          {i18n.t("field.primary_sources")}: <span className="rx-code">{(d.primary_sources ?? []).join(", ") || i18n.t("value.none")}</span>
        </p>
        <Button variant="ghost" icon="source" onPress={() => setSourcesOpen(true)}>{i18n.t("ui.sources.open")}</Button>
      </section>
      <SourceDrawer isOpen={sourcesOpen} onOpenChange={setSourcesOpen} requirementId={d.requirement_id}
        primary={d.primary_sources ?? []} supplementary={d.supplementary_sources ?? []} />

      <section className="rx-card rx-stack" aria-labelledby="assessment-title">
        <h3 id="assessment-title" className="rx-subsection-title">{i18n.t("ui.gap.title")}</h3>
        <p className="rx-body-sm rx-muted">{i18n.code("gap_reason", d.gap_reason)}</p>
        {actionError && actionError.code !== "INVALID_INPUT" && (
          <Banner tone="error" title={errorMessage(i18n.t, i18n.has, actionError)} />
        )}
        {reactivated && (
          <Banner tone="warning" title={i18n.t("ui.gap.reactivated_title")}
            action={editable ? <Button variant="secondary" onPress={async () => {
              const next = await run(() => api.post<Detail>(`${base}/requirements/${d.requirement_id}/confirm`), i18n.t("ui.gap.confirmed"));
              if (next) updated(next);
            }}>{i18n.t("ui.gap.confirm")}</Button> : undefined}>
            {i18n.t("ui.gap.reactivated_text", { status: d.answer ? i18n.code("gap_status", d.answer.status) : "" })}
          </Banner>
        )}
        {d.applicability !== "APPLICABLE" && d.answer && (
          <Banner tone="info" title={i18n.t("ui.gap.inactive_title")}>
            {i18n.t("ui.gap.inactive_text", { status: i18n.code("gap_status", d.answer.status),
              count: i18n.number(d.answer.evidence_ids.length) })}
          </Banner>
        )}
        {d.applicability === "APPLICABLE"
          ? <GapForm detail={d} onSaved={updated} />
          : <p className="rx-body-sm">{i18n.t(`ui.gap.not_settable.${d.applicability.toLowerCase()}`)}</p>}
        {d.applicability === "APPLICABLE" && (
          <>
            <h4 className="rx-subsection-title">{i18n.t("field.evidence_references")}</h4>
            <EvidenceDock detail={d} onChanged={updated} />
          </>
        )}
      </section>

      <Disclosure title={i18n.t("ui.trace.title")} defaultExpanded id="decision-trace">
        <DecisionTrace detail={d} />
      </Disclosure>
      <Disclosure title={i18n.t("field.measures")} meta={i18n.code("measure_mapping_status", d.measure_status)}>
        {d.measures.length === 0 ? <p className="rx-body-sm">{i18n.t("measure.open")}</p> : (
          <ul className="rx-stack rx-stack--tight" role="list">
            {d.measures.map((measure) => (
              <li key={measure.measure_key}>
                <p>{i18n.local(measure.label)} <span className="rx-code">{measure.measure_key}</span></p>
                <p className="rx-meta">{i18n.t("field.expected_evidence")}: {measure.evidence_types.map(([key, label]) => i18n.local(label) ?? key).join(", ")}</p>
              </li>
            ))}
          </ul>
        )}
      </Disclosure>
      {d.open_items.length > 0 && (
        <Disclosure title={i18n.t("field.open_items")} meta={i18n.number(d.open_items.length)}>
          <ul role="list" className="rx-stack rx-stack--tight">
            {d.open_items.map((item) => <li key={item}>{i18n.code("report_open_item", item)}</li>)}
          </ul>
        </Disclosure>
      )}
    </article>
  );
}
