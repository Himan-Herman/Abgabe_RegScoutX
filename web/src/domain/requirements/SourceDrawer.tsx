/**
 * Source Drawer (Signature Component): Quellenlokatoren einer Anforderung mit Registerkennung,
 * Kurzbezeichnung aus dem Quellenregister und Fundstelle. Lokatoren sind Katalogkennungen in der
 * Notation des Quellenregisters und werden nicht übersetzt; es werden keine Quelltexte angezeigt.
 */

import { useI18n } from "../../core/i18n/i18n";
import { Drawer } from "../../core/primitives/primitives";
import { useAppData } from "../app/AppData";

function SourceList({ title, locators }: { title: string; locators: string[] }) {
  const i18n = useI18n();
  const { sources } = useAppData();
  return (
    <section className="rx-stack rx-stack--tight">
      <h3 className="rx-subsection-title">{title}</h3>
      {locators.length === 0 ? <p className="rx-muted">{i18n.t("value.none")}</p> : (
        <ul className="rx-sources" role="list">
          {locators.map((locator) => {
            const [source, path = ""] = locator.split("#");
            return (
              <li key={locator} className="rx-sources__item">
                <p><span className="rx-code">{source}</span> · <span lang="de">{sources[source] ?? source}</span></p>
                {path && <p className="rx-meta">{i18n.t("ui.sources.locator")}: <span className="rx-code">{path}</span></p>}
              </li>
            );
          })}
        </ul>
      )}
    </section>
  );
}

export function SourceDrawer({ isOpen, onOpenChange, requirementId, primary, supplementary }:
  { isOpen: boolean; onOpenChange: (open: boolean) => void; requirementId: string; primary: string[]; supplementary: string[] }) {
  const i18n = useI18n();
  return (
    <Drawer isOpen={isOpen} onOpenChange={onOpenChange} closeLabel={i18n.t("ui.action.close")}
      title={i18n.t("ui.sources.title", { id: requirementId })}>
      <div className="rx-stack">
        <p className="rx-body-sm rx-muted">{i18n.t("ui.sources.note")}</p>
        <SourceList title={i18n.t("field.primary_sources")} locators={primary} />
        <SourceList title={i18n.t("field.supplementary_sources")} locators={supplementary} />
      </div>
    </Drawer>
  );
}
