"""Pipeline orchestrator: load CSV, render template, generate PDF."""

from __future__ import annotations

from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from weasyprint import HTML

from .csv_loader import load_csv


def render_html(template_path: Path, context: dict[str, object]) -> str:
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


def run(
    input_path: str | Path,
    template_path: str | Path,
    out_dir: str | Path,
    header: bool = False,
) -> Path:
    """Run the pipeline: CSV -> Jinja2 HTML -> WeasyPrint PDF."""
    # TODO: add optional transform stage before rendering.
    # TODO: return warnings for CLI summary.
    csv_path = Path(input_path)
    template_file = Path(template_path)
    output_dir = Path(out_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    columns, rows = load_csv(csv_path, header=header)
    context = {
        "columns": columns,
        "rows": rows,
        "records": rows,
        "meta": {"source": csv_path.name, "count": len(rows)},
    }
    html = render_html(template_file, context)

    output_path = output_dir / f"{csv_path.stem}.pdf"
    return generate_pdf(html, output_path)
