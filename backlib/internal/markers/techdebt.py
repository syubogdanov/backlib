from typing import TypeVar


T = TypeVar("T")


def refactor(debt: T) -> T:
    """Mark the object as needing refactoring."""
    return debt


def simplified(debt: T) -> T:
    """Mark the object as simplified.

    Notes
    -----
    * Simplified objects have reduced functionality.
    """
    return debt
