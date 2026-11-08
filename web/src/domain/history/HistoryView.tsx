/**
 * Verlauf: Revisionen mit Ursprung, Fingerprint und Katalogstand, Revisionsaktionen
 * (abschließen, wieder öffnen, mit aktuellem Katalog neu bewerten) und das nur anhängende Audit.
 */

import { useState } from "react";
import { api } from "../../core/api/client";
import type { AuditEntry, Overview, RevisionInfo } from "../../core/api/types";
import { useResource } from "../../core/api/useResource";
import { useI18n } from "../../core/i18n/i18n";
import { Banner, Button, ConfirmDialog, LinkButton, LoadingState, StatusTag } from "../../core/primitives/primitives";
import { href } from "../../core/router/router";
import { Page } from "../shell/AppShell";
import { errorMessage, useAssessment } from "../assessment/AssessmentContext";
import { ActionError, WriteStateBanner } from "../assessment/AssessmentSection";
import { ChangeSummary } from "../wizard/WizardView";

export function HistoryView() {
  const i18n = useI18n();
  const { base, id, overview, run, apply, editable } = useAssessment();
  const revisions = useResource(() => api.get<RevisionInfo[]>(`${base}/revisions`), [base, overview?.revision_count, overview?.state]);
  const audit = useResource(() => api.get<AuditEntry[]>(`${base}/audit`), [base, overview?.updated_at, overview?.state]);
  const [confirmFinalise, setConfirmFinalise] = useState(false);

  async function action(name: "finalise" | "reopen" | "rebase" | "recalculate", message: string) {
    const next = await run(() => api.post<Overview>(`${base}/${name}`), message);
    if (next) {
      apply(next);
      revisions.reload();
      audit.reload();
    }
  }

  if (!overview) return null;
  const canReopen = overview.state === "FINALISED" && overview.version_status === "MATCH";
  return (
    <Page eyebrow={i18n.t("ui.nav.history")} title={i18n.t("ui.history.title")} focusKey="history"
      lead={<p>{i18n.t("ui.history.lead")}</p>}
      actions={(
        <>
          {editable && <Button variant="primary" onPress={() => setConfirmFinalise(true)}>{i18n.t("ui.history.finalise")}</Button>}
          {canReopen && <Button variant="secondary" onPress={() => action("reopen", i18n.t("ui.history.reopened"))}>{i18n.t("ui.history.reopen")}</Button>}
          {editable && <Button variant="ghost" onPress={() => action("recalculate", i18n.t("ui.history.recalculated"))}>{i18n.t("ui.history.recalculate")}</Button>}
        </>
      )}>
      <WriteStateBanner />
      <ActionError />

      <section className="rx-section" aria-labelledby="revisions-title">
        <h2 id="revisions-title" className="rx-section-title">{i18n.t("revisions.caption")}</h2>
        {revisions.loading && !revisions.data && <LoadingState label={i18n.t("ui.state.loading")} />}
        {revisions.error && <Banner tone="error" title={errorMessage(i18n.t, i18n.has, revisions.error)} />}
        {revisions.data && (
          <ol className="rx-revisions" role="list" reversed>
            {[...revisions.data].reverse().map((revision) => {
              const current = revision.revision === overview.revision;
              return (
                <li key={revision.revision} className="rx-card rx-revision" data-current={current || undefined}>
                  <div className="rx-cluster rx-cluster--between">
                    <h3 className="rx-subsection-title">
                      {i18n.t("ui.history.revision", { revision: revision.revision })}
                      {current && <span className="rx-meta"> · {i18n.t("ui.history.current")}</span>}
                    </h3>
                    <div className="rx-cluster">
                      <StatusTag tone={revision.state === "DRAFT" ? "neutral" : "info"} glyph={revision.state === "DRAFT" ? "open" : "complete"}>
                        {i18n.code("assessment_state", revision.state)}
                      </StatusTag>
                      {!revision.same_catalog_versions && <StatusTag tone="review" glyph="attention">{i18n.t("revisions.other_versions")}</StatusTag>}
                    </div>
                  </div>
                  <dl className="rx-dl">
                    <dt>{i18n.t("col.origin")}</dt><dd>{i18n.code("revision_origin", revision.origin)}</dd>
                    {revision.based_on !== null && <><dt>{i18n.t("col.based_on")}</dt><dd>{revision.based_on}</dd></>}
                    <dt>{i18n.t("col.updated_at")}</dt><dd>{i18n.dateTime(revision.updated_at)}</dd>
                    <dt>{i18n.t("field.assessment_fingerprint")}</dt><dd className="rx-code">{revision.fingerprint}</dd>
                    <dt>{i18n.t("col.catalog_versions")}</dt>
                    <dd className="rx-code">{Object.entries(revision.catalog_versions).map(([k, v]) => `${k} ${v}`).join(" · ")}</dd>
                  </dl>
                  {revision.change && <ChangeSummary change={revision.change} />}
                  <LinkButton variant="ghost" icon="report" href={href(`/a/${id}/report`, { revision: String(revision.revision) })}>
                    {i18n.t("ui.history.open_revision")}
                  </LinkButton>
                </li>
              );
            })}
          </ol>
        )}
      </section>

      <section className="rx-section" aria-labelledby="audit-title">
        <h2 id="audit-title" className="rx-section-title">{i18n.t("ui.history.audit_title")}</h2>
        <p className="rx-body-sm rx-muted rx-reading">{i18n.t("ui.history.audit_lead")}</p>
        {audit.data && (
          <div className="rx-table-wrap">
            <table className="rx-table">
              <thead>
                <tr>
                  <th scope="col" className="rx-num">#</th>
                  <th scope="col">{i18n.t("col.revision")}</th>
                  <th scope="col">{i18n.t("ui.history.event")}</th>
                  <th scope="col">{i18n.t("ui.history.subject")}</th>
                  <th scope="col">{i18n.t("ui.history.time")}</th>
                </tr>
              </thead>
              <tbody>
                {[...audit.data].reverse().map((entry) => (
                  <tr key={entry.sequence}>
                    <td className="rx-num">{entry.sequence}</td>
                    <td className="rx-num">{entry.revision}</td>
                    <td>{i18n.code("audit_event_type", entry.event_type)}</td>
                    <td className="rx-code">{entry.subject_id ?? "–"}</td>
                    <td>{i18n.dateTime(entry.occurred_at)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>

      <ConfirmDialog isOpen={confirmFinalise} onOpenChange={setConfirmFinalise} title={i18n.t("ui.history.finalise_title")}
        body={i18n.t("ui.history.finalise_text")} confirmLabel={i18n.t("ui.history.finalise")} cancelLabel={i18n.t("ui.action.cancel")}
        onConfirm={() => action("finalise", i18n.t("ui.history.finalised"))} />
    </Page>
  );
}
