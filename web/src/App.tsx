/**
 * Anwendungsrahmen: lädt Sprachpaket und Stammdaten über die Anwendungs-API, stellt Präferenzen,
 * i18n, Ansagen und Fehlergrenze bereit und ordnet Routen den Ansichten zu.
 */

import { Component, useEffect, useState, type ErrorInfo, type ReactNode } from "react";
import { I18nProvider as AriaI18nProvider } from "react-aria-components";
import { api } from "./core/api/client";
import type { I18nBundle, Lang } from "./core/api/types";
import { AnnouncerProvider } from "./core/a11y/announcer";
import { I18nProvider, useI18n } from "./core/i18n/i18n";
import { PreferencesProvider, usePreferences } from "./core/preferences/preferences";
import { Banner, Button } from "./core/primitives/primitives";
import { navigate, useRoute } from "./core/router/router";
import { AppDataProvider, type AppMeta } from "./domain/app/AppData";
import { AssessmentProvider } from "./domain/assessment/AssessmentContext";
import { AppShell, Page } from "./domain/shell/AppShell";
import { SECTIONS, type SectionKey } from "./domain/shell/navigation";
import { StartView } from "./domain/start/StartView";
import { PreferencesView } from "./domain/preferences/PreferencesView";
import { AssessmentSection } from "./domain/assessment/AssessmentSection";

// Einzige Texte außerhalb der zentralen Ressourcen: Meldung, falls das Sprachpaket selbst nicht
// geladen werden kann (ohne Sprachpaket gibt es keine andere Textquelle).
const BOOT_FAILURE: Record<Lang, { title: string; text: string; retry: string }> = {
  de: { title: "RegScoutX ist nicht erreichbar", text: "Die lokale Anwendungs-API antwortet nicht. Bitte den lokalen Server starten und erneut versuchen.", retry: "Erneut versuchen" },
  en: { title: "RegScoutX is not reachable", text: "The local application API does not respond. Please start the local server and try again.", retry: "Try again" },
};

const LOCALES: Record<Lang, string> = { de: "de-DE", en: "en-GB" };

class ErrorBoundary extends Component<{ fallback: (reset: () => void) => ReactNode; children: ReactNode }, { failed: boolean }> {
  override state = { failed: false };
  static getDerivedStateFromError() {
    return { failed: true };
  }
  override componentDidCatch(error: Error, info: ErrorInfo) {
    if (import.meta.env.DEV) console.error(error, info.componentStack);
  }
  override render() {
    return this.state.failed ? this.props.fallback(() => this.setState({ failed: false })) : this.props.children;
  }
}

function RenderFailure({ reset }: { reset: () => void }) {
  const { t } = useI18n();
  return (
    <Banner tone="error" title={t("ui.error.render_title")}
      action={<Button variant="secondary" onPress={reset}>{t("ui.action.retry")}</Button>}>
      {t("ui.error.render_text")}
    </Banner>
  );
}

function NotFound() {
  const { t } = useI18n();
  return (
    <Page title={t("ui.not_found.title")} focusKey="not-found" lead={t("ui.not_found.text")}
      actions={<Button variant="primary" onPress={() => navigate("/")}>{t("ui.nav.start")}</Button>}>
      <span />
    </Page>
  );
}

function Routes() {
  const route = useRoute();
  const [first, id, section] = route.path;
  if (first === undefined) {
    return <AppShell section={null} view="start"><StartView /></AppShell>;
  }
  if (first === "preferences" && id === undefined) {
    return <AppShell section={null} view="preferences"><PreferencesView /></AppShell>;
  }
  if (first === "a" && id && /^[0-9a-f-]{36}$/.test(id)) {
    const known = SECTIONS.some((s) => s.key === section);
    if (!known) {
      if (section === undefined) navigate(`/a/${id}/profile`);
      return (
        <AssessmentProvider key={id} id={id}>
          <AppShell section={null} view="assessment">{section === undefined ? null : <NotFound />}</AppShell>
        </AssessmentProvider>
      );
    }
    return (
      <AssessmentProvider key={id} id={id}>
        <AppShell section={section as SectionKey} view="assessment">
          <AssessmentSection section={section as SectionKey} />
        </AppShell>
      </AssessmentProvider>
    );
  }
  return <AppShell section={null} view="start"><NotFound /></AppShell>;
}

function Localised() {
  const { preferences } = usePreferences();
  const [bundle, setBundle] = useState<I18nBundle | null>(null);
  const [meta, setMeta] = useState<AppMeta | null>(null);
  const [failed, setFailed] = useState(false);
  const [attempt, setAttempt] = useState(0);
  useEffect(() => {
    let active = true;
    setFailed(false);
    Promise.all([api.get<I18nBundle>(`/i18n/${preferences.language}`), api.get<AppMeta>("/meta")]).then(
      ([nextBundle, nextMeta]) => { if (active) { setBundle(nextBundle); setMeta(nextMeta); } },
      () => { if (active) setFailed(true); },
    );
    return () => { active = false; };
  }, [preferences.language, attempt]);

  if (failed && !bundle) {
    const text = BOOT_FAILURE[preferences.language];
    return (
      <main className="rx-boot" id="main-content">
        <Banner tone="error" title={text.title}
          action={<Button variant="secondary" onPress={() => setAttempt((n) => n + 1)}>{text.retry}</Button>}>
          {text.text}
        </Banner>
      </main>
    );
  }
  if (!bundle || !meta) {
    return <div className="rx-boot" role="status" aria-busy="true"><span className="rx-spinner" /></div>;
  }
  return (
    <I18nProvider bundle={bundle}>
      <AriaI18nProvider locale={LOCALES[bundle.language]}>
        <AppDataProvider meta={meta}>
          <AnnouncerProvider>
            <ErrorBoundary fallback={(reset) => <div className="rx-boot"><RenderFailure reset={reset} /></div>}>
              <Routes />
            </ErrorBoundary>
          </AnnouncerProvider>
        </AppDataProvider>
      </AriaI18nProvider>
    </I18nProvider>
  );
}

export function App() {
  return (
    <PreferencesProvider>
      <Localised />
    </PreferencesProvider>
  );
}
