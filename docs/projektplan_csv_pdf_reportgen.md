# Projektplan: CSV → PDF Report Generator (`csv-pdf-reportgen`)

## 0) Zielbild (1 Satz)
Ein CLI-Tool, das **CSV-Dateien validiert**, Daten **in Templates rendert** und **saubere PDFs** erzeugt (z. B. Rechnung/Report) – inkl. Logging, Tests, Beispiel-Daten, optional Docker.

---

## 1) Top-Checkliste (zum Abhaken)

### MVP (bis Ende Woche)
- [ ] Repo erstellt (public) + Lizenz + `.gitignore` + `pyproject.toml`
- [ ] CLI läuft: `reportgen input.csv --template invoice --out out/`
- [ ] CSV-Parsing + Schema-Validierung (Pflichtspalten, Typen, leere Felder)
- [ ] Template-Rendering (Jinja2) für mind. 2 Templates (z. B. `invoice`, `weekly_report`)
- [ ] PDF-Erzeugung funktioniert reproduzierbar
- [ ] Logging (INFO/ERROR) + Exit-Codes
- [ ] Beispiel-CSV + Beispiel-PDFs im Repo
- [ ] Unit-Tests für Parsing/Validation + 1 End-to-End Test
- [ ] README vollständig (Checkliste unten)
- [ ] GitHub Actions: `pytest` on push (optional, aber empfohlen)

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
├─ .github/workflows/tests.yml
├─ src/reportgen/
│  ├─ __init__.py
│  ├─ cli.py
│  ├─ logging_config.py
│  ├─ config.py
│  ├─ csv_loader.py
│  ├─ schema.py
│  ├─ validator.py
│  ├─ transform.py
│  ├─ templating.py
│  ├─ pdf_engine.py
│  ├─ pipeline.py
│  ├─ exceptions.py
│  └─ models.py
├─ templates/
│  ├─ invoice/
│  │  ├─ template.html
│  │  ├─ styles.css
│  │  └─ example_mapping.yml
│  └─ weekly_report/
│     ├─ template.html
│     ├─ styles.css
│     └─ example_mapping.yml
├─ examples/
│  ├─ invoice_example.csv
│  ├─ weekly_report_example.csv
│  └─ company_profile.yml
└─ tests/
   ├─ test_csv_loader.py
   ├─ test_validator.py
   ├─ test_pipeline_e2e.py
   └─ fixtures/
      └─ sample.csv
```

---

## 4) TODO-Kommentare pro Datei (zum Einfügen ins Skelett)

### `src/reportgen/cli.py`
```python
# TODO: Define argparse/typer CLI interface (input, template, out, config, verbose).
# TODO: Call pipeline.run(...) and translate exceptions to proper exit codes.
# TODO: Provide --list-templates option.
# TODO: Print short summary (files generated, warnings count).
```

### `src/reportgen/logging_config.py`
```python
# TODO: Configure logging (level, format, optional JSON).
# TODO: Support --verbose and --quiet flags from CLI.
```

### `src/reportgen/config.py`
```python
# TODO: Load YAML/JSON config (company profile, template mapping).
# TODO: Provide defaults if config missing.
# TODO: Validate config schema (required keys).
```

### `src/reportgen/csv_loader.py`
```python
# TODO: Load CSV with encoding detection or user-specified encoding.
# TODO: Return list[dict] records with normalized keys.
# TODO: Provide clear error messages for missing file / parse errors.
```

### `src/reportgen/schema.py`
```python
# TODO: Define schema structures for templates (required columns, types, constraints).
# TODO: Provide per-template schema loader (e.g., from example_mapping.yml).
```

### `src/reportgen/validator.py`
```python
# TODO: Validate records against schema (missing cols, type conversion, constraints).
# TODO: Return ValidationResult (errors, warnings, cleaned_records).
# TODO: Support strict mode (warnings become errors).
```

### `src/reportgen/transform.py`
```python
# TODO: Normalize dates, currency, whitespace, optional locale formatting.
# TODO: Compute derived fields (totals, VAT, etc.) for invoice template.
```

### `src/reportgen/templating.py`
```python
# TODO: Load Jinja2 environment, templates and assets (CSS).
# TODO: Render HTML from template + context.
# TODO: Provide template discovery function.
```

### `src/reportgen/pdf_engine.py`
```python
# TODO: Convert rendered HTML + CSS to PDF (WeasyPrint or fallback).
# TODO: Handle fonts and static assets.
# TODO: Write PDF to output directory and return path.
```

### `src/reportgen/pipeline.py`
```python
# TODO: Orchestrate load -> validate -> transform -> render -> pdf.
# TODO: Provide run(input_path, template_name, out_dir, config_path, strict) -> list[Path]
# TODO: Collect and return warnings for CLI summary.
```

### `src/reportgen/exceptions.py`
```python
# TODO: Define custom exceptions (ConfigError, ValidationError, TemplateError, PdfError).
# TODO: Include user-friendly messages.
```

### `src/reportgen/models.py`
```python
# TODO: Define dataclasses/pydantic models for Company, Customer, LineItem, InvoiceTotals.
# TODO: Provide serialization helpers for templating context.
```

---

## 5) README-Checkliste (optimal dokumentieren)

- [ ] 1-Minute Quickstart (Copy/Paste)
- [ ] Problem/Use-Case in 3 Sätzen (Business-Value)
- [ ] Features (MVP + optional)
- [ ] Install (pip/uv) + optional Docker
- [ ] Usage Beispiele (invoice, weekly_report)
- [ ] Template-HowTo: eigenes Template hinzufügen
- [ ] Input-CSV Format (Pflichtspalten) + Beispiel
- [ ] Output Beispiel (Screenshot oder Link zu Beispiel-PDF)
- [ ] Architektur (kurz): Pipeline + Module
- [ ] Testing: `pytest`
- [ ] Roadmap (3–5 bullets)
- [ ] Lizenz + Hinweis „for demo/portfolio“

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
