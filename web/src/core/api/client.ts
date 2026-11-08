/**
 * Application-Service-Adapter (Shared Product Core): einziger Zugang der Oberfläche zur
 * Anwendungs-API. Schreibende Anfragen tragen den Pflicht-Header gegen Cross-Site-Anfragen.
 * Fehler werden als stabile Codes weitergereicht und in der Oberfläche lokalisiert.
 */

import { platform } from "../platform/platform";

export class ApiError extends Error {
  constructor(
    public readonly status: number,
    public readonly code: string,
    public readonly field: string | null = null,
    public readonly detail: string | null = null,
  ) {
    super(code);
  }
}

async function request<T>(method: string, path: string, body?: unknown): Promise<T> {
  const headers: Record<string, string> = { Accept: "application/json" };
  if (method !== "GET") headers["X-RegScoutX-Request"] = "1";
  if (body !== undefined) headers["Content-Type"] = "application/json";
  let response: Response;
  try {
    response = await fetch(platform().apiBase + path, {
      method,
      headers,
      body: body === undefined ? undefined : JSON.stringify(body),
      credentials: "same-origin",
    });
  } catch {
    throw new ApiError(0, "NETWORK_UNAVAILABLE");
  }
  const text = await response.text();
  let data: unknown = null;
  try {
    data = text ? JSON.parse(text) : null;
  } catch {
    throw new ApiError(response.status, "INVALID_RESPONSE");
  }
  if (!response.ok) {
    const error = (data as { error?: { code?: string; field?: string; detail?: string } } | null)?.error;
    throw new ApiError(response.status, error?.code ?? "APPLICATION_ERROR", error?.field ?? null,
      error?.detail ?? null);
  }
  return data as T;
}

/** Lädt eine Datei (z. B. Bericht) und übergibt sie dem Plattform-Adapter zum Speichern. */
async function download(path: string): Promise<{ filename: string; contentHash: string | null }> {
  let response: Response;
  try {
    response = await fetch(platform().apiBase + path, { credentials: "same-origin" });
  } catch {
    throw new ApiError(0, "NETWORK_UNAVAILABLE");
  }
  if (!response.ok) {
    let code = "APPLICATION_ERROR";
    try {
      code = ((await response.json()) as { error?: { code?: string } }).error?.code ?? code;
    } catch {
      /* kein JSON-Fehlerobjekt */
    }
    throw new ApiError(response.status, code);
  }
  const disposition = response.headers.get("Content-Disposition") ?? "";
  const filename = /filename="([^"]+)"/.exec(disposition)?.[1] ?? "regscoutx-report";
  platform().saveFile(await response.blob(), filename);
  return { filename, contentHash: response.headers.get("X-RegScoutX-Content-Hash") };
}

export const api = {
  get: <T>(path: string) => request<T>("GET", path),
  post: <T>(path: string, body?: unknown) => request<T>("POST", path, body ?? {}),
  put: <T>(path: string, body: unknown) => request<T>("PUT", path, body),
  patch: <T>(path: string, body: unknown) => request<T>("PATCH", path, body),
  del: <T>(path: string) => request<T>("DELETE", path),
  url: (path: string) => platform().apiBase + path,
  download,
};
