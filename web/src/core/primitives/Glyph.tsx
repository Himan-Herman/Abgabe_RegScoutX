/**
 * Eigene, schlichte Symbole (Shared Product Core). Status werden immer durch Form und Text
 * vermittelt, Farbe ergänzt nur (UI_UX_DESIGN_SYSTEM.md 12.3). Symbole sind dekorativ
 * (aria-hidden); die Bedeutung trägt immer der begleitende Text.
 */

export type GlyphName =
  | "fulfilled" | "partial" | "not_fulfilled" | "not_assessed" | "unresolved" | "not_applicable"
  | "review" | "applicable" | "info" | "complete" | "open" | "attention" | "blocked"
  | "search" | "close" | "chevron" | "source" | "evidence" | "trace" | "external" | "download"
  | "plus" | "check" | "back" | "settings" | "list" | "profile" | "classification" | "requirements"
  | "gap" | "report" | "history" | "home" | "more";

const PATHS: Record<GlyphName, string> = {
  fulfilled: "M8 1.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13Zm-1 9.2L4.4 8.1l1.1-1.1L7 8.5l3.5-3.5 1.1 1.1Z",
  partial: "M8 1.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13Zm0 1.5v10a5 5 0 0 1 0-10Z",
  not_fulfilled: "M8 1.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13Zm2.6 8L9.5 10.6 8 9.1l-1.5 1.5-1.1-1.1L6.9 8 5.4 6.5l1.1-1.1L8 6.9l1.5-1.5 1.1 1.1L9.1 8Z",
  not_assessed: "M8 1.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13Zm0 1.5a5 5 0 1 1 0 10A5 5 0 0 1 8 3Z",
  unresolved: "M8 1.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13Zm.8 10.3H7.2v-1.5h1.6Zm1.5-4.9c-.3.6-.8.9-1.2 1.2-.4.2-.5.4-.5.8v.4H7.1v-.5c0-.8.4-1.3 1-1.7.4-.2.6-.4.6-.8 0-.4-.3-.7-.8-.7-.5 0-.8.3-.9.8L5.5 6.3C5.8 5 6.8 4.3 8 4.3c1.5 0 2.5.9 2.5 2 0 .2 0 .4-.2.6Z",
  not_applicable: "M8 1.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM4.5 7.2h7v1.6h-7Z",
  review: "M8 1.2 15 14H1Zm-.8 4.6v4.1h1.6V5.8Zm0 5.2v1.6h1.6V11Z",
  applicable: "M2 2h12v12H2Zm1.5 1.5v9h9v-9Z",
  info: "M8 1.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13Zm.8 10.5H7.2V7h1.6Zm0-6.2H7.2V4.2h1.6Z",
  complete: "M8 1.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13Zm-1 9.2L4.4 8.1l1.1-1.1L7 8.5l3.5-3.5 1.1 1.1Z",
  open: "M8 1.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13Zm0 1.5a5 5 0 1 1 0 10A5 5 0 0 1 8 3Zm0 2.2a2.8 2.8 0 1 0 0 5.6 2.8 2.8 0 0 0 0-5.6Z",
  attention: "M8 1.2 15 14H1Zm-.8 4.6v4.1h1.6V5.8Zm0 5.2v1.6h1.6V11Z",
  blocked: "M8 1.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM4.1 5.2l6.7 6.7A5 5 0 0 1 4.1 5.2Zm7.8 5.6L5.2 4.1a5 5 0 0 1 6.7 6.7Z",
  search: "M7 2a5 5 0 0 1 4 8l3.5 3.5-1 1L10 11a5 5 0 1 1-3-9Zm0 1.5a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7Z",
  close: "M4.1 3 8 6.9 11.9 3 13 4.1 9.1 8l3.9 3.9-1.1 1.1L8 9.1 4.1 13 3 11.9 6.9 8 3 4.1Z",
  chevron: "M6 3.5 10.5 8 6 12.5l-1.1-1.1L8.3 8 4.9 4.6Z",
  source: "M3 1.5h7l3 3v10H3Zm1.5 1.5v10h7V5.2L9.3 3Zm1.5 4h4v1.2H6Zm0 2.3h4v1.2H6Z",
  evidence: "M2 3h5l1.5 1.5H14v9H2Zm1.5 3v6h9V6Z",
  trace: "M3 2.5a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm10 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM8 10.5a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM4.2 4.4 7.6 10.8l-.9.5L3.3 4.9Zm7.6 0 .9.5-3.4 6.4-.9-.5Z",
  external: "M9 2h5v5h-1.5V4.6L7.8 9.3 6.7 8.2 11.4 3.5H9ZM3 4h4v1.5H4.5v6h6V9H12v4H3Z",
  download: "M7.2 2h1.6v6.4l2.4-2.4 1.1 1.1L8 11.4 3.7 7.1l1.1-1.1 2.4 2.4ZM3 12.5h10V14H3Z",
  plus: "M7.2 3h1.6v4.2H13v1.6H8.8V13H7.2V8.8H3V7.2h4.2Z",
  check: "M13.4 4.6 6.5 11.5 2.6 7.6l1.1-1.1 2.8 2.8 5.8-5.8Z",
  back: "M10 3.5 5.5 8l4.5 4.5-1.1 1.1L3.3 8l5.6-5.6Z",
  settings: "M7 1.5h2l.4 1.8 1.2.6 1.6-1 1.4 1.4-1 1.6.6 1.2 1.8.4v2l-1.8.4-.6 1.2 1 1.6-1.4 1.4-1.6-1-1.2.6-.4 1.8H7l-.4-1.8-1.2-.6-1.6 1-1.4-1.4 1-1.6-.6-1.2-1.8-.4V7l1.8-.4.6-1.2-1-1.6 1.4-1.4 1.6 1 1.2-.6ZM8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5Z",
  list: "M2 3h2v2H2Zm3.5.3H14v1.4H5.5ZM2 7h2v2H2Zm3.5.3H14v1.4H5.5ZM2 11h2v2H2Zm3.5.3H14v1.4H5.5Z",
  profile: "M3 1.5h10v13H3Zm1.5 1.5v10h7V3Zm1 1.5h5v1.2h-5Zm0 2.5h5v1.2h-5Zm0 2.5h3v1.2h-3Z",
  classification: "M8 1.5 14 5v6l-6 3.5L2 11V5Zm0 1.7L3.5 5.9v4.2L8 12.8l4.5-2.7V5.9Z",
  requirements: "M2.5 2h11v1.5h-11Zm0 3.5h11V7h-11Zm0 3.5h7v1.5h-7Zm0 3.5h7V14h-7Z",
  gap: "M2 2h5v5H2Zm1.2 1.2v2.6h2.6V3.2ZM9 2h5v5H9Zm0 7h5v5H9Zm1.2 1.2v2.6h2.6v-2.6ZM2 9h5v5H2Z",
  report: "M3 1.5h10v13H3Zm1.5 1.5v10h7V3ZM6 9h1.2v2.5H6Zm2-2h1.2v4.5H8Zm2 1h1.2v3.5H10Z",
  history: "M8 1.5a6.5 6.5 0 1 1-6.1 8.8l1.4-.5A5 5 0 1 0 4.1 4.8L5.8 6H2V2.2l1.1 1.3A6.5 6.5 0 0 1 8 1.5Zm-.8 3h1.6v3.2l2.4 1.4-.8 1.4-3.2-1.9Z",
  home: "M8 1.8 14.5 7v7.2h-4.2V10H5.7v4.2H1.5V7Z",
  more: "M3 6.5a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm5 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm5 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Z",
};

export function Glyph({ name, size = "md", className }: { name: GlyphName; size?: "sm" | "md"; className?: string }) {
  return (
    <svg className={`rx-glyph rx-glyph--${size}${className ? ` ${className}` : ""}`} viewBox="0 0 16 16"
      aria-hidden="true" focusable="false">
      <path d={PATHS[name]} fill="currentColor" fillRule="evenodd" />
    </svg>
  );
}
