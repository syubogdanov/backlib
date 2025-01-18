from __future__ import annotations

import os as py_os

from abc import ABC, abstractmethod
from contextlib import suppress
from typing import Final, Generic, TypeVar

from backlib.internal.typing import Self, TypeAlias
from backlib.internal.utils.lint import techdebt
from backlib.internal.utils.sys import is_nt, is_posix
from backlib.internal.utils.typing import ReadableBuffer


__all__: list[str] = [
    "F_OK",
    "O_APPEND",
    "O_CREAT",
    "O_EXCL",
    "O_RDONLY",
    "O_RDWR",
    "O_TRUNC",
    "O_WRONLY",
    "R_OK",
    "SEEK_CUR",
    "SEEK_END",
    "SEEK_SET",
    "W_OK",
    "X_OK",
    "altsep",
    "close",
    "closerange",
    "curdir",
    "defpath",
    "devnull",
    "error",
    "extsep",
    "ftruncate",
    "get_inheritable",
    "getcwd",
    "getcwdb",
    "isatty",
    "linesep",
    "lseek",
    "name",
    "pardir",
    "pathsep",
    "read",
    "sep",
    "strerror",
    "write",
]


if not is_nt() and not is_posix():
    detail = "no os specific module found"
    raise ImportError(detail)


AnyStr_co = TypeVar("AnyStr_co", bytes, str, covariant=True)


error: TypeAlias = OSError


curdir: Final[str] = "."
pardir: Final[str] = ".."
extsep: Final[str] = "."

name: Final[str] = "posix" if is_posix() else "nt"
linesep: Final[str] = "\n" if is_posix() else "\r\n"

sep: Final[str] = "/" if is_posix() else "\\"
pathsep: Final[str] = ":" if is_posix() else ";"
altsep: Final[str | None] = None if is_posix() else "/"

defpath: Final[str] = "/bin:/usr/bin" if is_posix() else ".;C:\\bin"
devnull: Final[str] = "/dev/null" if is_posix() else "nul"


SEEK_SET: Final[int] = 0
SEEK_CUR: Final[int] = 1
SEEK_END: Final[int] = 2


F_OK: Final[int] = techdebt(py_os.F_OK)
R_OK: Final[int] = techdebt(py_os.R_OK)
W_OK: Final[int] = techdebt(py_os.W_OK)
X_OK: Final[int] = techdebt(py_os.X_OK)


O_APPEND: Final[int] = techdebt(py_os.O_APPEND)
O_CREAT: Final[int] = techdebt(py_os.O_CREAT)
O_EXCL: Final[int] = techdebt(py_os.O_EXCL)
O_RDONLY: Final[int] = techdebt(py_os.O_RDONLY)
O_RDWR: Final[int] = techdebt(py_os.O_RDWR)
O_TRUNC: Final[int] = techdebt(py_os.O_TRUNC)
O_WRONLY: Final[int] = techdebt(py_os.O_WRONLY)


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


@techdebt
def close(fd: int) -> None:
    """Close file descriptor `fd`.

    See Also
    --------
    * `os.close`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.close(fd)


def closerange(fd_low: int, fd_high: int, /) -> None:
    """Close all descriptors from `fd_low` (inclusive) to `fd_high` (exclusive), ignoring errors.

    See Also
    --------
    * `os.closerange`.

    Version
    -------
    * Python 3.13.
    """
    for fd in range(fd_low, fd_high):
        with suppress(OSError):
            close(fd)


@techdebt
def ftruncate(fd: int, length: int, /) -> None:
    """Truncate the file corresponding to file descriptor `fd`.

    See Also
    --------
    * `os.ftruncate`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.ftruncate(fd, length)


@techdebt
def get_inheritable(fd: int, /) -> bool:
    """Get the 'inheritable' flag of the specified file descriptor (a boolean).

    See Also
    --------
    * `os.get_inheritable`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.get_inheritable(fd)


@techdebt
def getcwd() -> str:
    """Return a string representing the current working directory.

    See Also
    --------
    * `os.getcwd`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.getcwd()  # noqa: PTH109


@techdebt
def getcwdb() -> bytes:
    """Return a bytestring representing the current working directory.

    See Also
    --------
    * `os.getcwdb`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.getcwdb()  # noqa: PTH109


@techdebt
def isatty(fd: int, /) -> bool:
    """Check if the file descriptor `fd` is open and connected to a tty(-like) device.

    See Also
    --------
    * `os.isatty`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.isatty(fd)


@techdebt
def lseek(fd: int, position: int, whence: int, /) -> int:
    """Set the current position of file descriptor `fd` to position `pos`, modified by `whence`.

    See Also
    --------
    * `os.lseek`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.lseek(fd, position, whence)


@techdebt
def read(fd: int, length: int, /) -> bytes:
    """Read at most `length` bytes from file descriptor `fd`.

    See Also
    --------
    * `os.read`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.read(fd, length)


@techdebt
def set_inheritable(fd: int, inheritable: bool, /) -> None:  # noqa: FBT001
    """Set the 'inheritable' flag of the specified file descriptor.

    See Also
    --------
    * `os.set_inheritable`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.set_inheritable(fd, inheritable)


@techdebt
def strerror(code: int, /) -> str:
    """Return the error message corresponding to the error code in `code`.

    See Also
    --------
    * `os.strerror`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.strerror(code)


@techdebt
def write(fd: int, data: ReadableBuffer, /) -> int:
    """Write the bytestring in `data` to file descriptor `fd`.

    See Also
    --------
    * `os.write`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.write(fd, data)
