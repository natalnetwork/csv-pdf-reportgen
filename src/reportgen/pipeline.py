from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape
from weasyprint import HTML


def load_csv_records(csv_path: Path) -> list[dict[str, Any]]:
    """Load CSV file into a list of dict records."""
    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader)


def render_html(template_path: Path, context: dict[str, Any]) -> str:
    """Render HTML with Jinja2 using the template file."""
    env = Environment(
        loader=FileSystemLoader(str(template_path.parent)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template(template_path.name)
    return template.render(**context)


def generate_pdf(html: str, output_path: Path) -> Path:
    """Generate a PDF using WeasyPrint from rendered HTML."""
    HTML(string=html, base_url=str(output_path.parent)).write_pdf(output_path)
    return output_path


def run(input_path: str | Path, template_path: str | Path, out_dir: str | Path) -> Path:
    """Run the minimal pipeline: CSV -> Jinja2 HTML -> WeasyPrint PDF."""
    csv_path = Path(input_path)
    template_file = Path(template_path)
    output_dir = Path(out_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    records = load_csv_records(csv_path)
    context = {
        "records": records,
        "meta": {"source": csv_path.name, "count": len(records)},
    }
    html = render_html(template_file, context)

    output_path = output_dir / f"{csv_path.stem}.pdf"
    return generate_pdf(html, output_path)
