"""Einzige Brücke zu den Repository-Validatoren unter tools/ (ADR-0003).

Der fachliche Kern baut keine zweite Parser- oder Validierungslogik auf,
sondern nutzt die bestehenden Validatoren und deren YAML-Loader.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

TOOLS_DIR = Path(__file__).resolve().parent.parent / "tools"
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import traceability  # noqa: E402
import validate_data_model  # noqa: E402
import validate_rr_applicability  # noqa: E402
import validate_rr_catalog  # noqa: E402
import validate_rr_measures  # noqa: E402
import validate_rul_catalog  # noqa: E402
import validate_sr_catalog  # noqa: E402
import validate_standards_mapping  # noqa: E402

REPO_ROOT = validate_rr_catalog.REPO_ROOT
LOAD_ERRORS = (validate_rr_catalog.ReferenceDataError, validate_rr_catalog.CatalogLoadError)

PATHS = {
    "sources": validate_rr_catalog.SOURCES_PATH,
    "rr": validate_rr_catalog.CATALOG_PATH,
    "rul": validate_rul_catalog.CATALOG_PATH,
    "sr": validate_sr_catalog.CATALOG_PATH,
    "data_model": validate_data_model.MODEL_PATH,
    "rr_applicability": validate_rr_applicability.MAPPING_PATH,
    "standards_mapping": validate_standards_mapping.MAPPING_PATH,
    "rr_measure": validate_rr_measures.CATALOG_PATH,
}
VOCABULARY_PATH = validate_rr_catalog.VOCABULARY_PATH


def load_yaml(path: Path) -> Any:
    return validate_rr_catalog.load_catalog(path)


def validation_errors(repo_root: Path) -> list[str]:
    """Alle Validatoren und die Verweisintegrität prüfen; Befunde sammeln."""
    errors: list[str] = []
    for prefix, check in (
        ("RR", validate_rr_catalog.validate_repository),
        ("RUL", validate_rul_catalog.validate_repository),
        ("SR", validate_sr_catalog.validate_repository),
        ("DATA_MODEL", validate_data_model.validate_repository),
        ("RR_APPLICABILITY", validate_rr_applicability.validate_repository),
        ("STANDARDS_MAPPING", validate_standards_mapping.validate_repository),
        ("RR_MEASURE", validate_rr_measures.validate_repository),
    ):
        errors.extend(f"{prefix}: {error}" for error in check(repo_root))
    if errors:
        return errors
    artifacts = traceability.Artifacts(
        rr_catalog=load_yaml(repo_root / PATHS["rr"]),
        rul_catalog=load_yaml(repo_root / PATHS["rul"]),
        sr_catalog=load_yaml(repo_root / PATHS["sr"]),
        reference=validate_sr_catalog.load_reference_data(repo_root),
        applicability=load_yaml(repo_root / PATHS["rr_applicability"]),
        standards_mapping=load_yaml(repo_root / PATHS["standards_mapping"]),
        measure_catalog=load_yaml(repo_root / PATHS["rr_measure"]),
    )
    links = traceability.collect_links(artifacts)
    return [f"TRACEABILITY: {error}" for error in traceability.check_integrity(artifacts, links)]
