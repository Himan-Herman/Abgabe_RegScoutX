/**
 * App Shell (Domain UI): Navigationsleiste (Rail), Kontextkopf mit Regulatory Spine,
 * Arbeitsbereich und auf schmalen Bildschirmen eine untere Navigation mit Safe Areas.
 * Fokus und Seitentitel werden bei jedem Ansichtswechsel geführt.
 */

import { useEffect, useRef, useState, type ReactNode } from "react";
import { Glyph, type GlyphName } from "../../core/primitives/Glyph";
import { Drawer, StatusTag } from "../../core/primitives/primitives";
import { href } from "../../core/router/router";
import { useI18n } from "../../core/i18n/i18n";
import { useOptionalAssessment } from "../assessment/AssessmentContext";
import { looks, shortId } from "../assessment/status";
import { RegulatorySpine } from "./RegulatorySpine";
import { SECTIONS, sectionPath, type SectionKey } from "./navigation";

interface NavItem {
  key: string;
  label: string;
  glyph: GlyphName;
  to: string;
  current: boolean;
}

function NavLink({ item, variant }: { item: NavItem; variant: "rail" | "bottom" | "list" }) {
  return (
    <a className={`rx-nav-link rx-nav-link--${variant}`} href={href(item.to)}
      aria-current={item.current ? "page" : undefined}>
      <Glyph name={item.glyph} />
      <span className="rx-nav-link__label">{item.label}</span>
    </a>
  );
}

export function AppShell({ section, view, children }:
  { section: SectionKey | null; view: "start" | "preferences" | "assessment"; children: ReactNode }) {
  const { t, code } = useI18n();
  const assessment = useOptionalAssessment();
  const [moreOpen, setMoreOpen] = useState(false);
  const overview = assessment?.overview ?? null;

  const start: NavItem = { key: "start", label: t("ui.nav.start"), glyph: "home", to: "/", current: view === "start" };
  const preferences: NavItem = {
    key: "preferences", label: t("ui.nav.preferences"), glyph: "settings", to: "/preferences",
    current: view === "preferences",
  };
  const sections: NavItem[] = assessment ? SECTIONS.map((s) => ({
    key: s.key, label: t(`ui.nav.${s.key}`), glyph: s.glyph, to: sectionPath(assessment.id, s.key),
    current: section === s.key,
  })) : [];
  const bottomKeys = ["profile", "requirements", "gaps"];
  const bottom = assessment ? sections.filter((s) => bottomKeys.includes(s.key)) : [preferences];
  const more = assessment ? [...sections.filter((s) => !bottomKeys.includes(s.key)), preferences] : [];

  useEffect(() => setMoreOpen(false), [section, view]);

  return (
    <div className="rx-app">
      <a className="rx-skip-link" href="#main-content" onClick={(event) => {
        event.preventDefault();
        document.getElementById("main-content")?.focus();
      }}>{t("ui.shell.skip_to_content")}</a>
      <nav className="rx-rail" aria-label={t("ui.shell.navigation")}>
        <a className="rx-rail__brand" href={href("/")} aria-label={t("ui.shell.brand_home")}>
          <img src="./icons/regscoutx-mark.svg" alt="" width="32" height="32" />
          <span className="rx-rail__wordmark">RegScoutX</span>
        </a>
        <ul className="rx-rail__list" role="list">
          <li><NavLink item={start} variant="rail" /></li>
          {sections.length > 0 && <li className="rx-rail__divider" aria-hidden="true" />}
          {sections.map((item) => <li key={item.key}><NavLink item={item} variant="rail" /></li>)}
        </ul>
        <ul className="rx-rail__list rx-rail__list--end" role="list">
          <li><NavLink item={preferences} variant="rail" /></li>
        </ul>
      </nav>

      <div className="rx-frame">
        {assessment && (
          <header className="rx-context">
            <div className="rx-context__identity">
              <p className="rx-context__title">
                <span className="rx-eyebrow">{t("ui.context.assessment")}</span>
                <span className="rx-mono">{shortId(assessment.id)}</span>
                {overview && (
                  <span className="rx-context__revision rx-meta">
                    {t("ui.context.revision", { revision: overview.revision, count: overview.revision_count })}
                  </span>
                )}
              </p>
              {overview && (
                <div className="rx-cluster">
                  <StatusTag tone={overview.state === "DRAFT" ? "neutral" : "info"}
                    glyph={overview.state === "DRAFT" ? "open" : "complete"}>
                    {code("assessment_state", overview.state)}
                  </StatusTag>
                  {overview.version_status !== "MATCH" && (
                    <StatusTag {...looks.version(overview.version_status)}>
                      {t(`ui.version.short.${overview.version_status.toLowerCase()}`)}
                    </StatusTag>
                  )}
                </div>
              )}
            </div>
            {overview && <RegulatorySpine stages={overview.spine} assessmentId={assessment.id} current={section} />}
          </header>
        )}
        <main id="main-content" className="rx-main" tabIndex={-1}>
          {children}
        </main>
        <footer className="rx-footer">
          <p className="rx-meta">{t("ui.scope.footer")}</p>
        </footer>
      </div>

      <nav className="rx-bottom-nav" aria-label={t("ui.shell.navigation")}>
        <ul role="list">
          <li><NavLink item={start} variant="bottom" /></li>
          {bottom.map((item) => <li key={item.key}><NavLink item={item} variant="bottom" /></li>)}
          {more.length > 0 && (
            <li>
              <button type="button" className="rx-nav-link rx-nav-link--bottom" onClick={() => setMoreOpen(true)}
                aria-haspopup="dialog" data-current={more.some((i) => i.current) || undefined}>
                <Glyph name="more" />
                <span className="rx-nav-link__label">{t("ui.nav.more")}</span>
              </button>
            </li>
          )}
        </ul>
      </nav>
      <Drawer isOpen={moreOpen} onOpenChange={setMoreOpen} title={t("ui.nav.more")} closeLabel={t("ui.action.close")}>
        <ul className="rx-more-list" role="list">
          {more.map((item) => <li key={item.key}><NavLink item={item} variant="list" /></li>)}
        </ul>
      </Drawer>
    </div>
  );
}

// Beim ersten Laden beginnt die Tastaturnavigation am Seitenanfang (Skip-Link); erst bei
// späteren Ansichtswechseln wird der Fokus auf die neue Überschrift gesetzt.
let initialView = true;

/** Seitenrahmen: Überschrift erhält beim Ansichtswechsel den Fokus, Titel wird gesetzt. */
export function Page({ eyebrow, title, lead, actions, children, focusKey }:
  { eyebrow?: string; title: string; lead?: ReactNode; actions?: ReactNode; children: ReactNode; focusKey: string }) {
  const heading = useRef<HTMLHeadingElement>(null);
  // Fokus nur bei Ansichtswechsel auf die Überschrift verschieben, nicht bei jeder Aktualisierung.
  useEffect(() => {
    if (initialView) {
      initialView = false;
      return;
    }
    heading.current?.focus();
  }, [focusKey]);
  useEffect(() => { document.title = `${title} · RegScoutX`; }, [title]);
  return (
    <div className="rx-page rx-enter">
      <header className="rx-page__header">
        <div className="rx-page__heading">
          {eyebrow && <p className="rx-eyebrow">{eyebrow}</p>}
          <h1 ref={heading} tabIndex={-1} className="rx-title">{title}</h1>
          {lead && <div className="rx-page__lead rx-reading">{lead}</div>}
        </div>
        {actions && <div className="rx-page__actions">{actions}</div>}
      </header>
      {children}
    </div>
  );
}
