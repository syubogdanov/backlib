from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from backlib.internal.stdlib.typing import Self


__all__: list[str] = ["PathLike"]


AnyStr_co = TypeVar("AnyStr_co", bytes, str, covariant=True)


class PathLike(ABC, Generic[AnyStr_co]):
    """An abstract base class for objects representing a file system path.

    See Also
    --------
    * `os.PathLike`.

    Version
    -------
    * Python 3.13.
    """

    __slots__: tuple[str, ...] = ()

    @abstractmethod
    def __fspath__(self: Self) -> AnyStr_co:
        """Return the file system path representation of the object.

        See Also
        --------
        * `os.PathLike.__fspath__`.

        Version
        -------
        * Python 3.13.
        """

    @classmethod
    def __subclasshook__(cls: type[Self], subclass: type) -> bool:
        """Check if subclasses implement the `__fspath__` method.

        See Also
        --------
        * `os.PathLike.__subclasshook__`.

        Version
        -------
        * Python 3.13.
        """
        if cls is not PathLike:
            return NotImplemented

        if not hasattr(subclass, "__fspath__"):
            return NotImplemented

        if not callable(subclass.__fspath__):
            return NotImplemented

        return True
