/**
 * Einordnung und Anwendbarkeit: Entscheidungsbereiche mit Ergebnis, Regeln und offenen Prüfpunkten
 * sowie die Anwendbarkeitsblöcke mit Zustand und Zählung. Alles stammt aus dem gespeicherten Stand.
 */

import type { Decision } from "../../core/api/types";
import { useI18n } from "../../core/i18n/i18n";
import { Banner, Disclosure, LinkButton, StatusTag } from "../../core/primitives/primitives";
import { href } from "../../core/router/router";
import { Page } from "../shell/AppShell";
import { useAssessment } from "../assessment/AssessmentContext";
import { WriteStateBanner } from "../assessment/AssessmentSection";
import { looks } from "../assessment/status";

function DecisionCard({ decision }: { decision: Decision }) {
  const i18n = useI18n();
  const { id } = useAssessment();
  const look = looks.decision(decision.status);
  return (
    <article className="rx-card rx-decision-card" aria-labelledby={`decision-${decision.area}`}>
      <header className="rx-stack rx-stack--tight">
        <h3 id={`decision-${decision.area}`} className="rx-subsection-title">{i18n.code("decision_area", decision.area)}</h3>
        <StatusTag {...look}>{i18n.code("decision_status", decision.status)}</StatusTag>
      </header>
      {decision.outcome ? (
        <p className="rx-decision-card__outcome">
          {i18n.local(decision.outcome_label) ?? decision.outcome}
          {decision.mdr_class && <span className="rx-meta"> · {i18n.t("classification.mdr_class", { mdr_class: decision.mdr_class })}</span>}
        </p>
      ) : (
        <p className="rx-muted rx-body-sm">{i18n.t(`ui.classification.no_outcome.${decision.status.toLowerCase()}`)}</p>
      )}
      {decision.applicable_from && (
        <p className="rx-meta">{i18n.t("classification.applicable_from", { date: i18n.date(decision.applicable_from) })}</p>
      )}
      {decision.missing_input && (
        <Banner tone="unresolved" title={i18n.t("ui.classification.missing_title")}
          action={<LinkButton variant="secondary" href={href(`/a/${id}/profile`)}>{i18n.t("ui.classification.answer")}</LinkButton>}>
          {i18n.t("classification.missing_input", {
            rule: decision.missing_input[0], key: decision.missing_input[1],
            question: i18n.local(decision.missing_question) ?? "",
          })}
        </Banner>
      )}
      {decision.reviews && decision.reviews.length > 0 && (
        <ul className="rx-stack rx-stack--tight" role="list">
          {decision.reviews.map((review) => (
            <li key={`${review.rule_id}-${review.output}`}>
              <StatusTag tone="review" glyph="attention" variant="plain">{i18n.t("ui.classification.review")}</StatusTag>{" "}
              <span className="rx-body-sm">{i18n.t("classification.review", { rule: review.rule_id, cause: i18n.local(review.cause) ?? review.output })}</span>
            </li>
          ))}
        </ul>
      )}
      {decision.rules.length > 0 && (
        <Disclosure title={i18n.t("classification.rules_caption")} meta={i18n.number(decision.rules.length)}>
          <ul className="rx-rule-list" role="list">
            {decision.rules.map((rule) => (
              <li key={rule.rule_id}>
                <span className="rx-code">{rule.rule_id}</span>
                {rule.primary_legal_anchor && rule.primary_legal_anchor.length > 0 && (
                  <span className="rx-meta"> · {i18n.t("col.primary_legal_anchor")}: <span className="rx-code">{rule.primary_legal_anchor.join(", ")}</span></span>
                )}
                {rule.guidance_anchor && rule.guidance_anchor.length > 0 && (
                  <span className="rx-meta"> · {i18n.t("col.guidance_anchor")}: <span className="rx-code">{rule.guidance_anchor.join(", ")}</span></span>
                )}
              </li>
            ))}
          </ul>
        </Disclosure>
      )}
    </article>
  );
}

export function ClassificationView() {
  const i18n = useI18n();
  const { overview, id } = useAssessment();
  if (!overview) return null;
  const counts = overview.counts;
  const decisions = [...overview.decisions].sort((a, b) => a.area.localeCompare(b.area));
  const figures = [
    ["applicable", "applicable", counts.applicable],
    ["unresolved", "unresolved", counts.unresolved],
    ["not_applicable", "not_applicable", counts.not_applicable],
  ] as const;
  return (
    <Page eyebrow={i18n.t("ui.nav.classification")} title={i18n.t("ui.classification.title")} focusKey="classification"
      lead={<p>{i18n.t("classification.lead")}</p>}>
      <WriteStateBanner />
      <section className="rx-section" aria-labelledby="decisions-title">
        <h2 id="decisions-title" className="rx-section-title">{i18n.t("classification.caption")}</h2>
        {decisions.length === 0 ? <p className="rx-muted">{i18n.t("empty.decisions")}</p> : (
          <div className="rx-grid">{decisions.map((d) => <DecisionCard key={d.area} decision={d} />)}</div>
        )}
      </section>

      <section className="rx-section" aria-labelledby="applicability-title">
        <div className="rx-section__header">
          <h2 id="applicability-title" className="rx-section-title">{i18n.t("ui.classification.applicability_title")}</h2>
          <p className="rx-meta">{i18n.t("ui.classification.total", { count: i18n.number(counts.total) })}</p>
        </div>
        <dl className="rx-figures">
          {figures.map(([key, tone, value]) => (
            <div key={key} className={`rx-figure rx-figure--${tone}`}>
              <dt>{i18n.t(`figure.${key}`)}</dt>
              <dd>{i18n.number(value)}</dd>
            </div>
          ))}
        </dl>
        {counts.unresolved > 0 && (
          <Banner tone="unresolved" title={i18n.t("ui.classification.unresolved_title", { count: i18n.number(counts.unresolved) })}>
            {i18n.t("ui.classification.unresolved_text")}
          </Banner>
        )}
        <div className="rx-table-wrap">
          <table className="rx-table">
            <caption>{i18n.t("ui.classification.blocks_caption")}</caption>
            <thead>
              <tr>
                <th scope="col">{i18n.t("ui.classification.block")}</th>
                <th scope="col">{i18n.t("col.state")}</th>
                <th scope="col" className="rx-num">{i18n.t("col.short.applicable")}</th>
                <th scope="col" className="rx-num">{i18n.t("col.short.unresolved")}</th>
                <th scope="col" className="rx-num">{i18n.t("col.short.not_applicable")}</th>
              </tr>
            </thead>
            <tbody>
              {overview.blocks.map((block) => (
                <tr key={block.block}>
                  <th scope="row">
                    <a href={href(`/a/${id}/requirements`, { block: block.block })}>{i18n.local(block.description)}</a>
                    <div className="rx-code">{block.block}</div>
                  </th>
                  <td><StatusTag {...looks.block(block.state)}>{i18n.t(`ui.block_state.${block.state.toLowerCase()}`)}</StatusTag></td>
                  <td className="rx-num">{i18n.number(block.counts.applicable ?? 0)}</td>
                  <td className="rx-num">{i18n.number(block.counts.unresolved ?? 0)}</td>
                  <td className="rx-num">{i18n.number(block.counts.not_applicable ?? 0)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </Page>
  );
}
