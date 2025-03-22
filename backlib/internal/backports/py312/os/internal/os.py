from __future__ import annotations

import os as py_os

from typing import TYPE_CHECKING, Final, NamedTuple

from backlib.internal.backports.py311 import os as py311_os
from backlib.internal.backports.py312 import errno
from backlib.internal.backports.py312.os.internal import linux5
from backlib.internal.utils import alias


if TYPE_CHECKING:
    from backlib.internal.backports.py311.os import PathLike


__all__: list[str] = [
    "CLONE_FILES",
    "CLONE_FS",
    "CLONE_NEWCGROUP",
    "CLONE_NEWIPC",
    "CLONE_NEWNET",
    "CLONE_NEWNS",
    "CLONE_NEWPID",
    "CLONE_NEWTIME",
    "CLONE_NEWUSER",
    "CLONE_NEWUTS",
    "CLONE_SIGHAND",
    "CLONE_SYSVSEM",
    "CLONE_THREAD",
    "CLONE_VM",
    "PIDFD_NONBLOCK",
    "fstat",
    "lstat",
    "stat",
    "stat_result",
    "strerror",
    "supports_dir_fd",
    "supports_fd",
    "supports_follow_symlinks",
]

__backlib__: str = "backlib.py312.os"


CLONE_FILES: Final[int] = alias.or_platform(
    py_os,
    "CLONE_FILES",
    linux=linux5.CLONE_FILES,
    otherwise=linux5.CLONE_FILES,
)
CLONE_FS: Final[int] = alias.or_platform(
    py_os,
    "CLONE_FS",
    linux=linux5.CLONE_FS,
    otherwise=linux5.CLONE_FS,
)
CLONE_NEWCGROUP: Final[int] = alias.or_platform(
    py_os,
    "CLONE_NEWCGROUP",
    linux=linux5.CLONE_NEWCGROUP,
    otherwise=linux5.CLONE_NEWCGROUP,
)
CLONE_NEWIPC: Final[int] = alias.or_platform(
    py_os,
    "CLONE_NEWIPC",
    linux=linux5.CLONE_NEWIPC,
    otherwise=linux5.CLONE_NEWIPC,
)
CLONE_NEWNET: Final[int] = alias.or_platform(
    py_os,
    "CLONE_NEWNET",
    linux=linux5.CLONE_NEWNET,
    otherwise=linux5.CLONE_NEWNET,
)
CLONE_NEWNS: Final[int] = alias.or_platform(
    py_os,
    "CLONE_NEWNS",
    linux=linux5.CLONE_NEWNS,
    otherwise=linux5.CLONE_NEWNS,
)
CLONE_NEWPID: Final[int] = alias.or_platform(
    py_os,
    "CLONE_NEWPID",
    linux=linux5.CLONE_NEWPID,
    otherwise=linux5.CLONE_NEWPID,
)
CLONE_NEWTIME: Final[int] = alias.or_platform(
    py_os,
    "CLONE_NEWTIME",
    linux=linux5.CLONE_NEWTIME,
    otherwise=linux5.CLONE_NEWTIME,
)
CLONE_NEWUSER: Final[int] = alias.or_platform(
    py_os,
    "CLONE_NEWUSER",
    linux=linux5.CLONE_NEWUSER,
    otherwise=linux5.CLONE_NEWUSER,
)
CLONE_NEWUTS: Final[int] = alias.or_platform(
    py_os,
    "CLONE_NEWUTS",
    linux=linux5.CLONE_NEWUTS,
    otherwise=linux5.CLONE_NEWUTS,
)
CLONE_SIGHAND: Final[int] = alias.or_platform(
    py_os,
    "CLONE_SIGHAND",
    linux=linux5.CLONE_SIGHAND,
    otherwise=linux5.CLONE_SIGHAND,
)
CLONE_SYSVSEM: Final[int] = alias.or_platform(
    py_os,
    "CLONE_SYSVSEM",
    linux=linux5.CLONE_SYSVSEM,
    otherwise=linux5.CLONE_SYSVSEM,
)
CLONE_THREAD: Final[int] = alias.or_platform(
    py_os,
    "CLONE_THREAD",
    linux=linux5.CLONE_THREAD,
    otherwise=linux5.CLONE_THREAD,
)
CLONE_VM: Final[int] = alias.or_platform(
    py_os,
    "CLONE_VM",
    linux=linux5.CLONE_VM,
    otherwise=linux5.CLONE_VM,
)

PIDFD_NONBLOCK: Final[int] = alias.or_platform(
    py_os,
    "PIDFD_NONBLOCK",
    linux=linux5.PIDFD_NONBLOCK,
    otherwise=linux5.PIDFD_NONBLOCK,
)


class stat_result(NamedTuple):
    """Object whose attributes correspond roughly to the members of the `stat` structure.

    See Also
    --------
    * `os.stat_result`.
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


def stat(
    path: int | str | bytes | PathLike[str] | PathLike[bytes],
    *,
    dir_fd: int | None = None,
    follow_symlinks: bool = True,
) -> stat_result:
    """Get the status of a file or a file descriptor.

    See Also
    --------
    * `os.stat`.
    """
    st = py311_os.stat(path, dir_fd=dir_fd, follow_symlinks=follow_symlinks)

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
        st_birthtime=st.st_birthtime,
        st_birthtime_ns=alias.or_default(st, "st_birthtime_ns", otherwise=st.st_ctime_ns),
        st_blocks=st.st_blocks,
        st_blksize=st.st_blksize,
        st_rdev=st.st_rdev,
        st_flags=st.st_flags,
        st_gen=st.st_gen,
        st_fstype=st.st_fstype,
        st_rsize=st.st_rsize,
        st_creator=st.st_creator,
        st_type=st.st_type,
        st_file_attributes=st.st_file_attributes,
        st_reparse_tag=st.st_reparse_tag,
    )


def fstat(fd: int) -> stat_result:
    """Get the status of the file descriptor `fd`.

    See Also
    --------
    * `os.fstat`.
    """
    return stat(fd)


def lstat(
    path: str | bytes | PathLike[str] | PathLike[bytes],
    *,
    dir_fd: int | None = None,
) -> stat_result:
    """Perform the equivalent of an `lstat()` system call on the given path.

    See Also
    --------
    * `os.lstat`.
    """
    return stat(path, dir_fd=dir_fd, follow_symlinks=False)


def strerror(code: int, /) -> str:
    """Return the error message corresponding to the error code in `code`.

    See Also
    --------
    * `os.strerror`.
    """
    if code == errno.ENOTCAPABLE:
        return "Capabilities insufficient"

    if code == errno.EQFULL:
        return "Interface output queue is full"

    return py311_os.strerror(code)


supports_dir_fd = py311_os.supports_dir_fd.copy()

if py311_os.stat in py311_os.supports_dir_fd:
    supports_dir_fd.add(stat)


supports_fd = py311_os.supports_fd.copy()

if py311_os.stat in py311_os.supports_fd:
    supports_fd.add(stat)

if py311_os.lstat in py311_os.supports_fd:
    supports_fd.add(lstat)


supports_follow_symlinks = py311_os.supports_follow_symlinks.copy()

if py311_os.stat in py311_os.supports_follow_symlinks:
    supports_follow_symlinks.add(stat)


fstat.__module__ = __backlib__
lstat.__module__ = __backlib__
stat.__module__ = __backlib__
stat_result.__module__ = __backlib__
strerror.__module__ = __backlib__
