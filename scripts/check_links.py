# -*- coding: utf-8 -*-
"""Prueft, dass jeder Verweis im Repo auf eine Datei zeigt, die es gibt.

Zwei Gruppen mit zwei verschiedenen Bezugspunkten, und genau das war der Fehler,
den diese Pruefung gefunden hat:

1. **Verweise aus dem Skill.** Der Skill-Text nennt Dateien in Backticks, etwa
   `references/SOURCES.md`. Diese Pfade sind relativ zum Skill-Verzeichnis, denn
   Claude laedt den Skill aus seinem eigenen Ordner und nicht aus dem
   Repo-Wurzelverzeichnis. Ein Verweis, der aus dem Skill-Ordner herausfuehrt,
   ist im installierten Plugin ein toter Link, auch wenn die Datei im Repo
   existiert.

2. **Markdown-Links in der Doku.** README, CLAUDE.md, CHANGELOG und SECURITY
   verlinken mit [Text](pfad). Diese Pfade sind relativ zum
   Repo-Wurzelverzeichnis, denn dort liest sie GitHub.

Geprueft wird die Existenz der Datei. Nicht geprueft wird, ob der Verweis
inhaltlich passt, ob ein Anker in der Zieldatei existiert und ob eine externe
URL erreichbar ist.

Exitcode 0, wenn alle Verweise aufloesen. Exitcode 1 sonst, mit Datei und Zeile
je Verstoss.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Wurzel, gegen die Verweise aus dem Skill-Text aufloesen.
SKILL_ROOT = ROOT / "skills/linkedin-community-builder"

# Dateien, deren Backtick-Verweise relativ zum Skill-Verzeichnis gelten.
SKILL_DATEIEN = sorted(SKILL_ROOT.rglob("*.md"))

# Dateien, deren Markdown-Links relativ zum Repo-Wurzelverzeichnis gelten.
DOKU_DATEIEN = [ROOT / name for name in ["README.md", "CLAUDE.md", "CHANGELOG.md"]]

# `references/X.md`, `sub-skills/X.md`, `scripts/X.py`
BACKTICK = re.compile(r"`((?:references|sub-skills|scripts)/[A-Za-z0-9._/-]+\.(?:md|py|js))`")

# [Text](pfad) ohne Schema und ohne Anker-nur-Ziel
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)#][^)]*?)\)")


def pruefe_skill(fehler):
    for pfad in SKILL_DATEIEN:
        text = pfad.read_text(encoding="utf-8")
        for nummer, zeile in enumerate(text.splitlines(), 1):
            for ziel in BACKTICK.findall(zeile):
                if not (SKILL_ROOT / ziel).exists():
                    fehler.append(
                        "%s:%d: `%s` loest relativ zum Skill-Verzeichnis nicht auf. "
                        "Im installierten Plugin ist das ein toter Verweis."
                        % (pfad.relative_to(ROOT), nummer, ziel)
                    )


def pruefe_doku(fehler):
    for pfad in DOKU_DATEIEN:
        if not pfad.exists():
            fehler.append("%s fehlt" % pfad.name)
            continue
        text = pfad.read_text(encoding="utf-8")
        for nummer, zeile in enumerate(text.splitlines(), 1):
            for ziel in MD_LINK.findall(zeile):
                ziel = ziel.split("#", 1)[0].strip()
                if not ziel or "://" in ziel or ziel.startswith("mailto:"):
                    continue
                if not (ROOT / ziel).exists():
                    fehler.append(
                        "%s:%d: der Link auf %s zeigt ins Leere."
                        % (pfad.relative_to(ROOT), nummer, ziel)
                    )


def main() -> int:
    fehler = []
    pruefe_skill(fehler)
    pruefe_doku(fehler)

    if fehler:
        print("FEHLER:", file=sys.stderr)
        for eintrag in fehler:
            print("  - %s" % eintrag, file=sys.stderr)
        return 1

    print("OK: %d Skill-Dateien und %d Doku-Dateien, alle Verweise loesen auf"
          % (len(SKILL_DATEIEN), len(DOKU_DATEIEN)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
