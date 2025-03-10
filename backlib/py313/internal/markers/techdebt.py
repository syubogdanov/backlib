from typing import TypeVar


T = TypeVar("T")


def simplified(debt: T) -> T:
    """Mark the object as simplified.

    Notes
    -----
    * Simplified objects have reduced functionality.
    """
    return debt
