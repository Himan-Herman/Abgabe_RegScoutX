/**
 * Anwendungsweite Stammdaten (Domain UI): Katalogversionen, Anzahl der Anforderungen und
 * Kurzbezeichnungen der Quellen aus dem Quellenregister, einmal über die API geladen.
 */

import { createContext, useContext, type ReactNode } from "react";

export interface AppMeta {
  catalog_versions: Record<string, string>;
  languages: string[];
  requirement_count: number;
  sources: Record<string, string>;
}

const AppDataContext = createContext<AppMeta | null>(null);

export function AppDataProvider({ meta, children }: { meta: AppMeta; children: ReactNode }) {
  return <AppDataContext.Provider value={meta}>{children}</AppDataContext.Provider>;
}

export function useAppData(): AppMeta {
  const value = useContext(AppDataContext);
  if (!value) throw new Error("AppDataProvider missing");
  return value;
}
