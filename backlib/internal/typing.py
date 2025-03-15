from typing import Protocol, TypeVar, runtime_checkable


T_co = TypeVar("T_co", covariant=True)


@runtime_checkable
class SupportsRead(Protocol[T_co]):
    """An ABC with one abstract method `read`."""

    def read(self, length: int = ..., /) -> T_co:
        """Read and return up to `length` units."""
