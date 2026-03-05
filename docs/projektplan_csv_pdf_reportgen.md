# Projektplan: CSV → PDF Report Generator (`csv-pdf-reportgen`)

## 0) Zielbild (1 Satz)
Ein CLI-Tool, das **CSV-Dateien validiert**, Daten **in Templates rendert** und **saubere PDFs** erzeugt (z. B. Rechnung/Report) – inkl. Logging, Tests, Beispiel-Daten, optional Docker.

---

## 1) Top-Checkliste (zum Abhaken)

### MVP (bis Ende Woche)
- [x] Repo erstellt (public) + Lizenz + `.gitignore` + `pyproject.toml`
- [x] CLI läuft: `reportgen input.csv --out out/` (optional `--template ...`)
- [x] CSV-Parsing + strukturelle Validierung (leere Datei, Spaltenanzahl, Header-Flag)
- [x] Template-Rendering (Jinja2) für mind. 2 Templates (z. B. `minimal`, `table`)
- [x] PDF-Erzeugung funktioniert reproduzierbar
- [x] Logging (INFO/ERROR) + Exit-Codes
- [x] Beispiel-CSV + Beispiel-PDFs im Repo
- [x] Unit-Tests für Parsing/Validation + 1 End-to-End Test
- [x] README vollständig (Checkliste unten)
- [x] GitHub Actions: `pytest` on push (optional, aber empfohlen)

### Nice-to-have
- [ ] Dockerfile + optional `docker compose` (CLI-Container)
- [ ] Konfig über YAML/JSON (z. B. Mapping CSV→Template)
- [ ] Mehrsprachige Templates (DE/EN) oder lokalisierte Formate (Datum/Währung)
- [ ] PDF-Metadaten, Seitenzahlen, Footer/Header
- [ ] `--strict` Mode (Validierung bricht bei Warnungen ab)

---

## 2) Top-Level Ablaufplan (funktionsorientiert)

**A. CLI**
1. Parse Args (input, template, out, optional config, verbose/quiet)
2. Setup Logging
3. Load Template + Template-Kontext-Schema
4. Load CSV → DataFrame/Records
5. Validate Records gegen Schema (Pflichtspalten, Typen, Constraints)
6. Transform/Normalize (Datum/Währung/Strings)
7. Render HTML (oder direkt ReportLab Flowables) pro Output-Dokument
8. Generate PDF
9. Write Output + Summary
10. Exit-Code (0 ok, >0 Fehler)

**B. Validierung**
- Pflichtfelder
- Typkonversionen (int/float/date)
- Constraints (z. B. Betrag >= 0)
- Report: Fehlerliste + Warnungen

**C. Template**
- Jinja2 Template + CSS (bei HTML→PDF)
- Standard-Kontext: `company`, `customer`, `items`, `totals`, `meta`

**D. PDF Backend (empfohlen: WeasyPrint oder ReportLab)**
- Variante 1: Jinja2→HTML + CSS → WeasyPrint PDF
- Variante 2: ReportLab direkt (layout-lastiger)

> Empfehlung für Showcase: **Jinja2 + WeasyPrint**, weil Templates elegant sind und Business-Use klar wird.

---

## 3) Projektstruktur (Python Files)

```
csv-pdf-reportgen/
├─ pyproject.toml
├─ README.md
├─ LICENSE
├─ .gitignore
├─ .github/workflows/ci.yml
├─ src/reportgen/
│  ├─ __init__.py
│  ├─ __main__.py
│  ├─ cli.py
│  ├─ csv_loader.py
│  ├─ validator.py
│  ├─ pipeline.py
├─ templates/
│  ├─ minimal/
│  │  └─ template.html
│  └─ table/
│     └─ template.html
├─ examples/
│  ├─ minimal.csv
│  ├─ csv-pdf-pipeline.csv
│  ├─ minimal.pdf
│  └─ csv-pdf-pipeline.pdf
└─ tests/
   ├─ test_smoke.py
   ├─ test_csv_loader.py
   └─ test_pipeline_e2e.py
```

---

## 4) TODO-Kommentare pro Datei (zum Einfügen ins Skelett)

### `src/reportgen/cli.py`
```python
# TODO: Provide --list-templates option.
# TODO: Print short summary (files generated, warnings count).
```

### `src/reportgen/csv_loader.py`
```python
# TODO: Allow user-specified encoding via CLI.
# TODO: Normalize header keys (optional).
```

### `src/reportgen/validator.py`
```python
# TODO: Add schema-aware validation (optional per template).
# TODO: Add strict mode (warnings become errors).
```

### `src/reportgen/pipeline.py`
```python
# TODO: Add transform stage (optional normalization).
# TODO: Return warnings for CLI summary.
```

---

## 5) README-Checkliste (optimal dokumentieren)

- [x] 1-Minute Quickstart (Copy/Paste)
- [x] Problem/Use-Case in 3 Sätzen (Business-Value)
- [x] Features (MVP + optional)
- [x] Install (pip/uv) + optional Docker
- [x] Usage Beispiele (generisch + custom template)
- [x] Template-HowTo: eigenes Template hinzufügen
- [x] Input-CSV Format (Pflichtspalten) + Beispiel
- [x] Output Beispiel (Screenshot oder Link zu Beispiel-PDF)
- [x] Architektur (kurz): Pipeline + Module
- [x] Testing: `pytest`
- [x] Roadmap (3–5 bullets)
- [x] Lizenz + Hinweis "for demo/portfolio"

---

## 6) Startprompt für GitHub Copilot (Projektstart)

> **Role:** You are my senior backend/automation engineer.
> **Goal:** Build a production-quality Python CLI tool `reportgen` that converts CSV data into PDFs using Jinja2 templates and an HTML-to-PDF engine (prefer WeasyPrint).
> **Constraints:** Keep it small but professional: clean module boundaries, typed code, robust errors, logging, unit tests, examples, and a strong README. No unnecessary frameworks.
> **Required CLI:** `reportgen <input.csv> --template <invoice|weekly_report> --out <dir> [--config config.yml] [--strict] [--verbose]`.
> **Architecture:** Implement a pipeline: load CSV → validate against schema → transform/normalize → render HTML → generate PDF → write output.
> **Deliverables:**
> - `src/reportgen/` modules as in the plan
> - Two templates with HTML+CSS and example CSVs
> - Tests for csv loading and validation + one e2e test
> - GitHub Actions workflow for tests
> **Quality:** Prefer explicit errors, no global state, deterministic output. Include type hints and docstrings.
> **Now:** Start by generating the project skeleton (`pyproject.toml`, package structure), then implement `cli.py`, `pipeline.py`, and the minimal working path end-to-end before adding extra features.

---

## 7) Verbesserungsvorschläge (ohne weitere Fragen)
- Wenn du wenig Zeit hast: **MVP zuerst end-to-end** (ein Template + ein Beispiel-CSV + PDF) → danach Validierung/Tests erweitern.
- **Beispiel-PDFs** im Repo sind ein starker „Wow“-Faktor.
- Verwende **Exit-Codes** und klare Fehlertexte: Das wirkt professionell.
