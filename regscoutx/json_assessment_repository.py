"""Lokale JSON-Dateipersistenz des ASSESSMENT_REPOSITORY (ADR-0005).

Eine Datei <assessment_id>.json je Bewertung in einem Wurzelverzeichnis. Die
Kennung ist eine kanonische UUID, sodass kein Pfad außerhalb der Wurzel
entstehen kann. Schreiben erfolgt atomisch über eine temporäre Datei im selben
Verzeichnis, fsync und os.replace; Dateien sind nur für den Eigentümer lesbar.
Keine Netzwerkzugriffe, keine Protokollausgaben.
"""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from typing import Any, Mapping

from regscoutx.assessment_repository import AssessmentRepository, checked_assessment_id
from regscoutx.errors import InvalidInputError, PersistenceError

SUFFIX = ".json"


class JsonFileAssessmentRepository(AssessmentRepository):

    def __init__(self, root: Path | str) -> None:
        self._root = Path(root).resolve()
        self._root.mkdir(mode=0o700, parents=True, exist_ok=True)

    def _path(self, assessment_id: str) -> Path:
        path = (self._root / f"{checked_assessment_id(assessment_id)}{SUFFIX}").resolve()
        if path.parent != self._root:
            raise PersistenceError(assessment_id, "storage path outside repository root")
        return path

    def exists(self, assessment_id: str) -> bool:
        return self._path(assessment_id).is_file()

    def assessment_ids(self) -> tuple[str, ...]:
        ids = []
        for path in self._root.glob(f"*{SUFFIX}"):
            try:
                ids.append(checked_assessment_id(path.stem))
            except InvalidInputError:
                continue
        return tuple(sorted(ids))

    def _read(self, assessment_id: str) -> Any:
        try:
            with self._path(assessment_id).open(encoding="utf-8") as handle:
                return json.load(handle)
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise PersistenceError(assessment_id, f"unreadable document: {type(exc).__name__}") from exc

    def _write(self, assessment_id: str, document: Mapping[str, Any]) -> None:
        target = self._path(assessment_id)
        handle = tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=self._root,
                                             prefix=".tmp-", suffix=SUFFIX, delete=False)
        try:
            with handle:
                os.chmod(handle.name, 0o600)
                json.dump(document, handle, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
                          allow_nan=False)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(handle.name, target)
        except BaseException:
            Path(handle.name).unlink(missing_ok=True)
            raise
