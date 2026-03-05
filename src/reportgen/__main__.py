from __future__ import annotations

try:
    from .cli import main
except ImportError:  # pragma: no cover - fallback for direct script execution
    from reportgen.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
