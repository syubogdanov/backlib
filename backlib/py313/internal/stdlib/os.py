"""Backports for the `os` module.

Notes
-----
* According to the `os` implementation, only `POSIX` and `Windows NT` are supported.

See Also
--------
* `os`.

Version
-------
* Python 3.13.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Final, Generic, overload

from backlib.py313.internal.stdlib.typing import AnyStr, Self, TypeAlias
from backlib.py313.internal.utils.sys import is_nt, is_posix


__all__ = [
    "SEEK_CUR",
    "SEEK_END",
    "SEEK_SET",
    "PathLike",
    "error",
    "fspath",
]


if not is_nt() and not is_posix():
    detail = "Only 'POSIX' and 'Windows NT' are supported"
    raise ImportError(detail)


SEEK_SET: Final[int] = 0
SEEK_CUR: Final[int] = 1
SEEK_END: Final[int] = 2


error: TypeAlias = OSError


class PathLike(ABC, Generic[AnyStr]):
    """An abstract base for the file system path protocol.

    See Also
    --------
    * `os.PathLike`.

    Version
    -------
    * Python 3.13.
    """

    __slots__: list[str] = []

    @abstractmethod
    def __fspath__(self: Self) -> AnyStr:
        """Return the file system path representation of the object.

        See Also
        --------
        * `os.PathLike.__fspath__`.

        Version
        -------
        * Python 3.13.
        """
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls: type[Self], subclass: type) -> bool:
        """Check whether subclass is considered a subclass of this `ABC`.

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


@overload
def fspath(path: str) -> str:
    ...


@overload
def fspath(path: bytes) -> bytes:
    ...


@overload
def fspath(path: PathLike[AnyStr]) -> AnyStr:
    ...


def fspath(path: str | bytes | PathLike[AnyStr]) -> str | bytes | AnyStr:
    """Return the path representation of a path-like object.

    See Also
    --------
    * `os.fspath`.

    Version
    -------
    * Python 3.13.
    """
    if isinstance(path, (str, bytes)):
        return path

    try:
        path_type = type(path)
        path_repr = path_type.__fspath__(path)

    except AttributeError:
        if hasattr(path_type, "__fspath__"):
            raise

        detail = f"expected str, bytes or os.PathLike object, not {path_type.__name__}"
        raise TypeError(detail) from None

    except TypeError:
        if path_type.__fspath__ is not None:
            raise

        detail = f"expected str, bytes or os.PathLike object, not {path_type.__name__}"
        raise TypeError(detail) from None

    if isinstance(path_repr, (str, bytes)):
        return path_repr

    actual = type(path_repr).__name__
    expected = path_type.__name__

    detail = f"expected {expected}.__fspath__() to return str or bytes, not {actual}"
    raise TypeError(detail)
