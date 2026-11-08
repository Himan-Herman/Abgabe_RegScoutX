# EV-011 — Eingefrorene Referenzbewertung der Fallstudie (vor dem Evaluationslauf)

Version 1.0 · Status: aktiv · Datum: 28.09.2026

| Merkmal | Angabe |
| --- | --- |
| Evidenztyp | Referenzbewertung (manuell adjudizierte Schicht aus EV-003, regelbasierte Ableitung für alle 959 RR) |
| Artefakt | [REFERENCE_ASSESSMENT.yaml](../08-evaluation/REFERENCE_ASSESSMENT.yaml), Referenzversion 1.0 |
| SHA-256 der Referenzdatei | `45cf843e993eb7c9fc17dfeb810541b667087bbbd3effc726188d04f6ad2fc66` |
| Ableitung | `tools/derive_case_reference.py` (ohne Abhängigkeit von `regscoutx/`, reproduzierbar mit `--check`) |
| Validierung | `tools/validate_reference_assessment.py` PASS (Struktur, Codes, alle 959 RR, Szenario, Zirkularitätsschutz, Hash) |
| Katalogstände | RR_CATALOG 0.26 · RUL_CATALOG 0.2 · RR_APPLICABILITY 0.4 · RR_MEASURE 0.1 · DATA_MODEL 0.8 |
| Evaluierter Softwarestand | Commit `ee76ef8` (unverändert bis zum Evaluationslauf) |
| Bezug | TC-036 (Basisfall), [CASE_STUDY.md](../08-evaluation/CASE_STUDY.md), [EVALUATION_METHOD.md](../08-evaluation/EVALUATION_METHOD.md) |

Die Referenz wurde **vor** jedem Lauf des Demonstrators für die Fallstudie erstellt und mit diesem Nachweis im Referenz-Freeze-Commit festgehalten. Sie ist nicht aus einem Bewertungs-, Bericht- oder API-Ergebnis exportiert. Die Ableitung prüft sich gegen die manuell adjudizierten Teile von TC-036: 16 unabhängig nachgerechnete Blockzustände, 22 entscheidungskritische RR (Status und Begründung), scope-inaktiv 70 und scope-ungeklärt 0 – ohne Abweichung.

Inhalt: Referenzstatus aller 959 RR (542 `APPLICABLE`, 128 `NOT_APPLICABLE`, 289 `APPLICABILITY_UNRESOLVED`) mit Begründungscode und Referenzregel; Gap-Referenz-Umfang von 32 RR mit Szenarioangaben und erwarteten Ergebnissen; Stichprobe von 11 RR für die Nachvollziehbarkeitsprüfung; Referenzauslegungen RI-1 bis RI-5.

Grenzen: Referenz und Demonstrator stammen vom selben Projektbearbeiter; die regelbasierte Ableitung setzt dieselbe dokumentierte Methodik um (siehe EVALUATION_METHOD.md Abschnitt 2); kein unabhängiger Goldstandard, kein Expertenreview.

Bewertung: **PASS** (Referenz vollständig, validiert und eingefroren).
