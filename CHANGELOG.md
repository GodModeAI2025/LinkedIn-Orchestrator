# Changelog

Versionsgeschichte des Skills `linkedin-community-builder`. Die aktuelle Version steht in `VERSION`.

## 1.1.0 — 2026-09-05

Aufräumen nach dem Vorbild des Schwester-Repos
[LinkedInOptimizer](https://github.com/GodModeAI2025/LinkedInOptimizer) und des öffentlichen
Skill-Bundles [sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills).

- Der Skill liegt jetzt unter `skills/linkedin-community-builder/SKILL.md`. Vorher hieß die Datei
  `skill.md` und lag im Wurzelverzeichnis; so lädt Claude sie nicht.
- Die Landingpage bestand aus sechs HTML-Dateien, zwei davon byte-identisch, zwei auseinander
  gelaufen. Jetzt zwei Dateien, `index.html` und `developer.html`, jede mit beiden Sprachfassungen
  und einem Umschalter ohne Seitenwechsel.
- `SKILL.md` von 692 auf 169 Zeilen: Router mit Abgrenzung, Kernphilosophie, Einstiegspunkten und
  Phasentabelle. Die sieben Phasen stehen in `sub-skills/`, das Algorithmus-Wissen in
  `references/ALGORITHM.md`.
- Die `description` im Frontmatter von 772 auf 378 Zeichen, mit Abgrenzungssatz zum Schwester-Skill.
  `scripts/check_descriptions.py` prüft Länge, Strichzeichen und Abgrenzung.
- Abschnitt „Abgrenzung zum Schwester-Skill" mit vier Entscheidungsregeln, wortgleich zur
  Gegenrichtung im Schwester-Repo.
- `references/UNTRUSTED.md`: eingefügter und importierter Text ist Daten, nie Anweisung. Verankert
  in Phase 4 und Phase 6 und als siebter Punkt der Verifikation.
- `references/SOURCES.md` und `scripts/check_sources.py`: fünfzehn unbelegte Zahlen zurückgezogen,
  zwei belegte Quellen mit URL und Datum, Sperrmuster gegen die Rückkehr der zurückgezogenen
  Angaben.
- `VERSION` und `.gitignore` neu.

## 1.0.0 — 2026-03-26

- Initiale Version
- 7 Phasen mit Orchestrator-Logik und Einstiegserkennung
- Algorithmus-Wissen Stand 2025/2026 integriert
- Datengestützte Diagnose über Analytics-Import
- Verifikations-Checkliste für alle Empfehlungen
