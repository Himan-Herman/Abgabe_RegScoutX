/**
 * i18n (Shared Product Core): nutzt dieselben zentralen Sprachressourcen wie der Bericht
 * (regscoutx/resources/i18n, über /api/i18n/<sprache>), Code-Bezeichnungen aus DATA_MODEL und
 * Vokabular. Keine zweite Übersetzungsarchitektur, keine Fallback-Mischsprache: ein fehlender
 * Schlüssel wird sichtbar markiert und in Tests geprüft.
 */

import { createContext, useContext, useMemo, type ReactNode } from "react";
import type { I18nBundle, Lang, Localized } from "../api/types";

const LOCALES: Record<Lang, string> = { de: "de-DE", en: "en-GB" };

export interface I18n {
  lang: Lang;
  locale: string;
  t(key: string, params?: Record<string, string | number>): string;
  has(key: string): boolean;
  code(enumName: string, code: string | null | undefined): string;
  theme(code: string): string;
  phase(code: string): string;
  local(value: Localized | null | undefined): string | null;
  number(value: number): string;
  percent(part: number, total: number): string;
  date(iso: string | null | undefined): string;
  dateTime(iso: string | null | undefined): string;
  list(items: string[]): string;
  themeOrder: string[];
  phaseOrder: string[];
}

export function createI18n(bundle: I18nBundle): I18n {
  const lang = bundle.language;
  const locale = LOCALES[lang];
  const numbers = new Intl.NumberFormat(locale);
  const percents = new Intl.NumberFormat(locale, { style: "percent", maximumFractionDigits: 1 });
  const dates = new Intl.DateTimeFormat(locale, { dateStyle: "medium" });
  const dateTimes = new Intl.DateTimeFormat(locale, { dateStyle: "medium", timeStyle: "short" });
  const lists = new Intl.ListFormat(locale, { style: "long", type: "conjunction" });
  const missing = (key: string) => {
    if (import.meta.env.DEV) console.error(`i18n: missing key ${key}`);
    return `⟦${key}⟧`;
  };
  return {
    lang,
    locale,
    t(key, params) {
      const template = bundle.messages[key];
      if (template === undefined) return missing(key);
      return template.replace(/\{(\w+)\}/g, (_, name: string) =>
        params && name in params ? String(params[name]) : `{${name}}`);
    },
    has: (key) => key in bundle.messages,
    code(enumName, code) {
      if (code === null || code === undefined) return bundle.messages["value.none"] ?? "";
      return bundle.enums[enumName]?.[code] ?? missing(`${enumName}.${code}`);
    },
    theme: (code) => bundle.themes[code] ?? code,
    phase: (code) => bundle.phases[code] ?? code,
    local: (value) => (value ? value[lang] : null),
    number: (value) => numbers.format(value),
    percent: (part, total) => (total ? percents.format(part / total) : "–"),
    date: (iso) => (iso ? dates.format(new Date(iso.length === 10 ? `${iso}T00:00:00` : iso)) : ""),
    dateTime: (iso) => (iso ? dateTimes.format(new Date(iso)) : ""),
    list: (items) => lists.format(items),
    themeOrder: bundle.theme_order,
    phaseOrder: bundle.phase_order,
  };
}

const I18nContext = createContext<I18n | null>(null);

export function I18nProvider({ bundle, children }: { bundle: I18nBundle; children: ReactNode }) {
  const value = useMemo(() => createI18n(bundle), [bundle]);
  return <I18nContext.Provider value={value}>{children}</I18nContext.Provider>;
}

export function useI18n(): I18n {
  const value = useContext(I18nContext);
  if (!value) throw new Error("I18nProvider missing");
  return value;
}
