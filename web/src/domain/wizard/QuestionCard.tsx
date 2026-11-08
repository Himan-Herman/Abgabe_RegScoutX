/**
 * Eine Frage des adaptiven Fragebogens: Warum sie gestellt wird (DI-004), welche Werte zulässig
 * sind und welche Folge jeder Wert laut Katalog hat – sichtbar vor der Eingabe (DI-006).
 * Die Oberfläche wertet nichts aus; jede Antwort geht unverändert an den Kern.
 */

import { useEffect, useState } from "react";
import type { Question } from "../../core/api/types";
import { useI18n, type I18n } from "../../core/i18n/i18n";
import { Glyph } from "../../core/primitives/Glyph";
import { Button, ChoiceCards, ComboField, DateInputField, StatusTag, type ChoiceOption } from "../../core/primitives/primitives";

type Value = string | boolean;

export function valueLabel(i18n: I18n, question: Question, value: Value | null): string {
  if (value === null) return i18n.t("ui.wizard.no_answer");
  if (typeof value === "boolean") return i18n.t(value ? "ui.value.yes" : "ui.value.no");
  if (question.input_type === "date") return i18n.date(value);
  const option = question.options.find((o) => o.value === value);
  return i18n.local(option?.label) ?? value;
}

function Reason({ question }: { question: Question }) {
  const i18n = useI18n();
  const reason = question.reason;
  if (reason.kind === "ENTRY") {
    return <p className="rx-question__reason">{i18n.t(question.source === "RUL" ? "ui.wizard.reason.entry" : "ui.wizard.reason.entry_profile")}</p>;
  }
  if (reason.kind === "FOLLOWS") {
    const answer = typeof reason.answer === "boolean" ? i18n.t(reason.answer ? "ui.value.yes" : "ui.value.no")
      : i18n.local(reason.answer_label) ?? String(reason.answer);
    return (
      <p className="rx-question__reason">
        {i18n.t("ui.wizard.reason.follows", { answer, question: i18n.local(reason.question) ?? "", rule: reason.rule_id ?? "" })}
      </p>
    );
  }
  const total = reason.blocks.reduce((sum, [, , count]) => sum + count, 0);
  return (
    <div className="rx-question__reason">
      <p>{i18n.t("ui.wizard.reason.required_by", { count: i18n.number(total) })}</p>
      <ul className="rx-question__blocks">
        {reason.blocks.map(([block, description, count]) => (
          <li key={block}>
            {i18n.local(description)} <span className="rx-meta rx-num">({i18n.t("ui.wizard.requirements_count", { count: i18n.number(count) })})</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export function QuestionCard({ question, onAnswer, busy, disabled }:
  { question: Question; onAnswer: (value: Value | null) => void; busy: boolean; disabled: boolean }) {
  const i18n = useI18n();
  const options: ChoiceOption<string>[] = question.options.map((option) => {
    const consequence = option.consequence_kind && option.consequence
      ? i18n.t(`ui.wizard.consequence.${option.consequence_kind.toLowerCase()}`, { text: i18n.local(option.consequence) ?? "" })
      : null;
    return {
      value: String(option.value),
      label: typeof option.value === "boolean" ? i18n.t(option.value ? "ui.value.yes" : "ui.value.no")
        : i18n.local(option.label) ?? String(option.value),
      description: consequence,
    };
  });
  const toValue = (raw: string): Value => {
    const option = question.options.find((o) => String(o.value) === raw);
    return option ? option.value : raw;
  };
  // Gewählte Antwort bis zur Antwort des Kerns anzeigen; bei Fehler gilt wieder der gespeicherte Wert.
  const [pending, setPending] = useState<string | null>(null);
  useEffect(() => { if (!busy) setPending(null); }, [busy, question.answer]);
  const current = pending ?? (question.answer === null ? null : String(question.answer));
  const choose = (raw: string) => { setPending(raw); onAnswer(toValue(raw)); };
  // Datum erst auf ausdrückliche Bestätigung übernehmen (nicht bei jeder Ziffer).
  const stored = typeof question.answer === "string" ? question.answer : null;
  const [dateDraft, setDateDraft] = useState<string | null>(stored);
  useEffect(() => setDateDraft(stored), [stored]);
  const label = i18n.local(question.text) ?? question.key;
  const headingId = `question-${question.key}`;
  const isDisabled = disabled || busy;

  return (
    <article className="rx-question" id={`q-${question.key}`} aria-labelledby={headingId} data-answered={question.answered || undefined}
      aria-busy={busy || undefined}>
      <header className="rx-question__header">
        <div className="rx-cluster rx-cluster--between">
          <p className="rx-eyebrow">
            {question.source === "RUL"
              ? <><span className="rx-code">{question.rule_id}</span> · {i18n.t("ui.wizard.source.rul")}</>
              : i18n.t("ui.wizard.source.profile")}
          </p>
          {question.answered
            ? <StatusTag tone="info" glyph="check" variant="plain">{i18n.t("ui.wizard.answered")}</StatusTag>
            : <StatusTag tone="not_assessed" glyph="open" variant="plain">{i18n.t("ui.wizard.open")}</StatusTag>}
        </div>
        <h3 id={headingId} className="rx-question__title">{label}</h3>
        <details className="rx-question__why" open={!question.answered}>
          <summary><Glyph name="info" size="sm" />{i18n.t("ui.wizard.why")}</summary>
          <Reason question={question} />
        </details>
      </header>

      <div className="rx-question__input">
        {question.input_type === "date" ? (
          <div className="rx-stack rx-stack--tight">
            {question.date_thresholds.length > 0 && (
              <p className="rx-meta">
                {i18n.t("ui.wizard.date_thresholds", { dates: i18n.list(question.date_thresholds.map((d) => i18n.date(d))) })}
              </p>
            )}
            <DateInputField label={i18n.t("ui.wizard.date_label")} description={i18n.t("ui.wizard.date_format")}
              value={dateDraft} isDisabled={isDisabled} onChange={setDateDraft} />
            <div>
              <Button variant="secondary" isDisabled={isDisabled || !dateDraft || dateDraft === stored}
                onPress={() => { if (dateDraft) onAnswer(dateDraft); }}>{i18n.t("ui.wizard.date_apply")}</Button>
            </div>
          </div>
        ) : options.length > 6 ? (
          <ComboField label={i18n.t("ui.wizard.choose")} options={options} value={current}
            description={i18n.t("ui.wizard.allowed_count", { count: options.length })}
            emptyText={i18n.t("ui.wizard.no_match")} isDisabled={isDisabled}
            onChange={(value) => { if (value !== null) choose(value); }} />
        ) : (
          <ChoiceCards label={i18n.t("ui.wizard.allowed_values")} options={options} value={current} isDisabled={isDisabled}
            onChange={choose} />
        )}
      </div>

      {(question.answered || busy) && (
        <footer className="rx-question__footer">
          {busy
            ? <span className="rx-cluster rx-meta" role="status"><span className="rx-spinner" aria-hidden="true" />{i18n.t("ui.wizard.recalculating")}</span>
            : <span className="rx-meta">{i18n.t("ui.wizard.current_answer", { value: valueLabel(i18n, question, question.answer) })}</span>}
          {question.answered && !busy && (
            <Button variant="ghost" onPress={() => onAnswer(null)} isDisabled={disabled}>{i18n.t("ui.wizard.clear")}</Button>
          )}
        </footer>
      )}
    </article>
  );
}
