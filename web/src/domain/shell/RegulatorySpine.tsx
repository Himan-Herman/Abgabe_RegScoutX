/**
 * Regulatory Spine (Signature Component): der fachliche Verlauf einer Bewertung von Profil bis
 * Bericht als geordnete Stationen. Zustand je Station durch Form, Text und Zahl; Farbe ergänzt nur.
 * Die Zustände berechnet der Kern (assessment_views.spine); hier wird nur dargestellt.
 */

import type { SpineStage } from "../../core/api/types";
import { Glyph } from "../../core/primitives/Glyph";
import { href } from "../../core/router/router";
import { useI18n } from "../../core/i18n/i18n";
import { looks } from "../assessment/status";
import { STAGE_SECTION, sectionPath, type SectionKey } from "./navigation";

export function RegulatorySpine({ stages, assessmentId, current }:
  { stages: SpineStage[]; assessmentId: string; current: SectionKey | null }) {
  const i18n = useI18n();
  const complete = stages.filter((s) => s.state === "COMPLETE").length;
  // Mehrere Stationen können zur selben Ansicht führen; als aktuell gilt nur die erste.
  const currentStage = stages.find((s) => STAGE_SECTION[s.stage] === current)?.stage ?? null;
  return (
    <nav className="rx-spine" aria-label={i18n.t("spine.caption")}>
      <p className="rx-spine__summary rx-meta">
        {i18n.t("ui.spine.summary", { complete, total: stages.length })}
      </p>
      <ol className="rx-spine__list" role="list">
        {stages.map((stage) => {
          const look = looks.spine(stage.state);
          const section = STAGE_SECTION[stage.stage];
          const isCurrent = stage.stage === currentStage;
          return (
            <li key={stage.stage} className={`rx-spine__stage rx-spine__stage--${stage.state.toLowerCase()}`}
              data-current={isCurrent || undefined}>
              <a className="rx-spine__link" href={href(sectionPath(assessmentId, section))}
                aria-current={isCurrent ? "step" : undefined}>
                <span className={`rx-spine__mark rx-status--${look.tone}`}><Glyph name={look.glyph} size="sm" /></span>
                <span className="rx-spine__text">
                  <span className="rx-spine__label">{i18n.t(`spine.${stage.stage.toLowerCase()}`)}</span>
                  <span className="rx-spine__value rx-num">
                    {stage.total === null ? i18n.number(stage.value)
                      : i18n.t("value.part_of_total", { part: i18n.number(stage.value), total: i18n.number(stage.total) })}
                  </span>
                  <span className="rx-visually-hidden">{i18n.t(`ui.spine.state.${stage.state.toLowerCase()}`)}</span>
                </span>
              </a>
            </li>
          );
        })}
      </ol>
    </nav>
  );
}
