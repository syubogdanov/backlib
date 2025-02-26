from typing import TypeVar


T = TypeVar("T")


def platform(debt: T) -> T:
    """Mark the object as platform-specific.

    Notes
    -----
    * Platform-specific objects are not portable.
    """
    return debt


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
