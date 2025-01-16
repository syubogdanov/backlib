"""Backport of the `os` module.

Notes
-----
* The following constants are not backported:
    - `CLD_CONTINUED`;
    - `CLD_DUMPED`;
    - `CLD_EXITED`;
    - `CLD_KILLED`;
    - `CLD_STOPPED`;
    - `CLD_TRAPPED`;
    - `CLONE_FILES`;
    - `CLONE_FS`;
    - `CLONE_NEWCGROUP`;
    - `CLONE_NEWIPC`;
    - `CLONE_NEWNET`;
    - `CLONE_NEWNS`;
    - `CLONE_NEWPID`;
    - `CLONE_NEWTIME`;
    - `CLONE_NEWUSER`;
    - `CLONE_NEWUTS`;
    - `CLONE_SIGHAND`;
    - `CLONE_SYSVSEM`;
    - `CLONE_THREAD`;
    - `CLONE_VM`;
    - `EFD_CLOEXEC`;
    - `EFD_NONBLOCK`;
    - `EFD_SEMAPHORE`;
    - `EX_CANTCREAT`;
    - `EX_CONFIG`;
    - `EX_DATAERR`;
    - `EX_IOERR`;
    - `EX_NOHOST`;
    - `EX_NOINPUT`;
    - `EX_NOPERM`;
    - `EX_NOUSER`;
    - `EX_OSERR`;
    - `EX_OSFILE`;
    - `EX_PROTOCOL`;
    - `EX_SOFTWARE`;
    - `EX_TEMPFAIL`;
    - `EX_UNAVAILABLE`;
    - `EX_USAGE`;
    - `F_LOCK`;
    - `F_TEST`;
    - `F_TLOCK`;
    - `F_ULOCK`;
    - `GRND_NONBLOCK`;
    - `GRND_RANDOM`;
    - `MFD_ALLOW_SEALING`;
    - `MFD_CLOEXEC`;
    - `MFD_HUGETLB`;
    - `MFD_HUGE_16GB`;
    - `MFD_HUGE_16MB`;
    - `MFD_HUGE_1GB`;
    - `MFD_HUGE_1MB`;
    - `MFD_HUGE_256MB`;
    - `MFD_HUGE_2GB`;
    - `MFD_HUGE_2MB`;
    - `MFD_HUGE_32MB`;
    - `MFD_HUGE_512KB`;
    - `MFD_HUGE_512MB`;
    - `MFD_HUGE_64KB`;
    - `MFD_HUGE_8MB`;
    - `MFD_HUGE_MASK`;
    - `MFD_HUGE_SHIFT`;
    - `NGROUPS_MAX`;
    - `O_ACCMODE`;
    - `O_ASYNC`;
    - `O_BINARY`;
    - `O_CLOEXEC`;
    - `O_DIRECTORY`;
    - `O_DIRECT`;
    - `O_DSYNC`;
    - `O_EVTONLY`;
    - `O_EXEC`;
    - `O_EXLOCK`;
    - `O_FSYNC`;
    - `O_LARGEFILE`;
    - `O_NDELAY`;
    - `O_NOATIME`;
    - `O_NOCTTY`;
    - `O_NOFOLLOW_ANY`;
    - `O_NOFOLLOW`;
    - `O_NOINHERIT`;
    - `O_NONBLOCK`;
    - `O_PATH`;
    - `O_RANDOM`;
    - `O_RSYNC`;
    - `O_SEARCH`;
    - `O_SEQUENTIAL`;
    - `O_SHLOCK`;
    - `O_SHORT_LIVED`;
    - `O_SYMLINK`;
    - `O_SYNC`;
    - `O_TEMPORARY`;
    - `O_TEXT`;
    - `O_TMPFILE`;
    - `POSIX_FADV_DONTNEED`;
    - `POSIX_FADV_NOREUSE`;
    - `POSIX_FADV_NORMAL`;
    - `POSIX_FADV_RANDOM`;
    - `POSIX_FADV_SEQUENTIAL`;
    - `POSIX_FADV_WILLNEED`;
    - `POSIX_SPAWN_CLOSEFROM`;
    - `POSIX_SPAWN_CLOSE`;
    - `POSIX_SPAWN_DUP2`;
    - `POSIX_SPAWN_OPEN`;
    - `PRIO_DARWIN_BG`;
    - `PRIO_DARWIN_NONUI`;
    - `PRIO_DARWIN_PROCESS`;
    - `PRIO_DARWIN_THREAD`;
    - `PRIO_PGRP`;
    - `PRIO_PROCESS`;
    - `PRIO_USER`;
    - `P_ALL`;
    - `P_DETACH`;
    - `P_OVERLAY`;
    - `P_PGID`;
    - `P_PIDFD`;
    - `P_PID`;
    - `RTLD_DEEPBIND`;
    - `RTLD_GLOBAL`;
    - `RTLD_LAZY`;
    - `RTLD_LOCAL`;
    - `RTLD_NODELETE`;
    - `RTLD_NOLOAD`;
    - `RTLD_NOW`;
    - `RWF_APPEND`;
    - `RWF_DSYNC`;
    - `RWF_HIPRI`;
    - `RWF_NOWAIT`;
    - `RWF_SYNC`;
    - `SCHED_BATCH`;
    - `SCHED_FIFO`;
    - `SCHED_IDLE`;
    - `SCHED_OTHER`;
    - `SCHED_RESET_ON_FORK`;
    - `SCHED_RR`;
    - `SEEK_DATA`;
    - `SEEK_HOLE`;
    - `SPLICE_F_MORE`;
    - `SPLICE_F_MOVE`;
    - `SPLICE_F_NONBLOCK`;
    - `ST_APPEND`;
    - `ST_MANDLOCK`;
    - `ST_NOATIME`;
    - `ST_NODEV`;
    - `ST_NODIRATIME`;
    - `ST_NOEXEC`;
    - `ST_NOSUID`;
    - `ST_RDONLY`;
    - `ST_RELATIME`;
    - `ST_SYNCHRONOUS`;
    - `ST_WRITE`;
    - `TFD_CLOEXEC`;
    - `TFD_NONBLOCK`;
    - `TFD_TIMER_ABSTIME`;
    - `TFD_TIMER_CANCEL_ON_SET`;
    - `WCONTINUED`;
    - `WCOREDUMP`;
    - `WEXITED`;
    - `WEXITSTATUS`;
    - `WIFCONTINUED`;
    - `WIFEXITED`;
    - `WIFSIGNALED`;
    - `WIFSTOPPED`;
    - `WNOHANG`;
    - `WNOWAIT`;
    - `WSTOPPED`;
    - `WSTOPSIG`;
    - `WTERMSIG`;
    - `WUNTRACED`;
    - `XATTR_CREATE`;
    - `XATTR_REPLACE`;
    - `XATTR_SIZE_MAX`.
* The following functions are not backported:
    - `chflags`;
    - `chown`;
    - `chroot`;
    - `confstr_names`;
    - `confstr`;
    - `copy_file_range`;
    - `ctermid`;
    - `environb`;
    - `eventfd_read`;
    - `eventfd_write`;
    - `eventfd`;
    - `fchdir`;
    - `fchown`;
    - `fdatasync`;
    - `fork`;
    - `forkpty`;
    - `fpathconf`;
    - `fstatvfs`;
    - `fwalk`;
    - `get_handle_inheritable`;
    - `getegid`;
    - `getenvb`;
    - `geteuid`;
    - `getgid`;
    - `getgrouplist`;
    - `getgroups`;
    - `getloadavg`;
    - `getpgid`;
    - `getpgrp`;
    - `getpriority`;
    - `getrandom`;
    - `getresgid`;
    - `getresuid`;
    - `getsid`;
    - `getuid`;
    - `getxattr`;
    - `grantpt`;
    - `initgroups`;
    - `killpg`;
    - `lchflags`;
    - `lchmod`;
    - `lchown`;
    - `listdrives`;
    - `listmounts`;
    - `listvolumes`;
    - `listxattr`;
    - `lockf`;
    - `login_tty`;
    - `major`;
    - `makedev`;
    - `memfd_create`;
    - `minor`;
    - `mkfifo`;
    - `mknod`;
    - `nice`;
    - `openpty`;
    - `pathconf_names`;
    - `pathconf`;
    - `pidfd_open`;
    - `pipe2`;
    - `posix_fadvise`;
    - `posix_fallocate`;
    - `posix_openpt`;
    - `posix_spawn`;
    - `posix_spawnp`;
    - `pread`;
    - `preadv`;
    - `ptsname`;
    - `pwrite`;
    - `pwritev`;
    - `readv`;
    - `register_at_fork`;
    - `removexattr`;
    - `sched_get_priority_max`;
    - `sched_get_priority_min`;
    - `sched_getaffinity`;
    - `sched_getparam`;
    - `sched_getscheduler`;
    - `sched_param`;
    - `sched_rr_get_interval`;
    - `sched_setaffinity`;
    - `sched_setparam`;
    - `sched_setscheduler`;
    - `sched_yield`;
    - `sendfile`;
    - `set_handle_inheritable`;
    - `setegid`;
    - `seteuid`;
    - `setgid`;
    - `setgroups`;
    - `setns`;
    - `setpgid`;
    - `setpgrp`;
    - `setpriority`;
    - `setregid`;
    - `setresgid`;
    - `setresuid`;
    - `setreuid`;
    - `setsid`;
    - `setuid`;
    - `setxattr`;
    - `spawnlp`;
    - `spawnlpe`;
    - `spawnvp`;
    - `spawnvpe`;
    - `splice`;
    - `startfile`;
    - `statvfs`;
    - `sync`;
    - `sysconf_names`;
    - `sysconf`;
    - `tcgetpgrp`;
    - `tcsetpgrp`;
    - `timerfd_create`;
    - `timerfd_gettime_ns`;
    - `timerfd_gettime`;
    - `timerfd_settime_ns`;
    - `timerfd_settime`;
    - `ttyname`;
    - `uname`;
    - `unlockpt`;
    - `unshare`;
    - `wait3`;
    - `wait4`;
    - `wait`;
    - `waitid_result`;
    - `waitid`;
    - `writev`.

See Also
--------
* `os`.

Version
-------
* Python 3.13.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from os import environ, execv, execve, execvp, execvpe, spawnv
from sys import getfilesystemencodeerrors, getfilesystemencoding
from typing import Final, Generic, TypeVar, overload

from backlib.internal.typing import AnyStr, Self, TypeAlias
from backlib.internal.utils.sys import is_nt, is_posix


__all__: list[str] = [
    "EX_OK",
    "F_OK",
    "O_APPEND",
    "O_CREAT",
    "O_EXCL",
    "O_RDONLY",
    "O_RDWR",
    "O_TRUNC",
    "O_WRONLY",
    "P_NOWAIT",
    "P_NOWAITO",
    "P_WAIT",
    "R_OK",
    "SEEK_CUR",
    "SEEK_END",
    "SEEK_SET",
    "W_OK",
    "X_OK",
    "DirEntry",
    "PathLike",
    "_exit",
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
    "dup",
    "dup2",
    "environ",
    "environb",
    "error",
    "execl",
    "execle",
    "execlp",
    "execlpe",
    "execv",
    "execve",
    "execvp",
    "execvpe",
    "extsep",
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
    "getenv",
    "getenvb",
    "getlogin",
    "getpid",
    "getppid",
    "isatty",
    "kill",
    "linesep",
    "link",
    "listdir",
    "lseek",
    "lstat",
    "makedirs",
    "mkdir",
    "name",
    "open",
    "pardir",
    "path",
    "pathsep",
    "pipe",
    "popen",
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
    "spawnl",
    "spawnle",
    "spawnv",
    "spawnve",
    "stat",
    "stat_result",
    "strerror",
    "supports_bytes_environ",
    "supports_dir_fd",
    "supports_effective_ids",
    "supports_fd",
    "supports_follow_symlinks",
    "symlink",
    "system",
    "terminal_size",
    "times",
    "times_result",
    "truncate",
    "umask",
    "unlink",
    "unsetenv",
    "urandom",
    "utime",
    "waitpid",
    "waitstatus_to_exitcode",
    "walk",
    "write",
]


if not is_nt() and not is_posix():
    detail = "no os specific module found"
    raise ImportError(detail)


AnyStr_co = TypeVar("AnyStr_co", str, bytes, covariant=True)

T = TypeVar("T")


SEEK_SET: Final[int] = 0
SEEK_CUR: Final[int] = 1
SEEK_END: Final[int] = 2

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

    if isinstance(path_repr, (str, bytes)):
        return path_repr  # type: ignore[return-value]

    detail = (
        f"expected {path_type.__name__}.__fspath__() to return str or bytes, "
        f"not {type(path_repr).__name__}"
    )
    raise TypeError(detail)


@overload
def getenv(key: str) -> str | None:
    ...


@overload
def getenv(key: str, default: T) -> str | T:
    ...


def getenv(key: str, default: T | None = None) -> str | T | None:
    """Get the value of the environment variable `key` as a string, if exists, otherwise `default`.

    See Also
    --------
    * `os.getenv`.

    Version
    -------
    * Python 3.13.
    """
    return environ.get(key, default)


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


def spawnl(mode: int, file: AnyStr | PathLike[AnyStr], *args: AnyStr | PathLike[AnyStr]) -> int:
    """Execute `file` with arguments from `args` in a subprocess.

    See Also
    --------
    * `os.spawnl`.

    Version
    -------
    * Python 3.13.
    """
    return spawnv(mode, file, args)  # noqa: S606
