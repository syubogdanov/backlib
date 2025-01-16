from typing import TypeVar


__all__: list[str] = ["techdebt"]


T = TypeVar("T")


def techdebt(object_: T) -> T:
    """Mark an object as a technical debt."""
    return object_
