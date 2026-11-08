/**
 * Plattform-Adapter (Shared Product Core). Einzige Stelle mit Browser-APIs für Speicher,
 * Downloads, Medienabfragen und API-Basis; eine spätere Hybrid-/Store-Auslieferung ersetzt
 * nur diesen Adapter. Fachlogik greift nie auf Browser-APIs zu.
 */

export interface Platform {
  apiBase: string;
  readPreference(key: string): string | null;
  writePreference(key: string, value: string): void;
  saveFile(content: Blob, filename: string): void;
  prefersDark(): boolean;
  onPrefersDarkChange(listener: (dark: boolean) => void): () => void;
}

const PREFIX = "regscoutx.preference.";

export const browserPlatform: Platform = {
  apiBase: "/api",
  readPreference(key) {
    try {
      return window.localStorage.getItem(PREFIX + key);
    } catch {
      return null;
    }
  },
  writePreference(key, value) {
    try {
      window.localStorage.setItem(PREFIX + key, value);
    } catch {
      /* Speicher nicht verfügbar: Einstellung gilt nur für diese Sitzung. */
    }
  },
  saveFile(content, filename) {
    const url = URL.createObjectURL(content);
    const anchor = document.createElement("a");
    anchor.href = url;
    anchor.download = filename;
    anchor.rel = "noopener";
    document.body.appendChild(anchor);
    anchor.click();
    anchor.remove();
    window.setTimeout(() => URL.revokeObjectURL(url), 10_000);
  },
  prefersDark() {
    return typeof window.matchMedia === "function" && window.matchMedia("(prefers-color-scheme: dark)").matches;
  },
  onPrefersDarkChange(listener) {
    if (typeof window.matchMedia !== "function") return () => undefined;
    const query = window.matchMedia("(prefers-color-scheme: dark)");
    const handler = (event: MediaQueryListEvent) => listener(event.matches);
    query.addEventListener("change", handler);
    return () => query.removeEventListener("change", handler);
  },
};

let current: Platform = browserPlatform;

export function platform(): Platform {
  return current;
}

export function setPlatform(next: Platform): void {
  current = next;
}
