/**
 * Gap Lens mit Compliance Matrix (Signature Components): Verteilung der anwendbaren Anforderungen
 * nach Gap-Status und Matrix Themencluster × Lebenszyklusphase. Werte stehen immer als Zahl,
 * Stufen zusätzlich als Muster; Farbe allein trägt keine Bedeutung.
 */

import { useState } from "react";
import { api } from "../../core/api/client";
import type { Counts, Matrix } from "../../core/api/types";
import { useResource } from "../../core/api/useResource";
import { useI18n } from "../../core/i18n/i18n";
import { Glyph } from "../../core/primitives/Glyph";
import { Banner, Button, LoadingState, Segmented } from "../../core/primitives/primitives";
import { href } from "../../core/router/router";
import { Page } from "../shell/AppShell";
import { errorMessage, useAssessment } from "../assessment/AssessmentContext";
import { WriteStateBanner } from "../assessment/AssessmentSection";
import { looks } from "../assessment/status";

const DISTRIBUTION = [
  ["NOT_FULFILLED", "not_fulfilled"], ["PARTIALLY_FULFILLED", "partially_fulfilled"],
  ["EVIDENCE_REVIEW_REQUIRED", "evidence_review_required"], ["NOT_ASSESSED", "not_assessed"], ["FULFILLED", "fulfilled"],
] as const satisfies readonly (readonly [string, keyof Counts])[];

const METRICS = {
  gaps: { query: { gap: "GAPS" } },
  not_assessed: { query: { gap: "NOT_ASSESSED" } },
  unresolved: { query: { applicability: "APPLICABILITY_UNRESOLVED" } },
  applicable: { query: { applicability: "APPLICABLE" } },
} as const;
type Metric = keyof typeof METRICS;

function level(value: number, max: number): number {
  if (value === 0 || max === 0) return 0;
  return Math.min(4, Math.max(1, Math.ceil((value / max) * 4)));
}

function ComplianceMatrix({ matrix }: { matrix: Matrix & { theme_totals: Record<string, Record<string, number>>; phase_totals: Record<string, Record<string, number>> } }) {
  const i18n = useI18n();
  const { id } = useAssessment();
  const [metric, setMetric] = useState<Metric>("gaps");
  const cell = (theme: string, phase: string) => matrix.cells.find((c) => c.theme === theme && c.phase === phase)!;
  const max = Math.max(0, ...matrix.cells.map((c) => c[metric]));
  const link = (query: Record<string, string>) => href(`/a/${id}/requirements`, { ...METRICS[metric].query, ...query });
  return (
    <section className="rx-section" aria-labelledby="matrix-title">
      <div className="rx-section__header">
        <h2 id="matrix-title" className="rx-section-title">{i18n.t("ui.matrix.title")}</h2>
        <Segmented label={i18n.t("ui.matrix.metric")} value={metric} onChange={setMetric}
          options={(Object.keys(METRICS) as Metric[]).map((key) => ({ value: key, label: i18n.t(`ui.matrix.metric_${key}`) }))} />
      </div>
      <p className="rx-body-sm rx-muted rx-reading">{i18n.t("ui.matrix.lead")}</p>
      <div className="rx-table-wrap rx-matrix-wrap" tabIndex={0} role="region" aria-labelledby="matrix-caption">
        <table className="rx-table rx-matrix">
          <caption id="matrix-caption">{i18n.t("ui.matrix.caption", { metric: i18n.t(`ui.matrix.metric_${metric}`) })}</caption>
          <thead>
            <tr>
              <th scope="col">{i18n.t("col.theme")}</th>
              {matrix.phases.map((phase) => <th key={phase} scope="col">{i18n.phase(phase)}</th>)}
              <th scope="col" className="rx-num">{i18n.t("col.short.total")}</th>
            </tr>
          </thead>
          <tbody>
            {matrix.themes.map((theme) => (
              <tr key={theme}>
                <th scope="row">{i18n.theme(theme)}</th>
                {matrix.phases.map((phase) => {
                  const c = cell(theme, phase);
                  const value = c[metric];
                  return (
                    <td key={phase} className={`rx-matrix__cell rx-matrix__cell--${metric}`} data-level={level(value, max)}>
                      {c.total === 0 ? <span className="rx-matrix__empty" aria-label={i18n.t("ui.matrix.no_requirements")}>–</span> : (
                        <a href={link({ theme, phase })} className="rx-matrix__link"
                          aria-label={i18n.t("ui.matrix.cell_label", { value, total: c.total, metric: i18n.t(`ui.matrix.metric_${metric}`), theme: i18n.theme(theme), phase: i18n.phase(phase) })}>
                          <span className="rx-matrix__value rx-num">{i18n.number(value)}</span>
                          <span className="rx-matrix__total rx-num" aria-hidden="true">/{i18n.number(c.total)}</span>
                        </a>
                      )}
                    </td>
                  );
                })}
                <td className="rx-num"><a href={link({ theme })}>{i18n.number(matrix.theme_totals[theme]?.[metric] ?? 0)}</a></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <p className="rx-meta">{i18n.t("ui.matrix.legend")}</p>
    </section>
  );
}

export function GapLensView() {
  const i18n = useI18n();
  const { overview, base, id } = useAssessment();
  const matrix = useResource(() => api.get<Matrix & { theme_totals: Record<string, Record<string, number>>; phase_totals: Record<string, Record<string, number>> }>(`${base}/matrix`),
    [base, overview?.fingerprint]);
  if (!overview) return null;
  const counts = overview.counts;
  const applicable = counts.applicable;
  return (
    <Page eyebrow={i18n.t("ui.nav.gaps")} title={i18n.t("ui.gaps.title")} focusKey="gaps"
      lead={<p>{i18n.t("gap_summary.lead")}</p>}>
      <WriteStateBanner />
      <section className="rx-section" aria-labelledby="lens-title">
        <h2 id="lens-title" className="rx-section-title">{i18n.t("ui.gaps.lens_title")}</h2>
        <dl className="rx-figures">
          {([["applicable", "applicable"], ["gaps", "not_fulfilled"], ["not_assessed", "not_assessed"],
            ["evidence_review_required", "review"], ["unresolved", "unresolved"], ["answers_review_required", "review"]] as const).map(([key, tone]) => (
            <div key={key} className={`rx-figure rx-figure--${tone}`}>
              <dt>{i18n.t(`figure.${key}`)}</dt>
              <dd>{i18n.number(counts[key])}</dd>
            </div>
          ))}
        </dl>
        {applicable === 0 ? (
          <Banner tone="unresolved" title={i18n.t("ui.gaps.none_applicable")}
            action={<a className="rx-button rx-button--secondary" href={href(`/a/${id}/profile`)}>{i18n.t("ui.gaps.to_profile")}</a>}>
            {i18n.t("ui.gaps.none_applicable_text")}
          </Banner>
        ) : (
          <figure className="rx-distribution">
            <figcaption className="rx-subsection-title">{i18n.t("gap_summary.distribution_caption")}</figcaption>
            <div className="rx-distribution__bar" aria-hidden="true">
              {DISTRIBUTION.map(([code, key]) => counts[key] > 0 && (
                <span key={code} className={`rx-distribution__part rx-distribution__part--${looks.gap(code).tone}`}
                  style={{ flexGrow: counts[key] }} />
              ))}
            </div>
            <ul className="rx-distribution__legend" role="list">
              {DISTRIBUTION.map(([code, key]) => (
                <li key={code}>
                  <a href={href(`/a/${id}/requirements`, { gap: code })} className="rx-distribution__item">
                    <span className={`rx-distribution__swatch rx-distribution__part--${looks.gap(code).tone}`} aria-hidden="true" />
                    <Glyph name={looks.gap(code).glyph} size="sm" />
                    <span>{i18n.code("gap_result", code)}</span>
                    <span className="rx-num rx-distribution__count">{i18n.number(counts[key])}</span>
                    <span className="rx-meta rx-num">{i18n.percent(counts[key], applicable)}</span>
                  </a>
                </li>
              ))}
            </ul>
          </figure>
        )}
        <p className="rx-meta rx-reading">{i18n.t("gap_summary.note")}</p>
      </section>
      {matrix.loading && !matrix.data && <LoadingState label={i18n.t("ui.state.loading")} />}
      {matrix.error && <Banner tone="error" title={errorMessage(i18n.t, i18n.has, matrix.error)}
        action={<Button variant="secondary" onPress={matrix.reload}>{i18n.t("ui.action.retry")}</Button>} />}
      {matrix.data && <ComplianceMatrix matrix={matrix.data} />}
    </Page>
  );
}
