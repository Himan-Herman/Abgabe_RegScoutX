/**
 * Experience Profile „RegScoutX“ – semantische Farb-Tokens (UI_UX_DESIGN_SYSTEM.md Abschnitt 12).
 * Einzige Quelle für Farben der Oberfläche; die Theme Engine überträgt sie als CSS-Variablen.
 * Light: warmes Papier, Graphit-Text, mineralischer Petrol-Akzent. Dark: tiefes Graphit, kein Reinschwarz.
 * Jede Variante ist auf Kontrast geprüft (src/experience/regscoutx/palette.test.ts).
 */

export type ColorToken =
  | "surface" | "surfaceElevated" | "surfaceSubtle" | "surfaceInset"
  | "textPrimary" | "textSecondary" | "textMuted" | "textInverse"
  | "border" | "divider" | "borderStrong"
  | "interactive" | "interactiveHover" | "interactivePressed" | "interactiveSubtle" | "onInteractive"
  | "focus" | "selection" | "overlay" | "disabledText" | "disabledSurface"
  | "statusFulfilled" | "statusPartial" | "statusNotFulfilled" | "statusNotAssessed"
  | "statusUnresolved" | "statusNotApplicable" | "statusEvidenceReview" | "statusInfo" | "statusApplicable"
  | "statusFulfilledSubtle" | "statusPartialSubtle" | "statusNotFulfilledSubtle" | "statusNotAssessedSubtle"
  | "statusUnresolvedSubtle" | "statusNotApplicableSubtle" | "statusEvidenceReviewSubtle" | "statusInfoSubtle"
  | "statusApplicableSubtle" | "trace" | "danger" | "dangerHover" | "onDanger";

export type Palette = Record<ColorToken, string>;

const light: Palette = {
  surface: "#F7F6F2", surfaceElevated: "#FFFFFF", surfaceSubtle: "#F0EEE8", surfaceInset: "#E8E6DF",
  textPrimary: "#1A1D21", textSecondary: "#40454C", textMuted: "#565B63", textInverse: "#F7F6F2",
  border: "#D3D0C7", divider: "#E3E0D8", borderStrong: "#8A867C",
  interactive: "#0F5E66", interactiveHover: "#0B4E55", interactivePressed: "#083F45",
  interactiveSubtle: "#E0EBEA", onInteractive: "#FFFFFF",
  focus: "#0F5E66", selection: "#CFE3E1", overlay: "rgba(20, 22, 25, 0.40)",
  disabledText: "#8A8E94", disabledSurface: "#ECEAE4",
  statusFulfilled: "#1B6743", statusPartial: "#7E5409", statusNotFulfilled: "#9E272B",
  statusNotAssessed: "#454C55", statusUnresolved: "#583D88", statusNotApplicable: "#5A6068",
  statusEvidenceReview: "#8C4600", statusInfo: "#1C5883", statusApplicable: "#0F5E66",
  statusFulfilledSubtle: "#E2EFE7", statusPartialSubtle: "#F5ECD8", statusNotFulfilledSubtle: "#F6E2E2",
  statusNotAssessedSubtle: "#EAEBEC", statusUnresolvedSubtle: "#ECE6F3", statusNotApplicableSubtle: "#ECECEA",
  statusEvidenceReviewSubtle: "#F7E8DA", statusInfoSubtle: "#E1EAF2", statusApplicableSubtle: "#E0EBEA",
  trace: "#474C8C", danger: "#9E272B", dangerHover: "#831E22", onDanger: "#FFFFFF",
};

const dark: Palette = {
  surface: "#111418", surfaceElevated: "#171B20", surfaceSubtle: "#1C2127", surfaceInset: "#0C0F12",
  textPrimary: "#E7E9EB", textSecondary: "#C3C8CE", textMuted: "#A2A9B1", textInverse: "#111418",
  border: "#323941", divider: "#252B32", borderStrong: "#6E7883",
  interactive: "#6CC6CD", interactiveHover: "#8AD4DA", interactivePressed: "#A8E0E4",
  interactiveSubtle: "#133338", onInteractive: "#0A1A1C",
  focus: "#8AD4DA", selection: "#1D4448", overlay: "rgba(0, 0, 0, 0.58)",
  disabledText: "#6B727A", disabledSurface: "#1C2127",
  statusFulfilled: "#7DCB9F", statusPartial: "#E0B866", statusNotFulfilled: "#F0999C",
  statusNotAssessed: "#B4BBC3", statusUnresolved: "#C4B1EA", statusNotApplicable: "#A0A7B0",
  statusEvidenceReview: "#F0AE6D", statusInfo: "#8FC3EB", statusApplicable: "#6CC6CD",
  statusFulfilledSubtle: "#15291F", statusPartialSubtle: "#2C2414", statusNotFulfilledSubtle: "#321A1B",
  statusNotAssessedSubtle: "#1E2227", statusUnresolvedSubtle: "#231D33", statusNotApplicableSubtle: "#1E2226",
  statusEvidenceReviewSubtle: "#2F2116", statusInfoSubtle: "#14263A", statusApplicableSubtle: "#133338",
  trace: "#AEB2F0", danger: "#F0999C", dangerHover: "#F5B3B5", onDanger: "#1A0A0B",
};

const lightHighContrast: Palette = {
  ...light,
  surface: "#FFFFFF", surfaceSubtle: "#F4F3EF", surfaceInset: "#ECEBE6",
  textSecondary: "#1A1D21", textMuted: "#2C3036",
  border: "#5C6067", divider: "#8A8E94", borderStrong: "#1A1D21",
  interactive: "#083F45", interactiveHover: "#062F34", interactivePressed: "#041F22",
  focus: "#000000",
  statusFulfilled: "#0F4A2D", statusPartial: "#5A3B00", statusNotFulfilled: "#7A1A1D",
  statusNotAssessed: "#2C3036", statusUnresolved: "#3E2766", statusNotApplicable: "#3A3F46",
  statusEvidenceReview: "#6A3300", statusInfo: "#0F3F63", statusApplicable: "#083F45",
  trace: "#2D3170", danger: "#7A1A1D", dangerHover: "#5E1316",
};

const darkHighContrast: Palette = {
  ...dark,
  surface: "#000000", surfaceElevated: "#0B0D10", surfaceSubtle: "#12161A",
  textPrimary: "#FFFFFF", textSecondary: "#F0F2F4", textMuted: "#D9DDE1",
  border: "#A7B0BA", divider: "#6E7883", borderStrong: "#FFFFFF",
  interactive: "#9FE3E8", interactiveHover: "#C2EEF1", interactivePressed: "#DDF6F8", focus: "#FFFFFF",
  statusFulfilled: "#A6E4C1", statusPartial: "#F2D38F", statusNotFulfilled: "#FFBFC1",
  statusNotAssessed: "#D9DDE1", statusUnresolved: "#DCCFF7", statusNotApplicable: "#C9CED4",
  statusEvidenceReview: "#FFCB98", statusInfo: "#BADCF6", statusApplicable: "#9FE3E8",
  trace: "#CFD2FA", danger: "#FFBFC1", dangerHover: "#FFD9DA",
};

export const palettes = { light, dark, lightHighContrast, darkHighContrast } as const;
export type PaletteName = keyof typeof palettes;
