/**
 * Hash-Router (Shared Product Core): funktioniert ohne Serverkonfiguration, offline und in
 * späteren Hybrid-Wrappern. Routen sind reine Daten; Views entscheiden nichts fachlich.
 */

import { useEffect, useState, type AnchorHTMLAttributes, type ReactNode } from "react";

export interface Route {
  path: string[];
  query: URLSearchParams;
}

function parse(hash: string): Route {
  const raw = hash.replace(/^#/, "") || "/";
  const [pathPart, queryPart = ""] = raw.split("?");
  return { path: pathPart.split("/").filter(Boolean).map(decodeURIComponent), query: new URLSearchParams(queryPart) };
}

export function currentRoute(): Route {
  return parse(window.location.hash);
}

export function useRoute(): Route {
  const [route, setRoute] = useState<Route>(currentRoute);
  useEffect(() => {
    const onChange = () => setRoute(currentRoute());
    window.addEventListener("hashchange", onChange);
    return () => window.removeEventListener("hashchange", onChange);
  }, []);
  return route;
}

export function href(path: string, query?: Record<string, string | undefined>): string {
  const params = new URLSearchParams();
  for (const [key, value] of Object.entries(query ?? {})) if (value) params.set(key, value);
  const suffix = params.toString();
  return `#${path}${suffix ? `?${suffix}` : ""}`;
}

export function navigate(path: string, query?: Record<string, string | undefined>, options?: { replace?: boolean }): void {
  const target = href(path, query);
  if (options?.replace) {
    // Ersetzen statt neuer Verlaufseintrag (z. B. je Tastendruck in der Suche).
    window.history.replaceState(window.history.state, "", target);
    window.dispatchEvent(new HashChangeEvent("hashchange"));
    return;
  }
  window.location.hash = target.slice(1);
}

export function Link({ to, query, children, ...rest }: { to: string; query?: Record<string, string | undefined>; children: ReactNode }
  & Omit<AnchorHTMLAttributes<HTMLAnchorElement>, "href">) {
  return <a href={href(to, query)} {...rest}>{children}</a>;
}
