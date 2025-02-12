from typing import TypeVar


__all__: list[str] = ["refactorable", "simplified", "techdebt"]


T = TypeVar("T")


def techdebt(debt: T) -> T:
    """Mark the object as a technical debt."""
    return debt


def refactorable(debt: T) -> T:
    """Mark the object as a refactorable.

    Notes
    -----
    * Objects marked with this decorator must be refactored.
    """
    return debt


def simplified(debt: T) -> T:
    """Mark the object as a simplification.

    Notes
    -----
    * Objects marked with this decorator have reduced functionality;
    * Objects marked with this decorator must be reimplemented.
    """
    return debt
