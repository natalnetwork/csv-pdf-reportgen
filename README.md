# csv-pdf-reportgen

A minimal, production-oriented **CSV → PDF report generator** written in
Python.

The project demonstrates a clean backend architecture using a
deterministic data pipeline and modern tooling (pytest, ruff, CI)
suitable for professional software development and portfolio use.

------------------------------------------------------------------------

# Overview

`csv-pdf-reportgen` converts structured CSV data into formatted PDF
reports using HTML templates.

Pipeline architecture:

CSV → Validate → Transform → Render (Jinja2) → HTML → PDF

The goal of the project is **clarity, reliability, and testability**,
not feature overload.

------------------------------------------------------------------------

# Features (MVP v0.1)

• End‑to‑end CSV → PDF pipeline\
• Jinja2 template rendering\
• HTML → PDF conversion\
• Deterministic CLI interface\
• Automated tests using **pytest**\
• Static code quality checks with **ruff**\
• Continuous Integration using **GitHub Actions**

------------------------------------------------------------------------

# Architecture

The application follows a **pipeline pattern**:

load → validate → transform → render → generate → write

Design principles:

• No global state\
• Explicit error handling\
• Deterministic behavior\
• Typed Python code\
• Clear module responsibilities\
• Testability over feature count

Example module layout:

    reportgen/
        __init__.py
        __main__.py
        cli.py
        pipeline.py

Templates are stored separately:

    templates/
        minimal/
            template.html

------------------------------------------------------------------------

# Installation

Clone the repository:

    git clone https://github.com/natalnetwork/csv-pdf-reportgen.git
    cd csv-pdf-reportgen

Create a virtual environment:

    python -m venv .venv
    source .venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

------------------------------------------------------------------------

# Usage

Basic command:

    python -m reportgen input.csv output.pdf --template templates/minimal/template.html

Arguments:

  Argument     Description
  ------------ ----------------------
  input.csv    Source CSV file
  output.pdf   Target PDF file
  --template   HTML/Jinja2 template

------------------------------------------------------------------------

# Development

Run tests:

    pytest

Run linting:

    ruff check .

Format code if necessary:

    ruff format .

------------------------------------------------------------------------

# Continuous Integration

The repository uses **GitHub Actions** to automatically run:

• tests (pytest)\
• linting (ruff)

on every push to ensure code quality.

CI status should always remain **green on main**.

------------------------------------------------------------------------

# Roadmap

Possible next steps:

• CSV schema validation\
• Multiple built‑in report templates\
• Template configuration system\
• Docker distribution\
• Batch report generation\
• Web UI

------------------------------------------------------------------------

# Why this project exists

This repository was built as a **portfolio-quality backend engineering
example** demonstrating:

• Python architecture design\
• clean repository structure\
• CI/CD integration\
• reproducible builds\
• template-based document generation

The project intentionally keeps the MVP small while focusing on **code
quality and professional engineering practices**.

------------------------------------------------------------------------

# License

MIT License
