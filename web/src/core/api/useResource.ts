/**
 * Laden einer Ressource der Anwendungs-API mit expliziten Zuständen (Shared Product Core).
 * Veraltete Antworten werden verworfen, wenn sich die Abhängigkeiten inzwischen geändert haben.
 */

import { useCallback, useEffect, useRef, useState } from "react";
import { ApiError } from "./client";

export interface Resource<T> {
  data: T | null;
  error: ApiError | null;
  loading: boolean;
  reload(): void;
  setData(value: T): void;
}

export function toApiError(error: unknown): ApiError {
  return error instanceof ApiError ? error : new ApiError(0, "APPLICATION_ERROR");
}

export function useResource<T>(load: (() => Promise<T>) | null, deps: unknown[]): Resource<T> {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<ApiError | null>(null);
  const [loading, setLoading] = useState(load !== null);
  const [tick, setTick] = useState(0);
  const generation = useRef(0);
  useEffect(() => {
    if (!load) {
      setLoading(false);
      return;
    }
    const current = ++generation.current;
    setLoading(true);
    setError(null);
    load().then(
      (value) => {
        if (current === generation.current) {
          setData(value);
          setLoading(false);
        }
      },
      (reason: unknown) => {
        if (current === generation.current) {
          setError(toApiError(reason));
          setLoading(false);
        }
      },
    );
  }, [...deps, tick]);
  const reload = useCallback(() => setTick((value) => value + 1), []);
  return { data, error, loading, reload, setData };
}
