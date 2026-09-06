# -*- coding: utf-8 -*-
"""Prueft die beiden Landingpages auf die Struktur, die der Umschalter braucht.

Bis v1.0.0 lagen sechs HTML-Dateien im Repo: index.html und index_de.html waren
byte-identisch, developer.html und index_dev_de.html waren auseinandergelaufen.
Seit v1.1.0 gibt es zwei Dateien, jede mit beiden Sprachfassungen als <template>
und einem Umschalter, der nur eine Fassung in den DOM haengt.

Geprueft wird, was diese Bauform traegt:

1. Beide Sprach-Templates sind da, content-de und content-en.
2. In jedem Template steht ein Umschalter mit data-lang-switch.
3. Kein Verweis mehr auf die geloeschten Dateien. Ein href auf index_de.html
   waere ein 404 auf GitHub Pages.
4. Die Modul-IDs kommen je Template genau einmal vor. Laege beides gleichzeitig
   im DOM, waeren sie doppelt und die Navigation liefe auf die falsche Haelfte.

Exitcode 0, wenn beide Seiten das erfuellen. Exitcode 1 sonst.

5. In index.html tragen beide Sprachfassungen dieselbe Zahl an Abschnitten und
   Quizfragen. Die englische Fassung war lange kuerzer: sieben Abschnitte und
   das ganze Quiz fehlten. Wer einen Abschnitt nur auf einer Seite ergaenzt,
   faellt jetzt auf.

Fuer developer.html gilt Punkt 5 nicht, und das ist eine Entscheidung, keine
Nachlaessigkeit: die englische Fassung dieser Seite ist eine Kurzfassung mit
vier Abschnitten, waehrend die deutsche zwoelf fuehrt. Sie sagt das auf der
Seite selbst. Wer sie eines Tages ausbaut, nimmt PARITAET_PFLICHT diese Datei
hinzu und hat die Pruefung sofort im Ruecken.

Nicht geprueft wird, ob die beiden Fassungen inhaltlich dasselbe sagen. Gezaehlt
werden Abschnitte, nicht Bedeutungen: eine Ueberschrift ohne Inhalt zaehlt mit.
Ebenso wenig geprueft wird, ob die Kurzfassung ihren Hinweis noch traegt.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEITEN = ["index.html", "developer.html"]

# Seiten, deren Sprachfassungen gleich viele Abschnitte fuehren muessen.
# developer.html fehlt hier bewusst, siehe Docstring.
PARITAET_PFLICHT = {"index.html"}
GELOESCHT = ["index_de.html", "index_en.html", "index_dev_de.html", "index_dev_en.html"]

TEMPLATE = re.compile(r'<template id="content-(de|en)">(.*?)</template>', re.S)
ABSCHNITT = re.compile(r'class="screen-heading"')
QUIZFRAGE = re.compile(r'class="quiz-question-block"')
MODUL_ID = re.compile(r'\bid="(m\d+)"')


def pruefe(rel_pfad: str, fehler: list) -> None:
    pfad = ROOT / rel_pfad
    if not pfad.exists():
        fehler.append(f"{rel_pfad} fehlt")
        return
    inhalt = pfad.read_text(encoding="utf-8")

    templates = dict((sprache, koerper) for sprache, koerper in TEMPLATE.findall(inhalt))
    for sprache in ("de", "en"):
        if sprache not in templates:
            fehler.append(f"{rel_pfad}: das Template content-{sprache} fehlt")

    for sprache, koerper in templates.items():
        if "data-lang-switch" not in koerper:
            fehler.append(
                f"{rel_pfad}: das Template content-{sprache} hat keinen Umschalter "
                "(data-lang-switch). Ohne ihn kommt man aus dieser Fassung nicht heraus."
            )
        ids = MODUL_ID.findall(koerper)
        doppelt = sorted({i for i in ids if ids.count(i) > 1})
        if doppelt:
            fehler.append(
                f"{rel_pfad}: im Template content-{sprache} kommen die Modul-IDs "
                f"{', '.join(doppelt)} mehrfach vor."
            )

    # Nicht nur href="index_de.html": auch ./index_de.html, einfache
    # Anfuehrungszeichen und ein angehaengter Anker fuehren auf dieselbe
    # geloeschte Datei und damit auf dieselbe 404.
    if rel_pfad in PARITAET_PFLICHT and "de" in templates and "en" in templates:
        for muster, was in ((ABSCHNITT, "Abschnitte"), (QUIZFRAGE, "Quizfragen")):
            zahlen = dict(
                (sprache, len(muster.findall(koerper)))
                for sprache, koerper in templates.items()
            )
            if zahlen["de"] != zahlen["en"]:
                fehler.append(
                    f"{rel_pfad}: {was} ungleich verteilt, deutsch {zahlen['de']}, "
                    f"englisch {zahlen['en']}. Beide Fassungen fuehren denselben Kurs."
                )

    for name in GELOESCHT:
        muster = re.compile(
            r"""href\s*=\s*["']\s*\.?/?%s(?:[#?][^"']*)?\s*["']""" % re.escape(name)
        )
        for treffer in muster.finditer(inhalt):
            zeile = inhalt.count("\n", 0, treffer.start()) + 1
            fehler.append(
                f"{rel_pfad}:{zeile}: Verweis auf {name}. Die Datei ist entfernt, "
                "der Link waere ein 404."
            )


def main() -> int:
    fehler = []
    for rel_pfad in SEITEN:
        pruefe(rel_pfad, fehler)

    if fehler:
        print("FEHLER:", file=sys.stderr)
        for eintrag in fehler:
            print(f"  - {eintrag}", file=sys.stderr)
        return 1

    print("OK: %s tragen beide Sprachfassungen mit Umschalter" % " und ".join(SEITEN))
    return 0


if __name__ == "__main__":
    sys.exit(main())
