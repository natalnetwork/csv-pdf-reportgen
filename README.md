# CSV → PDF Report Generator

![CI](https://github.com/natalnetwork/csv-pdf-reportgen/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Ruff](https://img.shields.io/badge/linter-ruff-yellow)

A minimal, production‑style CLI tool that converts **CSV files into PDF
reports** using **Jinja2 templates** and **WeasyPrint**.

This project demonstrates a clean **pipeline architecture** suitable for
automation, reporting systems and backend services.

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

Run the CLI tool:

``` bash
reportgen examples/minimal.csv --out out
```

If your CSV has a header row, pass:

``` bash
reportgen examples/minimal.csv --out out --header yes
```

Generated output:

    out/minimal.pdf

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

# License

MIT License
