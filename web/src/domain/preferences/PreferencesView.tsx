/**
 * Darstellung und Bedienung: Präferenzen wirken nur auf die Darstellung, werden lokal
 * gespeichert und nie an die Anwendungs-API übertragen (kein Einfluss auf Fingerprint,
 * Anwendbarkeit, Gap-Status oder Audit).
 */

import { useI18n } from "../../core/i18n/i18n";
import { Segmented } from "../../core/primitives/primitives";
import { PREFERENCE_OPTIONS, usePreferences, type Preferences } from "../../core/preferences/preferences";
import { Page } from "../shell/AppShell";

const ORDER: (keyof Preferences)[] = ["language", "theme", "contrast", "textSize", "motion", "density"];

export function PreferencesView() {
  const i18n = useI18n();
  const { preferences, setPreference } = usePreferences();
  return (
    <Page eyebrow={i18n.t("ui.nav.preferences")} title={i18n.t("ui.preferences.title")} focusKey="preferences"
      lead={<p>{i18n.t("ui.preferences.lead")}</p>}>
      <div className="rx-preferences">
        {ORDER.map((key) => {
          const slug = key.replace(/[A-Z]/g, (c) => `_${c.toLowerCase()}`);
          return (
          <section key={key} className="rx-card rx-preference">
            <Segmented label={i18n.t(`ui.preferences.${slug}.label`)} description={i18n.t(`ui.preferences.${slug}.description`)}
              value={preferences[key]}
              onChange={(value) => setPreference(key, value as never)}
              options={(PREFERENCE_OPTIONS[key] as readonly string[]).map((option) => ({
                value: option, label: key === "language" ? i18n.t(`language.${option}`) : i18n.t(`ui.preferences.${slug}.${option}`),
              }))} />
          </section>
          );
        })}
      </div>
      <p className="rx-meta rx-reading">{i18n.t("ui.preferences.storage_note")}</p>
    </Page>
  );
}
