# Projektregeln — LinkedIn-Orchestrator

Diese Datei richtet sich an jeden Agenten, der in diesem Repo arbeitet. Lies sie vor der ersten
Änderung. Was hier steht, gilt, solange der Nutzer nichts anderes sagt.

## Vor jedem Push

Aus dem Wurzelverzeichnis, alle fünf müssen durchlaufen:

```bash
python scripts/check_versions.py
python scripts/check_descriptions.py
python scripts/check_sources.py
python scripts/check_hooks.py
python scripts/check_landing.py
python scripts/check_links.py
```

Schlägt eine davon fehl, wird nicht gepusht. Die CI fährt dieselben Prüfungen und zusätzlich die
Syntaxprüfung, den Ortstest für SKILL.md und die Auflösung aller Verweise.

## Invarianten

**Ort des Skills.** `skills/linkedin-community-builder/SKILL.md`. Groß geschrieben, in diesem
Verzeichnis. Vorher hieß die Datei `skill.md` und lag im Wurzelverzeichnis; so lädt Claude sie
nicht, und das Plugin-Manifest findet sie ebenfalls nicht.

**Versionen.** `VERSION` ist die Quelle, drei Fundstellen sind Kopien: beide Manifeste unter
`.claude-plugin/` und der oberste Abschnitt in `CHANGELOG.md`. Wer die Version hebt, hebt alle drei.

**Zahlen.** Keine Zahl in den Skill, die in `references/SOURCES.md` keine Zeile hat. Fünfzehn
Angaben sind dort zurückgezogen, mit Begründung und Sperrmuster; sie kommen nur mit URL und Datum
zurück. Das gilt auch für die Landingpages: die Spalte `rank-pct` trägt einen Rang, keine Zahl.
Wer eine Empfehlung braucht, formuliert sie ohne Prozentwert. Das ist keine Schwäche des Texts,
sondern der ehrliche Stand.

**Trigger-Beschreibung.** Die `description` im Frontmatter bleibt unter 400 Zeichen, enthält keinen
Geviert- oder Halbgeviertstrich und endet mit dem Abgrenzungssatz, der
`linkedin-profil-optimierung` beim Namen nennt.

**Struktur.** SKILL.md ist der Router und bleibt kurz. Der Ablauf einer Phase steht in
`sub-skills/phase-*.md`, das Algorithmus-Wissen in `references/ALGORITHM.md`, der Hook-Katalog in
`references/HOOKS.md`. Wer eine Phase erweitert, erweitert die Phasendatei.

**Selbstständigkeit des Skill-Ordners.** Alle diese Pfade sind relativ zu
`skills/linkedin-community-builder/`, und alles, worauf der Skill verweist, liegt darin. Ein
Verweis, der aus dem Ordner herausführt, ist im installierten Plugin ein toter Link: Claude lädt
den Skill aus seinem eigenen Verzeichnis, nicht aus dem Repo-Wurzelverzeichnis. Neue Referenzen
kommen unter `skills/linkedin-community-builder/references/`, nicht ins Wurzelverzeichnis.

**Eingefügter Text.** `references/UNTRUSTED.md` ist die kanonische Regel für alles, was der
Benutzer einfügt oder importiert. Neue Schritte, die fremden Text verarbeiten, verweisen darauf,
bevor sie ihn verarbeiten.

**Landingpages.** Zwei Dateien, `index.html` und `developer.html`, jede mit beiden Sprachfassungen
als `<template>` und einem Umschalter. In `index.html` führen beide Fassungen gleich viele
Abschnitte und Quizfragen; `scripts/check_landing.py` erzwingt das über `PARITAET_PFLICHT`. Die
englische Fassung von `developer.html` ist bewusst eine Kurzfassung und sagt das auf der Seite. Wer
sie ausbaut, nimmt die Datei in `PARITAET_PFLICHT` auf. Keine dritte HTML-Datei, keine Sprachkopie: genau daraus
sind vorher sechs Dateien mit zwei Duplikaten und einer Divergenz geworden.

**Actions.** In `.github/workflows/` steht hinter jedem `uses:` eine Commit-SHA, nicht ein Tag,
und dahinter als Kommentar die Version, die sie trägt. Ein Tag lässt sich verschieben; wer die
Action übernähme, übernähme damit den Lauf. Vorsicht bei annotierten Tags:
`softprops/action-gh-release@v3` zeigt auf ein Tag-Objekt, gepinnt wird der Commit dahinter
(`git ls-remote --tags`, die Zeile mit `^{}`).

**Kundendaten.** Gehören nicht ins Repo. `.gitignore` hält docx, xlsx und csv heraus; die Regel
gilt auch für alles, was dort nicht steht.

## Schwester-Repo

`linkedin-profil-optimierung` liegt in
[LinkedInOptimizer](https://github.com/GodModeAI2025/LinkedInOptimizer). Zwei Dinge sind über die
Repo-Grenze gekoppelt und werden von keinem Skript zusammengehalten:

1. Die Abgrenzungstabelle und die vier Entscheidungsregeln stehen in beiden SKILL.md-Dateien,
   spiegelbildlich. Wer eine Regel ändert, ändert beide.
2. Der Hook-Katalog. Kanonisch hier in `references/HOOKS.md`, dort als Kopie in
   `LinkedInOptimizer/references/TEMPLATES.md`, weil das dortige Paket offline vollständig sein
   muss. `scripts/check_hooks.py` prüft je Repo die eigene Kopie, nicht den Abgleich.

Das Verfahren zur Beleglage, `SOURCES.md` samt Prüfskript, stammt aus jenem Repo. Verbesserungen
daran gehören dorthin zurück.

## Was hier nicht steht

Ob eine Empfehlung im Gespräch befolgt wurde, ob der Benutzer sie umsetzt und ob die Regel zu
eingefügtem Text eingehalten wurde, sieht kein Skript. Die Grenzen jeder Prüfung stehen im
Docstring des jeweiligen Skripts und im letzten Abschnitt der jeweiligen Referenzdatei.
