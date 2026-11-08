/**
 * Verteilt die Bereiche einer Bewertung und behandelt die gemeinsamen Zustände:
 * Laden, nicht gefunden, beschädigt, Netzwerkfehler und Versionsabweichung (schreibgeschützt).
 */

import { Banner, Button, LoadingState } from "../../core/primitives/primitives";
import { navigate } from "../../core/router/router";
import { useI18n } from "../../core/i18n/i18n";
import { api } from "../../core/api/client";
import type { Overview } from "../../core/api/types";
import { Page } from "../shell/AppShell";
import type { SectionKey } from "../shell/navigation";
import { errorMessage, useAssessment } from "./AssessmentContext";
import { WizardView } from "../wizard/WizardView";
import { ClassificationView } from "../classification/ClassificationView";
import { RequirementsView } from "../requirements/RequirementsView";
import { GapLensView } from "../gaps/GapLensView";
import { EvidenceView } from "../evidence/EvidenceView";
import { ReportView } from "../report/ReportView";
import { HistoryView } from "../history/HistoryView";

/** Hinweis bei Versionsabweichung oder abgeschlossener Revision; bietet den zulässigen Weg an. */
export function WriteStateBanner() {
  const i18n = useI18n();
  const { overview, run, apply, base, editable } = useAssessment();
  if (!overview || editable) return null;
  if (overview.version_status !== "MATCH") {
    const canRebase = overview.version_status === "MISMATCH";
    return (
      <Banner tone="warning" title={i18n.t(`ui.version.title.${overview.version_status.toLowerCase()}`)}
        action={canRebase ? (
          <Button variant="secondary" icon="history" onPress={async () => {
            const next = await run(() => api.post<Overview>(`${base}/rebase`), i18n.t("ui.history.rebased"));
            if (next) apply(next);
          }}>{i18n.t("ui.history.rebase")}</Button>
        ) : undefined}>
        {i18n.t(`ui.version.text.${overview.version_status.toLowerCase()}`)}
      </Banner>
    );
  }
  return (
    <Banner tone="info" title={i18n.t("ui.finalised.title")}
      action={<Button variant="secondary" onPress={async () => {
        const next = await run(() => api.post<Overview>(`${base}/reopen`), i18n.t("ui.history.reopened"));
        if (next) apply(next);
      }}>{i18n.t("ui.history.reopen")}</Button>}>
      {i18n.t("ui.finalised.text")}
    </Banner>
  );
}

export function ActionError() {
  const i18n = useI18n();
  const { actionError, clearActionError } = useAssessment();
  if (!actionError) return null;
  return (
    <Banner tone="error" title={i18n.t("ui.error.action_title")}
      action={<Button variant="ghost" onPress={clearActionError}>{i18n.t("ui.action.dismiss")}</Button>}>
      {errorMessage(i18n.t, i18n.has, actionError)}
    </Banner>
  );
}

export function AssessmentSection({ section }: { section: SectionKey }) {
  const i18n = useI18n();
  const { overview, error, loading } = useAssessment();
  if (loading) return <LoadingState label={i18n.t("ui.state.loading_assessment")} />;
  if (error || !overview) {
    const code = error?.code ?? "APPLICATION_ERROR";
    return (
      <Page title={i18n.t(code === "ASSESSMENT_NOT_FOUND" ? "ui.state.not_found_title" : code === "CORRUPTED_ASSESSMENT"
        ? "ui.state.corrupted_title" : "ui.state.error_title")} focusKey={`error-${code}`}>
        <Banner tone="error" title={errorMessage(i18n.t, i18n.has, error ?? { code })} action={<Button variant="secondary" onPress={() => navigate("/")}>{i18n.t("ui.nav.start")}</Button>}>
          {code === "CORRUPTED_ASSESSMENT" ? i18n.t("ui.state.corrupted_text") : undefined}
        </Banner>
      </Page>
    );
  }
  switch (section) {
    case "profile": return <WizardView />;
    case "classification": return <ClassificationView />;
    case "requirements": return <RequirementsView />;
    case "gaps": return <GapLensView />;
    case "evidence": return <EvidenceView />;
    case "report": return <ReportView />;
    case "history": return <HistoryView />;
  }
}
