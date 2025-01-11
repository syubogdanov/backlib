from __future__ import annotations

from stat import S_ISDIR, S_ISLNK, S_ISREG
from typing import TYPE_CHECKING, Literal

from backlib.internal.stdlib.py313.os import fspath, fstat, lstat, stat, stat_result
from backlib.internal.typing import AnyStr


if TYPE_CHECKING:
    from collections.abc import Sequence

    from backlib.internal.stdlib.py313.os import PathLike


__all__: list[str] = [
    "abspath",
    "basename",
    "commonpath",
    "commonprefix",
    "dirname",
    "exists",
    "expanduser",
    "expandvars",
    "getatime",
    "getctime",
    "getmtime",
    "getsize",
    "isabs",
    "isdevdrive",
    "isdir",
    "isfile",
    "isjunction",
    "islink",
    "ismount",
    "join",
    "lexists",
    "normcase",
    "normpath",
    "realpath",
    "relpath",
    "samefile",
    "sameopenfile",
    "samestat",
    "split",
    "splitdrive",
    "splitext",
    "splitroot",
    "supports_unicode_filenames",
]


def commonprefix(m: Sequence[AnyStr | PathLike[AnyStr]]) -> Literal[""] | AnyStr:
    """Return the longest path prefix that is a prefix of all paths.

    See Also
    --------
    * `posixpath.commonprefix`.

    Version
    -------
    * Python 3.13.
    """
    if not m:
        return ""

    paths = tuple(map(fspath, m))

    p1 = min(paths)
    p2 = max(paths)

    for index, character in enumerate(p1):
        if character != p2[index]:
            return p1[:index]

    return p1


def getatime(filename: int | AnyStr | PathLike[AnyStr]) -> float:
    """Return the time of last access of `path`.

    See Also
    --------
    * `posixpath.getatime`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_atime


def getctime(filename: int | AnyStr | PathLike[AnyStr]) -> float:
    """Return the system's ctime which is the creation time for `path`.

    See Also
    --------
    * `posixpath.getctime`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_ctime


def getmtime(filename: int | AnyStr | PathLike[AnyStr]) -> float:
    """Return the time of last modification of `path`.

    See Also
    --------
    * `posixpath.getmtime`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_mtime


def getsize(filename: int | AnyStr | PathLike[AnyStr]) -> int:
    """Return the size, in bytes, of `path`.

    See Also
    --------
    * `posixpath.getsize`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_size


def samestat(s1: stat_result, s2: stat_result) -> bool:
    """Return `True` if the stat tuples `stat1` and `stat2` refer to the same file.

    See Also
    --------
    * `posixpath.samestat`.

    Version
    -------
    * Python 3.13.
    """
    return s1.st_ino == s2.st_ino and s1.st_dev == s2.st_dev


def samefile(f1: int | AnyStr | PathLike[AnyStr], f2: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if both pathname arguments refer to the same file or directory.

    See Also
    --------
    * `posixpath.samefile`.

    Version
    -------
    * Python 3.13.
    """
    s1 = stat(f1)
    s2 = stat(f2)
    return samestat(s1, s2)


def sameopenfile(fp1: int, fp2: int) -> bool:
    """Return `True` if the file descriptors `fp1` and `fp2` refer to the same file.

    See Also
    --------
    * `posixpath.sameopenfile`.

    Version
    -------
    * Python 3.13.
    """
    s1 = fstat(fp1)
    s2 = fstat(fp2)
    return samestat(s1, s2)


def isdir(s: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an existing directory.

    See Also
    --------
    * `posixpath.isdir`.

    Version
    -------
    * Python 3.13.
    """
    try:
        st = stat(s)
    except (OSError, ValueError):
        return False
    return S_ISDIR(st.st_mode)


def isfile(path: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an existing regular file.

    See Also
    --------
    * `posixpath.isfile`.

    Version
    -------
    * Python 3.13.
    """
    try:
        st = stat(path)
    except (OSError, ValueError):
        return False
    return S_ISREG(st.st_mode)


def islink(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a symbolic link.

    See Also
    --------
    * `posixpath.islink`.

    Version
    -------
    * Python 3.13.
    """
    try:
        st = lstat(path)
    except (OSError, ValueError, AttributeError):
        return False
    return S_ISLNK(st.st_mode)


def exists(path: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing path or an open file descriptor.

    See Also
    --------
    * `posixpath.exists`.

    Version
    -------
    * Python 3.13.
    """
    try:
        stat(path)
    except (OSError, ValueError):
        return False
    return True


def lexists(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing path, including broken symbolic links.

    See Also
    --------
    * `posixpath.lexists`.

    Version
    -------
    * Python 3.13.
    """
    try:
        lstat(path)
    except (OSError, ValueError):
        return False
    return True
