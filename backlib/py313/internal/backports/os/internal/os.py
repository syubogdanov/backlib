from __future__ import annotations

import os as py_os

from math import ceil
from typing import Final, NamedTuple, TypeVar

from backlib.py313.internal.backports.os.internal import linux5
from backlib.py313.internal.markers import techdebt
from backlib.py313.internal.utils import alias


__all__: list[str] = [
    "CLD_CONTINUED",
    "CLD_DUMPED",
    "CLD_EXITED",
    "CLD_KILLED",
    "CLD_STOPPED",
    "CLD_TRAPPED",
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
    "EFD_CLOEXEC",
    "EFD_NONBLOCK",
    "EFD_SEMAPHORE",
    "F_LOCK",
    "F_OK",
    "F_TEST",
    "F_TLOCK",
    "F_ULOCK",
    "GRND_NONBLOCK",
    "GRND_RANDOM",
    "MFD_ALLOW_SEALING",
    "MFD_CLOEXEC",
    "MFD_HUGETLB",
    "MFD_HUGE_1GB",
    "MFD_HUGE_1MB",
    "MFD_HUGE_2GB",
    "MFD_HUGE_2MB",
    "MFD_HUGE_8MB",
    "MFD_HUGE_16GB",
    "MFD_HUGE_16MB",
    "MFD_HUGE_32MB",
    "MFD_HUGE_64KB",
    "MFD_HUGE_256MB",
    "MFD_HUGE_512KB",
    "MFD_HUGE_512MB",
    "MFD_HUGE_MASK",
    "MFD_HUGE_SHIFT",
    "O_APPEND",
    "O_ASYNC",
    "O_CLOEXEC",
    "O_CREAT",
    "O_DIRECT",
    "O_DIRECTORY",
    "O_DSYNC",
    "O_EXCL",
    "O_NDELAY",
    "O_NOATIME",
    "O_NOCTTY",
    "O_NOFOLLOW",
    "O_NONBLOCK",
    "O_PATH",
    "O_RDONLY",
    "O_RDWR",
    "O_RSYNC",
    "O_SYNC",
    "O_TMPFILE",
    "O_TRUNC",
    "O_WRONLY",
    "PIDFD_NONBLOCK",
    "POSIX_FADV_DONTNEED",
    "POSIX_FADV_NOREUSE",
    "POSIX_FADV_NORMAL",
    "POSIX_FADV_RANDOM",
    "POSIX_FADV_SEQUENTIAL",
    "POSIX_FADV_WILLNEED",
    "PRIO_PGRP",
    "PRIO_PROCESS",
    "PRIO_USER",
    "P_ALL",
    "P_PGID",
    "P_PID",
    "P_PIDFD",
    "RTLD_DEEPBIND",
    "RTLD_GLOBAL",
    "RTLD_LAZY",
    "RTLD_LOCAL",
    "RTLD_NODELETE",
    "RTLD_NOLOAD",
    "RTLD_NOW",
    "RWF_APPEND",
    "RWF_DSYNC",
    "RWF_HIPRI",
    "RWF_NOWAIT",
    "RWF_SYNC",
    "R_OK",
    "SCHED_BATCH",
    "SCHED_FIFO",
    "SCHED_IDLE",
    "SCHED_OTHER",
    "SCHED_RESET_ON_FORK",
    "SCHED_RR",
    "SEEK_CUR",
    "SEEK_DATA",
    "SEEK_END",
    "SEEK_HOLE",
    "SEEK_SET",
    "SPLICE_F_MORE",
    "SPLICE_F_MOVE",
    "SPLICE_F_NONBLOCK",
    "TFD_CLOEXEC",
    "TFD_NONBLOCK",
    "TFD_TIMER_ABSTIME",
    "TFD_TIMER_CANCEL_ON_SET",
    "WCONTINUED",
    "WEXITED",
    "WNOHANG",
    "WNOWAIT",
    "WSTOPPED",
    "WUNTRACED",
    "W_OK",
    "XATTR_CREATE",
    "XATTR_REPLACE",
    "X_OK",
    "DirEntry",
    "PathLike",
    "abort",
    "access",
    "altsep",
    "chdir",
    "chmod",
    "close",
    "closerange",
    "cpu_count",
    "curdir",
    "defpath",
    "device_encoding",
    "devnull",
    "environ",
    "environb",
    "error",
    "extsep",
    "fchdir",
    "fchmod",
    "fdopen",
    "fsdecode",
    "fsencode",
    "fspath",
    "fstat",
    "fsync",
    "ftruncate",
    "get_blocking",
    "get_exec_path",
    "get_inheritable",
    "get_terminal_size",
    "getcwd",
    "getcwdb",
    "getpid",
    "getppid",
    "isatty",
    "linesep",
    "link",
    "listdir",
    "lseek",
    "lstat",
    "major",
    "makedev",
    "makedirs",
    "minor",
    "mkdir",
    "name",
    "open",
    "pardir",
    "pathsep",
    "pipe",
    "process_cpu_count",
    "putenv",
    "read",
    "readlink",
    "remove",
    "removedirs",
    "rename",
    "renames",
    "replace",
    "rmdir",
    "scandir",
    "sep",
    "set_blocking",
    "set_inheritable",
    "stat",
    "stat_result",
    "strerror",
    "supports_bytes_environ",
    "supports_dir_fd",
    "supports_effective_ids",
    "supports_fd",
    "supports_follow_symlinks",
    "symlink",
    "terminal_size",
    "times",
    "truncate",
    "umask",
    "unlink",
    "unsetenv",
    "urandom",
    "utime",
    "walk",
    "write",
]

__backlib__: str = "backlib.py313.os"


AnyStr = TypeVar("AnyStr", str, bytes)


# ---
# Version: Python 3.9+
# Explain: Available on Unix (not WASI).
# ---

PRIO_PROCESS: Final[int] = alias.or_platform(
    py_os,
    "PRIO_PROCESS",
    linux=linux5.PRIO_PROCESS,
    otherwise=linux5.PRIO_PROCESS,
)
PRIO_PGRP: Final[int] = alias.or_platform(
    py_os,
    "PRIO_PGRP",
    linux=linux5.PRIO_PGRP,
    otherwise=linux5.PRIO_PGRP,
)
PRIO_USER: Final[int] = alias.or_platform(
    py_os,
    "PRIO_USER",
    linux=linux5.PRIO_USER,
    otherwise=linux5.PRIO_USER,
)


# ---
# Version: Python 3.9+
# Explain: Available on Unix.
# ---

F_LOCK: Final[int] = alias.or_platform(
    py_os,
    "F_LOCK",
    linux=linux5.F_LOCK,
    otherwise=linux5.F_LOCK,
)
F_TLOCK: Final[int] = alias.or_platform(
    py_os,
    "F_TLOCK",
    linux=linux5.F_TLOCK,
    otherwise=linux5.F_TLOCK,
)
F_ULOCK: Final[int] = alias.or_platform(
    py_os,
    "F_ULOCK",
    linux=linux5.F_ULOCK,
    otherwise=linux5.F_ULOCK,
)
F_TEST: Final[int] = alias.or_platform(
    py_os,
    "F_TEST",
    linux=linux5.F_TEST,
    otherwise=linux5.F_TEST,
)

O_DSYNC: Final[int] = alias.or_platform(
    py_os,
    "O_DSYNC",
    linux=linux5.O_DSYNC,
    otherwise=linux5.O_DSYNC,
)
O_RSYNC: Final[int] = alias.or_platform(
    py_os,
    "O_RSYNC",
    linux=linux5.O_RSYNC,
    otherwise=linux5.O_RSYNC,
)
O_SYNC: Final[int] = alias.or_platform(
    py_os,
    "O_SYNC",
    linux=linux5.O_SYNC,
    otherwise=linux5.O_SYNC,
)
O_NONBLOCK: Final[int] = alias.or_platform(
    py_os,
    "O_NONBLOCK",
    linux=linux5.O_NONBLOCK,
    otherwise=linux5.O_NONBLOCK,
)
O_NOCTTY: Final[int] = alias.or_platform(
    py_os,
    "O_NOCTTY",
    linux=linux5.O_NOCTTY,
    otherwise=linux5.O_NOCTTY,
)

O_CLOEXEC: Final[int] = alias.or_platform(
    py_os,
    "O_CLOEXEC",
    linux=linux5.O_CLOEXEC,
    otherwise=linux5.O_CLOEXEC,
)
O_NDELAY: Final[int] = alias.or_platform(
    py_os,
    "O_NDELAY",
    linux=linux5.O_NDELAY,
    otherwise=linux5.O_NDELAY,
)

POSIX_FADV_NORMAL: Final[int] = alias.or_platform(
    py_os,
    "POSIX_FADV_NORMAL",
    linux=linux5.POSIX_FADV_NORMAL,
    otherwise=linux5.POSIX_FADV_NORMAL,
)
POSIX_FADV_SEQUENTIAL: Final[int] = alias.or_platform(
    py_os,
    "POSIX_FADV_SEQUENTIAL",
    linux=linux5.POSIX_FADV_SEQUENTIAL,
    otherwise=linux5.POSIX_FADV_SEQUENTIAL,
)
POSIX_FADV_RANDOM: Final[int] = alias.or_platform(
    py_os,
    "POSIX_FADV_RANDOM",
    linux=linux5.POSIX_FADV_RANDOM,
    otherwise=linux5.POSIX_FADV_RANDOM,
)
POSIX_FADV_NOREUSE: Final[int] = alias.or_platform(
    py_os,
    "POSIX_FADV_NOREUSE",
    linux=linux5.POSIX_FADV_NOREUSE,
    otherwise=linux5.POSIX_FADV_NOREUSE,
)
POSIX_FADV_WILLNEED: Final[int] = alias.or_platform(
    py_os,
    "POSIX_FADV_WILLNEED",
    linux=linux5.POSIX_FADV_WILLNEED,
    otherwise=linux5.POSIX_FADV_WILLNEED,
)
POSIX_FADV_DONTNEED: Final[int] = alias.or_platform(
    py_os,
    "POSIX_FADV_DONTNEED",
    linux=linux5.POSIX_FADV_DONTNEED,
    otherwise=linux5.POSIX_FADV_DONTNEED,
)

SCHED_OTHER: Final[int] = alias.or_platform(
    py_os,
    "SCHED_OTHER",
    linux=linux5.SCHED_OTHER,
    otherwise=linux5.SCHED_OTHER,
)
SCHED_FIFO: Final[int] = alias.or_platform(
    py_os,
    "SCHED_FIFO",
    linux=linux5.SCHED_FIFO,
    otherwise=linux5.SCHED_FIFO,
)
SCHED_RR: Final[int] = alias.or_platform(
    py_os,
    "SCHED_RR",
    linux=linux5.SCHED_RR,
    otherwise=linux5.SCHED_RR,
)
SCHED_BATCH: Final[int] = alias.or_platform(
    py_os,
    "SCHED_BATCH",
    linux=linux5.SCHED_BATCH,
    otherwise=linux5.SCHED_BATCH,
)
SCHED_IDLE: Final[int] = alias.or_platform(
    py_os,
    "SCHED_IDLE",
    linux=linux5.SCHED_IDLE,
    otherwise=linux5.SCHED_IDLE,
)
SCHED_RESET_ON_FORK: Final[int] = alias.or_platform(
    py_os,
    "SCHED_RESET_ON_FORK",
    linux=linux5.SCHED_RESET_ON_FORK,
    otherwise=linux5.SCHED_RESET_ON_FORK,
)

RTLD_LOCAL: Final[int] = alias.or_platform(
    py_os,
    "RTLD_LOCAL",
    linux=linux5.RTLD_LOCAL,
    otherwise=linux5.RTLD_LOCAL,
)
RTLD_LAZY: Final[int] = alias.or_platform(
    py_os,
    "RTLD_LAZY",
    linux=linux5.RTLD_LAZY,
    otherwise=linux5.RTLD_LAZY,
)

RTLD_NOW: Final[int] = alias.or_platform(
    py_os,
    "RTLD_NOW",
    linux=linux5.RTLD_NOW,
    otherwise=linux5.RTLD_NOW,
)
RTLD_NOLOAD: Final[int] = alias.or_platform(
    py_os,
    "RTLD_NOLOAD",
    linux=linux5.RTLD_NOLOAD,
    otherwise=linux5.RTLD_NOLOAD,
)
RTLD_DEEPBIND: Final[int] = alias.or_platform(
    py_os,
    "RTLD_DEEPBIND",
    linux=linux5.RTLD_DEEPBIND,
    otherwise=linux5.RTLD_DEEPBIND,
)
RTLD_GLOBAL: Final[int] = alias.or_platform(
    py_os,
    "RTLD_GLOBAL",
    linux=linux5.RTLD_GLOBAL,
    otherwise=linux5.RTLD_GLOBAL,
)
RTLD_NODELETE: Final[int] = alias.or_platform(
    py_os,
    "RTLD_NODELETE",
    linux=linux5.RTLD_NODELETE,
    otherwise=linux5.RTLD_NODELETE,
)


# ---
# Version: Python 3.9+
# Explain: Available on Linux >= 3.1, macOS, Unix.
# ---

SEEK_HOLE: Final[int] = alias.or_platform(
    py_os,
    "SEEK_HOLE",
    linux=linux5.SEEK_HOLE,
    otherwise=linux5.SEEK_HOLE,
)
SEEK_DATA: Final[int] = alias.or_platform(
    py_os,
    "SEEK_DATA",
    linux=linux5.SEEK_DATA,
    otherwise=linux5.SEEK_DATA,
)


# ---
# Version: Python 3.9+
# Explain: Available on Unix, Windows.
# ---

O_RDONLY: Final[int] = alias.or_platform(
    py_os,
    "O_RDONLY",
    linux=linux5.O_RDONLY,
    otherwise=linux5.O_RDONLY,
)
O_WRONLY: Final[int] = alias.or_platform(
    py_os,
    "O_WRONLY",
    linux=linux5.O_WRONLY,
    otherwise=linux5.O_WRONLY,
)
O_RDWR: Final[int] = alias.or_platform(
    py_os,
    "O_RDWR",
    linux=linux5.O_RDWR,
    otherwise=linux5.O_RDWR,
)
O_APPEND: Final[int] = alias.or_platform(
    py_os,
    "O_APPEND",
    linux=linux5.O_APPEND,
    otherwise=linux5.O_APPEND,
)
O_CREAT: Final[int] = alias.or_platform(
    py_os,
    "O_CREAT",
    linux=linux5.O_CREAT,
    otherwise=linux5.O_CREAT,
)
O_EXCL: Final[int] = alias.or_platform(
    py_os,
    "O_EXCL",
    linux=linux5.O_EXCL,
    otherwise=linux5.O_EXCL,
)
O_TRUNC: Final[int] = alias.or_platform(
    py_os,
    "O_TRUNC",
    linux=linux5.O_TRUNC,
    otherwise=linux5.O_TRUNC,
)


# ---
# Version: Python 3.9+
# Explain: May be incomplete.
# ---

@techdebt.simplified
class stat_result(NamedTuple):  # noqa: N801
    """Object whose attributes correspond roughly to the members of the `stat` structure.

    See Also
    --------
    * `os.stat_result`.

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
    """
    st = py_os.stat(path, dir_fd=dir_fd, follow_symlinks=follow_symlinks)  # noqa: PTH116

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


def fstat(fd: int) -> stat_result:
    """Get the status of the file descriptor `fd`.

    See Also
    --------
    * `os.fstat`.
    """
    return stat(fd)


def lstat(path: AnyStr | PathLike[AnyStr], *, dir_fd: int | None = None) -> stat_result:
    """Perform the equivalent of an `lstat()` system call on the given path.

    See Also
    --------
    * `os.lstat`.
    """
    return stat(path, dir_fd=dir_fd, follow_symlinks=False)


stat_result.__module__ = __backlib__

stat.__module__ = __backlib__
fstat.__module__ = __backlib__
lstat.__module__ = __backlib__


# ---
# Version: Python 3.9+
# Explain: May be undefined by the C library.
# ---

O_ASYNC: Final[int] = alias.or_platform(
    py_os,
    "O_ASYNC",
    linux=linux5.O_ASYNC,
    otherwise=linux5.O_ASYNC,
)
O_DIRECT: Final[int] = alias.or_platform(
    py_os,
    "O_DIRECT",
    linux=linux5.O_DIRECT,
    otherwise=linux5.O_DIRECT,
)
O_DIRECTORY: Final[int] = alias.or_platform(
    py_os,
    "O_DIRECTORY",
    linux=linux5.O_DIRECTORY,
    otherwise=linux5.O_DIRECTORY,
)
O_NOFOLLOW: Final[int] = alias.or_platform(
    py_os,
    "O_NOFOLLOW",
    linux=linux5.O_NOFOLLOW,
    otherwise=linux5.O_NOFOLLOW,
)

O_NOATIME: Final[int] = alias.or_platform(
    py_os,
    "O_NOATIME",
    linux=linux5.O_NOATIME,
    otherwise=linux5.O_NOATIME,
)
O_PATH: Final[int] = alias.or_platform(
    py_os,
    "O_PATH",
    linux=linux5.O_PATH,
    otherwise=linux5.O_PATH,
)
O_TMPFILE: Final[int] = alias.or_platform(
    py_os,
    "O_TMPFILE",
    linux=linux5.O_TMPFILE,
    otherwise=linux5.O_TMPFILE,
)


# ---
# Version: Python 3.9+
# Explain: Available on Linux >= 4.14.
# ---

RWF_NOWAIT: Final[int] = alias.or_platform(
    py_os,
    "RWF_NOWAIT",
    linux=linux5.RWF_NOWAIT,
    otherwise=linux5.RWF_NOWAIT,
)


# ---
# Version: Python 3.9+
# Explain: Available on Linux >= 4.6.
# ---

RWF_HIPRI: Final[int] = alias.or_platform(
    py_os,
    "RWF_HIPRI",
    linux=linux5.RWF_HIPRI,
    otherwise=linux5.RWF_HIPRI,
)


# ---
# Version: Python 3.9+
# Explain: Available on Linux >= 4.7.
# ---

RWF_DSYNC: Final[int] = alias.or_platform(
    py_os,
    "RWF_DSYNC",
    linux=linux5.RWF_DSYNC,
    otherwise=linux5.RWF_DSYNC,
)
RWF_SYNC: Final[int] = alias.or_platform(
    py_os,
    "RWF_SYNC",
    linux=linux5.RWF_SYNC,
    otherwise=linux5.RWF_SYNC,
)


# ---
# Version: Python 3.9+
# Explain: Available on Linux >= 3.17 with glibc >= 2.27.
# ---

MFD_CLOEXEC: Final[int] = alias.or_platform(
    py_os,
    "MFD_CLOEXEC",
    linux=linux5.MFD_CLOEXEC,
    otherwise=linux5.MFD_CLOEXEC,
)
MFD_ALLOW_SEALING: Final[int] = alias.or_platform(
    py_os,
    "MFD_ALLOW_SEALING",
    linux=linux5.MFD_ALLOW_SEALING,
    otherwise=linux5.MFD_ALLOW_SEALING,
)
MFD_HUGETLB: Final[int] = alias.or_platform(
    py_os,
    "MFD_HUGETLB",
    linux=linux5.MFD_HUGETLB,
    otherwise=linux5.MFD_HUGETLB,
)

MFD_HUGE_SHIFT: Final[int] = alias.or_platform(
    py_os,
    "MFD_HUGE_SHIFT",
    linux=linux5.MFD_HUGE_SHIFT,
    otherwise=linux5.MFD_HUGE_SHIFT,
)
MFD_HUGE_MASK: Final[int] = alias.or_platform(
    py_os,
    "MFD_HUGE_MASK",
    linux=linux5.MFD_HUGE_MASK,
    otherwise=linux5.MFD_HUGE_MASK,
)

MFD_HUGE_64KB: Final[int] = alias.or_platform(
    py_os,
    "MFD_HUGE_64KB",
    linux=linux5.MFD_HUGE_64KB,
    otherwise=linux5.MFD_HUGE_64KB,
)
MFD_HUGE_512KB: Final[int] = alias.or_platform(
    py_os,
    "MFD_HUGE_512KB",
    linux=linux5.MFD_HUGE_512KB,
    otherwise=linux5.MFD_HUGE_512KB,
)
MFD_HUGE_1MB: Final[int] = alias.or_platform(
    py_os,
    "MFD_HUGE_1MB",
    linux=linux5.MFD_HUGE_1MB,
    otherwise=linux5.MFD_HUGE_1MB,
)
MFD_HUGE_2MB: Final[int] = alias.or_platform(
    py_os,
    "MFD_HUGE_2MB",
    linux=linux5.MFD_HUGE_2MB,
    otherwise=linux5.MFD_HUGE_2MB,
)
MFD_HUGE_8MB: Final[int] = alias.or_platform(
    py_os,
    "MFD_HUGE_8MB",
    linux=linux5.MFD_HUGE_8MB,
    otherwise=linux5.MFD_HUGE_8MB,
)
MFD_HUGE_16MB: Final[int] = alias.or_platform(
    py_os,
    "MFD_HUGE_16MB",
    linux=linux5.MFD_HUGE_16MB,
    otherwise=linux5.MFD_HUGE_16MB,
)
MFD_HUGE_32MB: Final[int] = alias.or_platform(
    py_os,
    "MFD_HUGE_32MB",
    linux=linux5.MFD_HUGE_32MB,
    otherwise=linux5.MFD_HUGE_32MB,
)
MFD_HUGE_256MB: Final[int] = alias.or_platform(
    py_os,
    "MFD_HUGE_256MB",
    linux=linux5.MFD_HUGE_256MB,
    otherwise=linux5.MFD_HUGE_256MB,
)
MFD_HUGE_512MB: Final[int] = alias.or_platform(
    py_os,
    "MFD_HUGE_512MB",
    linux=linux5.MFD_HUGE_512MB,
    otherwise=linux5.MFD_HUGE_512MB,
)
MFD_HUGE_1GB: Final[int] = alias.or_platform(
    py_os,
    "MFD_HUGE_1GB",
    linux=linux5.MFD_HUGE_1GB,
    otherwise=linux5.MFD_HUGE_1GB,
)
MFD_HUGE_2GB: Final[int] = alias.or_platform(
    py_os,
    "MFD_HUGE_2GB",
    linux=linux5.MFD_HUGE_2GB,
    otherwise=linux5.MFD_HUGE_2GB,
)
MFD_HUGE_16GB: Final[int] = alias.or_platform(
    py_os,
    "MFD_HUGE_16GB",
    linux=linux5.MFD_HUGE_16GB,
    otherwise=linux5.MFD_HUGE_16GB,
)


# ---
# Version: Python 3.9+
# Explain: Available on Linux.
# ---

XATTR_CREATE: Final[int] = alias.or_platform(
    py_os,
    "XATTR_CREATE",
    linux=linux5.XATTR_CREATE,
    otherwise=linux5.XATTR_CREATE,
)
XATTR_REPLACE: Final[int] = alias.or_platform(
    py_os,
    "XATTR_REPLACE",
    linux=linux5.XATTR_REPLACE,
    otherwise=linux5.XATTR_REPLACE,
)

GRND_NONBLOCK: Final[int] = alias.or_platform(
    py_os,
    "GRND_NONBLOCK",
    linux=linux5.GRND_NONBLOCK,
    otherwise=linux5.GRND_NONBLOCK,
)
GRND_RANDOM: Final[int] = alias.or_platform(
    py_os,
    "GRND_RANDOM",
    linux=linux5.GRND_RANDOM,
    otherwise=linux5.GRND_RANDOM,
)

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


# ---
# Version: Python 3.9+
# Explain: Available on Unix, not WASI, not Android, not iOS.
# ---

P_PID: Final[int] = alias.or_platform(py_os, "P_PID", linux=linux5.P_PID, otherwise=linux5.P_PID)
P_PGID: Final[int] = alias.or_platform(
    py_os,
    "P_PGID",
    linux=linux5.P_PGID,
    otherwise=linux5.P_PGID,
)
P_ALL: Final[int] = alias.or_platform(py_os, "P_ALL", linux=linux5.P_ALL, otherwise=linux5.P_ALL)
P_PIDFD: Final[int] = alias.or_platform(
    py_os,
    "P_PIDFD",
    linux=linux5.P_PIDFD,
    otherwise=linux5.P_PIDFD,
)

WCONTINUED: Final[int] = alias.or_platform(
    py_os,
    "WCONTINUED",
    linux=linux5.WCONTINUED,
    otherwise=linux5.WCONTINUED,
)
WEXITED: Final[int] = alias.or_platform(
    py_os,
    "WEXITED",
    linux=linux5.WEXITED,
    otherwise=linux5.WEXITED,
)
WUNTRACED: Final[int] = alias.or_platform(
    py_os,
    "WUNTRACED",
    linux=linux5.WUNTRACED,
    otherwise=linux5.WUNTRACED,
)
WSTOPPED: Final[int] = alias.or_platform(
    py_os,
    "WSTOPPED",
    linux=linux5.WSTOPPED,
    otherwise=linux5.WSTOPPED,
)
WNOHANG: Final[int] = alias.or_platform(
    py_os,
    "WNOHANG",
    linux=linux5.WNOHANG,
    otherwise=linux5.WNOHANG,
)
WNOWAIT: Final[int] = alias.or_platform(
    py_os,
    "WNOWAIT",
    linux=linux5.WNOWAIT,
    otherwise=linux5.WNOWAIT,
)

CLD_EXITED: Final[int] = alias.or_platform(
    py_os,
    "CLD_EXITED",
    linux=linux5.CLD_EXITED,
    otherwise=linux5.CLD_EXITED,
)
CLD_KILLED: Final[int] = alias.or_platform(
    py_os,
    "CLD_KILLED",
    linux=linux5.CLD_KILLED,
    otherwise=linux5.CLD_KILLED,
)
CLD_DUMPED: Final[int] = alias.or_platform(
    py_os,
    "CLD_DUMPED",
    linux=linux5.CLD_DUMPED,
    otherwise=linux5.CLD_DUMPED,
)
CLD_TRAPPED: Final[int] = alias.or_platform(
    py_os,
    "CLD_TRAPPED",
    linux=linux5.CLD_TRAPPED,
    otherwise=linux5.CLD_TRAPPED,
)
CLD_STOPPED: Final[int] = alias.or_platform(
    py_os,
    "CLD_STOPPED",
    linux=linux5.CLD_STOPPED,
    otherwise=linux5.CLD_STOPPED,
)
CLD_CONTINUED: Final[int] = alias.or_platform(
    py_os,
    "CLD_CONTINUED",
    linux=linux5.CLD_CONTINUED,
    otherwise=linux5.CLD_CONTINUED,
)


# ---
# Version: Python 3.10+
# Explain: Available on Linux >= 4.16.
# ---

RWF_APPEND: Final[int] = alias.or_platform(
    py_os,
    "RWF_APPEND",
    linux=linux5.RWF_APPEND,
    otherwise=linux5.RWF_APPEND,
)

# ---
# Version: Python 3.10+
# Explain: Available on Linux >= 2.6.17 with glibc >= 2.5.
# ---

SPLICE_F_MOVE: Final[int] = alias.or_platform(
    py_os,
    "SPLICE_F_MOVE",
    linux=linux5.SPLICE_F_MOVE,
    otherwise=linux5.SPLICE_F_MOVE,
)
SPLICE_F_NONBLOCK: Final[int] = alias.or_platform(
    py_os,
    "SPLICE_F_NONBLOCK",
    linux=linux5.SPLICE_F_NONBLOCK,
    otherwise=linux5.SPLICE_F_NONBLOCK,
)
SPLICE_F_MORE: Final[int] = alias.or_platform(
    py_os,
    "SPLICE_F_MORE",
    linux=linux5.SPLICE_F_MORE,
    otherwise=linux5.SPLICE_F_MORE,
)

# ---
# Version: Python 3.10+
# Explain: Available on Linux >= 2.6.27.
# ---

EFD_CLOEXEC: Final[int] = alias.or_platform(
    py_os,
    "EFD_CLOEXEC",
    linux=linux5.EFD_CLOEXEC,
    otherwise=linux5.EFD_CLOEXEC,
)
EFD_NONBLOCK: Final[int] = alias.or_platform(
    py_os,
    "EFD_NONBLOCK",
    linux=linux5.EFD_NONBLOCK,
    otherwise=linux5.EFD_NONBLOCK,
)

# ---
# Version: Python 3.10+
# Explain: Available on Linux >= 2.6.30.
# ---

EFD_SEMAPHORE: Final[int] = alias.or_platform(
    py_os,
    "EFD_SEMAPHORE",
    linux=linux5.EFD_SEMAPHORE,
    otherwise=linux5.EFD_SEMAPHORE,
)


# ---
# Version: Python 3.12+
# Explain: Available on Linux >= 5.10.
# ---

PIDFD_NONBLOCK: Final[int] = alias.or_platform(
    py_os,
    "PIDFD_NONBLOCK",
    linux=linux5.PIDFD_NONBLOCK,
    otherwise=linux5.PIDFD_NONBLOCK,
)

# ---
# Version: Python 3.13+
# Explain: Available on Linux >= 2.6.27 with glibc >= 2.8.
# ---

TFD_NONBLOCK: Final[int] = alias.or_platform(
    py_os,
    "TFD_NONBLOCK",
    linux=linux5.TFD_NONBLOCK,
    otherwise=linux5.TFD_NONBLOCK,
)
TFD_CLOEXEC: Final[int] = alias.or_platform(
    py_os,
    "TFD_CLOEXEC",
    linux=linux5.TFD_CLOEXEC,
    otherwise=linux5.TFD_CLOEXEC,
)
TFD_TIMER_ABSTIME: Final[int] = alias.or_platform(
    py_os,
    "TFD_TIMER_ABSTIME",
    linux=linux5.TFD_TIMER_ABSTIME,
    otherwise=linux5.TFD_TIMER_ABSTIME,
)
TFD_TIMER_CANCEL_ON_SET: Final[int] = alias.or_platform(
    py_os,
    "TFD_TIMER_CANCEL_ON_SET",
    linux=linux5.TFD_TIMER_CANCEL_ON_SET,
    otherwise=linux5.TFD_TIMER_CANCEL_ON_SET,
)


# ---
# Version: Python 3.13+
# Explain: Changed in Python 3.13.
# ---

def cpu_count() -> int | None:
    """Return the number of logical CPUs in the system.

    See Also
    --------
    * `os.cpu_count`.
    """
    if count := environ.get("PYTHON_CPU_COUNT"):
        return int(count)
    return py_os.cpu_count()


@techdebt.simplified
def process_cpu_count() -> int | None:
    """Get the number of logical CPUs usable by the calling thread of the current process.

    See Also
    --------
    * `os.process_cpu_count`.

    Technical Debt
    --------------
    * This is an alias to `cpu_count`.
    """
    return cpu_count()


cpu_count.__module__ = __backlib__
process_cpu_count.__module__ = __backlib__


# ---
# Version: Python 3.9+
# Explain: No changes required.
# ---

error = py_os.error

curdir = py_os.curdir
pardir = py_os.pardir
extsep = py_os.extsep

name = py_os.name
linesep = py_os.linesep

sep = py_os.sep
pathsep = py_os.pathsep
altsep = py_os.altsep

defpath = py_os.defpath
devnull = py_os.devnull

F_OK = py_os.F_OK
R_OK = py_os.R_OK
W_OK = py_os.W_OK
X_OK = py_os.X_OK

SEEK_CUR = py_os.SEEK_CUR
SEEK_END = py_os.SEEK_END
SEEK_SET = py_os.SEEK_SET

PathLike = py_os.PathLike

terminal_size = py_os.terminal_size

abort = py_os.abort
access = py_os.access
chdir = py_os.chdir
close = py_os.close
closerange = py_os.closerange
environ = py_os.environ
fchdir = py_os.fchdir
fdopen = py_os.fdopen
fsdecode = py_os.fsdecode
fsencode = py_os.fsencode
fspath = py_os.fspath
fsync = py_os.fsync
ftruncate = py_os.ftruncate
get_blocking = py_os.get_blocking
get_exec_path = py_os.get_exec_path
get_inheritable = py_os.get_inheritable
get_terminal_size = py_os.get_terminal_size
getcwd = py_os.getcwd
getcwdb = py_os.getcwdb
getpid = py_os.getpid
getppid = py_os.getppid
isatty = py_os.isatty
link = py_os.link
listdir = py_os.listdir
lseek = py_os.lseek
major = py_os.major
makedev = py_os.makedev
makedirs = py_os.makedirs
minor = py_os.minor
pipe = py_os.pipe
putenv = py_os.putenv
read = py_os.read
readlink = py_os.readlink
remove = py_os.remove
removedirs = py_os.removedirs
rename = py_os.rename
renames = py_os.renames
replace = py_os.replace
rmdir = py_os.rmdir
set_inheritable = py_os.set_inheritable
supports_bytes_environ = py_os.supports_bytes_environ
symlink = py_os.symlink
times = py_os.times
truncate = py_os.truncate
umask = py_os.umask
unlink = py_os.unlink
unsetenv = py_os.unsetenv
utime = py_os.utime
write = py_os.write
