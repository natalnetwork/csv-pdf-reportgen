from __future__ import annotations

import csv
from pathlib import Path

from .validator import ValidationError


def _sniff_dialect(sample: str) -> csv.Dialect:
    sniffer = csv.Sniffer()
    try:
        return sniffer.sniff(sample, delimiters=[",", ";", "\t", "|"])
    except csv.Error:
        return csv.excel


def _generate_columns(column_count: int) -> list[str]:
    return [f"col{index + 1}" for index in range(column_count)]


def load_csv(path: str | Path, header: bool) -> tuple[list[str], list[dict[str, str]]]:
    csv_path = Path(path)
    with csv_path.open(newline="", encoding="utf-8-sig") as handle:
        sample = handle.read(4096)
        handle.seek(0)
        dialect = _sniff_dialect(sample)
        reader = csv.reader(handle, dialect)
        all_rows = list(reader)

    if not all_rows:
        raise ValidationError("CSV validation failed: empty file")

    if header:
        columns = [value.strip() for value in all_rows[0]]
        if not columns or not any(columns):
            raise ValidationError("CSV validation failed: missing header row")
        data_rows = all_rows[1:]
        row_offset = 2
    else:
        first_row = all_rows[0]
        if not first_row:
            raise ValidationError("CSV validation failed: no columns detected")
        columns = _generate_columns(len(first_row))
        data_rows = all_rows
        row_offset = 1

    expected_length = len(columns)
    for index, row in enumerate(data_rows):
        if len(row) != expected_length:
            row_num = index + row_offset
            raise ValidationError(
                f"CSV validation failed: inconsistent column count in row {row_num}"
            )

    rows = [dict(zip(columns, row)) for row in data_rows]
    return columns, rows
