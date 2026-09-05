# -*- coding: utf-8 -*-
"""Prueft, ob die Skill-Version an allen dokumentierten Stellen uebereinstimmt.

Die Quelle ist die Datei VERSION im Repo-Wurzelverzeichnis. Sie enthaelt eine
Zeile mit der Versionsnummer ohne fuehrendes v. Alles andere ist eine Kopie,
die hier gegen die Quelle geprueft wird.

Geprueft werden drei Fundstellen: das Plugin-Manifest, der Marketplace-Eintrag
und der oberste Abschnitt in CHANGELOG.md.

Exitcode 0, wenn alle drei die Version aus VERSION nennen. Exitcode 1, wenn eine
davon abweicht oder wenn eine Fundstelle gar nicht mehr gefunden wird. Der zweite
Fall ist Absicht: eine geloeschte oder umformulierte Versionszeile darf nicht
stillschweigend durchgehen.

Mit --expect X muss zusaetzlich VERSION selbst X sein. Ein Release-Workflow
uebergibt dort den Tagnamen ohne v, damit ein Tag, der nicht zum Repo passt,
kein Release erzeugt.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = ROOT / "VERSION"
VERSION = r"(\d+\.\d+\.\d+)"

CHECKS = [
    (
        ".claude-plugin/plugin.json",
        "Plugin-Manifest",
        re.compile(r'"version":\s*"' + VERSION + r'"'),
    ),
    (
        ".claude-plugin/marketplace.json",
        "Marketplace-Eintrag",
        re.compile(r'"version":\s*"' + VERSION + r'"'),
    ),
    (
        "CHANGELOG.md",
        "oberster Eintrag",
        re.compile(r"^## " + VERSION + r" ", re.M),
    ),
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Prueft die Versionsangaben gegen VERSION.")
    parser.add_argument("--expect", help="Erwartete Version, etwa aus einem Tagnamen ohne v.")
    args = parser.parse_args()

    if not VERSION_FILE.exists():
        print("FEHLER: VERSION fehlt.", file=sys.stderr)
        return 1

    quelle = VERSION_FILE.read_text(encoding="utf-8").strip()
    if not re.fullmatch(VERSION, quelle):
        print(f"FEHLER: VERSION enthaelt {quelle!r}, erwartet wird eine Nummer wie 1.2.3.", file=sys.stderr)
        return 1

    if args.expect and args.expect != quelle:
        print(f"FEHLER: VERSION sagt {quelle}, erwartet wurde {args.expect}.", file=sys.stderr)
        return 1

    print(f"  v{quelle:<9} VERSION (Quelle)")
    fehlend, abweichend = [], []
    for rel_pfad, was, muster in CHECKS:
        pfad = ROOT / rel_pfad
        if not pfad.exists():
            fehlend.append(f"{rel_pfad} ({was}): Datei fehlt")
            continue
        treffer = muster.search(pfad.read_text(encoding="utf-8"))
        if not treffer:
            fehlend.append(f"{rel_pfad} ({was}): Versionsangabe nicht gefunden")
            continue
        gefunden = treffer.group(1)
        if gefunden != quelle:
            abweichend.append(f"{rel_pfad} ({was}): v{gefunden}")
        print(f"  v{gefunden:<9} {rel_pfad} ({was})")

    if fehlend or abweichend:
        print("\nFEHLER:", file=sys.stderr)
        for eintrag in fehlend + abweichend:
            print(f"  - {eintrag}", file=sys.stderr)
        return 1

    print(f"\nOK: VERSION und alle {len(CHECKS)} Fundstellen nennen v{quelle}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
