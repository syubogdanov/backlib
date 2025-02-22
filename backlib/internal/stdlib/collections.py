from abc import abstractmethod
from typing import Protocol, runtime_checkable


__all__: list[str] = ["Buffer"]


@runtime_checkable
class Buffer(Protocol):
    """An object that provides the `__buffer__` method."""

    @abstractmethod
    def __buffer__(self, flags: int, /) -> memoryview:
        """Request the buffer from an object."""
