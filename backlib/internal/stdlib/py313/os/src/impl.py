from __future__ import annotations

import os as py_os

from abc import ABC, abstractmethod
from contextlib import suppress
from math import ceil
from sys import getfilesystemencodeerrors, getfilesystemencoding, stdout
from typing import Final, Generic, NamedTuple, TypeVar

from backlib.internal.markers import depends_on, todo
from backlib.internal.typing import AnyStr, Self, TypeAlias
from backlib.internal.utils import alias
from backlib.internal.utils.platform import is_nt, is_posix
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


F_OK: Final[int] = alias.to(py_os.F_OK)
R_OK: Final[int] = alias.to(py_os.R_OK)
W_OK: Final[int] = alias.to(py_os.W_OK)
X_OK: Final[int] = alias.to(py_os.X_OK)


O_APPEND: Final[int] = alias.to(py_os.O_APPEND)
O_CREAT: Final[int] = alias.to(py_os.O_CREAT)
O_EXCL: Final[int] = alias.to(py_os.O_EXCL)
O_RDONLY: Final[int] = alias.to(py_os.O_RDONLY)
O_RDWR: Final[int] = alias.to(py_os.O_RDWR)
O_TRUNC: Final[int] = alias.to(py_os.O_TRUNC)
O_WRONLY: Final[int] = alias.to(py_os.O_WRONLY)


@todo.restore
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


@todo.restore
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


def access(
    path: int | AnyStr | PathLike[AnyStr],
    mode: int,
    *,
    dir_fd: int | None = None,
    effective_ids: bool = False,
    follow_symlinks: bool = True,
) -> bool:
    """Use the real uid / gid to test for access to `path`.

    See Also
    --------
    * `os.access`.

    Version
    -------
    * Python 3.13.
    """
    py_access = alias.to(py_os.access)

    return py_access(
        path=path,
        mode=mode,
        dir_fd=dir_fd,
        effective_ids=effective_ids,
        follow_symlinks=follow_symlinks,
    )


def chdir(path: int | AnyStr | PathLike[AnyStr]) -> None:
    """Change the current working directory to path.

    See Also
    --------
    * `os.chdir`.

    Version
    -------
    * Python 3.13.
    """
    py_chdir = alias.to(py_os.chdir)
    return py_chdir(path)


def close(fd: int) -> None:
    """Close file descriptor `fd`.

    See Also
    --------
    * `os.close`.

    Version
    -------
    * Python 3.13.
    """
    py_close = alias.to(py_os.close)
    return py_close(fd)


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


def fspath(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Return the file system representation of the path.

    See Also
    --------
    * `os.fspath`.

    Version
    -------
    * Python 3.13.
    """
    py_fspath = alias.to(py_os.fspath)
    return py_fspath(path)


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


@depends_on.platform
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
    * This function is available on Unix, not POSIX.
    """
    py_ftruncate = alias.to(py_os.ftruncate)
    return py_ftruncate(fd, length)


def get_inheritable(fd: int, /) -> bool:
    """Get the 'inheritable' flag of the specified file descriptor (a boolean).

    See Also
    --------
    * `os.get_inheritable`.

    Version
    -------
    * Python 3.13.
    """
    py_get_inheritable = alias.to(py_os.get_inheritable)
    return py_get_inheritable(fd)


@depends_on.platform
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
    * This function is available on Unix, not POSIX.
    """
    if fd is None:
        fd = stdout.fileno()

    py_get_terminal_size = alias.to(py_os.get_terminal_size)
    py_terminal_size = py_get_terminal_size(fd)

    return terminal_size(*py_terminal_size)


def getcwd() -> str:
    """Return a string representing the current working directory.

    See Also
    --------
    * `os.getcwd`.

    Version
    -------
    * Python 3.13.
    """
    py_getcwd = alias.to(py_os.getcwd)
    return py_getcwd()


def getcwdb() -> bytes:
    """Return a bytestring representing the current working directory.

    See Also
    --------
    * `os.getcwdb`.

    Version
    -------
    * Python 3.13.
    """
    py_getcwdb = alias.to(py_os.getcwdb)
    return py_getcwdb()


def isatty(fd: int, /) -> bool:
    """Check if the file descriptor `fd` is open and connected to a tty(-like) device.

    See Also
    --------
    * `os.isatty`.

    Version
    -------
    * Python 3.13.
    """
    py_isatty = alias.to(py_os.isatty)
    return py_isatty(fd)


@depends_on.platform
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
    * This function is available on Unix, not POSIX.
    """
    py_link = alias.to(py_os.link)

    return py_link(
        src=src,
        dst=dst,
        src_dir_fd=src_dir_fd,
        dst_dir_fd=dst_dir_fd,
        follow_symlinks=follow_symlinks,
    )


def lseek(fd: int, position: int, whence: int, /) -> int:
    """Set the current position of file descriptor `fd` to position `pos`, modified by `whence`.

    See Also
    --------
    * `os.lseek`.

    Version
    -------
    * Python 3.13.
    """
    py_lseek = alias.to(py_os.lseek)
    return py_lseek(fd, position, whence)


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


def mkdir(path: AnyStr | PathLike[AnyStr], mode: int = 0o777, *, dir_fd: int | None = None) -> None:
    """Create a directory named `path` with numeric mode `mode`.

    See Also
    --------
    * `os.mkdir`.

    Version
    -------
    * Python 3.13.
    """
    py_mkdir = alias.to(py_os.mkdir)
    return py_mkdir(path, mode, dir_fd=dir_fd)


def open(  # noqa: A001
    path: AnyStr | PathLike[AnyStr],
    flags: int,
    mode: int = 0o777,
    *,
    dir_fd: int | None = None,
) -> int:
    """Open the file `path` and set various `flags` and, possibly, its `mode`.

    See Also
    --------
    * `os.open`.

    Version
    -------
    * Python 3.13.
    """
    py_open = alias.to(py_os.open)
    return py_open(path, flags, mode, dir_fd=dir_fd)


def read(fd: int, length: int, /) -> bytes:
    """Read at most `length` bytes from file descriptor `fd`.

    See Also
    --------
    * `os.read`.

    Version
    -------
    * Python 3.13.
    """
    py_read = alias.to(py_os.read)
    return py_read(fd, length)


@depends_on.platform
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
    * This function is available on Unix, not POSIX.
    """
    py_readlink = alias.to(py_os.readlink)
    return py_readlink(path, dir_fd=dir_fd)


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
    """
    py_rename = alias.to(py_os.rename)
    return py_rename(src, dst, src_dir_fd=src_dir_fd, dst_dir_fd=dst_dir_fd)


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
    """
    py_replace = alias.to(py_os.replace)
    return py_replace(src, dst, src_dir_fd=src_dir_fd, dst_dir_fd=dst_dir_fd)


def rmdir(path: AnyStr | PathLike[AnyStr], *, dir_fd: int | None = None) -> None:
    """Remove (delete) the directory `path`.

    See Also
    --------
    * `os.rmdir`.

    Version
    -------
    * Python 3.13.
    """
    py_rmdir = alias.to(py_os.rmdir)
    return py_rmdir(path, dir_fd=dir_fd)


def set_inheritable(fd: int, inheritable: bool, /) -> None:  # noqa: FBT001
    """Set the 'inheritable' flag of the specified file descriptor.

    See Also
    --------
    * `os.set_inheritable`.

    Version
    -------
    * Python 3.13.
    """
    py_set_inheritable = alias.to(py_os.set_inheritable)
    return py_set_inheritable(fd, inheritable)


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
    """
    py_stat = alias.to(py_os.stat)
    st = py_stat(path, dir_fd=dir_fd, follow_symlinks=follow_symlinks)

    return stat_result(
        st_mode=st.st_mode,
        st_ino=st.st_ino,
        st_dev=st.st_dev,
        st_nlink=st.st_nlink,
        st_uid=st.st_uid,
        st_gid=st.st_gid,
        st_size=st.st_size,
        st_atime=st.st_atime,
        st_mtime=st.st_mtime,
        st_ctime=st.st_ctime,
        st_atime_ns=st.st_atime_ns,
        st_mtime_ns=st.st_mtime_ns,
        st_ctime_ns=st.st_ctime_ns,
        st_birthtime=alias.or_default(st, "st_birthtime", otherwise=st.st_ctime),
        st_birthtime_ns=alias.or_default(st, "st_birthtime_ns", otherwise=st.st_ctime_ns),
        st_blocks=alias.or_default(st, "st_blocks", otherwise=ceil(st.st_size / 512)),
        st_blksize=alias.or_default(st, "st_blksize", otherwise=512),
        st_rdev=alias.or_default(st, "st_rdev", otherwise=0),
        st_flags=alias.or_default(st, "st_flags", otherwise=0),
        st_gen=alias.or_default(st, "st_gen", otherwise=0),
        st_fstype=alias.or_default(st, "st_fstype", otherwise=""),
        st_rsize=alias.or_default(st, "st_rsize", otherwise=st.st_size),
        st_creator=alias.or_default(st, "st_creator", otherwise=0),
        st_type=alias.or_default(st, "st_type", otherwise=0),
        st_file_attributes=alias.or_default(st, "st_file_attributes", otherwise=0),
        st_reparse_tag=alias.or_default(st, "st_reparse_tag", otherwise=0),
    )


@depends_on.platform
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
    * This function is available on Unix, not POSIX.
    """
    py_symlink = alias.to(py_os.symlink)
    return py_symlink(src, dst, target_is_directory, dir_fd=dir_fd)


def strerror(code: int, /) -> str:
    """Return the error message corresponding to the error code in `code`.

    See Also
    --------
    * `os.strerror`.

    Version
    -------
    * Python 3.13.
    """
    py_strerror = alias.to(py_os.strerror)
    return py_strerror(code)


def unlink(path: AnyStr | PathLike[AnyStr], *, dir_fd: int | None = None) -> None:
    """Remove (delete) the file path.

    See Also
    --------
    * `os.unlink`.

    Version
    -------
    * Python 3.13.
    """
    py_unlink = alias.to(py_os.unlink)
    return py_unlink(path, dir_fd=dir_fd)


def write(fd: int, data: ReadableBuffer, /) -> int:
    """Write the bytestring in `data` to file descriptor `fd`.

    See Also
    --------
    * `os.write`.

    Version
    -------
    * Python 3.13.
    """
    py_write = alias.to(py_os.write)
    return py_write(fd, data)
