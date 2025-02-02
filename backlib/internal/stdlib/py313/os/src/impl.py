from __future__ import annotations

import os as py_os

from abc import ABC, abstractmethod
from contextlib import suppress
from math import ceil
from sys import getfilesystemencodeerrors, getfilesystemencoding, stdout
from typing import Final, Generic, NamedTuple, TypeVar

from backlib.internal.markers.decorators import techdebt
from backlib.internal.typing import AnyStr, Self, TypeAlias
from backlib.internal.utils.sys import is_nt, is_posix, is_unix
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
    "fstat",
    "ftruncate",
    "get_inheritable",
    "get_terminal_size",
    "getcwd",
    "getcwdb",
    "isatty",
    "linesep",
    "link",
    "lseek",
    "lstat",
    "mkdir",
    "name",
    "open",
    "pardir",
    "pathsep",
    "read",
    "readlink",
    "rename",
    "replace",
    "rmdir",
    "sep",
    "set_inheritable",
    "stat",
    "stat_result",
    "strerror",
    "symlink",
    "terminal_size",
    "unlink",
    "write",
]


if not is_nt() and not techdebt(is_unix()):
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


@techdebt
class stat_result(NamedTuple):  # noqa: N801
    """Object whose attributes correspond roughly to the members of the `stat` structure.

    See Also
    --------
    * `os.stat_result`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * All the attributes should have docstrings;
    * This class is a `NamedTuple`, not `structeq[float]`.
    """

    st_mode: int
    st_ino: int
    st_dev: int
    st_nlink: int
    st_uid: int
    st_gid: int
    st_size: int

    st_atime: float
    st_mtime: float
    st_ctime: float

    st_atime_ns: int
    st_mtime_ns: int
    st_ctime_ns: int

    st_birthtime: float
    st_birthtime_ns: int

    # Unix
    st_blocks: int
    st_blksize: int
    st_rdev: int
    st_flags: int

    # FreeBSD
    st_gen: int

    # Solaris
    st_fstype: str

    # macOS
    st_rsize: int
    st_creator: int
    st_type: int

    # Windows
    st_file_attributes: int
    st_reparse_tag: int


@techdebt
class terminal_size(NamedTuple):  # noqa: N801
    """A subclass of tuple, holding `(columns, lines)` of the terminal window size.

    See Also
    --------
    * `os.terminal_size`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * All the attributes should have docstrings;
    * This class is a `NamedTuple`, not `structeq[int]`.
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


def fstat(fd: int) -> stat_result:
    """Get the status of the file descriptor `fd`.

    See Also
    --------
    * `os.fstat`.

    Version
    -------
    * Python 3.13.
    """
    return stat(fd)


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
    * This function is available on Unix, not POSIX;
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
def get_terminal_size(fd: int | None = None, /) -> terminal_size:
    """Return the size of the terminal window as `(columns, lines)`.

    See Also
    --------
    * `os.get_terminal_size`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is available on Unix, not POSIX;
    * This function is not a real backport.
    """
    if fd is None:
        fd = stdout.fileno()

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
    * This function is available on Unix, not POSIX;
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


def lstat(path: AnyStr | PathLike[AnyStr], *, dir_fd: int | None = None) -> stat_result:
    """Perform the equivalent of an `lstat()` system call on the given path.

    See Also
    --------
    * `os.lstat`.

    Version
    -------
    * Python 3.13.
    """
    return stat(path, dir_fd=dir_fd, follow_symlinks=False)


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
def open(  # noqa: A001
    path: AnyStr | PathLike[AnyStr],
    flags: int,
    mode: int = 0o777,
    *,
    dir_fd: int | None = None,
) -> int:
    """Open the file `path` and set various `flags` and possibly its `mode`.

    See Also
    --------
    * `os.open`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.open(path, flags, mode, dir_fd=dir_fd)


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
    * This function is available on Unix, not POSIX;
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
    """Rename the file or directory `src` to `dst`.

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
def rmdir(path: AnyStr | PathLike[AnyStr], *, dir_fd: int | None = None) -> None:
    """Remove (delete) the directory `path`.

    See Also
    --------
    * `os.rmdir`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.rmdir(path, dir_fd=dir_fd)  # noqa: PTH106


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
def stat(
    path: int | AnyStr | PathLike[AnyStr],
    *,
    dir_fd: int | None = None,
    follow_symlinks: bool = True,
) -> stat_result:
    """Get the status of a file or a file descriptor.

    See Also
    --------
    * `os.stat`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    py_stat_result = py_os.stat(path, dir_fd=dir_fd, follow_symlinks=follow_symlinks)  # noqa: PTH116

    return stat_result(
        st_mode=py_stat_result.st_mode,
        st_ino=py_stat_result.st_ino,
        st_dev=py_stat_result.st_dev,
        st_nlink=py_stat_result.st_nlink,
        st_uid=py_stat_result.st_uid,
        st_gid=py_stat_result.st_gid,
        st_size=py_stat_result.st_size,
        st_atime=py_stat_result.st_atime,
        st_mtime=py_stat_result.st_mtime,
        st_ctime=py_stat_result.st_ctime,
        st_atime_ns=py_stat_result.st_atime_ns,
        st_mtime_ns=py_stat_result.st_mtime_ns,
        st_ctime_ns=py_stat_result.st_ctime_ns,
        st_birthtime=getattr(py_stat_result, "st_birthtime", py_stat_result.st_ctime),
        st_birthtime_ns=getattr(py_stat_result, "st_birthtime_ns", py_stat_result.st_ctime_ns),
        st_blocks=getattr(py_stat_result, "st_blocks", ceil(py_stat_result.st_size / 512)),
        st_blksize=getattr(py_stat_result, "st_blksize", 512),
        st_rdev=getattr(py_stat_result, "st_rdev", 0),
        st_flags=getattr(py_stat_result, "st_flags", 0),
        st_gen=getattr(py_stat_result, "st_gen", 0),
        st_fstype=getattr(py_stat_result, "st_fstype", ""),
        st_rsize=getattr(py_stat_result, "st_rsize", py_stat_result.st_size),
        st_creator=getattr(py_stat_result, "st_creator", 0),
        st_type=getattr(py_stat_result, "st_type", 0),
        st_file_attributes=getattr(py_stat_result, "st_file_attributes", 0),
        st_reparse_tag=getattr(py_stat_result, "st_reparse_tag", 0),
    )


@techdebt
def symlink(
    src: AnyStr | PathLike[AnyStr],
    dst: AnyStr | PathLike[AnyStr],
    target_is_directory: bool = False,  # noqa: FBT001, FBT002
    *,
    dir_fd: int | None = None,
) -> None:
    """Create a symbolic link pointing to `src` named `dst`.

    See Also
    --------
    * `os.symlink`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is available on Unix, not POSIX;
    * This funciton is not a real backport.
    """
    return py_os.symlink(src, dst, target_is_directory, dir_fd=dir_fd)


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
def unlink(path: AnyStr | PathLike[AnyStr], *, dir_fd: int | None = None) -> None:
    """Remove (delete) the file path.

    See Also
    --------
    * `os.unlink`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.unlink(path, dir_fd=dir_fd)  # noqa: PTH108


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
