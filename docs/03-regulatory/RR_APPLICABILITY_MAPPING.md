# Nachweis der RR-Applicability-Zuordnung

Version 1.5 · Status: aktiv

Dieser Nachweis dokumentiert, wie [RR_APPLICABILITY.yaml](RR_APPLICABILITY.yaml) (Version 0.1, fortgeschrieben in Version 0.2 bis 0.5) aus dem bestehenden Bestand entstanden ist. Die Datei ist **kein** regulatorischer Anforderungskatalog und **keine** neue Adjudikation. Sie beschreibt die bereits adjudizierte Anwendbarkeit der `RR` aus [RR_CATALOG.yaml](RR_CATALOG.yaml) (Erstfassung gegen Version 0.24, fortgeschrieben bis Version 0.26) maschinenlesbar für den `APPLICABILITY_ENGINE` ([../04-architecture/ARCHITECTURE.md](../04-architecture/ARCHITECTURE.md) Abschnitt 8).

---

## 1. Grundlage und Verfahren

- **Inventur:** Für alle 377 Rechtsakt-`RR` (`RR-001` bis `RR-377`; Norm-`RR` in Abschnitt 6) wurde die Einordnung (regulär, bedingt, nicht dokumentiert) mit Outer und Inner Trigger ausschließlich aus den Evidenzdateien `RR_EXTRACTION_*.md` übernommen, einschließlich blockweiter Aussagen. Die 13 im Coverage-Plan dokumentierten Blocksummen stimmen vollständig überein. Stichproben wurden gegen die Evidenzdateien geprüft.
- **Keine Textauswertung:** Anforderungstexte werden weder per NLP noch per Regex oder Schlüsselwort ausgewertet. Quelle der Anwendbarkeit sind ausschließlich die dokumentierten Trigger, die Ergebnisse des `RULE_ENGINE` und kontrollierte Eingaben.
- **Zwei Ebenen:** Der Block beschreibt den übergeordneten Bereich (Outer Applicability), `local` die lokalen Bedingungen. Eine reguläre `RR` ist nur anwendbar, wenn ihr Block aktiv ist.

## 2. Modellierungsregel für lokale Bedingungen

| Behandlung | Kriterium | Beispiele |
| --- | --- | --- |
| als Eingabe modelliert (`local`) | Der dokumentierte Trigger ist ein faktisches Produkt- bzw. IFU-Merkmal, das der Hersteller zum Bewertungszeitpunkt ohne rechtliche Wertung mit Ja/Nein angeben kann. | Website, eingebautes Anzeigesystem, Speichermedium, Verfallsdatum, implantierbar, Prüfprodukt, Sonderanfertigung, Symbolverwendung, Restrisiko, Kalibrierung, Ergebnisinterpretation |
| nicht modelliert (`local_not_modelled`) | Angemessenheits- oder Relevanzvorbehalt, Ereignis im Betrieb, rechtlicher Stichtag, nicht operationalisierte rechtliche Einordnung oder Bedingung ohne konkreten Trigger | „soweit angemessen“, „gegebenenfalls“, Anforderung durch Behörde, Aktualisierungsbedarf, UDI-Registrierungszeitpunkt |

Nicht modellierte Bedingungen ergeben bei aktivem Block stets `APPLICABILITY_UNRESOLVED`. Die Einordnung ist konservativ: Im Zweifel wird nicht modelliert.

## 3. Ergebnis (Rechtsakt-`RR` `RR-001` bis `RR-377`)

| Einordnung laut Evidenz | Anzahl | maschinenlesbar bestimmbar | `APPLICABILITY_UNRESOLVED` bei aktivem Bereich |
| --- | --- | --- | --- |
| bedingt | 167 | 107 | 60 |
| regulär | 149 | 149 (davon 45 AI Act über den Block `AI_ACT_HIGH_RISK`) | 0 |
| nicht dokumentiert | 61 | 0 | 61 (alle AI Act; lokal fail-closed) |

Die 60 ungeklärten bedingten `RR` gliedern sich in: 23 Angemessenheits- bzw. Relevanzvorbehalt, 19 Ereignis im Betrieb, 9 lokale Bedingung im AI-Act-Bereich, 6 ohne konkret dokumentierten Trigger, 1 professioneller Nutzerpfad nach Art. 3 Abs. 1 der Verordnung (EU) 2021/2226 (`RR-205`), 1 rechtlicher Stichtag (`RR-264`), 1 nicht operationalisierte rechtliche Einordnung (`RR-317`). RR-ID, Kategorie und dokumentierter Trigger stehen je Eintrag in `local_not_modelled`.

**Blöcke:** `AI_ACT_HIGH_RISK`, `MDR_MDSW_CORE`, `MDR_LAY_USE`, `SRC009_ART3_1_PATH`, `SRC009_EIFU_REPLACEMENT`, `SRC009_EIFU_ADDITIONAL`, `MDR_ART85`, `MDR_ART86`, `MDR_ART86_IIB_III`, `MDR_ART86_IIA`, `MDR_ART86_ABS2`, `MDR_ART86_OUTSIDE_ABS2`. Die Zuordnung `MDR_MDSW` → MDR-Gap-Korpus, `NOT_MDSW` bzw. `OUT_OF_SCOPE_IVDR` → nicht aktiv folgt [DECISION_LOGIC_SRC_004_MDSW_QUALIFICATION_CLASSIFICATION.md](DECISION_LOGIC_SRC_004_MDSW_QUALIFICATION_CLASSIFICATION.md) Abschnitt 11. `NOT_COVERED_BY_SRC004`, die Sonderroute und Review-Ausgänge lassen den MDR-Bereich ungeklärt.

## 4. AI-Act-Applicability

Bis [RR_APPLICABILITY.yaml](RR_APPLICABILITY.yaml) Version 0.1 war die AI-Act-Applicability nicht modelliert; alle `RR-001` bis `RR-115` waren blockseitig `APPLICABILITY_UNRESOLVED`. Seit Version 0.2 ist der Block `AI_ACT_HIGH_RISK` an das kombinierte Art.-6-Routing `RUL-043` gebunden ([DECISION_LOGIC_SRC_002_AI_ACT_APPLICABILITY.md](DECISION_LOGIC_SRC_002_AI_ACT_APPLICABILITY.md) Abschnitt 9):

| Endzustand | `RR-001` bis `RR-115` |
| --- | --- |
| `AI_ACT_NOT_APPLICABLE`, `AI_ACT_APPLICABLE_NOT_HIGH_RISK` | 115 `NOT_APPLICABLE` (`SCOPE_INACTIVE`) |
| `AI_ACT_NOT_YET_APPLICABLE` | 115 `NOT_APPLICABLE` (`SCOPE_NOT_YET_APPLICABLE`) |
| `AI_ACT_HIGH_RISK_LEGACY_TRANSITION` | 115 `NOT_APPLICABLE` (`SCOPE_LEGACY_TRANSITION`) |
| `AI_ACT_HIGH_RISK` | 45 `APPLICABLE`; 61 `APPLICABILITY_UNRESOLVED` (Einordnung in der Evidenz nicht dokumentiert); 9 `APPLICABILITY_UNRESOLVED` (lokale Bedingung nicht modelliert) |
| `AI_ACT_APPLICABILITY_REVIEW_REQUIRED` oder nicht ausgeführt | 115 `APPLICABILITY_UNRESOLVED` (`SCOPE_UNRESOLVED`) |

Damit sind alle 115 AI-Act-`RR` blockseitig bestimmbar, darunter die 106 zuvor ausschließlich blockseitig ungeklärten `RR` (45 regulär, 61 ohne dokumentierte Einordnung). Bei wirksamem Hochrisiko-Status bleiben 70 `RR` lokal fail-closed ungeklärt (61 ohne dokumentierte Einordnung, 9 mit nicht modellierter lokaler Bedingung). Die Zahlen sind in `tests/test_ai_act_applicability.py` geprüft.

Seit Version 0.5 ist ausschließlich die Bindung auf RUL_CATALOG 0.3 fortgeschrieben. Die korrigierte Anhang-III-Übergangskette liefert die bestehenden Endzustände; Blöcke, Prädikate und alle 959 Einzelzuordnungen sind unverändert. Der frühere Gegenfall aktiviert damit den Hochrisiko-Block nicht mehr, solange kein anderer wirksamer Rechtsweg greift. Die Fassung 0.4 und die Evaluation R1/R2 bleiben unverändert; Nachweis: [EV-019](../09-evidence/EV-019_ANNEX_III_TRANSITION_FIX.md).

## 5. Prüfung abgeleiteter Eingaben (RUL-015, RUL-019)

Die Ableitung im `RULE_ENGINE` ist eine technische Graph-Ableitung ohne versteckte regulatorische Logik: `RUL-015` besitzt nur den zulässigen Wert `true` und ist nur über `RUL-013` erreichbar; `RUL-019` ist auf jedem erreichbaren Pfad `true`, weil jeder Pfad zu `RUL-019` über einen Zweig mit Klassenkandidaten aus Regel 11 führt. Beides wird in `tests/test_rule_engine.py` (`DerivedInputGraphTest`) über den Regelgraphen des Katalogs geprüft. Die Semantik von `RUL-001` bis `RUL-026` bleibt unverändert.

## 6. Normen `SRC-005` bis `SRC-008` (`RR-378` bis `RR-959`)

Seit Version 0.3 sind die 582 Norm-`RR` zugeordnet; Einzelheiten und Begründungen in [RR_EXTRACTION_STANDARDS_SRC_005_008.md](RR_EXTRACTION_STANDARDS_SRC_005_008.md) Abschnitt 8.

- **Blöcke:** `NORM_SRC_005_QMS`, `NORM_SRC_006_RISK_MANAGEMENT` (einschließlich der sechs Merge-`RR`), `NORM_SRC_007_SOFTWARE_LIFECYCLE`, `NORM_SRC_008_USABILITY`, jeweils mit dem bestehenden kanonischen Prädikat `MDR_MDSW` als Scope. Es wurde kein neues globales Normen- oder MDSW-Prädikat eingeführt; `SCOPE_INACTIVE` beschreibt hier den Scope des Demonstrators, nicht die normative Anwendbarkeit außerhalb davon.
- **Neue Eingaben (16):** ISO-13485-Ausschlussregel nach Abschnitt 1, QMS-Software, Outsourcing, Beschaffung, Software in Produktion/Dienstleistung, Software zur Überwachung/Messung, Kundeneigentum; IEC-62304-Sicherheitsklasse, -Route, SOUP, Softwareänderung, Problembericht; IEC-62366-1-Route, Usability-Test, Training, Sicherheitsinformation als Risikobeherrschung.
- **Erweiterung `PROFILE_INPUT`:** optionales Feld `unknown_values`. Eingabewerte darin ergeben fail-closed `UNKNOWN` (Legacy-Route für klassengebundene reguläre Pflichten, beanspruchte ISO-13485-Ausschlüsse). Noch nicht klassifizierte Software wird seit Version 0.4 nach der adjudizierten Regel `SRC-007#Abschnitt 4.3/g` wie Klasse C behandelt. Der Validator verlangt zulässige, zu `true_values` disjunkte Werte.
- **Ergebnis:** 120 regulär, 296 bedingt und vollständig modelliert, 166 mit nicht (vollständig) modellierter Bedingung (`local_not_modelled`, bei aktivem Block `APPLICABILITY_UNRESOLVED`). Geprüft in `tests/test_standards_applicability.py`.

| Einordnung (gesamt, 959 `RR`) | Anzahl |
| --- | --- |
| regulär | 269 |
| bedingt | 629 |
| nicht dokumentiert | 61 |

## 7. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung: Inventur der Conditionality aller 377 `RR`, Modellierungsregel, Ergebnis der Zuordnung, nicht modellierte AI-Act-Applicability mit fehlenden Primärrechtsknoten, Prüfung der abgeleiteten Eingaben. |
| 1.1 | Abschnitt 4 fortgeschrieben: AI-Act-Block an das kombinierte Art.-6-Routing (`RUL-027` bis `RUL-043`) gebunden; Wirkung je Endzustand und Zahlen vorher/nachher; Ergebnistabelle Abschnitt 3 angepasst. |
| 1.2 | Abschnitt 6 ergänzt: Zuordnung der Norm-`RR` `RR-378` bis `RR-959` (`RR_APPLICABILITY.yaml` 0.3), Normblöcke mit `MDR_MDSW`-Scope, 16 neue Eingaben, optionales `unknown_values`, Ergebniszahlen. |
| 1.3 | Abschnitt 6 fortgeschrieben: `RR_APPLICABILITY.yaml` 0.4 bildet die Regel `SRC-007#Abschnitt 4.3/g` ab (noch nicht klassifiziert = Klasse C); Bindung an `RR_CATALOG.yaml` 0.26. |
| 1.4 | Ausschließlich redaktionell: Einleitung sowie Abschnitte 1 und 3 als Stand der Rechtsakt-`RR` `RR-001` bis `RR-377` gekennzeichnet; Norm-`RR` weiterhin Abschnitt 6. Keine Änderung an Zuordnung oder Zahlen. |
| 1.5 | Bindung an RR_APPLICABILITY 0.5 / RUL_CATALOG 0.3 nach Anhang-III-Übergangskorrektur; keine Einzelzuordnung geändert. |
