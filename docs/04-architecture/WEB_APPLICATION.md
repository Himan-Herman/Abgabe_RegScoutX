# Web-Anwendung des Demonstrators (Interaktionskonzept und Designevidenz)

Version 1.1 · Status: aktiv · Stand: 29.09.2026 (Demonstrator D4, Korrektur aus Block 6)

Dieses Dokument beschreibt Interaktionskonzept, Informationsarchitektur, Komponenten, Tokens, Zustände, Barrierefreiheit, Sprachen, Sicherheit und Abhängigkeiten der Web-Oberfläche (`PRESENTATION`, Verzeichnis `web/`) und ihrer lokalen Anwendungs-API (`APPLICATION_API`). Verbindliche Leitlinie ist [UI_UX_DESIGN_SYSTEM.md](UI_UX_DESIGN_SYSTEM.md) (Version 1.1); die Technologieentscheidung steht in ADR-0007 (Entwicklungsarchiv), die Modulregeln in [ARCHITECTURE.md](ARCHITECTURE.md). Dieses Dokument trifft keine regulatorischen Aussagen; alle fachlichen Inhalte stammen aus den versionierten Katalogen und dem Kern.

---

## 1. Charakter und Grenzen

- **Charakter:** ruhiges, präzises Arbeitswerkzeug („Regulatory Observatory“ als Gestaltungsleitbild, nicht als Oberflächentext): warmes, helles Papier, Graphit-Text, mineralischer Petrol-Akzent; dunkles Schema in tiefem Graphit ohne Reinschwarz. Keine Dashboard-Kacheln mit Dekorationsgrafik, keine Farbverläufe, keine Illustrationen.
- **Aussagegrenze in der Oberfläche:** Startansicht und Fußzeile jeder Ansicht nennen Assistenzsystem, definierten Umfang (versionierte Kataloge), keine Rechtsberatung, keine Zertifizierung bzw. Konformitätsbestätigung und die offene Ausweisung ungeklärter Anwendbarkeit. Es gibt keine Formulierung, die eine Konformität bescheinigt.
- **Keine Fachlogik im Browser:** Fragen, Folgefragen, zulässige Werte, Segmentzustände, Spine-, Block- und Matrixwerte berechnet der Kern (`questionnaire.py`, `assessment_views.py`); die Oberfläche stellt dar, sendet Eingaben unverändert und zeigt die Antwort des Kerns.

## 2. Informationsarchitektur und Navigationskarte

Hash-Routing (keine Serverkonfiguration nötig, offline und in Hybrid-Hüllen lauffähig). Filter und Auswahl stehen in der Adresse (teilbar, Zurück-Navigation).

| Route | Ansicht | Inhalt |
| --- | --- | --- |
| `#/` | Bewertungen | Einordnung des Werkzeugs, gespeicherte Bewertungen (Revision, Zustand, Versionsabgleich, Kennzahlen; beschädigte Dateien einzeln markiert), neue Bewertung |
| `#/a/<id>/profile?segment=` | Produktprofil (Assessment Wizard) | acht Abschnitte, Fragen mit Auslöser, zulässige Werte mit Folge, Neuberechnung, nicht mehr verwendete Angaben, Kernentscheidungen |
| `#/a/<id>/classification` | Einordnung und Anwendbarkeit | Entscheidungsbereiche mit Ergebnis, Klasse, Stichtag, offenen Prüfpunkten, fehlenden Eingaben und Regeln; Anwendbarkeitsbereiche mit Zustand und Zählung |
| `#/a/<id>/requirements?q=&applicability=&gap=&theme=&phase=&block=&answer=&rr=` | Anforderungen (Requirement Explorer) | 959 Anforderungen mit Suche und Filtern; Detail mit Text, Lebenszyklus, Quellen, Erfüllungsbewertung, Evidence Dock, Decision Trace, Maßnahmen, offenen Punkten |
| `#/a/<id>/gaps` | Gap-Analyse (Gap Lens) | Kennzahlen, Verteilung nach Gap-Status, Anforderungsmatrix Thema × Phase |
| `#/a/<id>/evidence` | Nachweise | Register der Nachweisreferenzen, vorgesehene Maßnahmen mit Anzahl |
| `#/a/<id>/report?lang=&revision=` | Ergebnisbericht | ReportDocument aus D3, PDF/HTML-Erzeugung, frühere Revisionen |
| `#/a/<id>/history` | Verlauf | Revisionen, Revisionsaktionen, Audit-Protokoll |
| `#/preferences` | Darstellung | Sprache, Farbschema, Kontrast, Schriftgröße, Bewegung, Dichte |

**App Shell:** Rail (ab 48 rem Breite) mit Bewertungen, sieben Bereichen der geöffneten Bewertung und Darstellung; Kontextkopf mit Kennung, Revision, Zustand, Versionsabgleich und Regulatory Spine; Arbeitsbereich (max. 88 rem); unter 48 rem untere Navigation (Bewertungen, Profil, Anforderungen, Gaps, „Mehr“ als Drawer) mit Safe Areas (`env(safe-area-inset-*)`). Seitliche Panels (Source Drawer, Nachweisformular) sind modale Drawer mit Fokusfalle; das Anforderungsdetail ist ab 75 rem ein Split View, darunter eine eigene Detailansicht mit „Zur Liste“.

## 3. Nutzerabläufe

1. **Bewertung anlegen und Profil erfassen:** „Neue Bewertung“ → Produktprofil. Nur Einstiegsfragen sind offen; jede Antwort wird sofort vom Kern vollständig neu ausgewertet; Folgefragen erscheinen im jeweiligen Abschnitt mit Auslöser. Anwendbarkeitsangaben erscheinen, sobald eine Anforderung sie auswertet.
2. **Einordnung prüfen:** Kernentscheidungen im Wizard, ausführlich unter „Einordnung“ mit Regeln und Quellenankern; ungeklärte Anwendbarkeit wird mit Anzahl ausgewiesen.
3. **Anforderungen bewerten:** Explorer filtern → Anforderung öffnen → Erfüllungsbewertung mit Begründung (Pflicht nach SR-014) → Nachweisreferenz anlegen oder zuordnen → Gap-Status aus dem Kern. Bewertbar sind nur anwendbare Anforderungen; ist zu einer nicht anwendbaren oder ungeklärten Anforderung eine Bewertung gespeichert (z. B. aus einem früheren Profilstand oder über die API), zeigt das Detail sie als „Gespeicherte Bewertung ohne Wirkung“ mit Status und Anzahl der Nachweise (Korrektur F-3 aus Block 6, [EVALUATION_RESULTS.md](../08-evaluation/EVALUATION_RESULTS.md)).
4. **Eingabe ändern:** zu einem Abschnitt zurückgehen, Antwort ändern → Neuberechnungs-Panel mit geänderten Eingaben, Anwendbarkeits- und Statusänderungen, de- und reaktivierten Bewertungen, neuen Folgefragen; nicht mehr verwendete Angaben bleiben sichtbar und entfernbar; wieder anwendbare Bewertungen werden gesammelt und einzeln bestätigt.
5. **Bericht und Revision:** Berichtsansicht (dieselben Inhalte wie PDF/HTML) → PDF/HTML erzeugen (Audit `REPORT_CREATED`) → Revision abschließen → neue Revision öffnen; frühere Revisionen über ihren Bericht.
6. **Versionsabweichung:** gespeicherter Stand nur lesbar, Spine gesperrt, Fragebogen nicht bearbeitbar; „Mit aktuellem Katalog neu bewerten“ legt bewusst eine neue Revision an.

## 4. Schichten und Komponentenkarte

| Schicht | Verzeichnis | Inhalt |
| --- | --- | --- |
| Shared Product Core | `web/src/core/` | API-Adapter (`api/client.ts`, Pflicht-Header, stabile Fehlercodes, Dateidownload), `useResource`, Plattform-Adapter (Speicher, Download, Medienabfragen), Hash-Router, i18n, Präferenzen und Theme Engine, Live-Regionen, Primitives (`Button`, `LinkButton`, `Segmented`, `ChoiceCards`, `ComboField`, `DateInputField`, `TextInputField`, `TextAreaField`, `Disclosure`, `Drawer`, `ConfirmDialog`, `StatusTag`, `Banner`, `LoadingState`, `EmptyState`, `Glyph`), Basisstile |
| Domain UI | `web/src/domain/` | App Shell, Regulatory Spine, Assessment Wizard (`QuestionCard`, `WizardView`), Einordnung, Requirement Explorer, Anforderungsdetail, Decision Trace, Lifecycle Ribbon, Source Drawer, Evidence Dock, Gap Lens, Anforderungsmatrix, Nachweise, Report View, Verlauf, Darstellung, Status-Abbildung (`status.ts`) |
| Experience Profile | `web/src/experience/regscoutx/` | Farbpaletten (`palette.ts`), nicht-farbliche Tokens und Schriften (`tokens.css`) |

Primitives nutzen React Aria Components für Verhalten und Semantik (Radiogruppen, Combobox mit Listbox, Datumsfeld mit Segmenten, Disclosure, modale Dialoge); die Gestaltung stammt ausschließlich aus den Tokens.

### Signature Components

| Komponente | Zweck | Umsetzung |
| --- | --- | --- |
| Regulatory Spine | Verlauf Profil → Anwendbarkeit → Einordnung → Anforderungen → Gaps → Nachweise → Bericht | Stationen mit Form (Glyphe), Text, Zahl und verborgenem Zustandstext; aktuelle Station `aria-current="step"`; mobil einzeilig innerhalb der Leiste scrollbar |
| Assessment Wizard | adaptive, segmentierte Frageführung | Abschnittsübersicht (Zustand, beantwortet/gesamt, Ergebnis), Fragenkarten mit „Warum diese Frage?“, zulässigen Antworten mit Folge, Datumsstichtagen, optimistischer Auswahl bis zur Kernantwort, Neuberechnungs-Panel, nicht mehr verwendete Angaben, Kernentscheidungen |
| Decision Trace | Herleitung einer Anforderung | geordnete Kette Eingabe → Bedingung → Regel/Entscheidung → Anwendbarkeit → Anforderung → Gap-Status → Maßnahme → Nachweis mit Codes und Bezeichnungen |
| Requirement Explorer | alle 959 Anforderungen | Suche (Kennung, Titel, Quellenlokator), Filter Anwendbarkeit, Gap-Status (einschließlich „nur Gaps“), Themencluster, Lebenszyklusphase, Bereich, Bewertungszustand; `content-visibility` je Zeile |
| Gap Lens | Stand der Gap-Analyse | Kennzahlen, Verteilungsbalken mit Mustern und Legende mit Zahl und Anteil (Balken dekorativ, Legende trägt die Information) |
| Anforderungsmatrix | Thema × Lebenszyklusphase | echte Tabelle mit Zeilen- und Spaltenköpfen; Zahl und Zellgesamt immer sichtbar, Stufe zusätzlich als Muster; Kennzahl wählbar (Gaps, nicht bewertet, ungeklärt, anwendbar); Zelle filtert den Explorer |
| Lifecycle Ribbon | Lebenszyklusbezug (SR-041) | alle Phasen in Vokabularreihenfolge, zugeordnete gefüllt mit Häkchen und Textmarke |
| Source Drawer | Quellen einer Anforderung | Registerkennung, Kurzbezeichnung aus dem Quellenregister, Fundstelle; keine Quelltexte |
| Evidence Dock | Nachweise einer Anforderung | zugeordnete Referenzen, Zuordnung lösen, vorhandene zuordnen, neue anlegen und zuordnen |
| Report View | Bericht in der Oberfläche | rendert `ReportDocument` (D3); Abschnitte werden erst beim Aufklappen gerendert, lange Abschnitte in Schritten zu 60 Blöcken |

## 5. Design Tokens

**Farben** (`palette.ts`, vier Varianten; die Theme Engine setzt sie per CSSOM als `--color-*`, CSP-konform ohne Inline-Stile):

| Token | Hell | Dunkel | Hell, hoher Kontrast | Dunkel, hoher Kontrast |
| --- | --- | --- | --- | --- |
| `surface` | `#F7F6F2` | `#111418` | `#FFFFFF` | `#000000` |
| `surfaceElevated` | `#FFFFFF` | `#171B20` | `#FFFFFF` | `#0B0D10` |
| `textPrimary` | `#1A1D21` | `#E7E9EB` | `#1A1D21` | `#FFFFFF` |
| `textSecondary` | `#40454C` | `#C3C8CE` | `#1A1D21` | `#F0F2F4` |
| `interactive` | `#0F5E66` | `#6CC6CD` | `#083F45` | `#9FE3E8` |
| `focus` | `#0F5E66` | `#8AD4DA` | `#000000` | `#FFFFFF` |

Status (`fulfilled`, `partial`, `notFulfilled`, `notAssessed`, `unresolved`, `notApplicable`, `evidenceReview`, `info`, `applicable`) je mit Fläche (`…Subtle`). Geprüft in `palette.test.ts`: Text ≥ 4,5:1 (hoher Kontrast ≥ 7:1) auf allen Flächen, Statusfarbe ≥ 4,5:1 auf eigener und neutraler Fläche, Fokus und starke Linien ≥ 3:1. Das dunkle Standardschema verwendet kein Reinschwarz.

**Typografie:** IBM Plex Sans Variable (Gewichte 400/500/600) und IBM Plex Mono (400/500) für Kennungen, Codes und Prüfsummen, selbst gehostet. Skala mit `clamp()`: Display 1,75–2,375 rem, Titel 1,4–1,75 rem, Abschnitt 1,25 rem, Unterabschnitt 1,0625 rem, Text 1 rem / 0,9375 rem, Meta 0,8125 rem; Zeilenhöhen 1,2 / 1,35 / 1,55 / 1,65; Lesebreite 72 ch.

**Abstände und Formen:** 4er-Raster (`--space-0-5` bis `--space-16`), fluide Rinne und Abschnittsabstände; Radien 6/8/12 px und Pille; Bedienhöhe 2,5 rem, Touch-Ziel 2,75 rem (bei grobem Zeiger Standard).

**Bewegung:** 120/200/280 ms mit Standard- und Austrittskurve; nur Deckkraft und kleine Verschiebung; bei Präferenz „Reduziert“ oder Systemeinstellung (`prefers-reduced-motion`) alle Dauern 0 ms, Lade-Indikator statisch.

**Ebenen:** Kopf 20, Rail 30, Overlay 60, Drawer 70, Popover 80, Ansage 90.

## 6. Zustände

| Zustand | Umsetzung |
| --- | --- |
| Laden | `LoadingState` mit `role="status"`; Anwendungsstart mit neutralem Indikator |
| Leer | `EmptyState` mit Erklärung und nächster Aktion (keine Bewertung, keine Nachweise, keine Auswahl im Explorer, kein anwendbarer Gap) |
| Gefiltert leer | „Keine Anforderung entspricht den Filtern“ mit Zurücksetzen |
| Validierung | Feldfehler am Feld (`FieldError`, `aria-invalid`), Begründungspflicht, Pflichtfelder der Nachweisreferenz; Kernfehler `INVALID_INPUT` am betroffenen Feld |
| Anwendungsfehler | Banner mit stabilem, lokalisiertem Fehlercode; assertive Ansage; gespeicherter Stand unverändert; Fehlergrenze für Darstellungsfehler |
| Versionsabweichung | schreibgeschützt, Spine „gesperrt“, Banner mit bewusster Neubewertung (`MISMATCH`) bzw. ohne (`INCOMPLETE_VERSION_INFO`) |
| Beschädigt | eigene Seite „Bewertung beschädigt“, in der Liste einzeln markiert; keine Reparatur |
| Ungeklärt | eigene Form und Farbe, Kennzahl und Hinweis in Einordnung und Gap-Übersicht; nie als anwendbar oder nicht anwendbar gezählt |
| Abgeschlossen | Banner mit „Neue Revision öffnen“; Formulare deaktiviert |
| Nicht erreichbar | Startmeldung in der gewählten Sprache (einzige Texte außerhalb der zentralen Ressourcen, weil ohne Sprachpaket keine andere Quelle besteht) |

## 7. Responsive Verhalten

Breiten 1440/1280 (Rail, Split View ab 75 rem), 768 (Rail, Detail als eigene Ansicht), 390/360 (untere Navigation, Spine einzeilig scrollbar). Kein horizontaler Seitenüberlauf in allen Ansichten bei DE/EN und Hell/Dunkel; zusätzlich 200 % Zoom (halbe CSS-Breite, doppelte Pixeldichte) mit sehr großer Schrift und reduzierter Bewegung. Breite Tabellen scrollen innerhalb ihres fokussierbaren Bereichs. Geprüft in `web/e2e/responsive.spec.ts`.

## 8. Barrierefreiheit

- Semantisches HTML (Landmarken `nav`/`main`/`footer`, Überschriftenhierarchie, echte Tabellen mit `scope`, Listen), zugängliche Namen für alle Bedienelemente.
- Tastatur: Skip-Link als erstes Element; Fokus auf die neue Überschrift bei Ansichtswechsel und auf die Überschrift einer geöffneten Anforderung; Drawer und Dialoge mit Fokusfalle, Escape und Fokusrückgabe; Radiogruppen mit Pfeiltasten, Combobox mit Pfeiltasten und Enter; Datumsfeld segmentweise.
- Ansagen über `aria-live` (Neuberechnung, Speichern, Filterergebnis, Fehler assertiv).
- Status nie nur über Farbe: Glyphenform, Text und Farbe; Muster in Verteilung und Matrix.
- Kontrast rechnerisch geprüft; hoher Kontrast als eigene Palette; `forced-colors` mit sichtbaren Rahmen.
- Bedienelemente auf Touch-Geräten mindestens 44 px hoch (Browser-Test); Schaltflächen mit Mindestbreite 2,75 rem.
- Automatisiert: axe-core (WCAG 2.0/2.1/2.2 A und AA) für alle Ansichten, Drawer und Formulare in Hell, Dunkel, hohem Kontrast und Englisch ohne Befund; Komponententests mit axe-core.
- **Grenze:** Eine manuelle Prüfung mit Screenreadern (VoiceOver, NVDA) und eine Nutzerstudie wurden nicht durchgeführt; automatisierte Prüfungen erkennen nur einen Teil möglicher Barrieren.

## 9. Sprachen

- Alle Oberflächentexte liegen in `regscoutx/resources/i18n/de.json` und `en.json` (Präfix `ui.`), gemeinsam mit den Berichtstexten; Code-Bezeichnungen, Themen und Phasen kommen aus `DATA_MODEL.yaml` und dem Vokabular. Die API liefert sie als Sprachpaket; es gibt keine zweite Übersetzungsarchitektur und keinen Rückfall in eine andere Sprache (fehlende Schlüssel werden sichtbar markiert).
- `tests/test_i18n.py` prüft identische Schlüsselmengen, Platzhalter, dass jeder in `web/src` verwendete Schlüssel existiert, dass dynamische Schlüsselfamilien vollständig sind, dass kein `ui.`-Schlüssel verwaist und dass der Oberflächencode keine sichtbaren Textliterale enthält. Browser-Test: englische Ansichten ohne deutsche Oberflächenbegriffe.
- Datum, Zahl und Prozent über `Intl` (de-DE, en-GB); `lang` am Dokument folgt der Sprache (Silbentrennung, Screenreader).
- **Bewusste Ausnahmen:** Quellenbezeichnungen und Fundstellen-Lokatoren sind Kennungen des Quellenregisters in dessen Notation (z. B. `SRC-002#Art.13/Abs.1`, „Durchführungsverordnung (EU) 2021/2226“) und werden nicht übersetzt; sie tragen `lang="de"`. Codes (z. B. `RUL-001`, `MEAS_VERIFICATION`) sind sprachneutral.

## 10. Darstellungspräferenzen

Sprache, Farbschema (System/Hell/Dunkel), Kontrast (Standard/Hoch), Schriftgröße (100/112,5/131,25 %), Bewegung (System/Normal/Reduziert), Dichte (komfortabel/kompakt). Gespeichert ausschließlich im Browser (`localStorage`, Präfix `regscoutx.preference.`, über den Plattform-Adapter); sie gehen nie an die API und ändern weder Fingerprint noch Anwendbarkeit, Gap-Status oder Audit (Browser-Test und Komponententest).

## 11. Sicherheit und Datenschutz

- Lokaler Server nur an localhost; Host-Prüfung; Abweisung seitenfremder Anfragen (`Sec-Fetch-Site`); Pflicht-Header für schreibende Anfragen; JSON bis 1 MB; strikte Content-Security-Policy ohne `unsafe-inline` (die sonst von React Aria eingefügte Regel liegt als eigene Datei `public/styles/pressable.css` vor); keine CORS-Freigabe; keine Inhaltsprotokollierung; `Connection: close` und erhöhte Warteschlange für parallele Browserverbindungen.
- Keine externen Ressourcen: Schriften und Symbole selbst gehostet; keine Analytics, keine Telemetrie, keine KI-Dienste. Browser-Test: keine Anfrage außerhalb von localhost, keine Inline-Stile, keine Konsolenfehler.
- Freitexte (Begründung, Nachweistitel, Ablageort) werden nur als Text gerendert (keine HTML-Interpretation) und vom Kern nicht ausgewertet.
- Die Oberfläche greift nur über die API auf den `AssessmentApplicationService` zu; keine Datei- oder Katalogzugriffe.

## 12. Leistung

Explorer mit 959 Anforderungen: Laden bis zur vollständigen Liste 0,8 s, Suchfilter 39 ms, Öffnen einer Anforderung 0,3 s (lokaler Lauf, Chrome, gebaute Oberfläche; `presentation.spec.ts`, Grenzwerte 5 s / 1 s / 3 s). Maßnahmen: `content-visibility: auto` je Zeile, zurückgestellte Suche (`useDeferredValue`), Detail getrennt geladen, Bericht abschnittsweise gerendert, getrennte Bibliotheks-Chunks (Anwendung 102 kB, React 219 kB, React Aria 313 kB unkomprimiert).

## 13. PWA-Vorbereitung

Web-App-Manifest (`standalone`, Themenfarbe, Symbole 192/512/maskable/SVG, Apple-Touch-Icon), `theme-color` je Farbschema, `viewport-fit=cover` mit Safe Areas, Plattform-Adapter für eine spätere Hybrid-Hülle. Bewusst kein Service Worker (ADR-0007).

## 14. Abhängigkeiten, Lizenzen und Provenienz

Laufzeit (im ausgelieferten Bundle, 16 Pakete, `npm audit`: 0 Befunde):

| Paket | Version | Lizenz | Zweck |
| --- | --- | --- | --- |
| `react`, `react-dom`, `scheduler`, `use-sync-external-store` | 19.3.0 / 0.28.0 / 1.7.0 | MIT | Oberfläche |
| `react-aria-components`, `react-aria`, `react-stately`, `@react-types/shared` | 1.21.1 / 3.52.1 / 3.50.0 / 3.36.1 | Apache-2.0 | zugängliche Bausteine |
| `@internationalized/date`, `/number`, `/string` | 3.12.4 / 3.6.8 / 3.2.10 | Apache-2.0 | Datumsfeld, Lokalisierung |
| `@swc/helpers` | 0.5.23 | Apache-2.0 | Laufzeithilfen von React Aria |
| `aria-hidden`, `client-only`, `clsx` | 1.2.6 / 0.0.1 / 2.1.1 | MIT | Hilfsbibliotheken von React Aria |
| `tslib` | 2.8.1 | 0BSD | Laufzeithilfen |

Entwicklung und Test (nicht ausgeliefert): TypeScript 7.0.2 (Apache-2.0), Vite 8.3.1 und `@vitejs/plugin-react` 6.1.1 (MIT), Vitest 5.0.2 (MIT), jsdom 29.1.1 (MIT; 30.x verlangt Node ≥ 22.22.2), Testing Library 16.3.3/14.6.7 (MIT), Playwright 1.63.0 (Apache-2.0, nutzt das installierte Google Chrome), axe-core und `@axe-core/playwright` 4.13.0 (MPL-2.0, unverändert genutzt), lightningcss (MPL-2.0, Build-Werkzeug von Vite). Alle Versionen exakt gepinnt (`package-lock.json`).

Schriften: IBM Plex Sans Variable (Roman, Italic) und IBM Plex Mono (Regular, Medium) aus dem Repository IBM/plex, Version 6.4.0, SIL Open Font License 1.1 (`web/public/fonts/OFL-IBM-Plex-LICENSE.txt`), unverändert. Symbole und App-Icon: eigene Gestaltung.

## 15. Verworfene Gestaltungsalternativen

| Alternative | Grund der Verwerfung |
| --- | --- |
| Dashboard mit Kacheln und Diagrammen als Startseite | widerspricht dem ruhigen Werkzeugcharakter; Kennzahlen stehen dort, wo sie Entscheidungen stützen |
| Linearer Wizard mit genau einer Frage je Seite | verdeckt Zusammenhänge und verlängert lange Pfade ([L02] im Stand der Technik); stattdessen Abschnitte mit allen Fragen des aktuellen Pfads |
| Status nur als farbiger Punkt | nicht barrierefrei; stattdessen Form + Text + Farbe |
| Chart-Bibliothek für Verteilung und Matrix | farbabhängige Standardgrafiken, schwer zugänglich; stattdessen Tabelle und Legende mit Zahl |
| Unendliches Nachladen der Anforderungsliste | erschwert Orientierung und Tastaturbedienung; alle 959 Zeilen mit `content-visibility` genügen |
| Sofortiges Übernehmen jeder Datumsziffer | führte zu unbeabsichtigten Zwischenwerten (Jahr 0002); stattdessen ausdrückliches „Datum übernehmen“ |
| Kontrollierte Auswahl ohne optimistische Anzeige | Auswahl sprang bis zur Kernantwort zurück; stattdessen Anzeige der gewählten Antwort bis zur Antwort des Kerns, bei Fehler Rückkehr zum gespeicherten Wert |
| `unsafe-inline` in der CSP für die Stilregel von React Aria | schwächt den Schutz; stattdessen Regel als eigene Datei mit der erwarteten Kennung |

Technologische Alternativen: ADR-0007 (Entwicklungsarchiv) Abschnitt 4.

## 16. Screenshots (Designevidenz)

Erzeugt mit `RX_SCREENSHOTS=1 npx playwright test e2e/screenshots.spec.ts` aus synthetischen Testdaten (`web/e2e/seed.py`, Vorführbewertung mit Referenzprofil TC-036 und synthetischen Erfüllungsangaben). Die D4-Screenshots sind im Entwicklungsarchiv aufbewahrt und nicht Teil des Abgabepakets:

| Datei | Inhalt |
| --- | --- |
| `01-start.png` | Bewertungen mit Einordnung des Werkzeugs |
| `02-wizard.png` | Assessment Wizard, Abschnitt EU AI Act |
| `03-applicability.png` | Einordnung und Anwendbarkeit |
| `04-gap-lens.png` | Gap-Übersicht und Anforderungsmatrix (ganze Seite) |
| `05-requirement-detail.png` | Explorer mit Anforderungsdetail (Split View) |
| `06-decision-trace.png` | Herleitung einer Anforderung |
| `07-evidence.png` | Nachweisregister |
| `08-report.png` | Berichtsansicht |
| `09-dark-mode.png` | Anforderungsdetail im dunklen Schema |
| `10-mobile-wizard.png`, `10-mobile-requirement.png` | 390 px mit unterer Navigation |
| `11-version-mismatch.png` | Versionsabweichung, schreibgeschützt |
| `12-high-contrast-en.png` | Gap-Übersicht, hoher Kontrast, Englisch |

## 17. Tests

| Ebene | Datei | Inhalt |
| --- | --- | --- |
| Kern/API | `tests/test_web_application.py` | Fragebogen, Sichten, API-Vertrag, Fehlercodes, Serverschutz, Manifest und selbst gehostete Ressourcen |
| Komponenten | `web/src/**/*.test.ts(x)` (Vitest) | Kontraste, i18n, Präferenzen ohne API-Zugriff, Router, Primitives und Fragenkarte mit axe-core |
| Browser | `web/e2e/assessment-flow.spec.ts` | Abnahmeablauf Schritte 1–15; über die Oberfläche erfasstes Profil ergibt denselben Fingerprint wie der Referenzfall TC-036 |
| Browser | `web/e2e/presentation.spec.ts` | Englisch, Farbschemata, hoher Kontrast, Schriftgröße, Dichte, reduzierte Bewegung, Präferenzen ohne fachliche Wirkung, Tastatur, keine externen Verbindungen, Leistung |
| Browser | `web/e2e/accessibility.spec.ts` | axe-core für alle Ansichten in fünf Konfigurationen, Drawer und Formulare |
| Browser | `web/e2e/responsive.spec.ts` | Breitenmatrix, 200 % Zoom, Touch-Ziele |
| Browser (Block 6) | `web/e2e/case-study.spec.ts`, `web/e2e/case-study-performance.spec.ts` | Fallstudie über die Oberfläche, Vergleich mit dem API-Lauf, Screenshots B6, Leistung; nur mit `RX_CASE_STUDY=1` (EV-016) |

Ausführung: `cd web && npm ci && npm run build && npm test && npx playwright test` (Python-Umgebung nach README; der Test startet den lokalen Server mit frischen Testdaten auf Port 8788).

## 18. Bekannte Grenzen

- Keine manuelle Screenreader-Prüfung und keine Nutzerstudie (Abschnitt 8).
- Browser-Tests nur mit Google Chrome (Desktop-Chrome-Profil und mobile Emulation); Safari und Firefox nicht automatisiert geprüft.
- Einzelplatzbetrieb ohne Authentifizierung; der Server ist nicht für Netz- oder Mehrbenutzerbetrieb gedacht.
- Die Berichtsansicht zeigt den gespeicherten Stand; bei `MISMATCH` fehlen wie im PDF die Katalogtexte der damaligen Version.

## 19. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung (Demonstrator D4): Interaktionskonzept, Informationsarchitektur, Abläufe, Komponenten, Tokens, Zustände, Responsive, Barrierefreiheit, Sprachen, Präferenzen, Sicherheit, Leistung, PWA, Abhängigkeiten und Lizenzen, verworfene Alternativen, Screenshots, Tests, Grenzen. |
| 1.1 | Anzeige gespeicherter Bewertungen nicht anwendbarer bzw. ungeklärter Anforderungen (Korrektur F-3, Block 6); Browser-Spezifikationen der Fallstudie. |
