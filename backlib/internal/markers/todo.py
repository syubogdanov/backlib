from typing import TypeVar


__all__: list[str] = ["refactor", "restore"]


T = TypeVar("T")


def refactor(refactorable: T) -> T:
    """Mark up an object as subject to refactoring."""
    return refactorable


def restore(restorable: T) -> T:
    """Mark up an object as subject to be restored.

    Notes
    -----
    * Marked objects usually have reduced functionality.
    """
    return restorable
