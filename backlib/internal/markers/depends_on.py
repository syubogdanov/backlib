from typing import TypeVar

from backlib.internal.markers import todo


__all__: list[str] = ["platform"]


T = TypeVar("T")


def platform(dependent: T) -> T:
    """Mark up an object as dependent on a platform."""
    return todo.restore(dependent)
