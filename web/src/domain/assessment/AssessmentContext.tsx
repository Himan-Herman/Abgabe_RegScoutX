/**
 * Kontext der geöffneten Bewertung (Domain UI). Öffnet die Bewertung einmal bewusst
 * (Versionsabgleich mit Audit im Kern), hält den Überblick und bündelt schreibende Aufrufe:
 * Fehler werden als stabile Codes angezeigt und angesagt, nie still ersetzt.
 */

import { createContext, useCallback, useContext, useEffect, useMemo, useState, type ReactNode } from "react";
import { api, ApiError } from "../../core/api/client";
import type { Overview } from "../../core/api/types";
import { toApiError } from "../../core/api/useResource";
import { useAnnounce } from "../../core/a11y/announcer";
import { useI18n } from "../../core/i18n/i18n";

interface AssessmentContextValue {
  id: string;
  overview: Overview | null;
  error: ApiError | null;
  loading: boolean;
  editable: boolean;
  base: string;
  refresh(): Promise<void>;
  apply(overview: Overview): void;
  /** Führt eine schreibende Operation aus; liefert null bei Fehler (bereits angezeigt). */
  run<T>(operation: () => Promise<T>, success?: string): Promise<T | null>;
  actionError: ApiError | null;
  clearActionError(): void;
}

const AssessmentContext = createContext<AssessmentContextValue | null>(null);

export function errorMessage(t: (key: string, params?: Record<string, string | number>) => string,
  has: (key: string) => boolean, error: { code: string }): string {
  const key = `ui.error.${error.code.toLowerCase()}`;
  return has(key) ? t(key) : t("ui.error.application_error");
}

export function AssessmentProvider({ id, children }: { id: string; children: ReactNode }) {
  const { t, has } = useI18n();
  const announce = useAnnounce();
  const [overview, setOverview] = useState<Overview | null>(null);
  const [error, setError] = useState<ApiError | null>(null);
  const [loading, setLoading] = useState(true);
  const [actionError, setActionError] = useState<ApiError | null>(null);
  const base = `/assessments/${encodeURIComponent(id)}`;

  useEffect(() => {
    let active = true;
    setLoading(true);
    setError(null);
    setOverview(null);
    api.post<Overview>(`${base}/open`).then(
      (value) => { if (active) { setOverview(value); setLoading(false); } },
      (reason: unknown) => { if (active) { setError(toApiError(reason)); setLoading(false); } },
    );
    return () => { active = false; };
  }, [base]);

  const refresh = useCallback(async () => {
    try {
      setOverview(await api.get<Overview>(base));
    } catch (reason) {
      setError(toApiError(reason));
    }
  }, [base]);

  const run = useCallback(async <T,>(operation: () => Promise<T>, success?: string): Promise<T | null> => {
    setActionError(null);
    try {
      const result = await operation();
      if (success) announce(success);
      return result;
    } catch (reason) {
      const apiError = toApiError(reason);
      setActionError(apiError);
      announce(errorMessage(t, has, apiError), "assertive");
      return null;
    }
  }, [announce, t, has]);

  const value = useMemo<AssessmentContextValue>(() => ({
    id,
    overview,
    error,
    loading,
    editable: !!overview && overview.writable && overview.state === "DRAFT",
    base,
    refresh,
    apply: setOverview,
    run,
    actionError,
    clearActionError: () => setActionError(null),
  }), [id, overview, error, loading, base, refresh, run, actionError]);

  return <AssessmentContext.Provider value={value}>{children}</AssessmentContext.Provider>;
}

export function useAssessment(): AssessmentContextValue {
  const value = useContext(AssessmentContext);
  if (!value) throw new Error("AssessmentProvider missing");
  return value;
}

export function useOptionalAssessment(): AssessmentContextValue | null {
  return useContext(AssessmentContext);
}
