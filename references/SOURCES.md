# Quellen und Datenbasis

**Stand:** 2026-09-05
**Nächste Prüfung:** 2027-03-05 (halbjährlich)
**Geprüft von:** Repo-Wartung

Dieser Skill trifft Aussagen über den LinkedIn-Algorithmus und über Kennzahlen. Diese Datei sagt
für jede dieser Aussagen, worauf sie beruht. Aussagen ohne belegbare Quelle stehen unter
„Zurückgezogen" und sind aus SKILL.md, README.md und den beiden Landingpages entfernt.

Die Regel für künftige Änderungen: Eine Zahl darf nur dann in den Skill, wenn sie hier eine Zeile
mit URL und Veröffentlichungsdatum bekommt. Wer eine Zahl nicht belegen kann, streicht die Aussage,
statt eine Quelle zu suchen, die ungefähr passt.

Das Verfahren ist aus dem Schwester-Repo
[LinkedInOptimizer](https://github.com/GodModeAI2025/LinkedInOptimizer) übernommen, samt Prüfskript.
Dort waren dieselben Zahlen bereits zurückgezogen, während sie hier noch standen.

`scripts/check_sources.py` prüft, dass jede im Skill verwendete Quellen-ID hier existiert, dass jede
Zeile eine URL und ein Datum trägt und dass das Prüfdatum nach dem Stand liegt. Die Sperren gegen
zurückgezogene Aussagen erzeugt dasselbe Skript aus der Spalte „Sperrmuster". Sie prüfen
Schreibweisen, keine Aussagen: Ein frei formulierter Satz, der eine zurückgezogene Behauptung in
neuen Worten aufstellt, fällt ihnen nicht auf.

---

## Belegte Quellen

| ID | Belegt | Quelle | URL | Veröffentlicht | Abgerufen | Einstufung |
|----|--------|--------|-----|----------------|-----------|------------|
| Q1 | Dwell Time ist ein Ranking-Signal im LinkedIn-Feed. LinkedIn misst, wie lange ein Beitrag betrachtet wird, und nutzt das, weil Klicks und Reaktionen selten und binär sind. | LinkedIn Engineering Blog, „Understanding dwell time to improve LinkedIn feed ranking" | https://www.linkedin.com/blog/engineering/feed/understanding-feed-dwell-time | 2020-05-12 | 2026-09-05 | Primärquelle (Plattformbetreiber) |
| Q2 | LinkedIn setzt für das Feed-Ranking ein eigenes, groß angelegtes Ranking-Modell ein. Die Zusammenfassung nennt Feed-Ranking als einen der Einsatzorte. | Borisyuk et al., „LiRank: Industrial Large Scale Ranking Models at LinkedIn", arXiv:2402.06859 | https://arxiv.org/abs/2402.06859 | 2024-02-10 (v2: 2024-08-07) | 2026-09-05 | Primärquelle (Publikation des Betreibers) |

### Was diese Quellen ausdrücklich nicht belegen

- **Q1** belegt, dass Dwell Time als Signal genutzt wird. Sie belegt kein Gewicht, keinen
  Prozentwert und keinen Stand 2025 oder 2026. Der Beitrag ist von 2020.
- **Q2** nennt Feed-Ranking als Einsatzort eines großen Ranking-Modells. Sie nennt weder die drei
  Verteilungsstufen, die dieser Skill beschreibt, noch einzelne Ranking-Gewichte, noch eine
  Seed-Größe oder ein Zeitfenster.

Das dreistufige Verteilungsmodell (Qualitäts-Filter, Seed-Test, erweiterte Distribution) ist damit
ein Arbeitsmodell aus der Beratungspraxis, kein dokumentierter Aufbau. Es steht im Skill, weil es
Entscheidungen ordnet, nicht weil es gemessen wäre.

---

## Zurückgezogen

Diese Aussagen standen bis Version 1.0.0 im Skill und sind ohne Ersatz entfernt worden. Die
zugrunde liegende Empfehlung bleibt jeweils bestehen, die Zahl nicht. Sie kommen nur zurück, wenn
jemand eine Quelle mit URL und Datum beibringt.

Die Spalte **Sperrmuster** ist der maschinenlesbare Teil dieser Tabelle. Mehrere Muster werden mit
Semikolon getrennt. Das Skript normalisiert selbst: `%` fängt auch das ausgeschriebene Prozent,
Leerzeichen fangen auch das geschützte Leerzeichen und den Bindestrich, Bindestriche fangen die
typografischen Varianten, ein führendes `+` oder `~` ist optional, Groß- und Kleinschreibung ist
egal. Drei Punkte stehen für eine Lücke von bis zu 40 Zeichen in derselben Zeile.

Diese Lücke ist zugleich die Grenze der Tabelle: Auf der Landingpage stand die Prozentspalte des
Format-Rankings rund 120 Zeichen Markup von ihrem Label entfernt, ein Kontextmuster hätte sie nicht
gefasst. Für diesen Fall steht in `scripts/check_sources.py` eine eigene Prüfung im Code:
`<span class="rank-pct">` darf keine Ziffer enthalten. Das ist ein Codediff und keine Tabellenzelle.

| Frühere Aussage | Stand bis | Warum entfernt | Sperrmuster |
|-----------------|-----------|----------------|-------------|
| „Persönliche Profile erzielen 5x mehr Engagement als Firmenseiten" (SKILL.md, README, developer.html als „(5x Engagement)") | v1.0.0 | Kein Beleg auffindbar. Dass persönliche Profile im Feed sichtbarer sind als Unternehmensseiten, bleibt als Erfahrungswert; der Faktor nicht. | 5x mehr Engagement; 5x Engagement |
| „Kommentare zählen 8-15x mehr als Likes", auf der Landingpage „8–15x mehr Gewicht als Likes" | v1.0.0 | Kein belegbarer Faktor. Im Schwester-Repo war die verwandte Angabe „2,5× mehr algorithmisches Gewicht" aus demselben Grund zurückgezogen. Dass inhaltliche Kommentare schwerer wiegen als Likes, bleibt. | 8-15x |
| „Saves sind ca. 5x wertvoller als Likes", englisch „5x more valuable than likes" | v1.0.0 | Kein Beleg. Saves bleiben als stärkstes Signal dieses Skills benannt, ohne Faktor. | 5x wertvoller; 5x more valuable |
| „Posts ... werden 2-5% des Netzwerks gezeigt", Landingpage „nur 2–5% deines Netzwerks", englisch „only 2–5% of your network" | v1.0.0 | Kein Beleg. Die Seed-Größe ist von außen nicht messbar. Dass die Erstverteilung klein ist, bleibt als Modellannahme. | 2-5 % |
| „Die ersten 60-90 Minuten entscheiden über 70% der Gesamtreichweite", englisch „determine 70% of total reach" | v1.0.0 | Weder Zeitfenster noch Anteil sind belegbar. Dass die erste Zeit nach dem Posten den weiteren Verlauf prägt, bleibt als Erfahrungswert. | 70 % der Gesamtreichweite; 70 % of total reach; 60-90 Minuten |
| „Posts ... erhalten bis zu 40% mehr Reichweite als themenfremde Inhalte", Landingpage „Post passt zu deinem Profil = +40%" | v1.0.0 | Kein Beleg. Die Empfehlung thematischer Konsistenz bleibt ohne Prozentwert. | 40 % mehr Reichweite; = +40 %; match (+40 %) |
| „Externe Links im Post-Text: Bis zu 60% weniger Reichweite", englisch „up to -60%" | v1.0.0 | Kein Beleg. Die Empfehlung, den Link in den ersten Kommentar zu setzen, bleibt ohne Prozentwert. | 60 % weniger Reichweite; 60 % Reichweite; 60 % less reach; -60 % |
| Prozentwerte des Format-Rankings: „Höchstes Engagement (~24-46%)" und „bis zu 46%" (SKILL.md), Landingpage Karussells ~46%, Text-only ~35%, Video ~28%, Dokumente ~22%, Einzelbilder ~15%, Externe Links ~8% | v1.0.0 | Keine prüfbare Primärquelle. Anbieterstudien nennen für dieselben Formate deutlich abweichende Werte und wechseln sie jährlich. Die Rangfolge der Formate bleibt als Erfahrungswert, die Prozentwerte nicht. | 24-46 %; bis zu 46 %; Karussells...46 %; Text-only...35 %; Video...28 %; Dokumente...22 %; Einzelbilder...15 %; Externe Links...8 % |
| „Native Video: 20x mehr Shares", auf der Landingpage „20x Shares" | v1.0.0 | Kein Beleg. Dass Video geteilt wird, bleibt ohne Faktor. | 20x |
| „72% schauen ohne Ton" und „72% der LinkedIn-Aktivität ist mobil" | v1.0.0 | Kein Beleg, und zwei verschiedene Behauptungen mit derselben Zahl. Untertitel bleiben empfohlen, mobile Lesbarkeit bleibt Vorgabe, beides ohne Prozentwert. | 72 % |
| „Profile mit 100% Vollständigkeit erzielen bis zu 71% mehr Reichweite", englisch „Profiles at 100% completion get up to 71% more reach" | v1.0.0 | Kein Beleg. Die Empfehlung, das Profil zu vervollständigen, bleibt ohne Reichweitenversprechen. | 71 %; 100 % Vollständigkeit erzielen; at 100 % completion get |
| „Fragen in den ersten 5 Sekunden erzeugen 32% mehr Kommentare" | v1.0.0 | Kein Beleg, dazu eine Sekundenangabe, die für einen Textbeitrag nicht definiert ist. | 32 %; ersten 5 Sekunden |
| „7 Sekunden Scan-Zeit", englisch „7 seconds of scan time" | v1.0.0 | Kein Beleg. Dass im Vorbeiscrollen gelesen wird, bleibt als Vorgabe für den Hook. | 7 Sekunden Scan; 7 seconds of scan |
| „Erfolgreiche Posts können 2-3 Wochen sichtbar bleiben" | v1.0.0 | Kein Beleg. Im Schwester-Repo war die verwandte Angabe „bis zu 5 Tage Sichtbarkeit" aus demselben Grund zurückgezogen. | 2-3 Wochen |
| Beispiel-Hook „Warum scheitern 81% der [X]-Kampagnen?" | v1.0.0 | Eine erfundene Zahl in einer Vorlage lädt dazu ein, eine erfundene Zahl zu posten. Der Hook steht jetzt ohne Zahl, mit dem Hinweis, dass eine Zahl im Hook eine nennbare Quelle braucht. | 81 % |

---

## Erfahrungswerte ohne Quelle

Diese Angaben sind keine Messwerte. Sie sind nachvollziehbar begründet, aber nicht belegt, und
dürfen nicht als Benchmark gegen ein Konto gehalten werden:

- Das dreistufige Verteilungsmodell in „Algorithmus-Verständnis".
- Die Rangfolge der Formate (Karussells vor Text-only vor Video vor Dokumenten vor Einzelbildern
  vor Links).
- Die Gewichtung der Themen-Lanes 60/25/15, der Format-Mix 50/30/20/0 und die 90/10-Regel. Das sind
  Vorgaben dieses Skills, keine gemessenen Verteilungen.
- Die 15 bis 20 Minuten der täglichen Engagement-Routine und die Kadenz von 3 beziehungsweise
  5 Beiträgen pro Woche.
- Die Arbeitsgröße von rund 200 Zeichen für den Hook. Wo LinkedIn den Text abschneidet, hängt von
  Gerät und Fensterbreite ab.
- Die Stufen der Monetarisierungs-Leiter und die Warnsignal-Checkliste in Phase 6.

## Prüfrhythmus

Halbjährlich, jeweils zum Stand-Datum plus sechs Monate. Zu prüfen ist bei jedem Durchgang:

1. Sind die URLs in der Tabelle noch erreichbar und tragen sie noch dieselbe Aussage?
2. Lässt sich eine der zurückgezogenen Zahlen inzwischen belegen?
3. Stand-Datum und nächstes Prüfdatum hochsetzen und den Changelog in README.md ergänzen.
