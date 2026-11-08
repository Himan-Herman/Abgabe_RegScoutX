# EV-010 — Designevidenz Demonstrator D4 (Screenshots und Sichtprüfung)

Version 1.0 · Status: aktiv · Datum: 27.09.2026

Durchführung: gezielte Screenshots der Web-Anwendung mit `RX_SCREENSHOTS=1 npx playwright test e2e/screenshots.spec.ts` (3 Tests, alle bestanden) gegen die gebaute Oberfläche und den lokalen Server mit synthetischen Testdaten (`web/e2e/seed.py`: Vorführbewertung mit dem Profil des Referenzfalls TC-036 und synthetischen Erfüllungsangaben je Themencluster; keine fachliche Aussage). Viewport 1440 × 900 bzw. 390 × 844 mit doppelter Pixeldichte; Animationen deaktiviert, Fokus entfernt. Umgebung wie EV-009.

Ablage: [screenshots/D4/](screenshots/D4/); Inhalt je Datei in [WEB_APPLICATION.md](../04-architecture/WEB_APPLICATION.md) Abschnitt 16.

| Aspekt | Screenshot | Sichtbefund |
| --- | --- | --- |
| Start | `01-start.png` | Einordnung des Werkzeugs (Assistenzsystem, Umfang, keine Rechtsberatung, keine Zertifizierung, ungeklärte Anwendbarkeit offen) vor der Liste |
| Wizard | `02-wizard.png` | Abschnittsübersicht mit Zustand und Zählung, Frage mit Regelkennung, zulässige Antworten mit Folge |
| Einordnung | `03-applicability.png` | Entscheidungsbereiche mit Status, Ergebnis, Klasse, Stichtag; Kennzahlen der Anwendbarkeit |
| Gap Lens | `04-gap-lens.png` | Kennzahlen, Verteilung mit Mustern und Zahlen, Matrix mit Zahl je Zelle und Musterstufen |
| Anforderungsdetail | `05-requirement-detail.png` | Split View, Status als Form und Text, Lebenszyklusband, Primärquelle |
| Decision Trace | `06-decision-trace.png` | acht Stufen von der Eingabe bis zum Nachweis |
| Nachweise | `07-evidence.png` | Register mit Dokumentkennung, Version, Maßnahme und zugeordneten Anforderungen |
| Bericht | `08-report.png` | Berichtskopf aus dem ReportDocument, Inhaltsprüfsumme, PDF/HTML-Aktionen |
| Dunkles Schema | `09-dark-mode.png` | tiefes Graphit ohne Reinschwarz, lesbare Status und Formulare |
| Mobil | `10-mobile-wizard.png`, `10-mobile-requirement.png` | untere Navigation, einzeilige Spine, Detailansicht mit „Zur Liste“ |
| Versionsabweichung | `11-version-mismatch.png` | Hinweis mit bewusster Neubewertung, gesperrte Stationen |
| Hoher Kontrast, Englisch | `12-high-contrast-en.png` | vollständig englische Oberfläche, verstärkte Kontraste |

Die Sichtprüfung erfolgte im Rahmen der Umsetzung durch den Entwickler und ist keine unabhängige Gestaltungs- oder Nutzerbewertung. Befunde der Sichtprüfung wurden vor diesem Stand behoben (u. a. gedehnte Status-Kennzeichen in Karten, zu große Aufklapptitel, doppelt markierte Spine-Station, Silbentrennung in Navigation und Lebenszyklusband, falscher Kontext eines wiederverwendeten Berichtssatzes in der Nachweisansicht).

Geprüfte Testfälle: TC-060 (Darstellung, Sprachen, Barrierefreiheit, Responsive) als visuelle Ergänzung der automatisierten Prüfungen aus EV-009.

Bewertung: **PASS** (Sichtprüfung ohne offene Befunde).
