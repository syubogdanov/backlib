from typing import Protocol, TypeVar

from backlib.py313.internal.stdlib.typing import Self


__all__: list[str] = ["SupportsRead", "SupportsWrite"]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


class SupportsRead(Protocol[T_co]):
    """An object that provides the `read` method."""

    def read(self: Self, length: int = ..., /) -> T_co:
        """Perform a read operation."""


class SupportsWrite(Protocol[T_contra]):
    """An object that provides the `write` method."""

    def write(self: Self, s: T_contra, /) -> object:
        """Perform a write operation."""
