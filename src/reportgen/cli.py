from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import Sequence

from reportgen import pipeline


def _build_parser() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser(prog="reportgen")
	parser.add_argument("input_csv", help="Input CSV file")
	parser.add_argument("--template", required=True, help="HTML template file")
	parser.add_argument("--out", required=True, help="Output directory")

	group = parser.add_mutually_exclusive_group()
	group.add_argument("--verbose", action="store_true", help="Enable INFO logging")
	group.add_argument("--quiet", action="store_true", help="Enable ERROR logging")
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

	_configure_logging(args.verbose, args.quiet)

	input_path = Path(args.input_csv)
	template_path = Path(args.template)
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
		print(f"Error: could not create output directory: {out_dir} ({exc})", file=sys.stderr)
		return 2

	output_path = pipeline.run(input_path, template_path, out_dir)
	print(output_path)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
