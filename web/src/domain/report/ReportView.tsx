/**
 * Report View: rendert das formatneutrale ReportDocument aus REPORTING (D3) – dieselbe Quelle wie
 * HTML- und PDF-Bericht, keine zweite Berichtslogik. Abschnitte werden erst beim Aufklappen
 * gerendert (progressive Offenlegung); PDF und HTML entstehen im Kern und werden protokolliert.
 */

import { useState, type ReactNode } from "react";
import { api } from "../../core/api/client";
import type { Lang, ReportBlock, ReportDocument, RevisionInfo } from "../../core/api/types";
import { useResource } from "../../core/api/useResource";
import { useI18n } from "../../core/i18n/i18n";
import { useAnnounce } from "../../core/a11y/announcer";
import { Glyph } from "../../core/primitives/Glyph";
import { Banner, Button, ComboField, LoadingState, Segmented, StatusTag, type Tone } from "../../core/primitives/primitives";
import { navigate, useRoute } from "../../core/router/router";
import { Page } from "../shell/AppShell";
import { errorMessage, useAssessment } from "../assessment/AssessmentContext";
import { ActionError } from "../assessment/AssessmentSection";

const PAGE = 60;
const GLYPH_BY_TONE: Record<string, Parameters<typeof Glyph>[0]["name"]> = {
  fulfilled: "fulfilled", partial: "partial", not_fulfilled: "not_fulfilled", not_assessed: "not_assessed",
  review: "review", not_applicable: "not_applicable", unresolved: "unresolved", applicable: "applicable",
};

function Toned({ tone, children }: { tone: string | null; children: ReactNode }) {
  if (!tone) return <>{children}</>;
  return <StatusTag tone={tone as Tone} glyph={GLYPH_BY_TONE[tone]} variant="plain">{children}</StatusTag>;
}

function Block({ block }: { block: ReportBlock }) {
  if ("level" in block) {
    const Tag = block.level <= 2 ? "h3" : "h4";
    return <Tag className="rx-report__heading rx-subsection-title">{block.text}</Tag>;
  }
  if ("style" in block) return <p className={`rx-report__para rx-report__para--${block.style}`}>{block.text}</p>;
  if ("items" in block && "total" in block) {
    return (
      <figure className="rx-report__distribution">
        <figcaption className="rx-meta">{block.caption}</figcaption>
        <ul role="list" className="rx-stack rx-stack--tight">
          {block.items.map(([label, count, tone], index) => (
            <li key={label}><Toned tone={tone}>{block.legend[index] ?? `${label}: ${count}`}</Toned></li>
          ))}
        </ul>
      </figure>
    );
  }
  if ("items" in block) {
    return (
      <ul className="rx-report__chips" role="list">
        {block.items.map((chip) => (
          <li key={chip.label}><span className="rx-meta">{chip.label}: </span><Toned tone={chip.tone}>{chip.value}</Toned></li>
        ))}
      </ul>
    );
  }
  if ("stages" in block) {
    return (
      <ol className="rx-report__spine" role="list" aria-label={block.caption}>
        {block.stages.map(([stage, value]) => <li key={stage}><span>{stage}</span> <span className="rx-num rx-meta">{value}</span></li>)}
      </ol>
    );
  }
  if ("headers" in block) {
    return (
      <div className="rx-table-wrap">
        <table className="rx-table rx-report__table">
          <caption>{block.caption}</caption>
          <thead><tr>{block.headers.map((h, i) => <th key={i} scope="col" className={block.numeric.includes(i) ? "rx-num" : undefined}>{h}</th>)}</tr></thead>
          <tbody>
            {block.rows.length === 0 && block.empty ? (
              <tr><td colSpan={block.headers.length} className="rx-muted">{block.empty}</td></tr>
            ) : block.rows.map((row, r) => (
              <tr key={r}>
                {row.map(([text, tone], i) => (
                  <td key={i} className={[block.numeric.includes(i) ? "rx-num" : "", block.mono.includes(i) ? "rx-code" : ""].join(" ").trim() || undefined}>
                    <Toned tone={tone}>{text}</Toned>
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
  if ("rows" in block) {
    return (
      <dl className="rx-dl rx-report__fields">
        {block.rows.map(([label, value, mono]) => (
          <div key={label} className="rx-report__field">
            <dt>{label}</dt><dd className={mono ? "rx-code" : undefined}>{value}</dd>
          </div>
        ))}
      </dl>
    );
  }
  return (
    <div className={`rx-report__group rx-report__group--${block.kind}`}>
      {block.blocks.map((inner, index) => <Block key={index} block={inner} />)}
    </div>
  );
}

function Section({ section, expanded, onToggle }:
  { section: ReportDocument["sections"][number]; expanded: boolean; onToggle: () => void }) {
  const i18n = useI18n();
  const [limit, setLimit] = useState(PAGE);
  const blocks = section.blocks.slice(0, limit);
  const panelId = `report-${section.anchor}`;
  return (
    <section className="rx-report__section" aria-labelledby={`${panelId}-title`}>
      <h2 id={`${panelId}-title`} className="rx-report__section-title">
        <button type="button" className="rx-disclosure__trigger" aria-expanded={expanded} aria-controls={panelId} onClick={onToggle}>
          <Glyph name="chevron" size="sm" className="rx-disclosure__chevron" />
          <span className="rx-disclosure__title">{section.title}</span>
          <span className="rx-disclosure__meta">{i18n.t("ui.report.blocks", { count: section.blocks.length })}</span>
        </button>
      </h2>
      <div id={panelId} hidden={!expanded} className="rx-report__body">
        {expanded && blocks.map((block, index) => <Block key={index} block={block} />)}
        {expanded && section.blocks.length > limit && (
          <Button variant="secondary" onPress={() => setLimit((n) => n + PAGE)}>
            {i18n.t("ui.report.show_more", { shown: limit, total: section.blocks.length })}
          </Button>
        )}
      </div>
    </section>
  );
}

export function ReportView() {
  const i18n = useI18n();
  const announce = useAnnounce();
  const route = useRoute();
  const { base, id, overview, run, refresh } = useAssessment();
  const lang = (route.query.get("lang") as Lang | null) ?? i18n.lang;
  const revision = route.query.get("revision");
  const revisions = useResource(() => api.get<RevisionInfo[]>(`${base}/revisions`), [base, overview?.revision_count]);
  const query = `lang=${lang}${revision ? `&revision=${revision}` : ""}`;
  const document = useResource(() => api.get<ReportDocument>(`${base}/report/document?${query}`), [base, query, overview?.fingerprint]);
  const [expanded, setExpanded] = useState<Set<string>>(() => new Set(["identification", "summary", "disclaimer"]));
  const [busy, setBusy] = useState<"pdf" | "html" | null>(null);

  const setQuery = (next: Record<string, string | undefined>) =>
    navigate(`/a/${id}/report`, { lang: route.query.get("lang") ?? undefined, revision: revision ?? undefined, ...next });

  async function create(format: "pdf" | "html") {
    setBusy(format);
    const result = await run(() => api.download(`${base}/report.${format}?${query}`));
    setBusy(null);
    if (result) {
      announce(i18n.t("ui.report.created", { format: format.toUpperCase(), file: result.filename }));
      void refresh();
    }
  }

  const doc = document.data;
  const toggle = (anchor: string) => setExpanded((current) => {
    const next = new Set(current);
    if (next.has(anchor)) next.delete(anchor); else next.add(anchor);
    return next;
  });

  return (
    <Page eyebrow={i18n.t("ui.nav.report")} title={i18n.t("ui.report.title")} focusKey="report"
      lead={<p>{i18n.t("ui.report.lead")}</p>}
      actions={(
        <>
          <Button variant="primary" icon="download" isDisabled={busy !== null} onPress={() => create("pdf")}>
            {busy === "pdf" ? i18n.t("ui.report.creating") : i18n.t("ui.report.pdf")}
          </Button>
          <Button variant="secondary" icon="download" isDisabled={busy !== null} onPress={() => create("html")}>
            {busy === "html" ? i18n.t("ui.report.creating") : i18n.t("ui.report.html")}
          </Button>
        </>
      )}>
      <ActionError />
      <div className="rx-report__controls">
        <Segmented label={i18n.t("field.language")} value={lang} onChange={(value) => setQuery({ lang: value })}
          options={(["de", "en"] as const).map((code) => ({ value: code, label: i18n.t(`language.${code}`) }))} />
        {revisions.data && revisions.data.length > 1 && (
          <ComboField label={i18n.t("field.revision")} emptyText={i18n.t("ui.wizard.no_match")}
            value={revision ?? String(revisions.data[revisions.data.length - 1].revision)}
            onChange={(value) => setQuery({ revision: value ?? undefined })}
            options={revisions.data.map((r) => ({ value: String(r.revision),
              label: i18n.t("ui.report.revision_option", { revision: r.revision, state: i18n.code("assessment_state", r.state) }),
              description: i18n.dateTime(r.updated_at) }))} />
        )}
      </div>
      {document.loading && !doc && <LoadingState label={i18n.t("ui.report.loading")} />}
      {document.error && <Banner tone="error" title={errorMessage(i18n.t, i18n.has, document.error)}
        action={<Button variant="secondary" onPress={document.reload}>{i18n.t("ui.action.retry")}</Button>} />}
      {doc && (
        <article className="rx-report" lang={doc.language} aria-labelledby="report-title">
          <header className="rx-report__cover">
            <p className="rx-eyebrow">{doc.subtitle}</p>
            <h2 id="report-title" className="rx-title">{doc.title}</h2>
            {doc.banners.map((text) => <Banner key={text} tone="warning" title={text} />)}
            <Block block={doc.cover} />
            <p className="rx-meta">{i18n.t("field.content_hash")}: <span className="rx-code">{doc.content_hash}</span></p>
          </header>
          <nav className="rx-report__toc" aria-label={doc.contents_title}>
            <div className="rx-cluster rx-cluster--between">
              <h2 className="rx-subsection-title">{doc.contents_title}</h2>
              <div className="rx-cluster">
                <Button variant="ghost" onPress={() => setExpanded(new Set(doc.sections.map((s) => s.anchor)))}>{i18n.t("ui.report.expand_all")}</Button>
                <Button variant="ghost" onPress={() => setExpanded(new Set())}>{i18n.t("ui.report.collapse_all")}</Button>
              </div>
            </div>
          </nav>
          {doc.sections.map((section) => (
            <Section key={section.anchor} section={section} expanded={expanded.has(section.anchor)} onToggle={() => toggle(section.anchor)} />
          ))}
        </article>
      )}
    </Page>
  );
}
