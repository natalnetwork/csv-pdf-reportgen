from __future__ import annotations

import argparse
import logging
import sys
from collections.abc import Sequence
from pathlib import Path

from reportgen.validator import ValidationError

"""CLI entrypoint for reportgen."""


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="reportgen",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  reportgen data.csv --out out\n"
            "  reportgen data.csv --out out --header yes"
        ),
    )
    parser.add_argument("input_csv", nargs="?", help="Input CSV file")
    parser.add_argument("--template", help="HTML template file")
    parser.add_argument("--out", help="Output directory")
    parser.add_argument(
        "--header",
        choices=("yes", "no"),
        default="no",
        help="Header handling: yes (first row), no (generate)",
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--verbose", action="store_true", help="Enable INFO logging")
    group.add_argument("--quiet", action="store_true", help="Enable ERROR logging")
    # TODO: add --list-templates option.
    return parser


def _configure_logging(verbose: bool, quiet: bool) -> None:
    if quiet:
        level = logging.ERROR
    elif verbose:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(level=level)


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.input_csv is None:
        parser.print_help()
        return 0

    missing_flags: list[str] = []
    if not args.out:
        missing_flags.append("--out")
    if missing_flags:
        missing_str = ", ".join(missing_flags)
        print(
            f"Error: missing required option(s) for input CSV: {missing_str}",
            file=sys.stderr,
        )
        return 2

    _configure_logging(args.verbose, args.quiet)

    input_path = Path(args.input_csv)
    if args.template:
        template_path = Path(args.template)
    else:
        template_path = (
            Path(__file__).resolve().parents[2]
            / "templates"
            / "table"
            / "template.html"
        )
    out_dir = Path(args.out)

    if not input_path.is_file():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        return 2
    if not template_path.is_file():
        print(f"Error: template file not found: {template_path}", file=sys.stderr)
        return 2

    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(
            f"Error: could not create output directory: {out_dir} ({exc})",
            file=sys.stderr,
        )
        return 2

    try:
        from reportgen import pipeline

        output_path = pipeline.run(
            input_path,
            template_path,
            out_dir,
            header=args.header == "yes",
        )
    except ValidationError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    print(output_path)
    # TODO: print short summary (files generated, warnings count).
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
