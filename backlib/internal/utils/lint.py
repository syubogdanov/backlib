from collections.abc import Callable
from typing import TypeVar


__all__: list[str] = ["todo"]


T = TypeVar("T")


def todo(comment: str) -> Callable[[T], T]:  # noqa: ARG001
    """Mark an object as a technical debt."""
    return lambda obj: obj
