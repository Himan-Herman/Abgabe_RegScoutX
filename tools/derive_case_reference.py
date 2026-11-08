"""Referenzableitung der Fallstudie (Block 6) – unabhängig vom Demonstrator.

Erzeugt docs/08-evaluation/REFERENCE_ASSESSMENT.yaml ausschließlich aus
- dem manuell adjudizierten Referenzfall TC-036 (Profil, Entscheidungen, Blockzustände;
  docs/07-testing/TC_CATALOG.yaml, Herleitung in EV-003),
- der dokumentierten Applicability-Zuordnung (docs/03-regulatory/RR_APPLICABILITY.yaml)
  und ihrer dokumentierten Auswertungssemantik (RR_APPLICABILITY_MAPPING.md, ARCHITECTURE.md
  Abschnitt 8, DATA_MODEL.yaml RequirementResult),
- RR_CATALOG.yaml (Themencluster, Quellen, Lebenszyklusphasen) und RR_MEASURE_CATALOG.yaml,
- den in diesem Werkzeug festgelegten, vor dem Systemlauf eingefrorenen Szenarioregeln.

Das Werkzeug importiert bewusst keinen Code aus `regscoutx/` und liest keine Bewertungs-,
Bericht- oder Laufzeitartefakte (geprüft durch tools/validate_reference_assessment.py).
Es ist eine zweite, eigenständige Umsetzung der dokumentierten Regeln (N-Version-Prinzip);
Referenzauslegungen, wo die Dokumentation mehrdeutig ist, stehen als RI-1 bis RI-5 im Artefakt.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

from frozen_evaluation_inputs import FROZEN_INPUTS, load_evaluated_catalog

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT = Path("docs/08-evaluation/REFERENCE_ASSESSMENT.yaml")
INPUTS = {
    "tc_catalog": Path("docs/07-testing/TC_CATALOG.yaml"),
    "rr_applicability": Path("docs/03-regulatory/RR_APPLICABILITY.yaml"),
    "rr_catalog": Path("docs/03-regulatory/RR_CATALOG.yaml"),
    "rr_measure": Path("docs/03-regulatory/RR_MEASURE_CATALOG.yaml"),
    "rul_catalog": Path("docs/03-regulatory/RUL_CATALOG.yaml"),
    "vocabulary": Path("docs/03-regulatory/CONTROLLED_VOCABULARY.md"),
}
# Unter `inputs` der Referenz bleiben die Pfade zum Zeitpunkt des Freeze
# vermerkt; fortgeschriebene Kataloge werden ausschließlich hashgebunden gelesen.
BASE_CASE = "TC-036"
REFERENCE_VERSION = "1.0"
# Zyklus der Erfüllungsangaben im Szenario (Menge A): (Status, mit Nachweisreferenz)
CYCLE = (("FULFILLED", True), ("PARTIALLY_FULFILLED", True), ("NOT_FULFILLED", False),
         ("FULFILLED", False), ("NOT_ASSESSED", False), ("PARTIALLY_FULFILLED", False))
JUSTIFICATION = "Synthetische Fallstudienangabe (Block 6, Szenario laut REFERENCE_ASSESSMENT.yaml)"

TRUE, FALSE, UNKNOWN = "TRUE", "FALSE", "UNKNOWN"


def load(name: str) -> Any:
    if name in FROZEN_INPUTS:
        return load_evaluated_catalog(REPO_ROOT, name)
    return yaml.safe_load((REPO_ROOT / INPUTS[name]).read_text(encoding="utf-8"))


def theme_order() -> list[str]:
    text = (REPO_ROOT / INPUTS["vocabulary"]).read_text(encoding="utf-8")
    return [t.strip() for t in re.findall(r"^### 1\.\d+\s+(.+?)\s*$", text, re.MULTILINE)]


class Predicates:
    """Dreiwertige Auswertung nach ARCHITECTURE.md Abschnitt 8 (Kleene-Logik für ALL_OF/ANY_OF)."""

    def __init__(self, spec: dict, profile: dict, decisions: dict) -> None:
        self.spec, self.profile, self.decisions = spec, profile, decisions

    def value(self, name: str) -> str:
        p = self.spec[name]
        kind = p["kind"]
        if kind == "PROFILE_INPUT":
            if p["input"] not in self.profile:
                return UNKNOWN  # fehlende Eingabe: fail-closed
            v = self.profile[p["input"]]
            if v in (p.get("unknown_values") or []):
                return UNKNOWN
            return TRUE if v in p["true_values"] else FALSE
        if kind == "MDR_CLASS":
            d = self.decisions.get(p["area"])
            if not d or d["status"] != "DECIDED" or not d.get("mdr_class"):
                return UNKNOWN
            return TRUE if d["mdr_class"] in p["classes"] else FALSE
        if kind == "DECISION_OUTCOME":
            for item in p.get("true_if") or []:
                d = self.decisions.get(item["area"])
                if d and d["status"] == "DECIDED" and d["outcome"] == item["outcome"]:
                    return TRUE
            for item in p.get("false_if") or []:
                d = self.decisions.get(item["area"])
                if d and d["status"] == "DECIDED" and d["outcome"] == item["outcome"]:
                    return FALSE
            return UNKNOWN
        if kind == "NOT_MODELLED":
            return UNKNOWN
        parts = [self.value(q) for q in p["of"]]
        if kind == "ALL_OF":
            return FALSE if FALSE in parts else (UNKNOWN if UNKNOWN in parts else TRUE)
        if kind == "ANY_OF":
            return TRUE if TRUE in parts else (UNKNOWN if UNKNOWN in parts else FALSE)
        raise ValueError(f"unknown predicate kind {kind}")

    def conjunction(self, names: list[str]) -> str:
        values = [self.value(n) for n in names]
        return FALSE if FALSE in values else (UNKNOWN if UNKNOWN in values else TRUE)


def applicability(entry: dict, block_state: str, preds: Predicates) -> tuple[str, str, str]:
    """(Status, Begründungscode, Referenzregel) je RR."""
    if block_state == "INACTIVE":
        return "NOT_APPLICABLE", "SCOPE_INACTIVE", "RB-1 Block inaktiv"
    if block_state == "UNRESOLVED":
        return "APPLICABILITY_UNRESOLVED", "SCOPE_UNRESOLVED", "RB-2 Block ungeklärt"
    if entry["conditionality"] == "NOT_STATED":
        return "APPLICABILITY_UNRESOLVED", "CONDITIONALITY_NOT_DOCUMENTED", "RB-3 Einordnung nicht dokumentiert"
    if entry["conditionality"] == "REGULAR":
        return "APPLICABLE", "SCOPE_ACTIVE", "RB-4 regulär, Block aktiv"
    local = entry["local"] or []
    modelled = preds.conjunction(local) if local else TRUE
    not_modelled = bool(entry["local_not_modelled"])
    if modelled == FALSE:
        # RI-1: Konjunktion – eine nicht erfüllte modellierte Bedingung schließt aus.
        return "NOT_APPLICABLE", "LOCAL_CONDITION_NOT_MET", "RB-5 lokale Bedingung nicht erfüllt"
    if not_modelled:
        # RI-2: nicht modellierte Bedingung vor fehlender Eingabe (beide ungeklärt).
        return "APPLICABILITY_UNRESOLVED", "LOCAL_CONDITION_NOT_MODELLED", "RB-6 nicht modellierte lokale Bedingung"
    if modelled == UNKNOWN:
        return "APPLICABILITY_UNRESOLVED", "LOCAL_CONDITION_UNRESOLVED", "RB-7 lokale Eingabe fehlt oder unbestimmt"
    if not local:
        return "APPLICABLE", "SCOPE_ACTIVE", "RB-8 bedingt ohne lokale Bedingung, Block aktiv"
    return "APPLICABLE", "LOCAL_CONDITIONS_MET", "RB-9 alle lokalen Bedingungen erfüllt"


def expected_gap(applicable: str, answer: dict | None) -> dict:
    """Ableitungstabelle ARCHITECTURE.md Abschnitt 8 / DATA_MODEL RequirementResult (RI-3 Nachweisstatus)."""
    has_evidence = bool(answer and answer["with_evidence"])
    if applicable == "NOT_APPLICABLE":
        return {"gap_status": "NOT_APPLICABLE", "gap_reason": "RR_NOT_APPLICABLE", "is_gap": False,
                "answer_state": "INACTIVE" if answer else None, "evidence_state": "NOT_CONSIDERED"}
    if applicable == "APPLICABILITY_UNRESOLVED":
        return {"gap_status": "APPLICABILITY_UNRESOLVED", "gap_reason": "RR_APPLICABILITY_UNRESOLVED",
                "is_gap": False, "answer_state": "INACTIVE" if answer else None,
                "evidence_state": "NOT_CONSIDERED"}
    evidence_state = "EVIDENCE_REFERENCED" if has_evidence else "NO_EVIDENCE_REFERENCED"
    base = {"answer_state": "ACTIVE" if answer else None, "evidence_state": evidence_state}
    if answer is None:
        return {"gap_status": "NOT_ASSESSED", "gap_reason": "NO_ANSWER", "is_gap": False, **base}
    status = answer["status"]
    if status == "NOT_ASSESSED":
        return {"gap_status": "NOT_ASSESSED", "gap_reason": "ANSWER_NOT_ASSESSED", "is_gap": False, **base}
    if status == "NOT_FULFILLED":
        return {"gap_status": "NOT_FULFILLED", "gap_reason": "ANSWER_NOT_FULFILLED", "is_gap": True, **base}
    if has_evidence:
        return {"gap_status": status, "gap_reason": "ANSWER_WITH_EVIDENCE",
                "is_gap": status == "PARTIALLY_FULFILLED", **base}
    return {"gap_status": "EVIDENCE_REVIEW_REQUIRED", "gap_reason": "ANSWER_WITHOUT_EVIDENCE", "is_gap": True, **base}


def source_family(entry: dict) -> str:
    primary = (entry["sources"].get("primary") or [""])[0].split("#")[0]
    return {"SRC-001": "MDR", "SRC-002": "AI_ACT", "SRC-009": "EIFU"}.get(primary, "NORM" if primary else "NONE")


def derive() -> dict:
    tc = next(t for t in load("tc_catalog")["test_cases"] if t["id"] == BASE_CASE)
    golden = tc["golden_case"]
    profile = {k: v for inputs in golden["rule_inputs"].values() for k, v in inputs.items()}
    profile.update(golden["profile"])
    decisions = golden["expected_decisions"]
    mapping = load("rr_applicability")
    preds = Predicates(mapping["predicates"], profile, decisions)
    rr_catalog = {r["id"]: r for r in load("rr_catalog")["requirements"]}
    measures = load("rr_measure")["requirements"]

    # Blockzustände: manuell adjudiziert (TC-036); zusätzlich eigenständig nachgerechnet.
    block_states = golden["expected_block_states"]
    recomputed = {b: {TRUE: "ACTIVE", FALSE: "INACTIVE", UNKNOWN: "UNRESOLVED"}[preds.conjunction(s["scope"])]
                  for b, s in mapping["blocks"].items()}
    if recomputed != block_states:
        raise SystemExit(f"block states differ from adjudication: {recomputed}")

    applicability_ref = {}
    for rr_id in sorted(rr_catalog):
        entry = mapping["requirements"].get(rr_id)
        if entry is None:
            applicability_ref[rr_id] = ("APPLICABILITY_UNRESOLVED", "NO_MAPPING", "RB-0 keine Zuordnung", None)
            continue
        status, reason, rule = applicability(entry, block_states[entry["block"]], preds)
        applicability_ref[rr_id] = (status, reason, rule, entry["block"])

    # Abgleich mit den manuell adjudizierten Teilen von TC-036
    for rr_id, (status, reason) in golden["expected_requirements"].items():
        if applicability_ref[rr_id][:2] != (status, reason):
            raise SystemExit(f"{rr_id} differs from adjudicated reference")
    inactive = sum(1 for v in applicability_ref.values() if v[1] == "SCOPE_INACTIVE")
    unresolved_scope = sum(1 for v in applicability_ref.values() if v[1] == "SCOPE_UNRESOLVED")
    if (inactive, unresolved_scope) != (golden["expected_scope_totals"]["inactive"],
                                        golden["expected_scope_totals"]["unresolved"]):
        raise SystemExit("scope totals differ from adjudicated reference")

    # Gap-Referenz-Umfang (vor dem Systemlauf festgelegt, nur aus Referenz und Katalogen)
    themes = theme_order()
    applicable = [r for r in sorted(rr_catalog) if applicability_ref[r][0] == "APPLICABLE"]
    cond = {r: mapping["requirements"][r]["conditionality"] for r in applicable}
    mstat = {r: measures[r]["status"] for r in rr_catalog}
    scope: list[dict] = []
    chosen: set[str] = set()

    def pick(pool: list[str], predicate) -> str | None:
        for r in pool:
            if r not in chosen and predicate(r):
                chosen.add(r)
                return r
        return None

    set_a, set_b = [], []
    for theme in themes:
        pool = [r for r in applicable if rr_catalog[r]["theme_cluster"] == theme]
        picks = [
            ("A1 regulär, Maßnahme zugeordnet", lambda r: cond[r] == "REGULAR" and mstat[r] == "MAPPED"),
            ("A2 bedingt, Maßnahme zugeordnet", lambda r: cond[r] == "CONDITIONAL" and mstat[r] == "MAPPED"),
            ("A3 Maßnahmenzuordnung offen", lambda r: mstat[r] == "REVIEW_REQUIRED"),
        ]
        families = set()
        for label, predicate in picks:
            r = pick(pool, predicate)
            if r:
                set_a.append((r, label))
                families.add(source_family(rr_catalog[r]))
        # A4: erste weitere RR einer in diesem Themencluster noch nicht vertretenen Quellenfamilie
        r = pick(pool, lambda x: source_family(rr_catalog[x]) not in families)
        if r:
            set_a.append((r, "A4 weitere Quellenfamilie"))
        # B: repräsentative anwendbare RR ohne Erfüllungsangabe
        r = pick(pool, lambda x: True)
        if r:
            set_b.append((r, "B ohne Erfüllungsangabe"))

    # D: je Rechts- bzw. Normquelle mindestens eine RR, sofern noch nicht vertreten
    def primary(r: str) -> str:
        return (rr_catalog[r]["sources"].get("primary") or [""])[0].split("#")[0]
    covered = {primary(r) for r, _ in set_a + set_b}
    for src in ("SRC-001", "SRC-002", "SRC-005", "SRC-006", "SRC-007", "SRC-008"):
        if src not in covered:
            r = pick(applicable, lambda x, s=src: primary(x) == s)
            if r:
                set_a.append((r, f"D Quelle {src} noch nicht vertreten"))

    answers: dict[str, dict] = {}
    for index, (r, _) in enumerate(set_a):
        status, with_evidence = CYCLE[index % len(CYCLE)]
        answers[r] = {"status": status, "with_evidence": with_evidence}

    # C: Erfüllungsangaben an nicht anwendbaren bzw. ungeklärten RR (Ableitungstabelle Zeilen 1–2)
    ordered = sorted(rr_catalog)
    set_c = []
    for label, predicate, status, with_evidence in (
            ("C1 ungeklärt (nicht dokumentierte Einordnung)",
             lambda r: applicability_ref[r][1] == "CONDITIONALITY_NOT_DOCUMENTED", "FULFILLED", True),
            ("C2 ungeklärt (nicht modellierte lokale Bedingung)",
             lambda r: applicability_ref[r][1] == "LOCAL_CONDITION_NOT_MODELLED", "NOT_FULFILLED", False),
            ("C3 nicht anwendbar (Block inaktiv)",
             lambda r: applicability_ref[r][1] == "SCOPE_INACTIVE" and mstat[r] == "MAPPED",
             "PARTIALLY_FULFILLED", True)):
        r = pick(ordered, predicate)
        set_c.append((r, label))
        answers[r] = {"status": status, "with_evidence": with_evidence}

    evidence = []
    for r, answer in answers.items():
        if answer["with_evidence"]:
            mapped = measures[r]["measures"] if measures[r]["status"] == "MAPPED" else []
            evidence_id = f"CS-EV-{r}"  # szenariolokale Kennung; die Anwendung vergibt eigene IDs
            answer["evidence_id"] = evidence_id
            evidence.append({"evidence_id": evidence_id, "requirement_id": r,
                             "title": f"Fallstudie: Nachweis zu {r}", "document_identifier": f"CS-DOC-{r}",
                             "document_version": "1.0", "location": None,
                             "measure_key": mapped[0] if mapped else None})

    for r, label in set_a + set_b + set_c:
        entry = rr_catalog[r]
        status, reason, rule, block = applicability_ref[r]
        answer = answers.get(r)
        scope.append({
            "requirement_id": r, "stratum": label, "theme": entry["theme_cluster"],
            "source_family": source_family(entry), "conditionality": mapping["requirements"][r]["conditionality"],
            "block": block, "applicability": status, "applicability_reason": reason,
            "scenario_input": None if answer is None else
            {"status": answer["status"], "with_evidence": answer["with_evidence"]},
            **expected_gap(status, answer),
            "measure_status": measures[r]["status"], "measures": list(measures[r]["measures"]),
            "primary_sources": list(entry["sources"].get("primary") or []),
            "supplementary_sources": list(entry["sources"].get("supplementary") or []),
            "lifecycle": list(entry["lifecycle_phases"]),
        })

    # Stichprobe Nachvollziehbarkeit: je Themencluster die erste RR aus A plus C1–C3
    sample = []
    for theme in themes:
        first = next((r for r, _ in set_a if rr_catalog[r]["theme_cluster"] == theme), None)
        if first:
            sample.append(first)
    sample += [r for r, _ in set_c]

    counts = {s: sum(1 for v in applicability_ref.values() if v[0] == s)
              for s in ("APPLICABLE", "NOT_APPLICABLE", "APPLICABILITY_UNRESOLVED")}
    return {
        "reference_version": REFERENCE_VERSION,
        "status": "frozen",
        "provenance": {
            "kind": "manual_and_rule_derived_reference",
            "author": "Projektbearbeiter (Masterarbeit RegScoutX)",
            "base_case": BASE_CASE,
            "adjudicated_basis": "TC-036 golden_case (Profil, Regelpfade, Entscheidungen, 16 Blockzustände, "
                                 "22 entscheidungskritische RR, Scope-Summen) – manuelle Herleitung EV-003",
            "derivation_tool": "tools/derive_case_reference.py (keine Abhängigkeit von regscoutx/)",
            "inputs": {name: str(path) for name, path in INPUTS.items()},
            "not_derived_from": "keinem Bewertungs-, Bericht-, API- oder Laufzeitartefakt des Demonstrators",
            "consistency_checks": [
                "16 Blockzustände unabhängig nachgerechnet = adjudizierte Blockzustände",
                "22 entscheidungskritische RR (Status und Begründung) = adjudizierte Werte",
                f"scope-inaktiv {inactive} und scope-ungeklärt {unresolved_scope} = adjudizierte Summen",
            ],
        },
        "catalog_versions": {"rr_catalog": load("rr_catalog")["version"], "rul_catalog": load("rul_catalog")["version"],
                             "rr_applicability": mapping["version"], "rr_measure": load("rr_measure")["version"]},
        "interpretations": {
            "RI-1": "Lokale Bedingungen sind eine Konjunktion (dreiwertig); eine nicht erfüllte modellierte "
                    "Bedingung ergibt NOT_APPLICABLE auch dann, wenn zusätzlich eine nicht modellierte "
                    "Bedingung dokumentiert ist.",
            "RI-2": "Ist keine modellierte Bedingung falsch, geht eine dokumentierte nicht modellierte Bedingung "
                    "als Begründung LOCAL_CONDITION_NOT_MODELLED vor einer fehlenden Eingabe "
                    "(LOCAL_CONDITION_UNRESOLVED); der Status ist in beiden Fällen APPLICABILITY_UNRESOLVED.",
            "RI-3": "Bei anwendbaren RR: evidence_state EVIDENCE_REFERENCED genau bei mindestens einer "
                    "zugeordneten Nachweisreferenz, sonst NO_EVIDENCE_REFERENCED; bei nicht anwendbaren bzw. "
                    "ungeklärten RR NOT_CONSIDERED (DATA_MODEL RequirementResult).",
            "RI-4": "Fehlende Profileingaben (im Referenzfall nicht angegeben) ergeben UNKNOWN (fail-closed).",
            "RI-5": "Bedingte RR ohne lokale und ohne nicht modellierte Bedingung sind bei aktivem Block "
                    "APPLICABLE mit SCOPE_ACTIVE (wie die adjudizierten RR-174, RR-360, RR-376).",
        },
        "case_profile": profile,
        "expected_decisions": decisions,
        "expected_block_states": block_states,
        "applicability_totals": counts,
        "applicability": {r: {"status": v[0], "reason": v[1], "rule": v[2], "block": v[3]}
                          for r, v in applicability_ref.items()},
        "scenario": {
            "justification": JUSTIFICATION,
            "answers": {r: {"status": a["status"], "evidence_id": a.get("evidence_id")} for r, a in answers.items()},
            "evidence": evidence,
            "cycle": [f"{s}{' mit Nachweis' if e else ''}" for s, e in CYCLE],
        },
        "gap_scope": scope,
        "traceability_sample": sample,
    }


def main() -> int:
    reference = derive()
    text = ("# Eingefrorene Referenzbewertung der Fallstudie (Block 6). Erzeugt mit tools/derive_case_reference.py\n"
            "# vor dem Evaluationslauf; nicht aus Laufzeitergebnissen abgeleitet. Nicht nachträglich ändern.\n")
    text += yaml.safe_dump(reference, allow_unicode=True, sort_keys=False, width=110)
    target = REPO_ROOT / OUTPUT
    if "--check" in sys.argv:
        return 0 if target.read_text(encoding="utf-8") == text else 1
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    print(f"{OUTPUT}: {reference['applicability_totals']}, gap scope {len(reference['gap_scope'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
