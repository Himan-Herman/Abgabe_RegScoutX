# Extraktions- und Atomizitätsmethode für regulatorische Anforderungen (`RR`)

Version 1.2 · Status: aktiv

Diese Datei ist die führende methodische Festlegung dafür, wie aus einer Quellenfundstelle regulatorische Anforderungen (`RR`) gewonnen werden. Sie regelt RR-Relevanz, die 0/1/n-Entscheidung, Atomizität, Split-Regeln, den Umgang mit mehreren Quellen-Lokatoren, die Formulierung des Anforderungstextes sowie Format und Datenstruktur des Anforderungskatalogs.

Die Methode ist eine **Arbeitsanleitung für die Extraktion**. Sie enthält keine regulatorischen Aussagen, keine Auslegung konkreter Vorschriften und keine extrahierten Anforderungen. Es wird keine `RR` in dieser Datei angelegt.

Zweck ist die Reproduzierbarkeit gemäß [EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md) Abschnitt 3: Dieselbe Fundstelle soll bei erneuter Anwendung der Methode zum selben Extraktionsergebnis führen.

---

## 1. Definition der atomaren `RR`

**Verbindliche Definition:**

> Eine atomare `RR` ist die kleinste regulatorisch eigenständige Compliance-/Gap-Anforderung, für die ein aussagekräftiger Erfüllungsstatus unabhängig von anderen Verpflichtungen bestimmt werden kann, ohne bloße Modalitäten, Bedingungen, Zwecke oder Konkretisierungen künstlich zu verselbständigen.

**Klarstellung — eine `RR` ist nicht automatisch identisch mit:**

- einem Artikel,
- einem Absatz,
- einem Satz,
- einem Buchstaben,
- einem Aufzählungspunkt,
- einem Normabschnitt.

Die Gliederung der Quelle ist ein Ausgangspunkt für das Auffinden, aber kein Maßstab für die Atomizität.

**Eine Fundstelle kann ergeben:**

- **0 `RR`** — die Stelle enthält keine eigenständige, statusfähige Verpflichtung;
- **1 `RR`** — die Stelle enthält genau eine eigenständige Verpflichtung;
- **mehrere `RR`** — die Stelle enthält mehrere eigenständige Verpflichtungen.

Umgekehrt kann eine `RR` bei zwingend erforderlichem normativem Zusammenhang **mehrere Quellen-Lokatoren** benötigen (siehe Abschnitt 8).

---

## 2. Minimale Struktur einer `RR`

Für eine regulatorische Anforderung müssen aus der Hauptfundstelle oder dem zwingend erforderlichen Kontext bestimmbar sein:

| Element | Frage |
| --- | --- |
| Adressat / verpflichtetes Subjekt | Wen trifft die Pflicht? |
| Normative Handlung oder geforderter Sollzustand | Was ist zu tun oder herzustellen? |
| Objekt / Gegenstand | Worauf bezieht sich die Pflicht? |
| Bedingung / Trigger | Unter welchen Voraussetzungen gilt sie — sofern für den Geltungsumfang erforderlich? |
| Beurteilbares Compliance-Ergebnis | Woran lässt sich Erfüllung oder Nichterfüllung festmachen? |

**Nicht jedes Element muss wörtlich in derselben Fundstelle stehen.** Ergibt sich ein Element erst aus dem zwingend erforderlichen normativen Kontext, wird dieser Kontext als ergänzende Fundstelle geführt (Abschnitt 8).

Lässt sich auch nach Prüfung des Kontextes kein beurteilbares Compliance-Ergebnis bestimmen, liegt keine `RR` vor.

---

## 3. Entscheidungsalgorithmus

1. **Erforderlichen normativen Kontext bestimmen.** Welche weiteren Fundstellen sind nötig, um die Verpflichtung vollständig zu verstehen (Adressat, Definition, Bedingung, Umfang, Querverweis)?
2. **Compliance-/Gap-Relevanz prüfen.** Enthält die Stelle eine Verpflichtung, deren Erfüllungsstatus sinnvoll bestimmbar ist?
3. **Potenzielle Verpflichtungseinheiten identifizieren.** Welche voneinander unterscheidbaren Pflichten sind erkennbar?
4. **Atomizitäts- und Split-Test durchführen** (Abschnitte 4–6).
5. **Logische Struktur erhalten.** `und`-/`oder`-Verknüpfungen, Bedingungen und Ausnahmen dürfen durch die Zerlegung nicht verändert werden.
6. **Genau einen Themencluster bestimmen** gemäß [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Abschnitt 2.
7. **Mindestens eine Lebenszyklusphase bestimmen** gemäß [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Abschnitt 4.

### Zu Schritt 2 — keine `RR`

Keine `RR` wird angelegt, wenn die Stelle ausschließlich

- erläuternd ist,
- definitorisch ohne eigenständige Pflicht ist,
- Applicability-, Qualifikations- oder Klassifikationslogik enthält.

Für den letztgenannten Fall gilt die bereits in [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 5 dokumentierte `SRC → RUL`-Systematik einschließlich ihrer Schutzregel. Solche Stellen sind Material für Entscheidungsregeln, nicht für Gap-Anforderungen.

---

## 4. Verbindlicher Split-Test

**Zwei Bestandteile werden getrennt, wenn beide Bedingungen erfüllt sind:**

1. Ihre Erfüllungsstatus können unabhängig voneinander unterschiedlich sein.
2. Jeder Bestandteil bildet für sich eine vollständige, regulatorisch sinnvolle Compliance-Aussage.

Sind nicht beide Bedingungen erfüllt, wird nicht getrennt.

**Ausdrücklich nicht ausreichend:**

- Die Möglichkeit einer **getrennten technischen Messung** genügt nicht.
- Die Möglichkeit einer **getrennten Behebung** kann ein Indiz sein, ist aber **keine notwendige Bedingung** und für sich allein kein Split-Grund.

**Keine Zweifelsregel.** Es gilt weder „im Zweifel splitten" noch „im Zweifel bündeln". Eine solche Regel würde die Entscheidung von der Sache auf eine Konvention verlagern und wäre nicht reproduzierbar begründbar.

**Verbleibende Unklarheit.** Ist die Atomizität nach Prüfung des normativen Kontextes weiterhin begründet unklar, wird die Unsicherheit im Feld `Unsicherheit:` dokumentiert (siehe [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 4) und **vor endgültiger Aktivierung der betreffenden `RR` fachlich aufgelöst**. Eine `RR` mit ungeklärter Atomizität wird nicht auf `aktiv` gesetzt.

---

## 5. Muss trennen

Getrennt werden **muss**, wenn

- mehrere regulatorisch eigenständige Pflichten unabhängig voneinander erfüllt oder verletzt werden können;
- verschiedene Adressaten eigenständige Pflichten tragen;
- unterschiedliche Bedingungen tatsächlich getrennte eigenständige Verpflichtungen auslösen;
- zwei eigenständige Verpflichtungen wegen ihres normativen Hauptgegenstands unterschiedlichen Themenclustern zugeordnet werden müssen.

**Wichtig:** Unterschiedliche Themencluster sind nur dann ein Split-Grund, wenn bereits eigenständige Pflichten vorliegen. Die Clusterzuordnung ist Folge der Zerlegung, nicht ihr Auslöser — andernfalls würde die Taxonomie die regulatorische Struktur bestimmen statt umgekehrt.

---

## 6. Darf nicht trennen

Nicht künstlich abgespalten werden:

- die Modalität der Durchführung,
- eine notwendige Konkretisierung,
- Bedingung oder Trigger derselben Pflicht,
- eine Zweckangabe,
- der Umfang derselben Pflicht,
- ein unselbstständiges Qualitäts- oder Akzeptanzkriterium,
- eine Definition oder ein Querverweis, der lediglich dieselbe Pflicht vervollständigt.

Weiterhin gilt:

- **Mehrere Verben oder Aufzählungspunkte allein** sind kein Split-Grund.
- **Unterschiedliche mögliche Nachweisdokumente allein** sind kein Split-Grund.
- **Unterschiedliche Lebenszyklusphasen allein** sind kein Split-Grund; eine `RR` darf mehrere Phasen tragen.
- Ein **`A oder B`**, bei dem eine Alternative genügt, darf nicht in zwei kumulative `RR` verfälscht werden. Die Alternativität bleibt innerhalb einer `RR` erhalten.

---

## 7. Abstrakte Grenzfälle

Die folgenden Fälle sind **methodische Beispiele zur Anwendung der Regeln**. Sie enthalten keine `RR`-IDs, keine Fundstellen und keine Aussage über eine konkrete Vorschrift.

### Fall A — Mehrere Verben: `einrichten, dokumentieren, anwenden und aufrechterhalten`

**Regel:** Mehrere `RR`, **wenn** die konkrete Quellenstelle damit mehrere kumulativ geforderte und jeweils regulatorisch eigenständige Handlungen bezeichnet, deren Erfüllungsstatus unabhängig unterschiedlich sein kann.

Nicht wegen der bloßen Anzahl der Verben splitten. Maßgeblich ist, ob die einzelnen Handlungen im konkreten normativen Kontext eigenständig statusfähig sind.

### Fall B — Merkmalsreihe: `relevant, repräsentativ, fehlerfrei`

**Regel:** Mehrere `RR`, **wenn** jedes Qualitätsmerkmal im konkreten normativen Kontext selbstständig gefordert wird und einen eigenständig bewertbaren Compliance-Status besitzt.

**Eine `RR`**, wenn die Merkmale lediglich unselbstständige Konkretisierungen eines einzigen regulatorischen Qualitätsmaßstabs darstellen.

Die Entscheidung folgt aus dem Split-Test in Abschnitt 4, nicht aus der Anzahl der genannten Merkmale.

### Fall C — Zwei eigenständige Pflichten mit unterschiedlichen Themenclustern

**Regel:** Zwingender Split. Voraussetzung bleibt, dass bereits zwei eigenständige Pflichten vorliegen (siehe Abschnitt 5).

### Fall D — Reine Klassifizierungsregel

**Regel:** Keine `RR`. Die Stelle ist Material für die `SRC → RUL`-Systematik nach [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 5.

### Kontrollfall

> `Der Hersteller muss einen Prozess dokumentieren, sodass Verantwortlichkeiten eindeutig nachvollziehbar sind.`

**Bewertung:** Grundsätzlich **eine** `RR`. Die Nachvollziehbarkeit konkretisiert in dieser Struktur das geforderte Ergebnis bzw. Qualitätsmerkmal der Dokumentationspflicht und ist keine eigenständige zweite Pflicht.

---

## 8. Mehrere Quellen-Lokatoren

**Verbindliches Minimalitätsprinzip:**

> So wenige Fundstellen wie möglich, so viele wie zur vollständigen und reproduzierbaren Bestimmung der Anforderung erforderlich.

**Begriffliche Unterscheidung:**

| Begriff | Bedeutung |
| --- | --- |
| Normative Hauptfundstelle | Enthält die eigentliche Verpflichtung. |
| Ergänzende Fundstelle | Ergänzt einen zwingend erforderlichen Adressaten, eine Definition, eine Bedingung, den Umfang oder einen normativen Querverweis. |

Die Unterscheidung ist eine Lesehilfe innerhalb der bestehenden Struktur. Es wird **keine neue Artefaktart** und **keine neue Quellenhierarchie** eingeführt; alle Fundstellen bleiben Lokatoren auf `SRC`-Einträge nach [SOURCES.md](SOURCES.md) im Format aus [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 4.

Fundstellen, die für das Verständnis lediglich hilfreich, aber nicht erforderlich sind, werden nicht aufgenommen.

**Erwägungsgründe und Guidance** dürfen die Interpretation unterstützen. Sie dürfen eine gesetzliche Pflicht jedoch nicht scheinbar in eine Guidance-Pflicht umwandeln: Beruht eine Verpflichtung auf einem Rechtsakt, bleibt dieser die normative Hauptfundstelle.

---

## 9. Formulierung des `RR`-Textes

**Verbindliche Methode:** strukturierte normative Paraphrase mit präzisem Quellenbezug.

**Grundmuster:**

```
[Adressat] + [normativ geforderte Handlung/Sollzustand] + [Objekt] + [wesentliche Bedingung/Qualifikation, sofern erforderlich]
```

**Regeln:**

- Die normative Stärke wird nicht verändert.
- Es werden keine neuen Inhalte ergänzt.
- Bedingungen, Ausnahmen und Einschränkungen bleiben erhalten.
- Lange wörtliche Normtexte werden nicht übernommen.
- Insbesondere werden Inhalte lizenzierter Normen nicht umfangreich reproduziert.
- Die unterschiedliche normative Qualität von Rechtsakt, Guidance und Norm bleibt erhalten.

Guidance darf sprachlich nicht zu einer gesetzlichen Pflicht aufgewertet werden. Wörtliche Zitate werden gemäß den Pflichtfeldern in [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 6 als solche gekennzeichnet.

**Kein zusätzliches Pflichtattribut.** Für die Atomizitätsmethode wird derzeit **kein** zusätzliches Pflichtattribut `normative Qualität` eingeführt. Die normative Qualität ergibt sich aus der referenzierten Quelle und deren Status in [SOURCES.md](SOURCES.md) sowie aus der Formulierung des Anforderungstextes.

---

## 9.1 Divergierende authentische EU-Sprachfassungen

### Multilingual Source Divergence Protocol

1. Wird zwischen authentischen Sprachfassungen eines EU-Rechtsakts eine inhaltlich relevante Abweichung festgestellt, wird sie ausdrücklich dokumentiert und nicht redaktionell verdeckt.
2. Die bekannten und verifizierten betroffenen authentischen Sprachfassungen werden vergleichend geprüft.
3. Keine einzelne authentische Sprachfassung wird automatisch priorisiert.
4. Die Anzahl übereinstimmender Sprachfassungen bildet keine Mehrheitsregel und ersetzt keine unionsrechtliche Auslegung.
5. Projektinterne Übersetzungen oder Paraphrasen werden niemals als amtlicher Wortlaut behandelt.
6. Die divergierende Vorschrift wird unter Berücksichtigung von Regelungszusammenhang, Systematik, Zweck bzw. Zielsetzung und einschlägigem übrigem Unionsrecht ausgelegt. Erwägungsgründe dürfen dabei nach der bestehenden Regel aus Abschnitt 8 unterstützend herangezogen werden, bleiben aber keine normative Hauptfundstelle einer gesetzlichen `RR`.
7. Kann daraus eine hinreichend belastbare einheitliche normative Bedeutung bestimmt werden, gilt:
   - der deutsche und der englische `requirement_text` drücken diese einheitliche Bedeutung semantisch äquivalent aus;
   - die Auslegungsentscheidung bleibt nachvollziehbar dokumentiert;
   - die amtliche Textdivergenz wird nicht so dargestellt, als habe sie nie bestanden.
8. Kann keine hinreichend belastbare einheitliche Bedeutung bestimmt werden, gilt:
   - `uncertainty` enthält die konkrete Sprachfassungsdivergenz;
   - keine der authentischen Fassungen wird projektintern stillschweigend zur führenden Fassung erklärt;
   - die betreffende `RR` erhält den Status `aktiv` erst, wenn die Unsicherheit fachlich aufgelöst ist.

**Kein Vollvergleich aller Amtssprachen.** Dieses Protokoll verpflichtet nicht dazu, bei jeder Extraktion sämtliche authentischen EU-Sprachfassungen zu prüfen. Es greift, wenn eine relevante Divergenz bekannt wird oder bei der bilingualen DE-/EN-Prüfung auffällt.

### Rechtsmethodische Grundlage

| Entscheidung | Methodische Aussage |
| --- | --- |
| EuGH, Urteil vom 6. Oktober 2021, C-561/19, *Consorzio Italian Management*, Rn. 42 (CELEX `62019CJ0561`) | Die verschiedenen Sprachfassungen des Unionsrechts sind gleichermaßen verbindlich. |
| ebenda, Rn. 43 | Eine einzelne Sprachfassung darf weder alleinige Auslegungsgrundlage sein noch Vorrang vor den übrigen Fassungen beanspruchen; Unionsrecht ist im Licht aller Sprachfassungen einheitlich auszulegen und anzuwenden. |
| ebenda, Rn. 44 | Bekannte und festgestellte Abweichungen zwischen den Sprachfassungen sind zu berücksichtigen. |
| ebenda, Rn. 46 | Vorschriften sind in ihrem Zusammenhang und im Licht des Unionsrechts als Ganzes sowie seiner Ziele auszulegen. |
| EuGH, Urteil vom 26. November 2015, C-487/14, *Total Waste Recycling*, Rn. 46 (CELEX `62014CJ0487`) | Weichen die Sprachfassungen voneinander ab, ist die Vorschrift nach der allgemeinen Systematik und dem Zweck der Regelung auszulegen, zu der sie gehört. |

Diese Entscheidungen dienen ausschließlich als methodische Rechtsgrundlage des Extraktionsverfahrens. Sie sind **keine** regulatorischen `RR`-Extraktionsquellen des Katalogs und erhalten daher keine `SRC`-ID.

---

## 10. Katalogformat und Datenstruktur

### 10.1 Führende Vergabestelle

Die führende Vergabestelle und Single Source of Truth für regulatorische Anforderungen ist:

`docs/03-regulatory/RR_CATALOG.yaml`

Eine `RR` wird ausschließlich dort erstmalig mit einer `RR-NNN`-ID angelegt. Alle anderen Dateien dürfen `RR` nur referenzieren, nie neu vergeben. Das entspricht der Regel „genau eine Vergabestelle je Artefakttyp" aus [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 2.

### 10.2 Formatentscheidung: YAML

Führendes Format des Anforderungskatalogs ist **YAML**. Begründung:

- menschenlesbar und im Diff reviewbar,
- maschinenlesbar ohne zusätzliche Parserkonventionen,
- unterstützt verschachtelte DE/EN-Textfelder,
- unterstützt 1..n Lebenszyklusphasen als native Liste,
- unterstützt mehrere Quellen-Lokatoren als native Liste,
- vermeidet CSV-Sonderkonventionen für Listen in Zellen,
- besser manuell pflegbar als JSON.

Die Entscheidung ist begrenzt und reversibel; sie wird deshalb hier und nicht als eigener ADR geführt.

### 10.3 Pflichtstruktur je `RR`-Eintrag

Jeder Eintrag führt genau diese Felder:

| Feld | Inhalt |
| --- | --- |
| `id` | Identifikator im Format `RR-NNN` gemäß [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 1. |
| `status` | Genau ein Wert aus dem bestehenden Vokabular: `Entwurf`, `aktiv`, `ersetzt`, `zurückgezogen`. |
| `title.de` / `title.en` | Kurzer fachlicher Titel in Deutsch und Englisch. Kein wörtlicher Normtext. |
| `requirement_text.de` / `requirement_text.en` | Die nach Abschnitt 9 erzeugte strukturierte normative Paraphrase in Deutsch und Englisch. |
| `sources.primary` | Liste mit mindestens einem präzisen `SRC`-Lokator (normative Hauptfundstelle). |
| `sources.supplementary` | Liste mit 0..n ergänzenden `SRC`-Lokatoren. |
| `theme_cluster` | Genau ein kanonischer deutscher Wert aus [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Abschnitt 1. |
| `lifecycle_phases` | Liste mit mindestens einem kanonischen deutschen Wert aus [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) Abschnitt 3. |
| `uncertainty` | Pflichtfeld; `null` oder kurze sachliche Beschreibung. |
| `replaces` | Pflichtfeld; YAML-Liste mit 0..n existierenden `RR`-IDs. |
| `replaced_by` | Pflichtfeld; YAML-Liste mit 0..n existierenden `RR`-IDs. |

### 10.4 Semantik der Felder

**`id`** — Format gemäß Konvention. IDs werden ausschließlich in dieser Datei vergeben, sind unveränderlich und werden nie wiederverwendet.

**`status`** — Genau das bestehende Statusvokabular, keine weiteren Werte.

**`title`** — Kurzer fachlicher Titel zur Wiedererkennung, in beiden Sprachen. Kein wörtlicher Normtext.

**`requirement_text`** — Strukturierte normative Paraphrase nach Abschnitt 9. Grundsätzlich drücken beide Sprachfassungen **denselben ermittelten normativen Gehalt** aus. Die Projekttexte sind **keine zwei unabhängigen Interpretationen**, sondern die Übertragung derselben Aussage; beruht eine inhaltliche Differenz auf einer Übersetzungsabweichung im Projekt, ist das ein Fehler und keine zulässige Variante.

Wird dagegen eine Divergenz bereits in den authentischen EU-Quellfassungen festgestellt, gilt zwingend Abschnitt 9.1. Eine solche Quellendivergenz darf nicht durch freie Übersetzung verdeckt werden. Lässt sie sich nicht belastbar auflösen, bleibt `uncertainty` gesetzt und die `RR` erhält nicht den Status `aktiv`.

**`sources.primary`** — Mindestens ein präziser Lokator im Format aus [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 4. Normalerweise genau eine normative Hauptfundstelle. Mehrere Hauptfundstellen nur dann, wenn die Verpflichtung normativ tatsächlich erst durch deren Zusammenwirken vollständig begründet wird.

**`sources.supplementary`** — Nur Fundstellen, die für Adressat, Definition, Bedingung, Umfang oder zwingenden normativen Kontext erforderlich sind (Abschnitt 8). Lediglich interessante Hintergrundstellen werden nicht gesammelt. **Kein Lokator darf gleichzeitig in `primary` und `supplementary` stehen.**

**`theme_cluster`** — Genau ein kanonischer deutscher Wert, keine freie Texteingabe. Die englische Bezeichnung wird **nicht** redundant im Eintrag gespeichert, sondern aus dem kontrollierten Vokabular abgeleitet; so kann sie nicht auseinanderlaufen.

**`lifecycle_phases`** — Liste kanonischer deutscher Werte, mindestens einer, mehrere zulässig.

**`uncertainty`** — Pflichtfeld. `null`, wenn keine dokumentierte Unsicherheit besteht; andernfalls eine kurze sachliche Beschreibung. Eine ungeklärte Atomizitätsunsicherheit verhindert den Status `aktiv` (Abschnitt 4). Ebenso verhindert eine nach Abschnitt 9.1 ungelöste **materielle** Sprachfassungsdivergenz den Status `aktiv`; nicht jede sprachliche Abweichung ist eine solche Divergenz.

**`replaces` / `replaced_by`** — Pflichtfelder, jeweils als YAML-Liste mit 0..n existierenden `RR`-IDs:

- `replaces` enthält die `RR`-IDs der unmittelbar ersetzten Vorgänger.
- `replaced_by` enthält die `RR`-IDs der unmittelbaren Nachfolger.
- Besteht keine Ersetzungsbeziehung, ist die jeweilige Liste leer: `[]`.
- Mehrere IDs sind zulässig, damit Split- und Konsolidierungsfälle nachvollziehbar bleiben.
- Selbstreferenzen sind unzulässig: Eine `RR` darf ihre eigene ID in keiner der beiden Listen führen.
- IDs werden hierfür niemals erfunden; nur bereits im Katalog vergebene `RR`-IDs sind zulässig.

Befüllt werden die Listen bei inhaltlich wesentlicher Änderung gemäß der Lebenszykluskonvention in [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 3.

### 10.5 Katalogversionierung

`RR_CATALOG.yaml` führt eine Katalogversion im bestehenden `MAJOR.MINOR`-Format. Startwert ist `0.1`.

| Bereich | Bedeutung |
| --- | --- |
| `0.x` | Katalog befindet sich im kontrollierten Aufbau bzw. in der Extraktionsphase. |
| `1.0` | Erste eingefrorene Baseline, die für systematische Tests, Fallstudie bzw. Evaluation verwendet werden kann. |

Fortschreibung:

- **MINOR erhöhen** bei logisch abgeschlossenen Katalogänderungen, die die Struktur nicht inkompatibel verändern — etwa neue `RR`, Statusänderungen oder redaktionelle Korrekturen.
- **MAJOR erhöhen** bei inkompatiblen Änderungen der Katalogstruktur oder einer methodisch grundlegenden Änderung, die die Interpretation des Katalogs verändert.

**Wichtig:** Eine inhaltlich wesentliche Änderung einer bestehenden `RR` erhält weiterhin eine **neue `RR`-ID** gemäß [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) Abschnitt 3. Die Katalogversion ersetzt diese Regel nicht, sondern ergänzt sie auf Dateiebene.

Auswertungen, Tests und Evidenzen nennen die verwendete Katalogversion.

---

## 11. Verknüpfungen

| Dokument | Rolle |
| --- | --- |
| [DOCUMENTATION_CONVENTIONS.md](../00-project/DOCUMENTATION_CONVENTIONS.md) | ID-Schema, Lokator-Syntax, Pflichtfelder, Traceability-Pfade, `SRC → RUL`-Systematik |
| [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) | Zulässige Werte und Zuordnungsregeln für Themencluster und Lebenszyklusphase |
| [SOURCES.md](SOURCES.md) | Führendes Quellenregister und Fundstellen-Zitierweise je Quelle |
| [EXPOSE_SCOPE.md](../00-project/EXPOSE_SCOPE.md) | Verbindlicher wissenschaftlicher Rahmen und Untersuchungsumfang |

Die Methode führt keine zusätzlichen regulatorischen `RR`-Extraktionsquellen ein. Unmittelbar zitierte Rechtsprechung dient ausschließlich der methodischen Begründung des Extraktionsverfahrens; aus ihr entstehen weder `RR` noch zusätzliche `SRC`-Einträge des regulatorischen Anforderungskatalogs.

---

## 12. Änderungshistorie

| Version | Änderung |
| --- | --- |
| 1.0 | Erstfassung der methodischen Regeln für RR-Relevanz, Atomizität, 0/1/n-Extraktion, Split-Test, Quellenbezug und kontrollierte Paraphrase. |
| 1.1 | Abschnitt 10 ergänzt: YAML als führendes Katalogformat begründet, `RR_CATALOG.yaml` als führende Vergabestelle festgelegt, Pflichtstruktur und Feldsemantik eines `RR`-Eintrags sowie die Katalogversionierung definiert. Keine Änderung der Extraktions-, Atomizitäts- oder Split-Regeln. |
| 1.2 | Multilingual Source Divergence Protocol ergänzt: Umgang mit divergierenden authentischen EU-Sprachfassungen, unionsrechtliche Auslegungsgrundlage sowie Aktivierungssperre bei ungelöster materieller Sprachfassungsdivergenz festgelegt. Feldstruktur und Atomizitätsregeln unverändert; die Ergänzung betrifft die Source-Fidelity- und Interpretationslogik. |
