import sys

from typing import Protocol, TypeVar


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


T_co = TypeVar("T_co", covariant=True)


class SupportsRead(Protocol[T_co]):
    """An object that provides the `read` method."""

    def read(self: Self, length: int = ..., /) -> T_co:
        """Perform a read operation."""
