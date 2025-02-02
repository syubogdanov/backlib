import sys

from typing import TypeVar


__all__: list[str] = ["techdebt"]


T = TypeVar("T")


def techdebt(debt: T) -> T:
    """Mark the object as a technical debt."""
    if (3, 9, 0) <= sys.version_info < (3, 14, 0):
        return debt

    detail = f"Python {sys.version} is not supported"
    raise NotImplementedError(detail)
