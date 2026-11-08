/**
 * Requirement Explorer (Signature Component): alle Anforderungen mit Suche und Filtern
 * (Anwendbarkeit, Gap-Status, Themencluster, Lebenszyklusphase, Block, Bewertungszustand).
 * Filter stehen in der Adresse (teilbar, Zurück-Navigation); breite Ansicht als Split View,
 * schmale Ansicht mit eigener Detailseite.
 */

import { useDeferredValue, useEffect, useMemo, useRef } from "react";
import { api } from "../../core/api/client";
import type { RequirementDetail as Detail, RequirementRow } from "../../core/api/types";
import { useResource } from "../../core/api/useResource";
import { useI18n } from "../../core/i18n/i18n";
import { useAnnounce } from "../../core/a11y/announcer";
import { Banner, Button, ComboField, EmptyState, LinkButton, LoadingState, Segmented, StatusTag, TextInputField } from "../../core/primitives/primitives";
import { href, navigate, useRoute } from "../../core/router/router";
import { Page } from "../shell/AppShell";
import { errorMessage, useAssessment } from "../assessment/AssessmentContext";
import { ActionError, WriteStateBanner } from "../assessment/AssessmentSection";
import { GAP_ORDER, looks } from "../assessment/status";
import { RequirementDetail } from "./RequirementDetail";

const FILTER_KEYS = ["q", "applicability", "gap", "theme", "phase", "block", "answer"] as const;
type Filters = Partial<Record<(typeof FILTER_KEYS)[number], string>>;

function matches(row: RequirementRow, filters: Filters, query: string, title: string | null): boolean {
  if (filters.applicability && row.applicability !== filters.applicability) return false;
  if (filters.gap === "GAPS" ? !row.is_gap : filters.gap && row.gap_status !== filters.gap) return false;
  if (filters.theme && row.theme !== filters.theme) return false;
  if (filters.phase && !row.lifecycle.includes(filters.phase)) return false;
  if (filters.block && row.block !== filters.block) return false;
  if (filters.answer && row.answer_state !== filters.answer) return false;
  if (query) {
    const haystack = `${row.requirement_id} ${title ?? ""} ${row.primary_sources.join(" ")}`.toLowerCase();
    if (!query.split(/\s+/).every((part) => haystack.includes(part))) return false;
  }
  return true;
}

export function RequirementsView() {
  const i18n = useI18n();
  const announce = useAnnounce();
  const route = useRoute();
  const { base, id, overview } = useAssessment();
  const list = useResource(() => api.get<{ texts_available: boolean; items: RequirementRow[] }>(`${base}/requirements`), [base]);
  const filters: Filters = Object.fromEntries(FILTER_KEYS.map((k) => [k, route.query.get(k) ?? undefined]));
  const selected = route.query.get("rr");
  const query = useDeferredValue((filters.q ?? "").trim().toLowerCase());
  const detailHeading = useRef<HTMLHeadingElement>(null);

  const setFilter = (key: keyof Filters, value: string | null) => {
    const next: Record<string, string | undefined> = { ...filters, rr: selected ?? undefined };
    next[key] = value ?? undefined;
    navigate(`/a/${id}/requirements`, next, { replace: key === "q" });
  };

  const rows = useMemo(() => {
    if (!list.data) return [];
    return list.data.items.filter((row) => matches(row, filters, query, i18n.local(row.title)));
    // Filterwerte stehen vollständig in der Adresse.
  }, [list.data, query, filters.applicability, filters.gap, filters.theme, filters.phase, filters.block, filters.answer, i18n]);

  const total = list.data?.items.length ?? 0;
  useEffect(() => {
    if (list.data) announce(i18n.t("ui.explorer.result_count", { count: i18n.number(rows.length), total: i18n.number(total) }));
  }, [rows.length, total]);

  function updateRow(detail: Detail) {
    if (!list.data) return;
    list.setData({
      ...list.data,
      items: list.data.items.map((row) => row.requirement_id !== detail.requirement_id ? row : {
        ...row, gap_status: detail.gap_status, gap_reason: detail.gap_reason, is_gap: detail.is_gap,
        answer_state: detail.answer_state, answer_status: detail.answer_status, evidence_state: detail.evidence_state,
        evidence_count: detail.evidence.length, open_items: detail.open_items,
      }),
    });
  }

  const active = FILTER_KEYS.filter((k) => filters[k]);
  const clearAll = () => navigate(`/a/${id}/requirements`, selected ? { rr: selected } : undefined);

  const listPanel = (
    <section className="rx-explorer__list" aria-labelledby="explorer-results">
      <div className="rx-explorer__filters" role="search" aria-label={i18n.t("ui.explorer.filters")}>
        <TextInputField label={i18n.t("ui.explorer.search")} type="search" value={filters.q ?? ""}
          description={i18n.t("ui.explorer.search_hint")} onChange={(value) => setFilter("q", value || null)} />
        <Segmented label={i18n.t("chip.applicability")} value={filters.applicability ?? "ALL"}
          onChange={(value) => setFilter("applicability", value === "ALL" ? null : value)}
          options={[{ value: "ALL", label: i18n.t("ui.explorer.all") },
            ...["APPLICABLE", "APPLICABILITY_UNRESOLVED", "NOT_APPLICABLE"].map((code) => ({ value: code, label: i18n.code("applicability", code) }))]} />
        <div className="rx-explorer__combos">
          <ComboField label={i18n.t("chip.gap_status")} value={filters.gap ?? null} emptyText={i18n.t("ui.wizard.no_match")}
            onChange={(value) => setFilter("gap", value)}
            options={[{ value: "GAPS", label: i18n.t("ui.explorer.only_gaps") },
              ...GAP_ORDER.map((code) => ({ value: code, label: i18n.code("gap_result", code) }))]} />
          <ComboField label={i18n.t("field.theme")} value={filters.theme ?? null} emptyText={i18n.t("ui.wizard.no_match")}
            onChange={(value) => setFilter("theme", value)}
            options={i18n.themeOrder.map((code) => ({ value: code, label: i18n.theme(code) }))} />
          <ComboField label={i18n.t("col.by_lifecycle")} value={filters.phase ?? null} emptyText={i18n.t("ui.wizard.no_match")}
            onChange={(value) => setFilter("phase", value)}
            options={i18n.phaseOrder.map((code) => ({ value: code, label: i18n.phase(code) }))} />
        </div>
        {(filters.block || filters.answer) && (
          <div className="rx-cluster">
            {filters.block && (
              <Button variant="secondary" icon="close" onPress={() => setFilter("block", null)}>
                {i18n.t("ui.explorer.block_filter", { block: i18n.local(overview?.blocks.find((b) => b.block === filters.block)?.description) ?? filters.block })}
              </Button>
            )}
            {filters.answer && (
              <Button variant="secondary" icon="close" onPress={() => setFilter("answer", null)}>
                {i18n.code("answer_state", filters.answer)}
              </Button>
            )}
          </div>
        )}
      </div>
      <div className="rx-cluster rx-cluster--between rx-explorer__count">
        <p id="explorer-results" className="rx-meta" aria-live="off">
          {i18n.t("ui.explorer.result_count", { count: i18n.number(rows.length), total: i18n.number(total) })}
        </p>
        {active.length > 0 && <Button variant="ghost" onPress={clearAll}>{i18n.t("ui.explorer.reset")}</Button>}
      </div>
      {list.loading && !list.data && <LoadingState label={i18n.t("ui.state.loading")} />}
      {list.error && <Banner tone="error" title={errorMessage(i18n.t, i18n.has, list.error)}
        action={<Button variant="secondary" onPress={list.reload}>{i18n.t("ui.action.retry")}</Button>} />}
      {list.data && rows.length === 0 && (
        <EmptyState glyph="search" title={i18n.t("ui.explorer.filtered_empty")} text={i18n.t("ui.explorer.filtered_empty_text")}
          action={<Button variant="secondary" onPress={clearAll}>{i18n.t("ui.explorer.reset")}</Button>} />
      )}
      {rows.length > 0 && (
        <ul className="rx-rows" role="list" aria-labelledby="explorer-results">
          {rows.map((row) => {
            const current = row.requirement_id === selected;
            return (
              <li key={row.requirement_id} className="rx-row" data-current={current || undefined}>
                <a className="rx-row__link" href={href(`/a/${id}/requirements`, { ...filters, rr: row.requirement_id })}
                  aria-current={current ? "true" : undefined}>
                  <span className="rx-row__id rx-code">{row.requirement_id}</span>
                  <span className="rx-row__title">{i18n.local(row.title) ?? i18n.t("value.catalog_text_unavailable")}</span>
                  <span className="rx-row__meta rx-meta">{i18n.theme(row.theme)}</span>
                  <span className="rx-row__tags">
                    <StatusTag {...looks.gap(row.gap_status)} variant="plain">{i18n.code("gap_result", row.gap_status)}</StatusTag>
                    {row.answer_state === "REACTIVATED_REVIEW_REQUIRED" && (
                      <StatusTag {...looks.answer(row.answer_state)} variant="plain">{i18n.t("ui.explorer.confirm_needed")}</StatusTag>
                    )}
                    {row.evidence_count > 0 && <span className="rx-meta">{i18n.t("ui.explorer.evidence_count", { count: row.evidence_count })}</span>}
                  </span>
                </a>
              </li>
            );
          })}
        </ul>
      )}
    </section>
  );

  return (
    <Page eyebrow={i18n.t("ui.nav.requirements")} title={i18n.t("ui.explorer.title")} focusKey="requirements"
      lead={<p>{i18n.t("ui.explorer.lead")}</p>}>
      <WriteStateBanner />
      <ActionError />
      <div className="rx-explorer" data-selected={selected ? true : undefined}>
        {listPanel}
        <div className="rx-explorer__detail">
          {selected ? (
            <>
              <LinkButton href={href(`/a/${id}/requirements`, { ...filters })} variant="ghost" icon="back">
                {i18n.t("ui.explorer.back_to_list")}
              </LinkButton>
              <RequirementDetail key={selected} requirementId={selected} onUpdated={updateRow} headingRef={detailHeading} />
            </>
          ) : (
            <EmptyState glyph="requirements" title={i18n.t("ui.explorer.no_selection")} text={i18n.t("ui.explorer.no_selection_text")} />
          )}
        </div>
      </div>
    </Page>
  );
}
