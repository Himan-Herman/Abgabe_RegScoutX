/**
 * Nachweise: Register der nutzerseitigen Nachweisreferenzen (anlegen, ändern, entfernen) und
 * Übersicht der vorgesehenen Maßnahmen mit Anzahl anwendbarer Anforderungen und Referenzen.
 * RegScoutX speichert nur Referenzen, keine Dokumente, und bewertet deren Inhalt nicht.
 */

import { useState } from "react";
import { api } from "../../core/api/client";
import type { CatalogMeasure, EvidenceItem, EvidencePayload } from "../../core/api/types";
import { useResource } from "../../core/api/useResource";
import { useI18n } from "../../core/i18n/i18n";
import { Banner, Button, ConfirmDialog, Drawer, EmptyState, LoadingState } from "../../core/primitives/primitives";
import { href } from "../../core/router/router";
import { Page } from "../shell/AppShell";
import { errorMessage, useAssessment } from "../assessment/AssessmentContext";
import { ActionError, WriteStateBanner } from "../assessment/AssessmentSection";
import { EvidenceForm, draftOf, type EvidenceDraft } from "./EvidenceForm";

export function EvidenceView() {
  const i18n = useI18n();
  const { base, id, run, editable, refresh, actionError } = useAssessment();
  const payload = useResource(() => api.get<EvidencePayload>(`${base}/evidence`), [base]);
  const catalog = useResource(() => api.get<CatalogMeasure[]>("/measures"), []);
  const [editing, setEditing] = useState<EvidenceItem | "new" | null>(null);
  const [removing, setRemoving] = useState<EvidenceItem | null>(null);
  const measures = (catalog.data ?? []).map((m) => ({ measure_key: m.measure_key, label: m.label,
    evidence_types: m.evidence_types.map((e) => [e.key, e.label] as [string, typeof e.label]) }));

  async function save(draft: EvidenceDraft) {
    const body = { title: draft.title, document_identifier: draft.document_identifier,
      document_version: draft.document_version || null, location: draft.location || null, measure_key: draft.measure_key };
    const result = editing === "new"
      ? await run(() => api.post<EvidenceItem>(`${base}/evidence`, body), i18n.t("ui.evidence.created"))
      : await run(() => api.put<EvidenceItem>(`${base}/evidence/${(editing as EvidenceItem).evidence_id}`, body), i18n.t("ui.evidence.updated"));
    if (result) {
      setEditing(null);
      payload.reload();
      void refresh();
    }
  }

  async function remove(item: EvidenceItem) {
    const result = await run(() => api.del(`${base}/evidence/${item.evidence_id}`), i18n.t("ui.evidence.removed"));
    if (result) {
      payload.reload();
      void refresh();
    }
  }

  const items = payload.data?.items ?? [];
  return (
    <Page eyebrow={i18n.t("ui.nav.evidence")} title={i18n.t("ui.evidence.title")} focusKey="evidence"
      lead={<p>{i18n.t("ui.evidence.lead")}</p>}
      actions={editable ? <Button variant="primary" icon="plus" onPress={() => setEditing("new")}>{i18n.t("ui.evidence.new")}</Button> : undefined}>
      <WriteStateBanner />
      <ActionError />
      {payload.loading && !payload.data && <LoadingState label={i18n.t("ui.state.loading")} />}
      {payload.error && <Banner tone="error" title={errorMessage(i18n.t, i18n.has, payload.error)}
        action={<Button variant="secondary" onPress={payload.reload}>{i18n.t("ui.action.retry")}</Button>} />}

      {payload.data && (
        <section className="rx-section" aria-labelledby="register-title">
          <h2 id="register-title" className="rx-section-title">{i18n.t("measures.evidence_heading")}</h2>
          {items.length === 0 ? (
            <EmptyState glyph="evidence" title={i18n.t("empty.evidence")} text={i18n.t("ui.evidence.empty_text")}
              action={editable ? <Button variant="primary" icon="plus" onPress={() => setEditing("new")}>{i18n.t("ui.evidence.new")}</Button> : undefined} />
          ) : (
            <ul className="rx-evidence-list" role="list">
              {items.map((item) => (
                <li key={item.evidence_id} className="rx-card rx-evidence">
                  <div className="rx-evidence__main">
                    <h3 className="rx-subsection-title rx-evidence__title">{item.title}</h3>
                    <dl className="rx-dl">
                      <dt>{i18n.t("col.document")}</dt><dd className="rx-code">{item.document_identifier}</dd>
                      {item.document_version && <><dt>{i18n.t("col.document_version")}</dt><dd>{item.document_version}</dd></>}
                      {item.location && <><dt>{i18n.t("col.location")}</dt><dd>{item.location}</dd></>}
                      {item.measure_key && (
                        <><dt>{i18n.t("col.measure_key")}</dt>
                          <dd>{i18n.local(catalog.data?.find((m) => m.measure_key === item.measure_key)?.label)}{" "}
                            <span className="rx-code">{item.measure_key}</span></dd></>
                      )}
                      <dt>{i18n.t("col.requirements")}</dt>
                      <dd>{item.requirement_ids.length === 0 ? i18n.t("ui.evidence.unlinked_state") : (
                        <span className="rx-cluster">
                          {item.requirement_ids.map((rr) => (
                            <a key={rr} className="rx-code" href={href(`/a/${id}/requirements`, { rr })}>{rr}</a>
                          ))}
                        </span>
                      )}</dd>
                    </dl>
                  </div>
                  {editable && (
                    <div className="rx-cluster">
                      <Button variant="secondary" onPress={() => setEditing(item)}>{i18n.t("ui.action.edit")}</Button>
                      <Button variant="ghost" onPress={() => setRemoving(item)}>{i18n.t("ui.action.remove")}</Button>
                    </div>
                  )}
                </li>
              ))}
            </ul>
          )}
        </section>
      )}

      {payload.data && (
        <section className="rx-section" aria-labelledby="measures-title">
          <h2 id="measures-title" className="rx-section-title">{i18n.t("measures.caption")}</h2>
          {payload.data.mapping_review_required > 0 && (
            <Banner tone="unresolved" title={i18n.t("measures.mapping_review", { count: payload.data.mapping_review_required })} />
          )}
          {payload.data.measures.length === 0 ? <p className="rx-muted">{i18n.t("empty.measures")}</p> : (
            <div className="rx-table-wrap">
              <table className="rx-table">
                <thead>
                  <tr>
                    <th scope="col">{i18n.t("col.measure")}</th>
                    <th scope="col">{i18n.t("col.expected_evidence")}</th>
                    <th scope="col" className="rx-num">{i18n.t("col.planned")}</th>
                    <th scope="col" className="rx-num">{i18n.t("col.with_evidence")}</th>
                  </tr>
                </thead>
                <tbody>
                  {payload.data.measures.map((entry) => (
                    <tr key={entry.measure.measure_key}>
                      <th scope="row">{i18n.local(entry.measure.label)} <div className="rx-code">{entry.measure.measure_key}</div></th>
                      <td>{entry.measure.evidence_types.map(([key, label]) => i18n.local(label) ?? key).join(", ")}</td>
                      <td className="rx-num">{i18n.number(entry.planned)}</td>
                      <td className="rx-num">{i18n.number(entry.with_evidence)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </section>
      )}

      <Drawer isOpen={editing !== null} onOpenChange={(open) => { if (!open) setEditing(null); }}
        title={i18n.t(editing === "new" ? "ui.evidence.create_title" : "ui.evidence.edit_title")} closeLabel={i18n.t("ui.action.close")}>
        {editing !== null && (
          <EvidenceForm key={editing === "new" ? "new" : editing.evidence_id} initial={draftOf(editing === "new" ? null : editing)}
            measures={measures} error={actionError}
            submitLabel={i18n.t(editing === "new" ? "ui.evidence.create" : "ui.action.save")}
            onSubmit={save} onCancel={() => setEditing(null)} />
        )}
      </Drawer>
      <ConfirmDialog isOpen={removing !== null} onOpenChange={(open) => { if (!open) setRemoving(null); }}
        title={i18n.t("ui.evidence.remove_title")} body={i18n.t("ui.evidence.remove_text", { title: removing?.title ?? "" })}
        confirmLabel={i18n.t("ui.action.remove")} cancelLabel={i18n.t("ui.action.cancel")} destructive
        onConfirm={() => { if (removing) void remove(removing); }} />
    </Page>
  );
}
