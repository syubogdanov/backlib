from collections.abc import Callable
from typing import TypeVar


__all__: list[str] = ["techdebt"]


T = TypeVar("T")


def techdebt(comment: str) -> Callable[[T], T]:  # noqa: ARG001
    """Mark an object as a technical debt."""
    return lambda obj: obj
