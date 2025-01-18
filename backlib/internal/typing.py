import sys

from abc import abstractmethod
from typing import Protocol, TypeVar


__all__: list[str] = ["AnyStr", "Buffer", "ParamSpec", "Self", "TypeAlias"]


AnyStr = TypeVar("AnyStr", str, bytes)


class Buffer(Protocol):
    """An object that provides the `__buffer__` method."""

    @abstractmethod
    def __buffer__(self, flags: int, /) -> memoryview:
        """Request the buffer from an object."""


if sys.version_info >= (3, 10):
    from typing import ParamSpec
else:
    from typing_extensions import ParamSpec


if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self
