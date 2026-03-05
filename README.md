# CSV → PDF Report Generator

![CI](https://github.com/natalnetwork/csv-pdf-reportgen/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Ruff](https://img.shields.io/badge/linter-ruff-yellow)

A minimal, production‑style CLI tool that converts **CSV files into PDF
reports** using **Jinja2 templates** and **WeasyPrint**.

Use it to turn ad-hoc CSV exports into shareable PDF reports with a single command.
It is useful for quick status reports, invoices, or audit-friendly exports from
spreadsheets and back-office systems.
The default template is generic, but you can swap in custom templates anytime.

This project demonstrates a clean **pipeline architecture** suitable for
automation, reporting systems and backend services.

------------------------------------------------------------------------

# 1-Minute Quickstart

``` bash
reportgen examples/minimal.csv --out out
```

If your CSV has a header row:

``` bash
reportgen examples/minimal.csv --out out --header yes
```

Output:

    out/minimal.pdf

------------------------------------------------------------------------

# Example

    reportgen examples/minimal.csv --out out

Output:

    out/minimal.pdf

------------------------------------------------------------------------

# Features

-   CSV → PDF pipeline
-   Jinja2 template rendering
-   WeasyPrint PDF generation
-   CLI interface
-   reproducible output
-   typed Python code
-   Ruff linting & formatting
-   CI with GitHub Actions

------------------------------------------------------------------------

# Installation

Clone the repository:

``` bash
git clone https://github.com/natalnetwork/csv-pdf-reportgen.git
cd csv-pdf-reportgen
```

Create virtual environment:

``` bash
python -m venv .venv
source .venv/bin/activate
```

Install the project:

``` bash
pip install -e .
```

------------------------------------------------------------------------

# Usage

Generic usage with default template:

``` bash
reportgen data.csv --out out
```

CSV with header row:

``` bash
reportgen data.csv --out out --header yes
```

Custom template by path:

``` bash
reportgen data.csv --template templates/minimal/template.html --out out
```

Generated output:

        out/data.pdf

------------------------------------------------------------------------

# Template How-To

1. Create a folder under `templates/`.
2. Add a `template.html` file using Jinja2.
3. Use `columns` and `rows` in the template context.

Minimal example:

``` html
<table>
    <thead>
        <tr>
            {% for column in columns %}
                <th>{{ column }}</th>
            {% endfor %}
        </tr>
    </thead>
    <tbody>
        {% for row in rows %}
            <tr>
                {% for column in columns %}
                    <td>{{ row[column] }}</td>
                {% endfor %}
            </tr>
        {% endfor %}
    </tbody>
</table>
```

------------------------------------------------------------------------

# Input CSV Format

By default, the CLI assumes **no header** and generates column names `col1..colN`.
If the first row is a header, pass `--header yes`.

Example with header:

``` csv
name,amount,date
Alice,19.90,2026-03-03
Bob,5.00,2026-03-04
```

Example without header:

``` csv
Alice,19.90,2026-03-03
Bob,5.00,2026-03-04
```

------------------------------------------------------------------------

# Example Output

Generated sample PDFs live in:

- `examples/minimal.pdf`
- `examples/csv-pdf-pipeline.pdf`

------------------------------------------------------------------------

# Project Structure

    csv-pdf-reportgen
    │
    ├─ src/reportgen
    │  ├─ pipeline.py
    │  ├─ cli.py
    │  └─ __main__.py
    │
    ├─ templates
    │
    ├─ examples
    │
    ├─ tests
    │
    ├─ docs
    │
    └─ pyproject.toml

------------------------------------------------------------------------

# Pipeline Architecture

    load_csv
       ↓
    validate
       ↓
    transform
       ↓
    render_template
       ↓
    generate_pdf

------------------------------------------------------------------------

# Development

Run linting:

``` bash
ruff check .
```

Format code:

``` bash
ruff format .
```

Run tests:

``` bash
pytest
```

------------------------------------------------------------------------

# Future Improvements

Possible future extensions:

-   schema validation for CSV input
-   configurable report themes
-   plugin system for report types
-   HTML preview mode
-   Docker container for batch reporting

------------------------------------------------------------------------

# Roadmap

- Add schema-aware validation per template
- Optional transform stage (dates/currency)
- Template discovery via CLI

------------------------------------------------------------------------

# License

MIT License

For demo/portfolio use.
