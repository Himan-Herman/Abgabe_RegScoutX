/**
 * Darstellungspräferenzen und Theme Engine (Shared Product Core).
 * Präferenzen werden lokal und getrennt von Bewertungsdaten gespeichert und wirken nur auf die
 * Darstellung (UI_UX_DESIGN_SYSTEM.md 12.1, 17.1); sie gehen nie an die Anwendungs-API.
 */

import { createContext, useCallback, useContext, useEffect, useLayoutEffect, useMemo, useState, type ReactNode } from "react";
import type { Lang } from "../api/types";
import { platform } from "../platform/platform";
import { palettes, type PaletteName } from "../../experience/regscoutx/palette";

export interface Preferences {
  theme: "system" | "light" | "dark";
  textSize: "default" | "large" | "xlarge";
  contrast: "standard" | "high";
  motion: "system" | "normal" | "reduced";
  density: "comfortable" | "compact";
  language: Lang;
}

export const PREFERENCE_OPTIONS = {
  theme: ["system", "light", "dark"],
  textSize: ["default", "large", "xlarge"],
  contrast: ["standard", "high"],
  motion: ["system", "normal", "reduced"],
  density: ["comfortable", "compact"],
  language: ["de", "en"],
} as const satisfies { [K in keyof Preferences]: readonly Preferences[K][] };

const DEFAULTS: Preferences = {
  theme: "system", textSize: "default", contrast: "standard", motion: "system",
  density: "comfortable", language: "de",
};

function load(): Preferences {
  const result = { ...DEFAULTS };
  for (const key of Object.keys(DEFAULTS) as (keyof Preferences)[]) {
    const stored = platform().readPreference(key);
    if (stored && (PREFERENCE_OPTIONS[key] as readonly string[]).includes(stored)) {
      (result as Record<string, string>)[key] = stored;
    }
  }
  return result;
}

function toKebab(name: string): string {
  return name.replace(/[A-Z]/g, (c) => `-${c.toLowerCase()}`);
}

/** Überträgt die Palette als CSS-Variablen (CSSOM, CSP-konform) und setzt Datenattribute. */
export function applyAppearance(prefs: Preferences, systemDark: boolean): PaletteName {
  const dark = prefs.theme === "dark" || (prefs.theme === "system" && systemDark);
  const name: PaletteName = `${dark ? "dark" : "light"}${prefs.contrast === "high" ? "HighContrast" : ""}` as PaletteName;
  const root = document.documentElement;
  for (const [token, value] of Object.entries(palettes[name])) {
    root.style.setProperty(`--color-${toKebab(token)}`, value);
  }
  root.dataset.theme = dark ? "dark" : "light";
  root.dataset.contrast = prefs.contrast;
  root.dataset.textSize = prefs.textSize;
  root.dataset.density = prefs.density;
  root.dataset.motion = prefs.motion;
  root.lang = prefs.language;
  root.style.colorScheme = dark ? "dark" : "light";
  return name;
}

interface PreferencesContextValue {
  preferences: Preferences;
  setPreference<K extends keyof Preferences>(key: K, value: Preferences[K]): void;
}

const PreferencesContext = createContext<PreferencesContextValue | null>(null);

export function PreferencesProvider({ children }: { children: ReactNode }) {
  const [preferences, setPreferences] = useState<Preferences>(load);
  const [systemDark, setSystemDark] = useState(() => platform().prefersDark());
  useEffect(() => platform().onPrefersDarkChange(setSystemDark), []);
  // Vor dem ersten Zeichnen anwenden, damit keine ungestaltete Darstellung aufblitzt.
  useLayoutEffect(() => {
    applyAppearance(preferences, systemDark);
  }, [preferences, systemDark]);
  const setPreference = useCallback(<K extends keyof Preferences>(key: K, value: Preferences[K]) => {
    platform().writePreference(key, String(value));
    setPreferences((previous) => ({ ...previous, [key]: value }));
  }, []);
  const value = useMemo(() => ({ preferences, setPreference }), [preferences, setPreference]);
  return <PreferencesContext.Provider value={value}>{children}</PreferencesContext.Provider>;
}

export function usePreferences(): PreferencesContextValue {
  const value = useContext(PreferencesContext);
  if (!value) throw new Error("PreferencesProvider missing");
  return value;
}
