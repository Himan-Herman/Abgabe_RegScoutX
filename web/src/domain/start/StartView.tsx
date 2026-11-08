/**
 * Start / Bewertungen: Einordnung des Werkzeugs, vorhandene Bewertungen, neue Bewertung.
 */

import { useState } from "react";
import { api } from "../../core/api/client";
import type { AssessmentListItem, Overview } from "../../core/api/types";
import { useResource, toApiError } from "../../core/api/useResource";
import { useI18n } from "../../core/i18n/i18n";
import { Banner, Button, EmptyState, LoadingState, StatusTag } from "../../core/primitives/primitives";
import { Link, navigate } from "../../core/router/router";
import { useAnnounce } from "../../core/a11y/announcer";
import { Page } from "../shell/AppShell";
import { errorMessage } from "../assessment/AssessmentContext";
import { looks, shortId } from "../assessment/status";
import { useAppData } from "../app/AppData";

export function StartView() {
  const i18n = useI18n();
  const meta = useAppData();
  const announce = useAnnounce();
  const list = useResource(() => api.get<AssessmentListItem[]>("/assessments"), []);
  const [creating, setCreating] = useState(false);
  const [createError, setCreateError] = useState<string | null>(null);

  async function create() {
    setCreating(true);
    setCreateError(null);
    try {
      const overview = await api.post<Overview>("/assessments", { profile: {} });
      announce(i18n.t("ui.start.created"));
      navigate(`/a/${overview.assessment_id}/profile`);
    } catch (error) {
      const message = errorMessage(i18n.t, i18n.has, toApiError(error));
      setCreateError(message);
      announce(message, "assertive");
      setCreating(false);
    }
  }

  return (
    <Page eyebrow={i18n.t("ui.start.eyebrow")} title={i18n.t("ui.start.title")} focusKey="start"
      lead={<p>{i18n.t("ui.start.lead", { count: i18n.number(meta.requirement_count) })}</p>}
      actions={<Button variant="primary" icon="plus" onPress={create} isDisabled={creating}>{i18n.t("ui.start.new")}</Button>}>
      {createError && <Banner tone="error" title={createError} />}

      <section className="rx-scope" aria-labelledby="scope-title">
        <h2 id="scope-title" className="rx-subsection-title">{i18n.t("ui.scope.title")}</h2>
        <ul className="rx-scope__list" role="list">
          {["assistance", "scope", "no_legal_advice", "no_certification", "unresolved"].map((key) => (
            <li key={key}><span className="rx-scope__marker" aria-hidden="true" />{i18n.t(`ui.scope.${key}`)}</li>
          ))}
        </ul>
      </section>

      <section className="rx-section" aria-labelledby="assessments-title">
        <div className="rx-section__header">
          <h2 id="assessments-title" className="rx-section-title">{i18n.t("ui.start.list_title")}</h2>
          {list.data && <p className="rx-meta">{i18n.t("ui.start.count", { count: list.data.length })}</p>}
        </div>
        {list.loading && <LoadingState label={i18n.t("ui.state.loading")} />}
        {list.error && (
          <Banner tone="error" title={errorMessage(i18n.t, i18n.has, list.error)}
            action={<Button variant="secondary" onPress={list.reload}>{i18n.t("ui.action.retry")}</Button>} />
        )}
        {list.data && list.data.length === 0 && (
          <EmptyState title={i18n.t("ui.start.empty_title")} text={i18n.t("ui.start.empty_text")}
            action={<Button variant="primary" icon="plus" onPress={create} isDisabled={creating}>{i18n.t("ui.start.new")}</Button>} />
        )}
        {list.data && list.data.length > 0 && (
          <ul className="rx-assessment-list" role="list">
            {list.data.map((item) => item.corrupted ? (
              <li key={item.assessment_id} className="rx-assessment-row">
                <div className="rx-assessment-row__main">
                  <Link to={`/a/${item.assessment_id}/profile`} className="rx-assessment-row__link">
                    <span className="rx-mono">{shortId(item.assessment_id)}</span>
                  </Link>
                  <p className="rx-meta">{i18n.t("ui.state.corrupted_text")}</p>
                </div>
                <StatusTag tone="not_fulfilled" glyph="blocked">{i18n.t("ui.state.corrupted_title")}</StatusTag>
              </li>
            ) : (
              <li key={item.assessment_id} className="rx-assessment-row">
                <div className="rx-assessment-row__main">
                  <Link to={`/a/${item.assessment_id}/profile`} className="rx-assessment-row__link">
                    <span className="rx-mono">{shortId(item.assessment_id)}</span>
                    <span className="rx-visually-hidden">{i18n.t("ui.start.open_assessment")}</span>
                  </Link>
                  <p className="rx-meta">
                    {i18n.t("ui.context.revision", { revision: item.revision, count: item.revision_count })}
                    {" · "}{i18n.t("ui.start.updated", { date: i18n.dateTime(item.updated_at) })}
                  </p>
                </div>
                <div className="rx-cluster">
                  <StatusTag tone={item.state === "DRAFT" ? "neutral" : "info"} glyph={item.state === "DRAFT" ? "open" : "complete"}>
                    {i18n.code("assessment_state", item.state)}
                  </StatusTag>
                  {item.version_status !== "MATCH" && (
                    <StatusTag {...looks.version(item.version_status)}>{i18n.t(`ui.version.short.${item.version_status.toLowerCase()}`)}</StatusTag>
                  )}
                </div>
                {item.counts && (
                  <dl className="rx-assessment-row__counts">
                    {(["applicable", "unresolved", "gaps"] as const).map((key) => (
                      <div key={key}>
                        <dt>{i18n.t(`col.short.${key}`)}</dt>
                        <dd className="rx-num">{i18n.number(item.counts![key])}</dd>
                      </div>
                    ))}
                  </dl>
                )}
              </li>
            ))}
          </ul>
        )}
      </section>
    </Page>
  );
}
