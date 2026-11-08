/** Informationsarchitektur (Domain UI): Bereiche einer Bewertung und ihre Spine-Stationen. */

import type { GlyphName } from "../../core/primitives/Glyph";
import type { SpineStageName } from "../../core/api/types";

export type SectionKey = "profile" | "classification" | "requirements" | "gaps" | "evidence" | "report" | "history";

export const SECTIONS: { key: SectionKey; glyph: GlyphName }[] = [
  { key: "profile", glyph: "profile" },
  { key: "classification", glyph: "classification" },
  { key: "requirements", glyph: "requirements" },
  { key: "gaps", glyph: "gap" },
  { key: "evidence", glyph: "evidence" },
  { key: "report", glyph: "report" },
  { key: "history", glyph: "history" },
];

export const STAGE_SECTION: Record<SpineStageName, SectionKey> = {
  PROFILE: "profile",
  APPLICABILITY: "classification",
  CLASSIFICATION: "classification",
  REQUIREMENTS: "requirements",
  GAP: "gaps",
  EVIDENCE: "evidence",
  REPORT: "report",
};

export function sectionPath(assessmentId: string, section: SectionKey): string {
  return `/a/${assessmentId}/${section}`;
}
