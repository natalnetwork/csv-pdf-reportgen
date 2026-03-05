from __future__ import annotations

"""Validation error types for reportgen."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ValidationError(Exception):
    message: str

    def __str__(self) -> str:
        return self.message
