from __future__ import annotations

from pathlib import Path

import pytest

from reportgen.csv_loader import load_csv
from reportgen.validator import ValidationError


def _write_csv(path: Path, content: str) -> Path:
    path.write_text(content, encoding="utf-8")
    return path


def test_load_csv_with_header(tmp_path: Path) -> None:
    csv_path = _write_csv(tmp_path / "input.csv", "name,amount\nAlice,10\nBob,5\n")

    columns, rows = load_csv(csv_path, header=True)

    assert columns == ["name", "amount"]
    assert rows == [
        {"name": "Alice", "amount": "10"},
        {"name": "Bob", "amount": "5"},
    ]


def test_load_csv_without_header(tmp_path: Path) -> None:
    csv_path = _write_csv(tmp_path / "input.csv", "Alice,10\nBob,5\n")

    columns, rows = load_csv(csv_path, header=False)

    assert columns == ["col1", "col2"]
    assert rows == [
        {"col1": "Alice", "col2": "10"},
        {"col1": "Bob", "col2": "5"},
    ]


def test_load_csv_inconsistent_columns(tmp_path: Path) -> None:
    csv_path = _write_csv(tmp_path / "input.csv", "a,b\n1\n")

    with pytest.raises(ValidationError, match="row 2"):
        load_csv(csv_path, header=False)


def test_load_csv_empty_file(tmp_path: Path) -> None:
    csv_path = _write_csv(tmp_path / "input.csv", "")

    with pytest.raises(ValidationError, match="empty file"):
        load_csv(csv_path, header=False)
