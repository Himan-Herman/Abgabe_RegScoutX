/**
 * Lifecycle Ribbon (Signature Component): alle kontrollierten Lebenszyklusphasen in Reihenfolge;
 * zugeordnete Phasen sind gefüllt und textlich markiert (nicht nur farbig).
 */

import { useI18n } from "../../core/i18n/i18n";
import { Glyph } from "../../core/primitives/Glyph";

export function LifecycleRibbon({ phases }: { phases: string[] }) {
  const i18n = useI18n();
  const assigned = new Set(phases);
  return (
    <ol className="rx-ribbon" role="list" aria-label={i18n.t("field.lifecycle")}>
      {i18n.phaseOrder.map((phase) => {
        const on = assigned.has(phase);
        return (
          <li key={phase} className="rx-ribbon__phase" data-assigned={on || undefined}>
            <span className="rx-ribbon__mark" aria-hidden="true">{on && <Glyph name="check" size="sm" />}</span>
            <span className="rx-ribbon__label">{i18n.phase(phase)}</span>
            <span className="rx-visually-hidden">{i18n.t(on ? "ui.ribbon.assigned" : "ui.ribbon.not_assigned")}</span>
          </li>
        );
      })}
    </ol>
  );
}
