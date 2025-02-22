from backlib.internal.backports.py313.stat.src.flags import (
    S_IFBLK,
    S_IFCHR,
    S_IFDIR,
    S_IFIFO,
    S_IFLNK,
    S_IFREG,
    S_IFSOCK,
)
from backlib.internal.markers import todo


__all__: list[str] = [
    "S_IFMT",
    "S_IMODE",
    "S_ISBLK",
    "S_ISCHR",
    "S_ISDIR",
    "S_ISDOOR",
    "S_ISFIFO",
    "S_ISLNK",
    "S_ISPORT",
    "S_ISREG",
    "S_ISSOCK",
    "S_ISWHT",
]


def S_IMODE(mode: int) -> int:  # noqa: N802
    """Return the portion of the file's mode that can be set by `os.chmod()`.

    See Also
    --------
    * `stat.S_IMODE`.

    Version
    -------
    * Python 3.13.
    """
    return mode & 0o7777


def S_IFMT(mode: int) -> int:  # noqa: N802
    """Return the portion of the file's mode that describes the file type.

    See Also
    --------
    * `stat.S_IFMT`.

    Version
    -------
    * Python 3.13.
    """
    return mode & 0o170000


def S_ISDIR(mode: int) -> bool:  # noqa: N802
    """Return `True` if the mode is from a directory.

    See Also
    --------
    * `stat.S_ISDIR`.

    Version
    -------
    * Python 3.13.
    """
    return S_IFMT(mode) == S_IFDIR


def S_ISCHR(mode: int) -> bool:  # noqa: N802
    """Return `True` if the mode is from a character special device file.

    See Also
    --------
    * `stat.S_ISCHR`.

    Version
    -------
    * Python 3.13.
    """
    return S_IFMT(mode) == S_IFCHR


def S_ISBLK(mode: int) -> bool:  # noqa: N802
    """Return `True` if the mode is from a block special device file.

    See Also
    --------
    * `stat.S_ISBLK`.

    Version
    -------
    * Python 3.13.
    """
    return S_IFMT(mode) == S_IFBLK


def S_ISREG(mode: int) -> bool:  # noqa: N802
    """Return `True` if the mode is from a regular file.

    See Also
    --------
    * `stat.S_ISREG`.

    Version
    -------
    * Python 3.13.
    """
    return S_IFMT(mode) == S_IFREG


def S_ISFIFO(mode: int) -> bool:  # noqa: N802
    """Return `True` if the mode is from a FIFO (named pipe).

    See Also
    --------
    * `stat.S_ISFIFO`.

    Version
    -------
    * Python 3.13.
    """
    return S_IFMT(mode) == S_IFIFO


def S_ISLNK(mode: int) -> bool:  # noqa: N802
    """Return `True` if the mode is from a symbolic link.

    See Also
    --------
    * `stat.S_ISLNK`.

    Version
    -------
    * Python 3.13.
    """
    return S_IFMT(mode) == S_IFLNK


def S_ISSOCK(mode: int) -> bool:  # noqa: N802
    """Return `True` if the mode is from a socket.

    See Also
    --------
    * `stat.S_ISSOCK`.

    Version
    -------
    * Python 3.13.
    """
    return S_IFMT(mode) == S_IFSOCK


@todo.restore
def S_ISDOOR(mode: int) -> bool:  # noqa: ARG001, N802
    """Return `True` if the mode is from a door.

    See Also
    --------
    * `stat.S_ISDOOR`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * Always returns `False`.
    """
    return False


@todo.restore
def S_ISPORT(mode: int) -> bool:  # noqa: ARG001, N802
    """Return `True` if the mode is from an event port.

    See Also
    --------
    * `stat.S_ISPORT`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * Always returns `False`.
    """
    return False


@todo.restore
def S_ISWHT(mode: int) -> bool:  # noqa: ARG001, N802
    """Return `True` if the mode is from a whiteout.

    See Also
    --------
    * `stat.S_ISWHT`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * Always returns `False`.
    """
    return False
