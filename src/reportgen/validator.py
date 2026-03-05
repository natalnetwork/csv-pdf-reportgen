from __future__ import annotations

from dataclasses import dataclass

"""Validation error types for reportgen."""


@dataclass(frozen=True)
class ValidationError(Exception):
    message: str

    def __str__(self) -> str:
        return self.message
