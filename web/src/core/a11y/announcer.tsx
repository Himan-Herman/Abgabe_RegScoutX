/**
 * Live-Region (Shared Product Core): kündigt Statusänderungen wie Neuberechnung, Speichern,
 * Filterergebnisse und Fehler Screenreadern an (aria-live), ohne den Fokus zu verschieben.
 */

import { createContext, useCallback, useContext, useRef, useState, type ReactNode } from "react";

type Politeness = "polite" | "assertive";

const AnnouncerContext = createContext<(message: string, politeness?: Politeness) => void>(() => undefined);

export function AnnouncerProvider({ children }: { children: ReactNode }) {
  const [polite, setPolite] = useState("");
  const [assertive, setAssertive] = useState("");
  const toggle = useRef(false);
  const announce = useCallback((message: string, politeness: Politeness = "polite") => {
    // Wechselnder Zusatz erzwingt erneute Ansage identischer Meldungen.
    toggle.current = !toggle.current;
    const text = message + (toggle.current ? "​" : "");
    (politeness === "assertive" ? setAssertive : setPolite)(text);
  }, []);
  return (
    <AnnouncerContext.Provider value={announce}>
      {children}
      <div className="rx-visually-hidden" aria-live="polite" aria-atomic="true" data-testid="live-polite">{polite}</div>
      <div className="rx-visually-hidden" aria-live="assertive" aria-atomic="true">{assertive}</div>
    </AnnouncerContext.Provider>
  );
}

export function useAnnounce() {
  return useContext(AnnouncerContext);
}
