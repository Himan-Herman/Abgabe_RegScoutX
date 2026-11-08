"""Domain-Fehler des fachlichen Kerns. Alle Fehler sind fail-closed: Es gibt keine stillen Ersatzwerte."""

from __future__ import annotations

from typing import Any


class RegScoutXError(Exception):
    """Basisklasse aller Domain-Fehler."""


class CatalogValidationError(RegScoutXError):
    """Ein Katalog ist nicht lesbar oder nicht schemakonform; es wird nichts ausgewertet."""

    def __init__(self, errors: list[str]) -> None:
        self.errors = tuple(errors)
        super().__init__(f"catalog validation failed with {len(errors)} error(s): "
                         + "; ".join(errors[:5]))


class UnknownRuleError(RegScoutXError):
    def __init__(self, rule_id: Any) -> None:
        self.rule_id = rule_id
        super().__init__(f"unknown rule '{rule_id}'")


class UnknownRequirementError(RegScoutXError):
    def __init__(self, requirement_id: Any) -> None:
        self.requirement_id = requirement_id
        super().__init__(f"unknown requirement '{requirement_id}'")


class UnknownOutputError(RegScoutXError):
    def __init__(self, output: Any) -> None:
        self.output = output
        super().__init__(f"unknown rule output '{output}'")


class InvalidInputError(RegScoutXError):
    """Eine Eingabe ist unbekannt, abgeleitet oder liegt außerhalb der zulässigen Werte."""

    def __init__(self, input_key: str, value: Any, reason: str) -> None:
        self.input_key = input_key
        self.value = value
        self.reason = reason
        super().__init__(f"invalid input '{input_key}'={value!r}: {reason}")


class MissingInputError(RegScoutXError):
    """Ein entscheidungsnotwendiger Wert fehlt, obwohl ein vollständiges Ergebnis verlangt wurde."""

    def __init__(self, rule_id: str, input_key: str) -> None:
        self.rule_id = rule_id
        self.input_key = input_key
        super().__init__(f"missing input '{input_key}' required by {rule_id}")


class InvalidRuleReferenceError(RegScoutXError):
    def __init__(self, rule_id: str, target: Any) -> None:
        self.rule_id = rule_id
        self.target = target
        super().__init__(f"{rule_id}: next rule '{target}' does not exist")


class RuleCycleError(RegScoutXError):
    def __init__(self, rule_id: str) -> None:
        self.rule_id = rule_id
        super().__init__(f"rule execution revisited {rule_id}")


class UnexpectedEndStateError(RegScoutXError):
    def __init__(self, rule_id: str, detail: str) -> None:
        self.rule_id = rule_id
        super().__init__(f"{rule_id}: unexpected end state: {detail}")


class CatalogVersionMismatchError(RegScoutXError):
    """Eine Bewertung ist an andere Katalogversionen gebunden als die geladenen (SR-037)."""

    def __init__(self, fixed: Any, loaded: Any) -> None:
        self.fixed = fixed
        self.loaded = loaded
        super().__init__(f"assessment is bound to {fixed}, loaded catalogs are {loaded}")


class UnsupportedDerivationError(RegScoutXError):
    """Ein abgeleiteter Eingabewert kann nicht nach den festgelegten Ableitungsregeln bestimmt werden."""

    def __init__(self, rule_id: str, input_key: str) -> None:
        self.rule_id = rule_id
        self.input_key = input_key
        super().__init__(f"{rule_id}: no supported derivation for '{input_key}'")


class AssessmentStateError(RegScoutXError):
    """Die Operation ist im aktuellen Zustand bzw. Versionsabgleich der Bewertung nicht zulässig."""

    def __init__(self, assessment_id: Any, operation: str, reason: str) -> None:
        self.assessment_id = assessment_id
        self.operation = operation
        self.reason = reason
        super().__init__(f"{operation} not allowed for assessment '{assessment_id}': {reason}")


class AssessmentNotFoundError(RegScoutXError):
    def __init__(self, assessment_id: Any) -> None:
        self.assessment_id = assessment_id
        super().__init__(f"assessment '{assessment_id}' not found")


class PersistenceError(RegScoutXError):
    """Gespeicherte Bewertung ist beschädigt, nicht schemakonform oder verletzt die Anhängeregel; nichts wird ausgewertet."""

    def __init__(self, assessment_id: Any, reason: str) -> None:
        self.assessment_id = assessment_id
        self.reason = reason
        super().__init__(f"assessment '{assessment_id}': {reason}")


class I18nError(RegScoutXError):
    """Sprachressource fehlt oder ist unvollständig; es wird nicht in eine andere Sprache ausgewichen."""

    def __init__(self, language: Any, reason: str) -> None:
        self.language = language
        self.reason = reason
        super().__init__(f"i18n ({language}): {reason}")


class ReportGenerationError(RegScoutXError):
    """Bericht konnte nicht erzeugt werden; gespeicherte Bewertung und Audit bleiben unverändert (SR-036)."""

    def __init__(self, assessment_id: Any, revision: Any, reason: str) -> None:
        self.assessment_id = assessment_id
        self.revision = revision
        self.reason = reason
        super().__init__(f"report for assessment '{assessment_id}' revision {revision} "
                         f"could not be generated: {reason}")
