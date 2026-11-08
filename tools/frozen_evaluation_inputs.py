"""Hashgebundene Kataloge der historischen R1/R2-Referenz, keine Arbeitskataloge.

Gemeinsame Lesefunktion für Referenz-Reproduktion und TC-061. Die Dateien
werden ausschließlich gelesen; der aktuelle Demonstrator verwendet sie nicht.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

import yaml


FROZEN_INPUTS = {
    "rul_catalog": (
        "docs/08-evaluation/frozen/RUL_CATALOG_0.2.yaml", "0.2",
        "2db67d46d097eadcff27b2ac36b3c2eb5fd5d6ac4c4d2ba0367e1a937865df0b"),
    "rr_applicability": (
        "docs/08-evaluation/frozen/RR_APPLICABILITY_0.4.yaml", "0.4",
        "58e5b8ff7022e31520b79ce3bf225510b70948b7c91b63adf65a6344687104be"),
    "rr_measure": (
        "docs/08-evaluation/frozen/RR_MEASURE_CATALOG_0.1.yaml", "0.1",
        "3b8fffa428212207d4eb6d2443e84f9c1c8071b325102c920d5ce9b2e0cf544d"),
}


def load_evaluated_catalog(root: Path, name: str) -> dict[str, Any]:
    relative, version, expected_hash = FROZEN_INPUTS[name]
    data = (root / relative).read_bytes()
    if hashlib.sha256(data).hexdigest() != expected_hash:
        raise ValueError(f"{relative} differs from the frozen evaluation catalog")
    catalog = yaml.safe_load(data)
    if not isinstance(catalog, dict) or catalog.get("version") != version:
        raise ValueError(f"{relative} has an unexpected evaluation version")
    return catalog
