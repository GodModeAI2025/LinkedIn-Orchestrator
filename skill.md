---
name: code-kurs-generator
description: Verwandelt beliebige Codebases in interaktive, visuell ansprechende Single-Page-HTML-Kurse im Energiekonzern-Design (Tiefenblau/Impuls-Orange). IMMER verwenden bei Anfragen wie "mach einen Kurs aus diesem Code", "erkläre diese Codebase interaktiv", "erstelle ein Tutorial aus diesem Projekt", "turn this into a course", "teach me how this code works", "interactive tutorial from code", "Codebase-Walkthrough", "codebase erklären", "Code verstehen lernen", "interaktiver Kurs aus Repository", "turn this repo into a learning experience", "Vibe Coder Tutorial". Auch verwenden wenn Benutzer GitHub-Links teilen und verstehen wollen wie der Code funktioniert, oder wenn sie sagen "ich verstehe meinen eigenen Code nicht" oder "erkläre mir was unter der Haube passiert". Erzeugt eine einzelne HTML-Datei mit Scroll-Navigation, animierten Visualisierungen, eingebetteten Quizzes und Code-mit-Klartext-Übersetzungen.
---

# Code-Kurs-Generator

Verwandelt beliebige Codebases in interaktive Single-Page-HTML-Kurse. Output ist eine einzelne, selbstständige HTML-Datei (keine Abhängigkeiten außer Google Fonts), die über Scroll-Module, animierte Visualisierungen, Quizzes und Klartext-Übersetzungen von Code lehrt, wie der Code funktioniert.

**Design-Identität:** Professionelles Energiekonzern-Design — Tiefenblau für Autorität und Vertrauen, Impuls-Orange für Energie und Aufmerksamkeit, Warmgrau für Wärme. Kein Logo, kein Firmenname — nur der Farbraum und die Ästhetik.

---

## ORCHESTRATOR — Phasensteuerung

```
┌─────────────────────────────────────────────────────────────┐
│  Phase 0: BOOTSTRAP — Quelle identifizieren & einlesen     │
│  ↓                                                          │
│  🛑 WEICHEN KLÄREN — Perspektive + Integration fragen       │
│  ↓  (Pflicht! Nicht überspringen!)                          │
│  Phase 1: ANALYSE — Codebase vollständig verstehen          │
│  ↓                                                          │
│  Phase 2: CURRICULUM — Modulstruktur entwerfen (intern)     │
│  ↓                                                          │
│  Phase 3: FOUNDATION — HTML-Skelett + CSS + JS-Framework    │
│  ↓                                                          │
│  Phase 4: BUILD — Module einzeln befüllen (1 nach 1)        │
│  ↓                                                          │
│  Phase 5: POLISH — Responsiveness, Übergänge, Konsistenz    │
│  ↓                                                          │
│  OUTPUT → Einzelne HTML-Datei, im Browser öffnen            │
└─────────────────────────────────────────────────────────────┘
```

### Orchestrator-Regeln

0. **🛑 BEIDE WEICHEN KLÄREN vor Phase 1** — Perspektive (👤/🔧) UND Integrationsmodus (📄/🌐) müssen beantwortet sein bevor die Analyse startet. Wenn auch nur EINE unklar ist → gebündelte Rückfrage stellen. NIEMALS stillschweigend annehmen. Siehe "Weichenstellungen VOR Phase 1".
1. **Kein Curriculum-Review durch den User** — Direkt bauen.
2. **Ein Modul pro Durchgang** — Niemals alle Module in einem Schritt. Build → Verify → Next.
3. **Qualitätsgates pro Modul:**
   - Mindestens 1 interaktives Element
   - Maximal 2–3 Sätze pro Textblock
   - Mindestens 50% visuelle Elemente pro Screen
   - Alle Fachbegriffe mit Tooltip versehen
   - 🔧 Bearbeiter: Mindestens 1 Code↔Klartext-Übersetzungsblock pro Modul
   - 👤 Anwender: Mindestens 1 Workflow-Flow oder UI-Walkthrough pro Modul
4. **Fehler-Checkliste vor Abschluss:**
   - [ ] **Perspektive durchgängig** — 👤 oder 🔧, kein Mischmasch ohne bewusste Entscheidung
   - [ ] **Integrationsmodus korrekt** — Standalone: kein Footer, keine Header-Links. Eingebettet: alle angegebenen Links vorhanden, target="_blank", Footer mit korrekten URLs
   - [ ] Tooltip-Clipping geprüft (position: fixed, body-append)
   - [ ] Genug Tooltips (jeder Fachbegriff)
   - [ ] Keine Textwände (max 3 Sätze am Stück)
   - [ ] Keine recycelten Metaphern
   - [ ] Code unverändert aus der echten Codebase
   - [ ] Quiz testet Anwendung, nicht Auswendiglernen
   - [ ] scroll-snap-type: y proximity (NICHT mandatory)
   - [ ] Jedes Modul hat interaktive Elemente
   - [ ] **Farbraum korrekt** — Tiefenblau/Impuls-Orange/Warmgrau durchgängig

---

## Phase 0: BOOTSTRAP

### Begrüßung (wenn keine Codebase angegeben)

> **Ich kann jede Codebase in einen interaktiven Kurs verwandeln — kein technisches Vorwissen nötig.**
>
> Zeig mir einfach ein Projekt:
> * **Lokaler Ordner** — z.B. "mach einen Kurs aus ./mein-projekt"
> * **GitHub-Link** — z.B. "erstelle einen Kurs aus https://github.com/user/repo"
> * **Das aktuelle Projekt** — sag einfach "mach daraus einen Kurs"

### Quell-Erkennung

- **GitHub-Link** → `git clone <url> /tmp/<repo-name>` ausführen
- **Lokaler Ordner** → Pfad direkt verwenden
- **"Dieses Projekt"** → Aktuelles Working Directory verwenden

### ⚡ Weichenstellungen VOR Phase 1 — IMMER FRAGEN

**STOPP-REGEL:** Bevor Phase 1 (Analyse) beginnt, MÜSSEN zwei Entscheidungen gefallen sein: Perspektive und Integrationsmodus. Wenn BEIDE aus dem User-Input eindeutig hervorgehen → direkt starten. Wenn EINE ODER BEIDE unklar sind → den User fragen. **NIEMALS stillschweigend annehmen und losbhauen.**

**Die zwei Weichen:**

| Weiche | Optionen | Default wenn unklar |
|---|---|---|
| **Perspektive** | 👤 Anwender · 🔧 Bearbeiter | ❌ KEIN Default — MUSS geklärt werden |
| **Integrationsmodus** | 📄 Standalone · 🌐 Eingebettet | ❌ KEIN Default — MUSS geklärt werden |

---

#### Weiche 1: Perspektive

| | 👤 **ANWENDER** | 🔧 **BEARBEITER** |
|---|---|---|
| **Wer** | Nutzer, Kunden, Fachabteilung, Stakeholder | Entwickler, Autoren, DevOps, QA, neue Teammitglieder |
| **Kernfrage** | "Was kann ich damit tun?" | "Wie ist das gebaut?" |
| **Synonyme** | User, Endanwender, Kunde, Betrachter | Developer, Contributor, Maintainer, Editor |

**Erkennung — Cascading Priority:**

1. **Expliziter User-Input** (höchste Priorität) — "für Entwickler", "für unsere Nutzer", "für das Team", "für Kunden"
2. **Kontext-Signale** im Prompt:
   - Anwender-Signale: "Benutzerhandbuch", "Onboarding", "wie benutze ich", "Tutorial für Kunden", "User Guide"
   - Bearbeiter-Signale: "Codebase verstehen", "Architektur", "für neue Devs", "Onboarding ins Team", "wie funktioniert der Code"
3. **Art des Inputs**:
   - IPA/APK-Datei oder laufende App → **tendenziell Anwender** (man sieht die App von außen)
   - Source-Code-Repo → **tendenziell Bearbeiter** (man sieht den Code von innen)
4. **Im Zweifel:** → Frage stellen (siehe gebündelte Rückfrage unten)

**Mischform möglich:** Wenn der User sagt "beides" oder "hauptsächlich Bearbeiter, aber auch ein Kapitel für Anwender" → Bearbeiter-Perspektive als Basis, mit einem einleitenden Anwender-Modul (Modul 1) das die App aus Nutzersicht zeigt bevor es unter die Haube geht.

---

#### Weiche 2: Integrationsmodus

| | 📄 **STANDALONE** | 🌐 **EINGEBETTET** |
|---|---|---|
| **Was** | Einzelne HTML-Datei, komplett eigenständig | Teil einer Website, Dokumentation oder Plattform |
| **Typisch** | Per E-Mail/Slack geteilt, lokal geöffnet | Auf GitHub Pages, Firmen-Wiki, Doku-Site gehostet |
| **Header** | Nur Kurstitel + Nav-Dots + Fortschritt | + Externe Links (GitHub, Doku, Home) + Buttons |
| **Footer** | Keiner nötig | Impressum, Datenschutz, Copyright, Kontakt |

**Erkennung — Cascading Priority:**

1. **Expliziter User-Input** — "soll auf unsere Website", "für GitHub Pages", "mit Impressum", "mit Link zum Repo", "standalone", "offline"
2. **Kontext-Signale:**
   - Eingebettet-Signale: "veröffentlichen", "online stellen", "hosten", "Website", "Impressum", "Datenschutz", "GitHub Pages", "GitHub-Link", "Button"
   - Standalone-Signale: "per E-Mail teilen", "offline", "runterladen", "intern", "Workshop"
3. **Im Zweifel:** → Frage stellen (siehe gebündelte Rückfrage unten)

---

### 🛑 Die gebündelte Rückfrage (PFLICHT wenn etwas unklar ist)

**Wenn Perspektive ODER Integrationsmodus nicht eindeutig aus dem User-Input hervorgehen → EINE gebündelte Nachricht mit ALLEN offenen Fragen stellen. NICHT stillschweigend annehmen. NICHT losbhauen und hoffen dass es passt.**

**Entscheidungsmatrix — Was muss gefragt werden?**

| Perspektive klar? | Integration klar? | Aktion |
|---|---|---|
| ✅ Ja | ✅ Ja | → Direkt starten, keine Frage nötig |
| ✅ Ja | ❌ Nein | → Nur Integrationsmodus fragen |
| ❌ Nein | ✅ Ja | → Nur Perspektive fragen |
| ❌ Nein | ❌ Nein | → Beides fragen in einer Nachricht |

**Beispiel: Beides unklar** (User sagt nur "mach einen Kurs aus diesem Repo"):

> **Bevor ich loslege, zwei kurze Fragen:**
>
> **1. Für wen ist der Kurs?**
> * 👤 **Anwender** — Leute die die App/das Produkt BENUTZEN wollen
> * 🔧 **Bearbeiter** — Leute die den Code VERSTEHEN und ÄNDERN wollen
> * 🔀 **Beides** — Bearbeiter-Fokus mit Anwender-Einstiegskapitel
>
> **2. Wie wird der Kurs genutzt?**
> * 📄 **Standalone** — Einzelne Datei, per E-Mail/Slack teilen, offline nutzbar
> * 🌐 **Eingebettet** — Teil einer Website (dann brauche ich: Header-Links? Impressum-URL? Copyright?)

**Beispiel: Nur Integration unklar** (User sagt "mach einen Kurs für Entwickler"):

> **Kurze Frage bevor ich starte: Wie wird der Kurs genutzt?**
> * 📄 **Standalone** — Einzelne Datei zum Teilen/Offline-Nutzen
> * 🌐 **Eingebettet** — Teil einer Website (dann brauche ich: GitHub-Link? Impressum-URL?)

**Beispiel: Nur Perspektive unklar** (User sagt "mach einen Kurs mit GitHub-Button und Impressum"):

> **Kurze Frage: Für wen ist der Kurs?**
> * 👤 **Anwender** — Nutzer die die App kennenlernen wollen
> * 🔧 **Bearbeiter** — Entwickler die den Code verstehen wollen

**Wenn Eingebettet gewählt → Folge-Frage nur zu den fehlenden Details:**

> **Verstanden — eingebettet. Was brauche ich?**
> * 🔗 **GitHub-URL** für den Header-Button?
> * 📋 **Impressum-URL** für den Footer?
> * 🔒 **Datenschutz-URL**? (oder nicht nötig?)
> * ©️ **Copyright-Text**? (z.B. "© 2026 Firma GmbH")
>
> Nur angeben was du brauchst — was du weglässt, wird weggelassen.

**KRITISCH — Häufiger Fehler den dieser Skill gemacht hat:**
Claude neigt dazu, die Integrations-Frage zu überspringen und stillschweigend Standalone anzunehmen. Das passiert besonders wenn der User schon eine klare Perspektive angibt ("für Entwickler") — Claude fühlt sich dann "genug informiert" und startet. **DAS IST EIN BUG.** Perspektive beantwortet ≠ Integration beantwortet. Beide Weichen sind unabhängig voneinander. IMMER BEIDE prüfen.

### Integrationsmodus → Auswirkung auf Phase 3 und 5

**Phase 3 (Foundation):**

Standalone-Modus (Default):
```html
<nav class="nav">
  <div class="progress-bar"></div>
  <div class="nav-inner">
    <span class="nav-title">Kurstitel</span>
    <div class="nav-dots"><!-- Module --></div>
  </div>
</nav>
<!-- Kein Footer -->
```

Eingebettet-Modus:
```html
<nav class="nav">
  <div class="progress-bar"></div>
  <div class="nav-inner">
    <span class="nav-title">Kurstitel</span>
    <div class="nav-dots"><!-- Module --></div>
    <div class="nav-links">
      <!-- Nur was angegeben wurde: -->
      <a href="[URL]" class="nav-link" target="_blank" rel="noopener">
        <span class="nav-link-icon"><!-- Icon --></span> Button-Text
      </a>
    </div>
  </div>
</nav>

<!-- Am Ende, NACH dem letzten Modul: -->
<footer class="site-footer">
  <div class="footer-inner">
    <span class="footer-copy">© 2026 [Copyright-Text]</span>
    <div class="footer-links">
      <a href="[Impressum-URL]">Impressum</a>
      <a href="[Datenschutz-URL]">Datenschutz</a>
    </div>
  </div>
</footer>
```

**CSS für Header-Links (Eingebettet-Modus):**
```css
.nav-links { display: flex; gap: var(--space-3); align-items: center; }
.nav-link {
  display: flex; align-items: center; gap: var(--space-2);
  padding: var(--space-1) var(--space-4);
  border-radius: var(--radius-full);
  border: 1px solid rgba(255,255,255,.25);
  color: #FFFFFF;
  font-size: var(--text-xs);
  font-family: var(--font-body);
  font-weight: 500;
  text-decoration: none;
  transition: all var(--duration-fast);
}
.nav-link:hover {
  border-color: var(--color-impulse-orange);
  background: rgba(254,143,17,.15);
  color: var(--color-impulse-orange);
}
.nav-link-icon { font-size: .9rem; }
```

**CSS für Footer (Eingebettet-Modus):**
```css
.site-footer {
  background: var(--color-deep-blue);
  color: rgba(255,255,255,.6);
  padding: var(--space-6) var(--space-6);
  font-size: var(--text-xs);
}
.footer-inner {
  max-width: var(--content-width);
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: var(--space-4);
}
.footer-links { display: flex; gap: var(--space-6); }
.footer-links a {
  color: rgba(255,255,255,.5);
  text-decoration: none;
  transition: color var(--duration-fast);
}
.footer-links a:hover { color: var(--color-impulse-orange); }
```

**Header-Link-Icons (vordefiniert):**

| Link-Typ | Icon | Beispiel |
|---|---|---|
| GitHub | `<svg viewBox="0 0 16 16" width="14" height="14" fill="currentColor">...</svg>` | GitHub-Octocat als inline SVG |
| Home/Website | 🏠 oder `←` | Pfeil zurück + Text |
| Dokumentation | 📚 | Buch-Emoji |
| Custom | — | Nur Text, kein Icon |

Das GitHub-Icon als inline SVG (kein externer Request):
```html
<svg class="nav-link-icon" viewBox="0 0 16 16" width="14" height="14" fill="currentColor">
  <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
</svg>
```

**Phase 5 (Polish) — zusätzliche Prüfungen für Eingebettet-Modus:**
- [ ] Alle Header-Links öffnen in `target="_blank"` mit `rel="noopener"`
- [ ] Footer-Links sind korrekt und erreichbar
- [ ] Footer-Design passt zum Tiefenblau-Farbschema
- [ ] Responsive: Header-Links auf Mobile nie display:none — nur Text ausblenden, Icon-Button bleibt (Artifact-Viewer sind oft <480px breit!)
- [ ] Copyright-Jahr ist aktuell

---

### Perspektive → Auswirkung auf alle Phasen

Die gewählte Perspektive durchdringt JEDEN Aspekt des Kurses:

**Phase 1 (Analyse) — Was wird extrahiert?**

| 👤 Anwender | 🔧 Bearbeiter |
|---|---|
| Features, Workflows, UI-Screens, Benutzerrollen | Architektur, Code-Struktur, APIs, Patterns |
| User-Journeys (Login → Dashboard → Aktion) | Datenflüsse (Request → API → DB → State → UI) |
| Berechtigungen aus Nutzersicht ("Was darf ich?") | Berechtigungen aus Code-Sicht (OAuth, RBAC-Logik) |
| Fehlermeldungen die der User sieht | Error Handling, Sentry, Logging-Architektur |

**Phase 2 (Curriculum) — Andere Modulstruktur**

| Pos. | 👤 Anwender-Modul | 🔧 Bearbeiter-Modul |
|---|---|---|
| 1 | Was ist das? + Erster Eindruck | Was die App tut + Erste Aktion tracen |
| 2 | Die Hauptbereiche (Screens/Features) | Die Akteure (Komponenten/Services) |
| 3 | So funktioniert [Kern-Feature] | Wie die Teile kommunizieren |
| 4 | Tipps & Tricks, Einstellungen | APIs, Datenbank, externe Dienste |
| 5 | Häufige Fragen / Probleme lösen | Clevere Patterns & Engineering-Tricks |
| 6 | — | Wenn etwas kaputt geht (Debugging) |
| 7 | — | Das große Ganze (Architektur-Überblick) |

**Phase 4 (Build) — Andere Element-Typen**

| Element | 👤 Anwender | 🔧 Bearbeiter |
|---|---|---|
| Code↔Klartext | Selten — nur Konfig/Einstellungen | Kern-Element, in jedem Modul |
| Workflow-Flows | Hauptelement (Schritt 1→2→3→4) | Sekundär (für User-Journeys in Modul 1) |
| Chat-Animationen | Zwischen User und App ("Du klickst → App zeigt") | Zwischen Komponenten ("API sagt zu DB...") |
| Architektur-Diagramme | Vereinfacht (3–4 Boxen max) | Detailliert (alle Schichten) |
| Quiz-Typ | "Was passiert wenn du X machst?" | "Wo liegt der Bug?" / "Welcher Endpunkt?" |
| Tooltips | UI-Begriffe (Dashboard, Filter, Favorit) | Tech-Begriffe (DTO, Riverpod, OAuth, Drift) |
| Metaphern | Alltagsnah (Fahrkartenautomat, Fernbedienung) | Tech-nah (Postamt, Matrjoschka, Notstromaggregat) |
| Screenshots/Mockups | Ja — UI zeigen wenn möglich | Selten — Code zeigt die Wahrheit |
| Dateibaum | Nein | Ja — Projektstruktur visualisieren |
| Badge-Listen | Feature-Listen, Einstellungen | API-Endpunkte, DTOs, Severity-Stufen |

**Phase 5 (Polish) — Andere Tonalität**

| 👤 Anwender | 🔧 Bearbeiter |
|---|---|
| Freundlich, einladend, ermutigend | Sachlich, präzise, respektvoll |
| "Du kannst..." / "Probier mal..." | "Das System..." / "Der Datenfluss..." |
| Fehler = "Kein Problem, versuch..." | Fehler = "Hier liegt die Ursache..." |
| Kein Fachjargon ohne Tooltip | Fachjargon OK, aber Konzept-Tooltips für Einsteiger |

---

## Phase 1: ANALYSE

Codebase tiefgehend verstehen. Alle Schlüsseldateien lesen, Datenflüsse nachvollziehen, "Hauptfiguren" identifizieren.

**Zu extrahieren:** Hauptakteure, primäre User-Journey, APIs/Datenflüsse, Engineering-Patterns, Tech-Stack.

**Selbst herausfinden was die App tut** — README + Einstiegspunkte lesen. Modul 1 startet immer mit konkreter User-Aktion.

---

## Phase 2: CURRICULUM

5–8 Module. Der Bogen beginnt bei dem was der Lernende kennt → was er nicht kennt.

**Die Modulstruktur hängt von der Perspektive ab (siehe Phase 0).**

### 🔧 Bearbeiter-Curriculum (Standard bei Code-Repos)

| Modul | Zweck | Warum wichtig |
|-------|-------|---------------|
| 1 | App + Kernaktion tracen | Konkreter Einstieg |
| 2 | Akteure kennenlernen | KI/Kollegen präziser anweisen |
| 3 | Kommunikation der Teile | Datenfluss debuggen |
| 4 | Außenwelt (APIs, DB) | Kosten/Fehler einschätzen |
| 5 | Clevere Tricks | Patterns verstehen/anfordern |
| 6 | Wenn etwas kaputt geht | Debug-Intuition |
| 7 | Das große Ganze | Bessere Entscheidungen |

### 👤 Anwender-Curriculum (Standard bei App-Binaries/Demos)

| Modul | Zweck | Warum wichtig |
|-------|-------|---------------|
| 1 | Was ist das? Erster Eindruck | Motivation und Orientierung |
| 2 | Die Hauptbereiche | Wo finde ich was? |
| 3 | Kern-Feature im Detail | Die wichtigste Funktion Schritt für Schritt |
| 4 | Tipps, Tricks, Einstellungen | Produktiver werden |
| 5 | Häufige Fragen & Problembehebung | Selbsthilfe statt Support |

### Mischform

Wenn der User "beides" sagt → Bearbeiter-Basis mit Anwender-Modul 1 (App aus Nutzersicht) als Einstieg.

**Jedes Modul (beide Perspektiven):** 3–6 Screens, ≥1 interaktives Element, 1–2 Aha-Callouts, einzigartige Metapher. **Bearbeiter** zusätzlich: ≥1 Code↔Klartext pro Modul. **Anwender** zusätzlich: ≥1 Workflow-Flow pro Modul.

---

## Phase 3: FOUNDATION — Design-System

### Zielgruppe (perspektivabhängig)

**👤 Anwender:** Menschen die die App/das Produkt BENUTZEN. Null technischen Hintergrund annehmen. Ton wie ein freundlicher Kollege der eine neue App zeigt. Keine Code-Snippets außer Konfigurationshinweisen.

**🔧 Bearbeiter:** "Vibe Coder" oder neue Teammitglieder die den Code VERSTEHEN wollen. Geringe bis mittlere technische Tiefe annehmen. Ton wie ein kluger Freund der den Code erklärt. Code↔Klartext ist das Kern-Lehrelement.

### Google Fonts (in `<head>`)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700;12..96,800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400;1,9..40,500&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

### ⚡ FARBRAUM — Energiekonzern-Palette (KRITISCH)

Das gesamte Design baut auf diesem Farbraum auf. **Kein Logo, kein Firmenname** — nur die Farbwerte und ihre Anwendungsregeln.

```css
:root {
  /* ═══ PRIMÄRE BRAND-FARBEN ═══ */
  --color-deep-blue:      #000099;   /* Tiefenblau — Autorität, Vertrauen, Kompetenz */
  --color-impulse-orange:  #FE8F11;   /* Impuls-Orange — Energie, Aufmerksamkeit, Aktion */
  --color-warm-gray:       #E4DAD4;   /* Warmgrau — Wärme, Zugänglichkeit, Ruhe */

  /* ═══ HINTERGRÜNDE ═══ */
  --color-bg:              #FFFFFF;   /* Weiß — Standard-Inhaltsflächen */
  --color-bg-warm:         #F3EFEB;   /* Aufgehelltes Warmgrau — alternierende Module */
  --color-bg-code:         #000066;   /* Tiefes Dunkelblau — Code-Blöcke (dunkler als Tiefenblau) */

  /* ═══ TEXT ═══ */
  --color-text:            #1A1A2E;   /* Fast-Schwarz mit Blau-Unterton */
  --color-text-secondary:  #5C5A6B;   /* Gedämpft mit Blau-Unterton */
  --color-text-muted:      #9995A0;   /* Dezent für Labels, Timestamps */

  /* ═══ BORDERS & SURFACES ═══ */
  --color-border:          #E4DAD4;   /* Warmgrau als Hauptborder */
  --color-border-light:    #EDE8E4;   /* Aufgehelltes Warmgrau */
  --color-surface:         #FFFFFF;   /* Card-Oberflächen */
  --color-surface-warm:    #F8F5F2;   /* Warme Card-Oberfläche */

  /* ═══ AKZENT = Impuls-Orange ═══ */
  --color-accent:          #FE8F11;   /* Impuls-Orange — DER Hauptakzent */
  --color-accent-hover:    #E57D00;   /* Dunkleres Orange für Hover */
  --color-accent-light:    #FFF3E5;   /* Ganz helles Orange für Hintergründe */
  --color-accent-muted:    #FEB85C;   /* Gedämpftes Orange */

  /* ═══ SEMANTISCHE FARBEN ═══ */
  --color-success:         #84C041;   /* Grün — Positiv, Bestanden, Wachstum */
  --color-success-light:   #EFF7E5;
  --color-error:           #CC0000;   /* Rot — Fehler, Negativ, Blocker */
  --color-error-light:     #FFE5E5;
  --color-info:            #1195EB;   /* Hellblau — Information, Hinweis */
  --color-info-light:      #E5F2FC;
  --color-warning:         #FDC83A;   /* Gelb — Warnung, Aufmerksamkeit */
  --color-warning-light:   #FFF9E5;

  /* ═══ AKTEUR-FARBEN (für Diagramme, Chat-Bubbles, Highlights) ═══
     Jede Hauptkomponente der Codebase bekommt eine eigene Farbe.
     Reihenfolge: Tiefenblau → Orange → Grün → Hellblau → Türkis → Gelb */
  --color-actor-1:         #000099;   /* Tiefenblau */
  --color-actor-2:         #FE8F11;   /* Impuls-Orange */
  --color-actor-3:         #84C041;   /* Grün */
  --color-actor-4:         #1195EB;   /* Hellblau */
  --color-actor-5:         #5BE3D6;   /* Türkis */
  --color-actor-6:         #FDC83A;   /* Gelb */

  /* ═══ DIAGRAMM-PALETTE (geordnet für maximale Unterscheidbarkeit) ═══ */
  --color-chart-1:         #000099;
  --color-chart-2:         #FE8F11;
  --color-chart-3:         #84C041;
  --color-chart-4:         #1195EB;
  --color-chart-5:         #FDC83A;
  --color-chart-6:         #E2C39A;   /* Beige/Tan als 6. Farbe */

  /* ═══ FONTS ═══ */
  --font-display:  'Bricolage Grotesque', Georgia, serif;
  --font-body:     'DM Sans', -apple-system, sans-serif;
  --font-mono:     'JetBrains Mono', 'Fira Code', 'Consolas', monospace;

  /* ═══ TYPOGRAFIE ═══ */
  --text-xs:.75rem; --text-sm:.875rem; --text-base:1rem; --text-lg:1.125rem;
  --text-xl:1.25rem; --text-2xl:1.5rem; --text-3xl:1.875rem; --text-4xl:2.25rem;
  --text-5xl:3rem; --text-6xl:3.75rem;
  --leading-tight:1.15; --leading-snug:1.3; --leading-normal:1.6; --leading-loose:1.8;

  /* ═══ ABSTÄNDE ═══ */
  --space-1:.25rem; --space-2:.5rem; --space-3:.75rem; --space-4:1rem;
  --space-5:1.25rem; --space-6:1.5rem; --space-8:2rem; --space-10:2.5rem;
  --space-12:3rem; --space-16:4rem; --space-20:5rem; --space-24:6rem;

  /* ═══ LAYOUT ═══ */
  --content-width:820px; --content-width-wide:1000px; --nav-height:50px;
  --radius-sm:8px; --radius-md:12px; --radius-lg:16px; --radius-full:9999px;

  /* ═══ SCHATTEN — warm getönt mit Blau-Anteil ═══ */
  --shadow-sm:  0 1px 2px rgba(0,0,60,.05);
  --shadow-md:  0 4px 12px rgba(0,0,60,.08);
  --shadow-lg:  0 8px 24px rgba(0,0,60,.10);
  --shadow-xl:  0 16px 48px rgba(0,0,60,.12);

  /* ═══ ANIMATIONEN ═══ */
  --ease-out:cubic-bezier(.16,1,.3,1); --ease-in-out:cubic-bezier(.65,0,.35,1);
  --duration-fast:150ms; --duration-normal:300ms; --duration-slow:500ms; --stagger-delay:120ms;
}
```

### Syntax-Highlighting (auf Tiefenblau-Code-Hintergrund #000066)

```css
.code-keyword  { color: #FEB85C; }  /* gedämpftes Orange — if, else, return, function */
.code-string   { color: #84C041; }  /* Grün — "strings" */
.code-function { color: #5BE3D6; }  /* Türkis — Funktionsnamen */
.code-comment  { color: #7B7BA0; }  /* gedämpftes Blaugrau — // Kommentare */
.code-number   { color: #FDC83A; }  /* Gelb — Zahlen */
.code-property { color: #E2C39A; }  /* Beige — Objekt-Keys */
.code-operator { color: #1195EB; }  /* Hellblau — =, =>, + */
.code-tag      { color: #FE8F11; }  /* Impuls-Orange — HTML-Tags */
.code-attr     { color: #E2C39A; }  /* Beige — HTML-Attribute */
.code-value    { color: #84C041; }  /* Grün — Attribut-Werte */
```

### ⚡ Design-Regeln (NICHT VERHANDELBAR)

| Regel | Detail |
|-------|--------|
| **Primärfarbe** | Tiefenblau (#000099) für: Nav-Bar-Akzente, Modulnummern (15% Opacity), Hero-Sektionen, dunkle Hintergründe. Strahlt Autorität und Vertrauen aus. |
| **Akzentfarbe** | Impuls-Orange (#FE8F11) für: Buttons, Links, Fortschrittsbalken, aktive Zustände, Callout-Borders, Step-Nummern. IMMER der Eye-Catcher. |
| **Warmgrau** | #E4DAD4 für: Borders, Hintergrund-Alternation, Trennlinien, Bullet-Farben. Gibt Wärme und Zugänglichkeit. |
| **Hintergründe** | Gerade Module: Weiß (#FFFFFF). Ungerade Module: Aufgehelltes Warmgrau (#F3EFEB). Hero/Titel-Sektionen: Tiefenblau (#000099) mit weißem Text. |
| **Code-Blöcke** | Auf tiefem Dunkelblau (#000066). NICHT Charcoal/Schwarz. Syntax-Farben aus der Sekundärpalette. |
| **Schatten** | Warm getönt mit Blau-Anteil rgba(0,0,60,x). Nie reines Schwarz. |
| **Typografie** | Bricolage Grotesque Headings (NIEMALS Inter/Roboto/Arial). DM Sans Body. JetBrains Mono Code. |
| **Kein Logo** | Keine Logos, keine Firmennamen. Nur der Farbraum transportiert die Identität. |
| **Kein Purple** | KEINE Purple-Gradienten. Die Palette ist Blau-Orange-dominiert. |

### Spezielle Modul-Varianten

```css
/* HERO / TITEL-SEKTION — Tiefenblau mit weißem Text */
.module-hero {
  background: var(--color-deep-blue);
  color: #FFFFFF;
}
.module-hero .module-number { color: rgba(255,255,255,.15); }
.module-hero .module-title { color: #FFFFFF; }
.module-hero .module-subtitle { color: rgba(255,255,255,.7); }

/* STANDARD — Weiß */
.module-light { background: var(--color-bg); }

/* ALTERNIEREND — Warmgrau-Hauch */
.module-warm { background: var(--color-bg-warm); }

/* EMPFEHLUNG: Hero-Modul (0) = Tiefenblau. Danach alternierend Weiß/Warmgrau. */
```

### Navigation & Fortschrittsbalken

```css
.nav {
  background: rgba(0,0,153,.95);  /* Tiefenblau, leicht transparent */
  backdrop-filter: blur(12px);
  border-bottom: 2px solid var(--color-impulse-orange);  /* Orange-Akzentlinie */
}
.nav-title { color: #FFFFFF; }
.progress-bar { background: var(--color-impulse-orange); }  /* Orange Fortschritt */
.nav-dot { border-color: rgba(255,255,255,.4); }
.nav-dot.active { border-color: var(--color-impulse-orange); background: var(--color-impulse-orange); }
.nav-dot.visited { background: var(--color-impulse-orange); border-color: var(--color-impulse-orange); }
```

### Scroll & Layout

```css
html { scroll-snap-type: y proximity; scroll-behavior: smooth; }
.module { min-height: 100dvh; scroll-snap-align: start;
  padding: var(--space-16) var(--space-6); padding-top: calc(var(--nav-height) + var(--space-12)); }
.module-content { max-width: var(--content-width); margin: 0 auto; }

/* Atmosphärischer Hintergrund — subtiler Blau-Schimmer */
body {
  background: var(--color-bg);
  background-image: radial-gradient(ellipse at 20% 50%, rgba(0,0,153,.02) 0%, transparent 50%);
}

pre, code { white-space: pre-wrap; word-break: break-word; overflow-x: hidden; }
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--color-warm-gray); border-radius: var(--radius-full); }
```

### Responsive Breakpoints

```css
@media (max-width: 768px) {
  :root { --text-4xl: 1.875rem; --text-5xl: 2.25rem; --text-6xl: 3rem; }
  .translation-block { grid-template-columns: 1fr; }
  /* Eingebettet-Modus: Header-Links kompakter */
  .nav-links { gap: var(--space-2); }
  .nav-link span:not(.nav-link-icon) { display: none; }  /* Nur Icons auf Tablet */
}
@media (max-width: 480px) {
  :root { --text-4xl: 1.5rem; --text-5xl: 1.875rem; --text-6xl: 2.25rem; }
  .module { padding: var(--space-8) var(--space-4); }
  .flow-steps { flex-direction: column; }
  /* Eingebettet-Modus: Header-Links: nur Text ausblenden, Icon bleibt sichtbar */
  .nav-link-text { display: none; }
  .nav-links { gap: var(--space-1); }
  .nav-link { padding: var(--space-1) var(--space-2); }
  /* Footer stacken */
  .footer-inner { flex-direction: column; text-align: center; }
}
```

### Animationen

```css
.animate-in { opacity: 0; transform: translateY(20px);
  transition: opacity var(--duration-slow) var(--ease-out), transform var(--duration-slow) var(--ease-out); }
.animate-in.visible { opacity: 1; transform: translateY(0); }
.stagger-children > .animate-in { transition-delay: calc(var(--stagger-index, 0) * var(--stagger-delay)); }
```

### JS-Basis (IIFE)

```javascript
(function() {
  // Animate-in Observer
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -10% 0px', threshold: 0.1 });
  document.querySelectorAll('.animate-in').forEach(el => obs.observe(el));

  // Stagger-Delay
  document.querySelectorAll('.stagger-children').forEach(p =>
    Array.from(p.children).forEach((c, i) => c.style.setProperty('--stagger-index', i)));

  // Progress Bar + Nav Dots — SCROLL-BASIERT (nicht IntersectionObserver!)
  const pb = document.querySelector('.progress-bar');
  const dots = document.querySelectorAll('.nav-dot');
  const mods = document.querySelectorAll('.module');
  const navH = 60; // Höhe der fixierten Nav-Bar in px

  // Aktiven Modul-Index berechnen: Welches Modul ist gerade am nächsten am oberen Rand?
  function activeIndex() {
    let idx = 0;
    mods.forEach((m, i) => { if (m.getBoundingClientRect().top <= navH + 20) idx = i; });
    return idx;
  }

  // Dots aktualisieren bei jedem Scroll-Event
  function updateDots() {
    const ai = activeIndex();
    dots.forEach((d, i) => {
      d.classList.toggle('active', i === ai);
      if (i <= ai) d.classList.add('visited');
    });
  }

  window.addEventListener('scroll', () => requestAnimationFrame(() => {
    // Progress Bar
    if (pb) pb.style.width = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight) * 100) + '%';
    // Dot-State
    updateDots();
  }), { passive: true });

  // Initial-State setzen
  updateDots();

  // Dot-Klick: scrollTo mit Offset für fixierte Nav-Bar
  dots.forEach(d => d.addEventListener('click', () => {
    const target = document.getElementById(d.dataset.target);
    if (!target) return;
    const top = target.getBoundingClientRect().top + window.scrollY - navH;
    window.scrollTo({ top: Math.max(0, top), behavior: 'smooth' });
  }));

  // Keyboard-Navigation
  function nextModule() { const i = Math.min(activeIndex() + 1, mods.length - 1); scrollToModule(i); }
  function prevModule() { const i = Math.max(activeIndex() - 1, 0); scrollToModule(i); }
  function scrollToModule(i) {
    const top = mods[i].getBoundingClientRect().top + window.scrollY - navH;
    window.scrollTo({ top: Math.max(0, top), behavior: 'smooth' });
  }
  window.nextModule = nextModule;
  window.prevModule = prevModule;

  document.addEventListener('keydown', e => {
    if (['INPUT','TEXTAREA'].includes(e.target.tagName)) return;
    if (e.key === 'ArrowDown' || e.key === 'ArrowRight') { nextModule(); e.preventDefault(); }
    if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') { prevModule(); e.preventDefault(); }
  });
})();
```

**KRITISCH — Häufige Fehler bei Nav-Dots:**

| Fehler | Problem | Lösung |
|--------|---------|--------|
| IntersectionObserver mit threshold > 0.2 für Dots | Module sind oft 200-300vh hoch, 40% Sichtbarkeit ist unmöglich | Scroll-basiert mit getBoundingClientRect statt IntersectionObserver |
| scrollIntoView für Dot-Klicks | Ignoriert fixierte Nav-Bar, Modul-Top verschwindet hinter der Nav | window.scrollTo mit manuellem Offset (navH = 60px) |
| Kein Initial-State | Dots zeigen beim Laden keinen aktiven Zustand | updateDots() direkt nach Setup aufrufen |
| IntersectionObserver für animate-in UND Dots mischen | Verschiedene Anforderungen, verschiedene Lösungen | animate-in = IntersectionObserver (einmalig). Dots = Scroll-Event (kontinuierlich) |

---

## Phase 4: BUILD — Interaktive Elemente

### Farbzuweisung-Regeln bei jedem Element

| Element | Primärfarbe | Akzent | Varianten |
|---------|-------------|--------|-----------|
| Step-Nummern (Kreise) | — | Impuls-Orange Hintergrund, weiße Zahl | — |
| Callout-Border | — | Impuls-Orange (accent), Hellblau (info), Rot (warning) | — |
| Card-Top-Border | — | Akteur-Farben rotierend (1→6) | — |
| Quiz-Option selected | — | Impuls-Orange Border + heller BG | Grün (correct), Rot (incorrect) |
| Chat-Avatare | Akteur-Farben | — | Tiefenblau, Orange, Grün, Hellblau, Türkis |
| Flow-Actor active | — | Impuls-Orange Glow + Scale | — |
| Nav-Dot active | — | Impuls-Orange | — |
| Fortschrittsbalken | — | Impuls-Orange | — |
| Code-Block BG | Tiefes Dunkelblau #000066 | — | — |
| Translation-Border | — | Impuls-Orange (3px links) | — |
| Badge-Severity F4 | — | — | Rot #CC0000 |
| Badge-Severity F3 | — | — | Gelb #FDC83A |
| Badge-Severity F2 | — | — | Hellblau #1195EB |
| Badge-Severity F0 | — | — | Grün #84C041 |
| Glossar-Tooltip BG | Tiefes Dunkelblau #000066 | — | Heller Text |

### E1: Code ↔ Klartext-Übersetzung

```css
.translation-code {
  background: var(--color-bg-code);   /* #000066 Tiefes Dunkelblau */
  color: #D0D0E8;                     /* Heller Blaugrau-Text */
}
.translation-english {
  background: var(--color-surface-warm);
  border-left: 3px solid var(--color-impulse-orange);  /* Orange-Akzent */
}
```

### E2–E12: Alle anderen Elemente

Identisch zur Basisversion (Quiz, Drag-and-Drop, Chat, Datenfluss, Architektur-Diagramm, Bug-Challenge, Callouts, Pattern-Cards, Flow-Diagramme, Dateibaum, Schritt-Cards) — aber mit den oben definierten Farbzuweisungen.

### E13: Glossar-Tooltips

```css
.term { border-bottom: 1.5px dashed var(--color-accent-muted); cursor: pointer; }
.term:hover { border-bottom-color: var(--color-impulse-orange); color: var(--color-impulse-orange); }

.term-tooltip {
  position: fixed;
  background: var(--color-bg-code);   /* #000066 */
  color: #D0D0E8;
  z-index: 10000;
  /* ... restliche Tooltip-Styles wie Basisversion */
}
.term-tooltip::after { border-top-color: var(--color-bg-code); }
```

---

## Phase 5: POLISH

1. **Farb-Konsistenz:** Durchgehend Tiefenblau/Impuls-Orange/Warmgrau. Kein verwaistes Lila, kein Charcoal.
2. **Hero-Modul:** Tiefenblau-Hintergrund (#000099) mit weißem Text und Impuls-Orange-Akzenten.
3. **Nav-Bar:** Tiefenblau mit Orange-Unterstrich und Orange-Fortschrittsbalken.
4. **Code-Blöcke:** #000066 Hintergrund, Syntax-Farben aus der Sekundärpalette (kein Catppuccin-Lila).
5. **Mobile:** Translation-Blocks stacken, Flow-Diagramme rotieren, Touch funktioniert.
6. **ARIA:** Alle interaktiven Elemente haben aria-labels.
7. **Integrationsmodus (wenn 🌐 Eingebettet):**
   - Header-Links vorhanden und korrekt (target="_blank", rel="noopener")
   - Footer mit allen angegebenen URLs (Impressum, Datenschutz)
   - Copyright-Text und Jahr korrekt
   - Responsive: Header-Links auf Tablet nur Icons, auf Mobile ausgeblendet
   - Footer stackt auf Mobile vertikal
   - GitHub-Icon als inline SVG (kein externer Request)

---

## Inhalts-Regeln (identisch zur Basisversion)

| Regel | Detail |
|-------|--------|
| 50% visuell | Jeder Screen mindestens zur Hälfte Diagramme, Cards, Animationen |
| Max 2–3 Sätze | Kein vierter Satz — stattdessen Visual |
| Code original | 🔧 Exakte Kopien, natürlich kurze Snippets (5–10 Zeilen) |
| Metaphern einzigartig | Nie recyceln. Nie Restaurant/Küche. |
| 1 Konzept/Screen | Mehr Platz → neuer Screen |
| Quiz = Anwendung | 🔧 "Wo liegt der Bug?" · 👤 "Was passiert wenn du X machst?" |

### Perspektive-spezifische Regeln

| | 👤 Anwender | 🔧 Bearbeiter |
|---|---|---|
| **Tonalität** | Freundlich, einladend ("Probier mal...") | Sachlich, präzise ("Das System...") |
| **Code zeigen** | Minimal — nur Konfig/Einstellungen | Kern-Element jedes Moduls |
| **Fehler** | "Kein Problem, versuch..." | "Hier liegt die Ursache..." |
| **Jargon** | Null Jargon ohne Tooltip | Tech-Jargon OK, Konzept-Tooltips für Einsteiger |
| **Workflows** | Hauptelement (Schritt 1→2→3) | Sekundär (in Modul 1) |
| **Architektur** | Vereinfacht (3–4 Boxen) | Detailliert (alle Schichten) |

---

## Modul-Template

**Hero-Varianten nach Perspektive:**

| | 👤 Anwender | 🔧 Bearbeiter |
|---|---|---|
| **Titel** | "[App] kennenlernen" | "[App] verstehen" |
| **Untertitel** | "Alles was du brauchst um [Kernnutzen]" | "Architektur, Datenfluss und Patterns" |
| **Badges** | Feature-basiert ("Schritt für Schritt") | Tech-basiert ("Flutter · Riverpod") |

```html
<!-- HERO (Modul 0) — Tiefenblau -->
<section class="module module-hero" id="module-0">
  <div class="module-content" style="text-align:center">
    <h1 style="color:#FFFFFF">Kurstitel</h1>
    <p style="color:rgba(255,255,255,.7)">Perspektivabhängiger Untertitel</p>
  </div>
</section>

<!-- INHALT (alternierend) -->
<section class="module" id="module-N" style="background:var(--color-bg)">
  <!-- oder: style="background:var(--color-bg-warm)" -->
  <div class="module-content">
    <header class="module-header animate-in">
      <span class="module-number" style="color:var(--color-deep-blue);opacity:.15">0N</span>
      <h1 class="module-title">Modul-Titel</h1>
    </header>
    <div class="module-body">
      <section class="screen animate-in">
        <!-- Inhalt -->
      </section>
    </div>
  </div>
</section>
```

### Typografie-Zuordnung

| Element | Stil |
|---------|------|
| Modulnummern | --text-6xl, font-display, weight 800, Tiefenblau 15% Opacity |
| Modultitel | --text-4xl, font-display, weight 700, Textfarbe |
| Screen-Headings | --text-2xl, font-display, weight 600 |
| Fließtext | --text-base/lg, font-body, --leading-normal |
| Code | --text-sm, font-mono, auf #000066 Hintergrund |
| Labels/Badges | --text-xs, font-mono, uppercase |

---

## Farb-Schnellreferenz

```
PRIMÄR:     #000099  Tiefenblau      — Vertrauen, Autorität, Hintergründe
AKZENT:     #FE8F11  Impuls-Orange   — Energie, CTAs, Fortschritt, Highlights
WARM:       #E4DAD4  Warmgrau        — Borders, Alternation, Ruhe

SEKUNDÄR:   #84C041  Grün            — Erfolg, Positiv, Bestanden
            #CC0000  Rot             — Fehler, Negativ, Blocker
            #1195EB  Hellblau        — Info, Links, unterstützend
            #5BE3D6  Türkis          — Tertiär, Diagramme
            #FDC83A  Gelb            — Warnung, Aufmerksamkeit
            #E2C39A  Beige           — Dezent, 6. Diagrammfarbe

CODE-BG:    #000066  Tiefes Dunkelblau
TEXT:        #1A1A2E  Fast-Schwarz (Blau-Unterton)
```
