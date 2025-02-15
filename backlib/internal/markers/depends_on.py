from typing import TypeVar


__all__: list[str] = ["platform"]


T = TypeVar("T")


def platform(dependent: T) -> T:
    """Mark up an object as dependent on a platform."""
    return dependent
