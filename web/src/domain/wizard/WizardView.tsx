/**
 * Assessment Wizard (Signature Component): segmentierter, adaptiver Fragebogen.
 * Semantischer Fortschritt je Abschnitt (DI-001), Begründung jeder Folgefrage (DI-004),
 * zulässige Werte vor der Eingabe (DI-006), Rücknavigation, sichtbare Neuberechnung,
 * nicht mehr verwendete und wieder anwendbare Angaben sowie die Kernentscheidungen.
 */

import { useEffect, useMemo, useState } from "react";
import { api } from "../../core/api/client";
import type { AssessmentChange, Decision, ProfileUpdate, Question, Questionnaire } from "../../core/api/types";
import { useResource } from "../../core/api/useResource";
import { useI18n } from "../../core/i18n/i18n";
import { useAnnounce } from "../../core/a11y/announcer";
import { Glyph } from "../../core/primitives/Glyph";
import { Banner, Button, LinkButton, LoadingState, StatusTag } from "../../core/primitives/primitives";
import { href, navigate, useRoute } from "../../core/router/router";
import { Page } from "../shell/AppShell";
import { ActionError, WriteStateBanner } from "../assessment/AssessmentSection";
import { errorMessage, useAssessment } from "../assessment/AssessmentContext";
import { looks } from "../assessment/status";
import { QuestionCard, valueLabel } from "./QuestionCard";

const DECISION_AREAS = ["QUALIFICATION", "BOUNDARY", "CLASSIFICATION", "AI_ACT_APPLICABILITY"];

export function DecisionSummary({ decisions, compact }: { decisions: Decision[]; compact?: boolean }) {
  const i18n = useI18n();
  const shown = decisions.filter((d) => DECISION_AREAS.includes(d.area))
    .sort((a, b) => DECISION_AREAS.indexOf(a.area) - DECISION_AREAS.indexOf(b.area));
  return (
    <ul className={`rx-decisions${compact ? " rx-decisions--compact" : ""}`} role="list">
      {shown.map((decision) => {
        const look = looks.decision(decision.status);
        return (
          <li key={decision.area} className="rx-decision">
            <p className="rx-decision__area">{i18n.code("decision_area", decision.area)}</p>
            <StatusTag {...look}>{i18n.code("decision_status", decision.status)}</StatusTag>
            {decision.outcome && (
              <p className="rx-decision__outcome">
                {i18n.local(decision.outcome_label) ?? decision.outcome}
                {decision.mdr_class && <> · {i18n.t("classification.mdr_class", { mdr_class: decision.mdr_class })}</>}
              </p>
            )}
            {decision.applicable_from && (
              <p className="rx-meta">{i18n.t("classification.applicable_from", { date: i18n.date(decision.applicable_from) })}</p>
            )}
          </li>
        );
      })}
    </ul>
  );
}

export function ChangeSummary({ change }: { change: AssessmentChange }) {
  const i18n = useI18n();
  const items = [
    ["changed_inputs", change.changed_inputs.length],
    ["applicability_changes", change.applicability_changes.length],
    ["gap_status_changes", change.gap_status_changes.length],
    ["deactivated_answers", change.deactivated_answers.length],
    ["reactivated_answers", change.reactivated_answers.length],
  ] as const;
  return (
    <dl className="rx-change">
      {items.map(([key, count]) => (
        <div key={key} className="rx-change__item" data-zero={count === 0 || undefined}>
          <dt>{i18n.t(`ui.change.${key}`)}</dt>
          <dd className="rx-num">{i18n.number(count)}</dd>
        </div>
      ))}
    </dl>
  );
}

function changeAnnouncement(i18n: ReturnType<typeof useI18n>, change: AssessmentChange | null): string {
  if (!change) return i18n.t("ui.wizard.saved");
  return i18n.t("ui.wizard.recalculated", {
    applicability: i18n.number(change.applicability_changes.length),
    gaps: i18n.number(change.gap_status_changes.length),
  });
}

export function WizardView() {
  const i18n = useI18n();
  const announce = useAnnounce();
  const route = useRoute();
  const { overview, base, apply, editable, run, id } = useAssessment();
  const questionnaire = useResource(() => api.get<Questionnaire>(`${base}/questionnaire`),
    [base, overview?.revision, overview?.version_status]);
  const [busyKey, setBusyKey] = useState<string | null>(null);
  const [lastChange, setLastChange] = useState<{ change: AssessmentChange | null; key: string; appeared: string[] } | null>(null);

  const data = questionnaire.data;
  const segments = data?.segments ?? [];
  const requested = route.query.get("segment");
  const fallback = useMemo(() => {
    if (!data) return null;
    const next = data.segments.find((s) => s.questions.some((q) => q.key === data.next_question));
    return (next ?? data.segments.find((s) => s.questions.length > 0) ?? data.segments[0])?.segment ?? null;
  }, [data]);
  const active = segments.find((s) => s.segment === requested)?.segment ?? fallback;
  const index = segments.findIndex((s) => s.segment === active);
  const segment = index >= 0 ? segments[index] : null;
  const answered = segments.reduce((sum, s) => sum + s.answered, 0);
  const open = segments.reduce((sum, s) => sum + s.open, 0);

  useEffect(() => { setLastChange(null); }, [active]);

  async function answer(question: Question, value: string | boolean | null) {
    if (!data) return;
    // Abschnitt festhalten, damit die Neuberechnung im aktuellen Abschnitt sichtbar bleibt.
    if (!requested && active) navigate(`/a/${id}/profile`, { segment: active });
    const before = new Set(data.segments.flatMap((s) => s.questions.map((q) => q.key)));
    setBusyKey(question.key);
    const update = await run(() => api.patch<ProfileUpdate>(`${base}/profile`, { key: question.key, value }));
    setBusyKey(null);
    if (!update) return;
    apply(update.overview);
    questionnaire.setData(update.questionnaire);
    const appeared = update.questionnaire.segments.flatMap((s) => s.questions)
      .filter((q) => !before.has(q.key)).map((q) => q.key);
    setLastChange({ change: update.change, key: question.key, appeared });
    const extra = appeared.length ? ` ${i18n.t("ui.wizard.new_questions", { count: appeared.length })}` : "";
    announce(changeAnnouncement(i18n, update.change) + extra);
  }

  const goto = (segmentName: string) => navigate(`/a/${id}/profile`, { segment: segmentName });
  const allQuestions = segments.flatMap((s) => s.questions);
  const questionLabel = (key: string) => i18n.local(allQuestions.find((q) => q.key === key)?.text) ?? key;

  return (
    <Page eyebrow={i18n.t("ui.nav.profile")} title={i18n.t("ui.wizard.title")} focusKey="profile"
      lead={<p>{i18n.t("ui.wizard.lead")}</p>}>
      <WriteStateBanner />
      <ActionError />
      {questionnaire.loading && !data && <LoadingState label={i18n.t("ui.state.loading")} />}
      {questionnaire.error && (
        <Banner tone={questionnaire.error.code === "VERSION_MISMATCH" ? "warning" : "error"}
          title={errorMessage(i18n.t, i18n.has, questionnaire.error)}
          action={questionnaire.error.code === "VERSION_MISMATCH" ? undefined
            : <Button variant="secondary" onPress={questionnaire.reload}>{i18n.t("ui.action.retry")}</Button>}>
          {questionnaire.error.code === "VERSION_MISMATCH" ? i18n.t("ui.wizard.mismatch_text") : undefined}
        </Banner>
      )}

      {data && segment && (
        <div className="rx-wizard">
          <aside className="rx-wizard__aside">
            <nav aria-label={i18n.t("ui.wizard.segments")} className="rx-segments">
              <p className="rx-meta rx-segments__summary">
                {i18n.t("ui.wizard.progress", { answered: i18n.number(answered), open: i18n.number(open) })}
              </p>
              <ol role="list" className="rx-segments__list">
                {segments.map((s, position) => {
                  const look = looks.segment(s.status);
                  const current = s.segment === active;
                  return (
                    <li key={s.segment}>
                      <a href={href(`/a/${id}/profile`, { segment: s.segment })} className="rx-segment-link"
                        aria-current={current ? "step" : undefined} data-status={s.status}>
                        <span className="rx-segment-link__index rx-num" aria-hidden="true">{position + 1}</span>
                        <span className="rx-segment-link__body">
                          <span className="rx-segment-link__label">{i18n.t(`ui.wizard.segment.${s.segment}`)}</span>
                          <span className={`rx-status rx-status--${look.tone}`}>
                            <Glyph name={look.glyph} size="sm" />
                            <span>{i18n.t(`ui.wizard.status.${s.status.toLowerCase()}`)}</span>
                          </span>
                          {(s.answered + s.open) > 0 && (
                            <span className="rx-meta rx-num">
                              {i18n.t("ui.wizard.segment_counts", { answered: s.answered, total: s.answered + s.open })}
                            </span>
                          )}
                          {s.outcome_label && <span className="rx-segment-link__outcome">{i18n.local(s.outcome_label)}</span>}
                        </span>
                      </a>
                    </li>
                  );
                })}
              </ol>
            </nav>
            {overview && (
              <section className="rx-card rx-card--flat" aria-labelledby="core-decisions">
                <h2 id="core-decisions" className="rx-subsection-title">{i18n.t("ui.wizard.core_decisions")}</h2>
                <DecisionSummary decisions={overview.decisions} compact />
                <LinkButton href={href(`/a/${id}/classification`)} variant="ghost" icon="chevron">
                  {i18n.t("ui.wizard.to_classification")}
                </LinkButton>
              </section>
            )}
          </aside>

          <section className="rx-wizard__main" aria-labelledby="segment-title">
            <header className="rx-wizard__segment-header">
              <p className="rx-eyebrow">{i18n.t("ui.wizard.segment_position", { index: index + 1, total: segments.length })}</p>
              <h2 id="segment-title" className="rx-section-title">{i18n.t(`ui.wizard.segment.${segment.segment}`)}</h2>
              <p className="rx-body-sm rx-muted rx-reading">{i18n.t(`ui.wizard.segment_desc.${segment.segment}`)}</p>
            </header>

            {lastChange && (
              <section className="rx-recalc rx-enter" aria-labelledby="recalc-title">
                <h3 id="recalc-title" className="rx-subsection-title">
                  <Glyph name="check" /> {i18n.t("ui.wizard.recalc_title", { question: questionLabel(lastChange.key) })}
                </h3>
                {lastChange.change && <ChangeSummary change={lastChange.change} />}
                {lastChange.appeared.length > 0 && (
                  <p className="rx-body-sm">{i18n.t("ui.wizard.new_questions", { count: lastChange.appeared.length })}</p>
                )}
                {lastChange.change && lastChange.change.reactivated_answers.length > 0 && (
                  <LinkButton href={href(`/a/${id}/requirements`, { answer: "REACTIVATED_REVIEW_REQUIRED" })} variant="secondary">
                    {i18n.t("ui.wizard.review_reactivated")}
                  </LinkButton>
                )}
              </section>
            )}

            {segment.questions.length === 0 ? (
              <div className="rx-state">
                <p className="rx-state__title">{i18n.t(`ui.wizard.empty.${segment.status.toLowerCase()}`)}</p>
                {segment.outcome_label && <p className="rx-state__text">{i18n.local(segment.outcome_label)}</p>}
              </div>
            ) : (
              <div className="rx-stack">
                {segment.questions.map((question) => (
                  <QuestionCard key={question.key} question={question} busy={busyKey === question.key}
                    disabled={!editable || (busyKey !== null && busyKey !== question.key)}
                    onAnswer={(value) => answer(question, value)} />
                ))}
              </div>
            )}

            <nav className="rx-wizard__pager" aria-label={i18n.t("ui.wizard.pager")}>
              <Button variant="secondary" icon="back" isDisabled={index <= 0}
                onPress={() => goto(segments[index - 1].segment)}>{i18n.t("ui.wizard.previous")}</Button>
              {index < segments.length - 1 ? (
                <Button variant="primary" onPress={() => goto(segments[index + 1].segment)}>
                  {i18n.t("ui.wizard.next", { segment: i18n.t(`ui.wizard.segment.${segments[index + 1].segment}`) })}
                </Button>
              ) : (
                <Button variant="primary" onPress={() => navigate(`/a/${id}/classification`)}>{i18n.t("ui.wizard.finish")}</Button>
              )}
            </nav>

            {data.stale.length > 0 && (
              <section className="rx-card" aria-labelledby="stale-title">
                <h3 id="stale-title" className="rx-subsection-title">{i18n.t("ui.wizard.stale_title")}</h3>
                <p className="rx-body-sm rx-muted rx-reading">{i18n.t("ui.wizard.stale_text")}</p>
                <ul className="rx-stale" role="list">
                  {data.stale.map((question) => (
                    <li key={question.key} className="rx-stale__item">
                      <div>
                        <p>{i18n.local(question.text) ?? question.key}</p>
                        <p className="rx-meta">{i18n.t("ui.wizard.current_answer", { value: valueLabel(i18n, question, question.answer) })}</p>
                      </div>
                      <Button variant="ghost" isDisabled={!editable || busyKey !== null}
                        onPress={() => answer(question, null)}>{i18n.t("ui.wizard.remove_stale")}</Button>
                    </li>
                  ))}
                </ul>
              </section>
            )}
            {overview && overview.counts.answers_review_required > 0 && (
              <Banner tone="warning" title={i18n.t("ui.wizard.reactivated_title", { count: overview.counts.answers_review_required })}
                action={<LinkButton href={href(`/a/${id}/requirements`, { answer: "REACTIVATED_REVIEW_REQUIRED" })} variant="secondary">
                  {i18n.t("ui.wizard.review_reactivated")}</LinkButton>}>
                {i18n.t("ui.wizard.reactivated_text")}
              </Banner>
            )}
          </section>
        </div>
      )}
    </Page>
  );
}
