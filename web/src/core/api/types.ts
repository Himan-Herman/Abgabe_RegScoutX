/** Typen der lokalen Anwendungs-API (regscoutx/web_api.py). Codes bleiben sprachneutral. */

export type Localized = { de: string; en: string };
export type Lang = "de" | "en";

export interface Counts {
  total: number;
  applicable: number;
  not_applicable: number;
  unresolved: number;
  fulfilled: number;
  partially_fulfilled: number;
  not_fulfilled: number;
  not_assessed: number;
  evidence_review_required: number;
  gaps: number;
  mapping_review_required: number;
  answers_review_required: number;
}

export interface RuleReference {
  rule_id: string;
  primary_legal_anchor: string[] | null;
  guidance_anchor: string[] | null;
}

export interface ReviewEntry {
  rule_id: string;
  output: string;
  cause: Localized | null;
}

export interface Decision {
  area: string;
  status: string;
  outcome: string | null;
  outcome_label: Localized | null;
  mdr_class: string | null;
  applicable_from: string | null;
  missing_input: [string, string] | null;
  missing_question: Localized | null;
  rules: RuleReference[];
  reviews: ReviewEntry[] | null;
}

export interface BlockState {
  block: string;
  description: Localized;
  state: "ACTIVE" | "INACTIVE" | "UNRESOLVED";
  counts: Record<string, number>;
  reasons: Record<string, number>;
}

export type SpineStageName =
  | "PROFILE" | "APPLICABILITY" | "CLASSIFICATION" | "REQUIREMENTS" | "GAP" | "EVIDENCE" | "REPORT";
export type SpineState = "COMPLETE" | "OPEN" | "ATTENTION" | "BLOCKED";

export interface SpineStage {
  stage: SpineStageName;
  state: SpineState;
  value: number;
  total: number | null;
}

export interface AssessmentChange {
  changed_inputs: string[];
  recorded_answers: string[];
  recorded_evidence: string[];
  removed_evidence: string[];
  deactivated_answers: string[];
  reactivated_answers: string[];
  applicability_changes: [string, string | null, string | null][];
  gap_status_changes: [string, string | null, string | null][];
}

export interface Overview {
  assessment_id: string;
  revision: number;
  revision_count: number;
  state: "DRAFT" | "FINALISED";
  origin: string;
  version_status: "MATCH" | "MISMATCH" | "INCOMPLETE_VERSION_INFO";
  writable: boolean;
  created_at: string;
  updated_at: string;
  fingerprint: string;
  catalog_versions: Record<string, string>;
  loaded_catalog_versions: Record<string, string>;
  counts: Counts;
  decisions: Decision[];
  blocks: BlockState[];
  spine: SpineStage[];
  last_change: AssessmentChange | null;
}

export type AssessmentListItem = AssessmentSummaryItem | { assessment_id: string; corrupted: true; updated_at: string };

export interface AssessmentSummaryItem {
  assessment_id: string;
  corrupted: false;
  revision: number;
  revision_count: number;
  state: string;
  version_status: string;
  created_at: string;
  updated_at: string;
  counts: Counts | null;
  decisions: { area: string; status: string; outcome: string | null; mdr_class: string | null }[];
}

export interface Option {
  value: string | boolean;
  label: Localized | null;
  consequence_kind: "RESULT" | "REVIEW" | "NEXT" | null;
  consequence: Localized | null;
}

export interface Reason {
  kind: "ENTRY" | "FOLLOWS" | "REQUIRED_BY";
  rule_id: string | null;
  question: Localized | null;
  answer: string | boolean | null;
  answer_label: Localized | null;
  blocks: [string, Localized, number][];
}

export interface Question {
  key: string;
  source: "RUL" | "PROFILE";
  rule_id: string | null;
  segment: string;
  text: Localized;
  input_type: "boolean" | "enum" | "date";
  options: Option[];
  date_thresholds: string[];
  answer: string | boolean | null;
  answered: boolean;
  reason: Reason;
}

export interface Segment {
  segment: string;
  status: "COMPLETE" | "OPEN" | "REVIEW" | "NOT_REQUIRED" | "WAITING";
  answered: number;
  open: number;
  outcome: string | null;
  outcome_label: Localized | null;
  questions: Question[];
}

export interface Questionnaire {
  segments: Segment[];
  stale: Question[];
  next_question: string | null;
}

export interface ProfileUpdate {
  overview: Overview;
  questionnaire: Questionnaire;
  change: AssessmentChange | null;
}

export interface RequirementRow {
  requirement_id: string;
  title: Localized | null;
  theme: string;
  lifecycle: string[];
  applicability: string;
  reason_code: string;
  block: string | null;
  gap_status: string;
  gap_reason: string;
  is_gap: boolean;
  answer_state: string | null;
  answer_status: string | null;
  evidence_state: string;
  evidence_count: number;
  measure_status: string;
  measures: string[];
  primary_sources: string[];
  open_items: string[];
}

export interface MeasureReference {
  measure_key: string;
  label: Localized | null;
  evidence_types: [string, Localized | null][];
}

export interface EvidenceItem {
  evidence_id: string;
  title: string;
  document_identifier: string;
  document_version: string | null;
  location: string | null;
  measure_key: string | null;
  requirement_ids: string[];
}

export interface RequirementDetail {
  requirement_id: string;
  title: Localized | null;
  text: Localized | null;
  theme: string;
  lifecycle: string[];
  primary_sources: string[] | null;
  supplementary_sources: string[] | null;
  applicability: string;
  reason_code: string;
  block: string | null;
  block_description: Localized | null;
  evaluated_predicates: [string, string][];
  relevant_inputs: [string, string | boolean][];
  supporting_rule_ids: string[];
  determined_by_areas: string[] | null;
  gap_status: string;
  gap_reason: string;
  is_gap: boolean;
  answer_state: string | null;
  answer_status: string | null;
  justification: string | null;
  evidence_state: string;
  evidence_ids: string[];
  measure_status: string;
  measures: MeasureReference[];
  open_items: string[];
  answer: { status: string; justification: string | null; evidence_ids: string[]; stale: boolean } | null;
  predicates: { key: string; value: string; description: Localized | null }[];
  decisions: Decision[];
  evidence: EvidenceItem[];
  texts_available: boolean;
  catalog_versions: Record<string, string>;
}

export type MatrixCell = Record<
  "total" | "applicable" | "not_applicable" | "unresolved" | "fulfilled" | "partially_fulfilled"
  | "not_fulfilled" | "not_assessed" | "evidence_review_required" | "gaps", number
> & { theme: string; phase: string };

export interface Matrix {
  themes: string[];
  phases: string[];
  cells: MatrixCell[];
}

export interface MeasureOverviewEntry {
  measure: MeasureReference;
  planned: number;
  with_evidence: number;
}

export interface EvidencePayload {
  items: EvidenceItem[];
  measures: MeasureOverviewEntry[];
  mapping_review_required: number;
}

export interface CatalogMeasure {
  measure_key: string;
  label: Localized;
  evidence_types: { key: string; label: Localized }[];
}

export interface RevisionInfo {
  revision: number;
  state: string;
  origin: string;
  based_on: number | null;
  created_at: string;
  updated_at: string;
  fingerprint: string;
  catalog_versions: Record<string, string>;
  same_catalog_versions: boolean;
  counts: Counts | null;
  change: AssessmentChange | null;
}

export interface AuditEntry {
  sequence: number;
  revision: number;
  occurred_at: string;
  event_type: string;
  subject_id: string | null;
  details: Record<string, unknown>;
}

// Berichtsdokument (regscoutx/report_document.py), formatneutral und bereits lokalisiert.
export type ReportBlock =
  | { level: number; text: string; anchor: string | null }
  | { text: string; style: string }
  | { items: { label: string; value: string; tone: string | null }[] }
  | { rows: [string, string, boolean][] }
  | { caption: string; headers: string[]; rows: [string, string | null][][]; widths: number[];
      numeric: number[]; mono: number[]; empty: string | null }
  | { caption: string; stages: [string, string][] }
  | { caption: string; items: [string, number, string][]; total: number; legend: string[] }
  | { kind: string; blocks: ReportBlock[] };

export interface ReportDocument {
  language: string;
  title: string;
  subtitle: string;
  banners: string[];
  cover: { rows: [string, string, boolean][] };
  running_header: string;
  page_template: string;
  contents_title: string;
  sections: { anchor: string; title: string; blocks: ReportBlock[] }[];
  content_hash: string;
}

export interface I18nBundle {
  language: Lang;
  messages: Record<string, string>;
  enums: Record<string, Record<string, string>>;
  themes: Record<string, string>;
  phases: Record<string, string>;
  theme_order: string[];
  phase_order: string[];
}
