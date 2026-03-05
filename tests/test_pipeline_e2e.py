from __future__ import annotations

from pathlib import Path

from reportgen import pipeline


def test_pipeline_generates_pdf(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    input_csv = repo_root / "examples" / "minimal.csv"
    template = repo_root / "templates" / "minimal" / "template.html"

    output_path = pipeline.run(input_csv, template, tmp_path, header=True)

    assert output_path.exists()
    assert output_path.stat().st_size > 0
