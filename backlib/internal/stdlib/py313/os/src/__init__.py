from __future__ import annotations

import os as py_os

from abc import ABC, abstractmethod
from contextlib import suppress
from sys import getfilesystemencodeerrors, getfilesystemencoding
from typing import Final, Generic, NamedTuple, TypeVar

from backlib.internal.typing import AnyStr, Self, TypeAlias
from backlib.internal.utils.lint import techdebt
from backlib.internal.utils.sys import STDOUT_FILENO, is_nt, is_posix, is_unix
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
    "PathLike",
    "access",
    "altsep",
    "chdir",
    "close",
    "closerange",
    "curdir",
    "defpath",
    "devnull",
    "error",
    "extsep",
    "fsdecode",
    "fsencode",
    "fspath",
    "ftruncate",
    "get_inheritable",
    "get_terminal_size",
    "getcwd",
    "getcwdb",
    "isatty",
    "linesep",
    "link",
    "lseek",
    "mkdir",
    "name",
    "pardir",
    "pathsep",
    "read",
    "readlink",
    "rename",
    "replace",
    "sep",
    "set_inheritable",
    "strerror",
    "terminal_size",
    "write",
]


if not is_nt() and not is_unix():
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


class terminal_size(NamedTuple):  # noqa: N801
    """A subclass of tuple, holding `(columns, lines)` of the terminal window size.

    See Also
    --------
    * `os.terminal_size`.

    Version
    -------
    * Python 3.13.
    """

    columns: int
    lines: int


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
def access(
    path: int | AnyStr | PathLike[AnyStr],
    mode: int,
    *,
    dir_fd: int | None = None,
    effective_ids: bool = False,
    follow_symlinks: bool = True,
) -> bool:
    """Use the real uid/gid to test for access to `path`.

    See Also
    --------
    * `os.access`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.access(
        path=path,
        mode=mode,
        dir_fd=dir_fd,
        effective_ids=effective_ids,
        follow_symlinks=follow_symlinks,
    )


@techdebt
def chdir(path: int | AnyStr | PathLike[AnyStr]) -> None:
    """Change the current working directory to path.

    See Also
    --------
    * `os.chdir`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.chdir(path)


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
    * This function is only available on UNIX;
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
def get_terminal_size(fd: int = STDOUT_FILENO, /) -> terminal_size:
    """Return the size of the terminal window as `(columns, lines)`.

    See Also
    --------
    * `os.get_terminal_size`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is only available on UNIX;
    * This function is not a real backport.
    """
    py_terminal_size = py_os.get_terminal_size(fd)
    return terminal_size(*py_terminal_size)


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
def link(
    src: AnyStr | PathLike[AnyStr],
    dst: AnyStr | PathLike[AnyStr],
    *,
    src_dir_fd: int | None = None,
    dst_dir_fd: int | None = None,
    follow_symlinks: bool = True,
) -> None:
    """Create a hard link pointing to `src` named `dst`.

    See Also
    --------
    * `os.link`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is only available on UNIX;
    * This function is not a real backport.
    """
    return py_os.link(
        src=src,
        dst=dst,
        src_dir_fd=src_dir_fd,
        dst_dir_fd=dst_dir_fd,
        follow_symlinks=follow_symlinks,
    )


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
def mkdir(path: AnyStr | PathLike[AnyStr], mode: int = 0o777, *, dir_fd: int | None = None) -> None:
    """Create a directory named `path` with numeric mode `mode`.

    See Also
    --------
    * `os.mkdir`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.mkdir(path, mode, dir_fd=dir_fd)  # noqa: PTH102


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
def readlink(path: AnyStr | PathLike[AnyStr], *, dir_fd: int | None = None) -> AnyStr:
    """Return a string representing the path to which the symbolic link points.

    See Also
    --------
    * `os.readlink`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is only available on UNIX;
    * This function is not a real backport.
    """
    return py_os.readlink(path, dir_fd=dir_fd)  # noqa: PTH115


@techdebt
def rename(
    src: AnyStr | PathLike[AnyStr],
    dst: AnyStr | PathLike[AnyStr],
    *,
    src_dir_fd: int | None = None,
    dst_dir_fd: int | None = None,
) -> None:
    """Rename the file or directory `src` to `dst`.

    See Also
    --------
    * `os.rename`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.rename(src, dst, src_dir_fd=src_dir_fd, dst_dir_fd=dst_dir_fd)  # noqa: PTH104


@techdebt
def replace(
    src: AnyStr | PathLike[AnyStr],
    dst: AnyStr | PathLike[AnyStr],
    *,
    src_dir_fd: int | None = None,
    dst_dir_fd: int | None = None,
) -> None:
    """Rename the file or directory src to dst.

    See Also
    --------
    * `os.replace`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.replace(src, dst, src_dir_fd=src_dir_fd, dst_dir_fd=dst_dir_fd)  # noqa: PTH105


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


@techdebt
def fspath(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Return the file system representation of the path.

    See Also
    --------
    * `os.fspath`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.fspath(path)


def fsencode(filename: AnyStr | PathLike[AnyStr]) -> bytes:
    """Encode path-like `filename` to the filesystem encoding and error handler.

    See Also
    --------
    * `os.fsencode`.

    Version
    -------
    * Python 3.13.
    """
    filename = fspath(filename)

    if isinstance(filename, bytes):
        return filename

    encoding = getfilesystemencoding()
    errors = getfilesystemencodeerrors()

    return filename.encode(encoding, errors)


def fsdecode(filename: AnyStr | PathLike[AnyStr]) -> str:
    """Decode the path-like `filename` from the filesystem encoding and error handler.

    See Also
    --------
    * `os.fsdecode`.

    Version
    -------
    * Python 3.13.
    """
    filename = fspath(filename)

    if isinstance(filename, str):
        return filename

    encoding = getfilesystemencoding()
    errors = getfilesystemencodeerrors()

    return filename.decode(encoding, errors)
