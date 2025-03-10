from __future__ import annotations

from typing import Any


def int_or_none(value: Any) -> int | None:
    """Convert `value`, if possible, to `int` otherwise `None`."""
    try:
        as_int = int(value)
    except (TypeError, ValueError):
        return None
    return as_int
