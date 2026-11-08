/**
 * Zugängliche Bausteine (Shared Product Core) auf Basis von React Aria Components (Apache-2.0).
 * Die Bibliothek liefert Verhalten und Semantik; das Erscheinungsbild stammt ausschließlich aus
 * den eigenen Tokens (primitives.css). Keine Texte: alle Beschriftungen kommen vom Aufrufer.
 */

import type { ReactNode } from "react";
import {
  Button as AriaButton,
  ComboBox,
  DateField,
  DateInput,
  DateSegment,
  Dialog,
  Disclosure as AriaDisclosure,
  DisclosurePanel,
  FieldError,
  Heading,
  Input,
  Label,
  ListBox,
  ListBoxItem,
  Modal,
  ModalOverlay,
  Popover,
  Radio,
  RadioGroup,
  Text,
  TextArea,
  TextField,
  type ButtonProps as AriaButtonProps,
} from "react-aria-components";
import { parseDate, type CalendarDate } from "@internationalized/date";
import { Glyph, type GlyphName } from "./Glyph";

export type ButtonVariant = "primary" | "secondary" | "ghost" | "destructive";

export function Button({ variant = "secondary", icon, children, className, ...rest }:
  AriaButtonProps & { variant?: ButtonVariant; icon?: GlyphName; children: ReactNode }) {
  return (
    <AriaButton {...rest} className={`rx-button rx-button--${variant}${className ? ` ${className}` : ""}`}>
      {icon && <Glyph name={icon} />}
      <span>{children}</span>
    </AriaButton>
  );
}

export function LinkButton({ href, variant = "secondary", icon, children, download }:
  { href: string; variant?: ButtonVariant; icon?: GlyphName; children: ReactNode; download?: boolean }) {
  return (
    <a href={href} className={`rx-button rx-button--${variant}`} download={download ? "" : undefined}>
      {icon && <Glyph name={icon} />}
      <span>{children}</span>
    </a>
  );
}

export interface ChoiceOption<T extends string | boolean> {
  value: T;
  label: string;
  description?: string | null;
  meta?: string | null;
}

/** Kleine exklusive Mengen: Segmented Control (Radio-Semantik). */
export function Segmented<T extends string | boolean>({ label, options, value, onChange, description, isDisabled }:
  { label: string; options: ChoiceOption<T>[]; value: T | null; onChange: (value: T) => void; description?: string;
    isDisabled?: boolean }) {
  return (
    <RadioGroup className="rx-segmented" value={value === null ? null : String(value)} isDisabled={isDisabled}
      onChange={(v) => onChange(options.find((o) => String(o.value) === v)!.value)} orientation="horizontal">
      <Label className="rx-field__label">{label}</Label>
      {description && <Text slot="description" className="rx-field__description">{description}</Text>}
      <div className="rx-segmented__track">
        {options.map((option) => (
          <Radio key={String(option.value)} value={String(option.value)} className="rx-segmented__option">
            <span className="rx-segmented__mark" aria-hidden="true"><Glyph name="check" size="sm" /></span>
            <span>{option.label}</span>
          </Radio>
        ))}
      </div>
    </RadioGroup>
  );
}

/** Regulatorisch wichtige Alternativen: Entscheidungskarten mit Erläuterung und Folge. */
export function ChoiceCards<T extends string | boolean>({ label, options, value, onChange, description, isDisabled }:
  { label: string; options: ChoiceOption<T>[]; value: T | null; onChange: (value: T) => void; description?: string;
    isDisabled?: boolean }) {
  return (
    <RadioGroup className="rx-cards" value={value === null ? null : String(value)} isDisabled={isDisabled}
      onChange={(v) => onChange(options.find((o) => String(o.value) === v)!.value)}>
      <Label className="rx-field__label">{label}</Label>
      {description && <Text slot="description" className="rx-field__description">{description}</Text>}
      <div className="rx-cards__grid">
        {options.map((option) => (
          <Radio key={String(option.value)} value={String(option.value)} className="rx-cards__card">
            <span className="rx-cards__indicator" aria-hidden="true" />
            <span className="rx-cards__body">
              <span className="rx-cards__label">{option.label}</span>
              {option.description && <span className="rx-cards__description">{option.description}</span>}
              {option.meta && <span className="rx-cards__meta">{option.meta}</span>}
            </span>
          </Radio>
        ))}
      </div>
    </RadioGroup>
  );
}

/** Größere kontrollierte Vokabulare: durchsuchbare Combobox mit mehrzeiligen Einträgen. */
export function ComboField<T extends string>({ label, options, value, onChange, description, placeholder, emptyText,
  isDisabled }: { label: string; options: ChoiceOption<T>[]; value: T | null; onChange: (value: T | null) => void;
    description?: string; placeholder?: string; emptyText: string; isDisabled?: boolean }) {
  return (
    <ComboBox className="rx-combo" selectedKey={value} isDisabled={isDisabled}
      onSelectionChange={(key) => onChange(key === null ? null : (String(key) as T))} menuTrigger="focus">
      <Label className="rx-field__label">{label}</Label>
      {description && <Text slot="description" className="rx-field__description">{description}</Text>}
      <div className="rx-combo__control">
        <Glyph name="search" size="sm" className="rx-combo__icon" />
        <Input className="rx-input rx-combo__input" placeholder={placeholder} />
        <AriaButton className="rx-combo__toggle"><Glyph name="chevron" size="sm" /></AriaButton>
      </div>
      <Popover className="rx-popover" offset={4}>
        <ListBox className="rx-listbox" renderEmptyState={() => <div className="rx-listbox__empty">{emptyText}</div>}>
          {options.map((option) => (
            <ListBoxItem key={option.value} id={option.value} textValue={option.label} className="rx-listbox__item">
              <span className="rx-listbox__label">{option.label}</span>
              {option.description && <span className="rx-listbox__description">{option.description}</span>}
            </ListBoxItem>
          ))}
        </ListBox>
      </Popover>
    </ComboBox>
  );
}

/** Datumseingabe mit sichtbarem Format; Wert als ISO-Datum. */
export function DateInputField({ label, value, onChange, description, isDisabled }:
  { label: string; value: string | null; onChange: (value: string | null) => void; description?: string;
    isDisabled?: boolean }) {
  let parsed: CalendarDate | null = null;
  try {
    parsed = value ? parseDate(value) : null;
  } catch {
    parsed = null;
  }
  return (
    <DateField className="rx-date" value={parsed} isDisabled={isDisabled}
      onChange={(date) => onChange(date ? date.toString() : null)}>
      <Label className="rx-field__label">{label}</Label>
      {description && <Text slot="description" className="rx-field__description">{description}</Text>}
      <DateInput className="rx-date__input">
        {(segment) => <DateSegment segment={segment} className="rx-date__segment" />}
      </DateInput>
      <FieldError className="rx-field__error" />
    </DateField>
  );
}

export function TextAreaField({ label, value, onChange, description, isRequired, errorMessage, isDisabled }:
  { label: string; value: string; onChange: (value: string) => void; description?: string; isRequired?: boolean;
    errorMessage?: string | null; isDisabled?: boolean }) {
  return (
    <TextField className="rx-field" value={value} onChange={onChange} isRequired={isRequired}
      isInvalid={!!errorMessage} isDisabled={isDisabled}>
      <Label className="rx-field__label">{label}</Label>
      {description && <Text slot="description" className="rx-field__description">{description}</Text>}
      <TextArea className="rx-input rx-textarea" rows={3} />
      <FieldError className="rx-field__error">{errorMessage}</FieldError>
    </TextField>
  );
}

export function TextInputField({ label, value, onChange, description, isRequired, errorMessage, type = "text",
  isDisabled }: { label: string; value: string; onChange: (value: string) => void; description?: string;
    isRequired?: boolean; errorMessage?: string | null; type?: "text" | "search"; isDisabled?: boolean }) {
  return (
    <TextField className="rx-field" value={value} onChange={onChange} isRequired={isRequired}
      isInvalid={!!errorMessage} type={type} isDisabled={isDisabled}>
      <Label className="rx-field__label">{label}</Label>
      {description && <Text slot="description" className="rx-field__description">{description}</Text>}
      <Input className="rx-input" />
      <FieldError className="rx-field__error">{errorMessage}</FieldError>
    </TextField>
  );
}

/** Fortschreitende Offenlegung. */
export function Disclosure({ title, meta, children, defaultExpanded, id }:
  { title: ReactNode; meta?: ReactNode; children: ReactNode; defaultExpanded?: boolean; id?: string }) {
  return (
    <AriaDisclosure className="rx-disclosure" defaultExpanded={defaultExpanded} id={id}>
      <Heading level={3} className="rx-disclosure__heading">
        <AriaButton slot="trigger" className="rx-disclosure__trigger">
          <Glyph name="chevron" size="sm" className="rx-disclosure__chevron" />
          <span className="rx-disclosure__title">{title}</span>
          {meta && <span className="rx-disclosure__meta">{meta}</span>}
        </AriaButton>
      </Heading>
      <DisclosurePanel className="rx-disclosure__panel">{children}</DisclosurePanel>
    </AriaDisclosure>
  );
}

/** Seitliches Panel (Source Drawer, Evidence-Formulare): Fokusfalle und Escape über React Aria. */
export function Drawer({ isOpen, onOpenChange, title, closeLabel, children }:
  { isOpen: boolean; onOpenChange: (open: boolean) => void; title: string; closeLabel: string; children: ReactNode }) {
  return (
    <ModalOverlay className="rx-drawer-overlay" isOpen={isOpen} onOpenChange={onOpenChange} isDismissable>
      <Modal className="rx-drawer">
        <Dialog className="rx-drawer__dialog">
          <header className="rx-drawer__header">
            <Heading slot="title" className="rx-drawer__title">{title}</Heading>
            <AriaButton slot="close" className="rx-icon-button" aria-label={closeLabel}>
              <Glyph name="close" />
            </AriaButton>
          </header>
          <div className="rx-drawer__body">{children}</div>
        </Dialog>
      </Modal>
    </ModalOverlay>
  );
}

export function ConfirmDialog({ isOpen, onOpenChange, title, body, confirmLabel, cancelLabel, onConfirm,
  destructive }: { isOpen: boolean; onOpenChange: (open: boolean) => void; title: string; body: string;
    confirmLabel: string; cancelLabel: string; onConfirm: () => void; destructive?: boolean }) {
  return (
    <ModalOverlay className="rx-dialog-overlay" isOpen={isOpen} onOpenChange={onOpenChange} isDismissable>
      <Modal className="rx-dialog">
        <Dialog className="rx-dialog__body" role="alertdialog">
          <Heading slot="title" className="rx-dialog__title">{title}</Heading>
          <p className="rx-dialog__text">{body}</p>
          <div className="rx-dialog__actions">
            <Button variant="ghost" slot="close">{cancelLabel}</Button>
            <Button variant={destructive ? "destructive" : "primary"} onPress={() => { onConfirm(); onOpenChange(false); }}>
              {confirmLabel}
            </Button>
          </div>
        </Dialog>
      </Modal>
    </ModalOverlay>
  );
}

export type Tone = "fulfilled" | "partial" | "not_fulfilled" | "not_assessed" | "unresolved" | "not_applicable"
  | "review" | "applicable" | "info" | "neutral";

/** Statusanzeige: Symbolform + Text + Farbton; nie Farbe allein. */
export function StatusTag({ tone, glyph, children, variant = "soft", title }:
  { tone: Tone; glyph?: GlyphName; children: ReactNode; variant?: "soft" | "plain"; title?: string }) {
  return (
    <span className={`rx-status rx-status--${tone} rx-status--${variant}`} title={title}>
      {glyph && <Glyph name={glyph} size="sm" />}
      <span className="rx-status__text">{children}</span>
    </span>
  );
}

export function Banner({ tone, title, children, action }:
  { tone: "info" | "warning" | "error" | "unresolved"; title: string; children?: ReactNode; action?: ReactNode }) {
  const glyph: GlyphName = tone === "info" ? "info" : tone === "unresolved" ? "unresolved" : "attention";
  return (
    <section className={`rx-banner rx-banner--${tone}`} role={tone === "error" ? "alert" : "note"}>
      <Glyph name={glyph} />
      <div className="rx-banner__content">
        <p className="rx-banner__title">{title}</p>
        {children && <div className="rx-banner__text">{children}</div>}
      </div>
      {action && <div className="rx-banner__action">{action}</div>}
    </section>
  );
}

export function LoadingState({ label }: { label: string }) {
  return (
    <div className="rx-state rx-state--loading" role="status" aria-live="polite">
      <span className="rx-spinner" aria-hidden="true" />
      <span>{label}</span>
    </div>
  );
}

export function EmptyState({ title, text, action, glyph = "info" }:
  { title: string; text?: string; action?: ReactNode; glyph?: GlyphName }) {
  return (
    <div className="rx-state rx-state--empty">
      <Glyph name={glyph} />
      <p className="rx-state__title">{title}</p>
      {text && <p className="rx-state__text">{text}</p>}
      {action}
    </div>
  );
}

export function VisuallyHidden({ children }: { children: ReactNode }) {
  return <span className="rx-visually-hidden">{children}</span>;
}
