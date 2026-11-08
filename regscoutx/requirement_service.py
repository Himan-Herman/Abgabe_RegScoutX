"""REQUIREMENT_SERVICE: Lesesicht auf eine RR mit Texten, Quellen, Lebenszyklus und Maßnahmen.

Alle Inhalte stammen unverändert aus den versionierten Katalogen über den
CATALOG_REPOSITORY (SR-011, SR-041, SR-043). Es werden keine Texte ausgewertet
und keine Maßnahmen oder Nachweise erzeugt.
"""

from __future__ import annotations

from dataclasses import dataclass

from regscoutx.catalog_repository import CatalogRepository
from regscoutx.domain import Language


@dataclass(frozen=True)
class MeasureView:
    measure_key: str
    label: str
    evidence_types: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class RequirementView:
    requirement_id: str
    title: str
    text: str
    primary_sources: tuple[str, ...]
    supplementary_sources: tuple[str, ...]
    theme_cluster: str
    lifecycle_phases: tuple[tuple[str, str], ...]
    measure_status: str
    measures: tuple[MeasureView, ...]


class RequirementService:
    """Liefert RR in der gewählten Sprache; Codes bleiben sprachneutral."""

    def __init__(self, repository: CatalogRepository) -> None:
        self._repository = repository

    def view(self, requirement_id: str, language: Language) -> RequirementView:
        entry = self._repository.requirement(requirement_id)
        mapping = self._repository.measure_mapping(requirement_id)
        measures = []
        for key in mapping["measures"]:
            measure = self._repository.measure(key)
            measures.append(MeasureView(
                measure_key=key,
                label=measure["label"][language.value],
                evidence_types=tuple(
                    (evidence, self._repository.evidence_type(evidence)["label"][language.value])
                    for evidence in measure["evidence_types"]),
            ))
        return RequirementView(
            requirement_id=requirement_id,
            title=entry["title"][language.value],
            text=entry["requirement_text"][language.value],
            primary_sources=tuple(entry["sources"]["primary"]),
            supplementary_sources=tuple(entry["sources"]["supplementary"]),
            theme_cluster=entry["theme_cluster"],
            lifecycle_phases=tuple((phase, self._repository.phase_label(phase, language))
                                   for phase in entry["lifecycle_phases"]),
            measure_status=mapping["status"],
            measures=tuple(measures),
        )
