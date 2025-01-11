from __future__ import annotations

from abc import ABC, abstractmethod
from os import environ as environ
from os import fsdecode as fsdecode
from os import fsencode as fsencode
from os import fstat as fstat
from os import getcwd as getcwd
from os import getcwdb as getcwdb
from os import lstat as lstat
from os import stat as stat
from os import stat_result as stat_result
from typing import Generic, TypeVar

from backlib.internal.typing import AnyStr, Self


AnyStr_co = TypeVar("AnyStr_co", str, bytes, covariant=True)


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
        raise NotImplementedError

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


def fspath(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Return the file system representation of the path.

    See Also
    --------
    * `os.fspath`.

    Version
    -------
    * Python 3.13.
    """
    if isinstance(path, (str, bytes)):
        return path

    path_type = type(path)

    try:
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

    if not isinstance(path_repr, (str, bytes)):
        return path_repr

    detail = (
        f"expected {path_type.__name__}.__fspath__() to return str or bytes, "
        f"not {type(path_repr).__name__}"
    )
    raise TypeError(detail)
