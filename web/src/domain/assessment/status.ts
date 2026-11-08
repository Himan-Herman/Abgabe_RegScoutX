/**
 * Darstellung sprachneutraler Codes (Domain UI): jede Statusart erhält eine eigene Form
 * (Glyphe) und einen Farbton. Bezeichnungen kommen immer aus den zentralen Enum-Labels.
 * Hier wird nichts entschieden; die Codes stammen unverändert aus dem Kern.
 */

import type { GlyphName } from "../../core/primitives/Glyph";
import type { Tone } from "../../core/primitives/primitives";

export interface Look {
  tone: Tone;
  glyph: GlyphName;
}

const GAP: Record<string, Look> = {
  FULFILLED: { tone: "fulfilled", glyph: "fulfilled" },
  PARTIALLY_FULFILLED: { tone: "partial", glyph: "partial" },
  NOT_FULFILLED: { tone: "not_fulfilled", glyph: "not_fulfilled" },
  NOT_ASSESSED: { tone: "not_assessed", glyph: "not_assessed" },
  EVIDENCE_REVIEW_REQUIRED: { tone: "review", glyph: "review" },
  NOT_APPLICABLE: { tone: "not_applicable", glyph: "not_applicable" },
  APPLICABILITY_UNRESOLVED: { tone: "unresolved", glyph: "unresolved" },
};

const APPLICABILITY: Record<string, Look> = {
  APPLICABLE: { tone: "applicable", glyph: "applicable" },
  NOT_APPLICABLE: { tone: "not_applicable", glyph: "not_applicable" },
  APPLICABILITY_UNRESOLVED: { tone: "unresolved", glyph: "unresolved" },
};

const DECISION: Record<string, Look> = {
  DECIDED: { tone: "info", glyph: "complete" },
  REVIEW_REQUIRED: { tone: "review", glyph: "attention" },
  INCOMPLETE: { tone: "not_assessed", glyph: "open" },
  NOT_EVALUATED: { tone: "neutral", glyph: "not_assessed" },
};

const BLOCK: Record<string, Look> = {
  ACTIVE: { tone: "applicable", glyph: "applicable" },
  INACTIVE: { tone: "not_applicable", glyph: "not_applicable" },
  UNRESOLVED: { tone: "unresolved", glyph: "unresolved" },
};

const SEGMENT: Record<string, Look> = {
  COMPLETE: { tone: "info", glyph: "complete" },
  OPEN: { tone: "not_assessed", glyph: "open" },
  REVIEW: { tone: "review", glyph: "attention" },
  NOT_REQUIRED: { tone: "not_applicable", glyph: "not_applicable" },
  WAITING: { tone: "neutral", glyph: "not_assessed" },
};

const SPINE: Record<string, Look> = {
  COMPLETE: { tone: "info", glyph: "complete" },
  OPEN: { tone: "not_assessed", glyph: "open" },
  ATTENTION: { tone: "review", glyph: "attention" },
  BLOCKED: { tone: "not_fulfilled", glyph: "blocked" },
};

const VERSION: Record<string, Look> = {
  MATCH: { tone: "info", glyph: "check" },
  MISMATCH: { tone: "review", glyph: "attention" },
  INCOMPLETE_VERSION_INFO: { tone: "not_fulfilled", glyph: "blocked" },
};

const ANSWER: Record<string, Look> = {
  ACTIVE: { tone: "info", glyph: "check" },
  INACTIVE: { tone: "not_applicable", glyph: "not_applicable" },
  REACTIVATED_REVIEW_REQUIRED: { tone: "review", glyph: "attention" },
};

const FALLBACK: Look = { tone: "neutral", glyph: "info" };

export const looks = {
  gap: (code: string) => GAP[code] ?? FALLBACK,
  applicability: (code: string) => APPLICABILITY[code] ?? FALLBACK,
  decision: (code: string) => DECISION[code] ?? FALLBACK,
  block: (code: string) => BLOCK[code] ?? FALLBACK,
  segment: (code: string) => SEGMENT[code] ?? FALLBACK,
  spine: (code: string) => SPINE[code] ?? FALLBACK,
  version: (code: string) => VERSION[code] ?? FALLBACK,
  answer: (code: string) => ANSWER[code] ?? FALLBACK,
};

/** Reihenfolge der Gap-Ergebnisse für Legenden, Filter und Verteilungen. */
export const GAP_ORDER = [
  "NOT_FULFILLED", "PARTIALLY_FULFILLED", "EVIDENCE_REVIEW_REQUIRED", "NOT_ASSESSED", "FULFILLED",
  "APPLICABILITY_UNRESOLVED", "NOT_APPLICABLE",
] as const;

/** Setzbare Erfüllungsbewertungen (NOT_APPLICABLE ist nach SR-013 nicht setzbar). */
export const SETTABLE_GAP_STATUS = ["FULFILLED", "PARTIALLY_FULFILLED", "NOT_FULFILLED", "NOT_ASSESSED"] as const;

/** Status, die eine Begründung verlangen (SR-014); maßgeblich prüft der Kern. */
export const JUSTIFICATION_REQUIRED = new Set(["FULFILLED", "PARTIALLY_FULFILLED", "NOT_FULFILLED"]);

export function shortId(id: string): string {
  return id.slice(0, 8);
}
