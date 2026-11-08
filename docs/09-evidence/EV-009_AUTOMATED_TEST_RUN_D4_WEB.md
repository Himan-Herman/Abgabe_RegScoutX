# EV-009 — Automatisierter Testlauf Demonstrator D4 (vollständig, einschließlich Browser)

Version 1.0 · Status: aktiv · Datum: 27.09.2026

Durchführung: vollständige Test- und Prüfläufe auf Basis von Commit `958b33c` mit den abschließenden D4-Änderungen (Web-Anwendung, Anwendungs-API, Dokumentation). Alle Läufe arbeiten ausschließlich lokal mit synthetischen Daten in temporären Verzeichnissen bzw. in `web/e2e/.data` (bei jedem Browserlauf neu erzeugt durch `web/e2e/seed.py`). Umgebung: macOS, Python 3.13.15, Node.js 22.21.0, Google Chrome 153.0.8010.53 (Playwright-Kanal `chrome`). Dieses Artefakt beeinflusst kein Testergebnis.

| Katalog | Wert |
| --- | --- |
| rr_catalog | 0.26 |
| rul_catalog | 0.2 |
| sr_catalog | 0.6 |
| rr_applicability | 0.4 |
| data_model | 0.8 |
| rr_measure | 0.1 |

| Suite | Tests | Exit-Code | Ergebnis |
| --- | --- | --- | --- |
| `.venv/bin/python -m unittest discover -s tools -p test_*.py` | 129 | 0 | OK |
| `.venv/bin/python -m unittest discover -s tests -t .` | 202 | 0 | OK |
| alle Validatoren unter `tools/` und `tools/traceability.py` | — | 0 | PASS, ohne Befund |
| `cd web && npm run build` (Typprüfung und Produktionsbuild) | — | 0 | ohne Warnung |
| `cd web && npx vitest run` | 32 | 0 | OK |
| `cd web && npx playwright test` | 30 (+ 3 übersprungen) | 0 | OK, keine instabilen Tests |

Browser-Spezifikationen: `assessment-flow.spec.ts` (5 Tests, Abnahmeablauf Schritte 1–15; das über die Oberfläche erfasste Profil ergibt denselben fachlichen Fingerprint wie der Referenzfall TC-036), `presentation.spec.ts` (7: Englisch ohne deutsche Oberflächentexte, Farbschemata, hoher Kontrast, Schriftgröße, Dichte, reduzierte Bewegung, Präferenzen ohne API-Schreibzugriff und ohne Änderung von Fingerprint und Audit, Tastatur, keine externen Verbindungen/Inline-Stile/Konsolenfehler, Leistung), `accessibility.spec.ts` (6: axe-core WCAG 2.0/2.1/2.2 A und AA für alle Ansichten in Hell/DE, Dunkel/DE, hohem Kontrast Hell/DE, hohem Kontrast Dunkel/EN, Hell/EN sowie Drawer und Formulare – 0 Verstöße), `responsive.spec.ts` (12: 1440, 1280, 768, 390, 360 px × DE/Hell und EN/Dunkel ohne horizontalen Überlauf, 200 % Zoom mit sehr großer Schrift und reduzierter Bewegung, Touch-Ziele ≥ 44 px). Die drei übersprungenen Tests sind die Screenshot-Erzeugung (`screenshots.spec.ts`), die nur auf ausdrücklichen Aufruf läuft (EV-010).

Leistung (Explorer mit 959 Anforderungen, gebaute Oberfläche, lokal): Laden bis zur vollständigen Liste 814 ms, Suchfilter 38 ms, Öffnen einer Anforderung 289 ms.

Während der Umsetzung aufgedeckt und behoben (vor diesem Lauf): Inline-`<style>` von React Aria durch die CSP blockiert (Regel als Datei ausgeliefert), Datumsübernahme bei jeder Ziffer (ausdrückliches Übernehmen), zurückspringende Auswahl bis zur Kernantwort (optimistische Anzeige), abgewiesene Browserverbindungen durch die Standard-Warteschlange des Servers (erhöht), horizontaler Überlauf durch verborgene Zustandstexte in der mobilen Spine (Bezugsrahmen), beschädigte Datei ließ die Bewertungsliste fehlschlagen (einzeln gemeldet).

Geprüfte Testfälle: alle 59 automatisierten TC (TC-001 bis TC-060 ohne den Validatorlauf TC-029), darunter die Web-Abnahmeszenarien TC-055 bis TC-060 auf API-, Komponenten- und Browserebene.

Grenzen: nur Google Chrome (Desktop-Profil und mobile Emulation); automatisierte Barrierefreiheitsprüfung ersetzt keine manuelle Screenreader-Prüfung.

Bewertung: **PASS**.
