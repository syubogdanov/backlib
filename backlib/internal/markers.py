import sys

from typing import TypeVar


__all__: list[str] = ["py_alias", "techdebt"]


T = TypeVar("T")


def py_alias(mockable: T) -> T:
    """Mark the object as an alias to Python implementation."""
    if (3, 9, 0) <= sys.version_info < (3, 14, 0):
        return mockable

    detail = f"Python {sys.version} is not supported"
    raise NotImplementedError(detail)


def techdebt(debt: T) -> T:
    """Mark the object as a technical debt."""
    return debt
