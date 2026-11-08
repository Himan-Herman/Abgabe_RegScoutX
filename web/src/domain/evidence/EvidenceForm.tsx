/**
 * Formular einer Nachweisreferenz (Domain UI). Freitexte werden nur als Text gespeichert und
 * angezeigt; die Prüfung (Pflichtfelder, zulässige Maßnahme) nimmt der Kern vor.
 */

import { useState, type FormEvent } from "react";
import type { EvidenceItem, MeasureReference } from "../../core/api/types";
import { useI18n } from "../../core/i18n/i18n";
import { ApiError } from "../../core/api/client";
import { Button, ComboField, TextInputField } from "../../core/primitives/primitives";

export interface EvidenceDraft {
  title: string;
  document_identifier: string;
  document_version: string;
  location: string;
  measure_key: string | null;
}

export function draftOf(item: EvidenceItem | null): EvidenceDraft {
  return {
    title: item?.title ?? "", document_identifier: item?.document_identifier ?? "",
    document_version: item?.document_version ?? "", location: item?.location ?? "", measure_key: item?.measure_key ?? null,
  };
}

export function EvidenceForm({ initial, measures, submitLabel, onSubmit, onCancel, error }:
  { initial: EvidenceDraft; measures: MeasureReference[]; submitLabel: string; error: ApiError | null;
    onSubmit: (draft: EvidenceDraft) => Promise<void>; onCancel: () => void }) {
  const i18n = useI18n();
  const [draft, setDraft] = useState(initial);
  const [attempted, setAttempted] = useState(false);
  const [busy, setBusy] = useState(false);
  const set = (key: keyof EvidenceDraft) => (value: string | null) => setDraft((d) => ({ ...d, [key]: value }));
  const missing = (value: string) => attempted && !value.trim() ? i18n.t("ui.evidence.required") : null;
  const serverField = error?.code === "INVALID_INPUT" ? error.field ?? "" : "";
  const fieldError = (name: string) => serverField.endsWith(name) ? i18n.t("ui.error.invalid_input") : null;

  async function submit(event: FormEvent) {
    event.preventDefault();
    setAttempted(true);
    if (!draft.title.trim() || !draft.document_identifier.trim()) return;
    setBusy(true);
    await onSubmit(draft);
    setBusy(false);
  }

  return (
    <form className="rx-stack" onSubmit={submit} noValidate>
      <p className="rx-body-sm rx-muted">{i18n.t("ui.evidence.form_note")}</p>
      <TextInputField label={i18n.t("ui.evidence.title_label")} value={draft.title} onChange={set("title")} isRequired
        errorMessage={missing(draft.title) ?? fieldError("title")} />
      <TextInputField label={i18n.t("col.document")} value={draft.document_identifier} onChange={set("document_identifier")}
        isRequired errorMessage={missing(draft.document_identifier) ?? fieldError("document_identifier")}
        description={i18n.t("ui.evidence.document_hint")} />
      <TextInputField label={i18n.t("col.document_version")} value={draft.document_version} onChange={set("document_version")}
        errorMessage={fieldError("document_version")} />
      <TextInputField label={i18n.t("col.location")} value={draft.location} onChange={set("location")}
        description={i18n.t("ui.evidence.location_hint")} errorMessage={fieldError("location")} />
      {measures.length > 0 && (
        <ComboField label={i18n.t("col.measure_key")} value={draft.measure_key} onChange={set("measure_key")}
          description={i18n.t("ui.evidence.measure_hint")} emptyText={i18n.t("ui.wizard.no_match")}
          options={measures.map((m) => ({ value: m.measure_key, label: i18n.local(m.label) ?? m.measure_key,
            description: m.measure_key }))} />
      )}
      <div className="rx-cluster">
        <Button type="submit" variant="primary" isDisabled={busy}>{submitLabel}</Button>
        <Button variant="ghost" onPress={onCancel}>{i18n.t("ui.action.cancel")}</Button>
      </div>
    </form>
  );
}
