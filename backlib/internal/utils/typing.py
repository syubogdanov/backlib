from typing import Protocol, TypeVar

from backlib.internal.collections import Buffer
from backlib.internal.typing import Self, TypeAlias


__all__: list[str] = [
    "ReadOnlyBuffer",
    "ReadableBuffer",
    "SupportsRead",
    "SupportsWrite",
    "WriteableBuffer",
]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


ReadableBuffer: TypeAlias = Buffer
ReadOnlyBuffer: TypeAlias = Buffer
WriteableBuffer: TypeAlias = Buffer


class SupportsRead(Protocol[T_co]):
    """An object that provides the `read` method."""

    def read(self: Self, length: int = ..., /) -> T_co:
        """Perform a read operation."""


class SupportsWrite(Protocol[T_contra]):
    """An object that provides the `write` method."""

    def write(self: Self, s: T_contra, /) -> object:
        """Perform a write operation."""
