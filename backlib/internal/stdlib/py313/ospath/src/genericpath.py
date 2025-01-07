from __future__ import annotations

from stat import S_ISDIR, S_ISLNK, S_ISREG
from typing import TYPE_CHECKING, Literal, overload

from backlib.internal.stdlib.py313 import os
from backlib.internal.stdlib.py313.ospath.src.typing import FileDescriptorOrPath, StrOrBytesPath
from backlib.internal.typing import AnyStr


if TYPE_CHECKING:
    from collections.abc import Sequence

    from backlib.internal.stdlib.py313.os import PathLike


__all__: list[str] = [
    "commonprefix",
    "exists",
    "getatime",
    "getctime",
    "getmtime",
    "getsize",
    "isdir",
    "isfile",
    "islink",
    "lexists",
    "samefile",
    "sameopenfile",
    "samestat",
]


@overload
def commonprefix(m: Sequence[AnyStr]) -> Literal[""] | AnyStr:
    ...


@overload
def commonprefix(m: Sequence[PathLike[AnyStr]]) -> Literal[""] | AnyStr:
    ...


def commonprefix(m: Sequence[AnyStr] | Sequence[PathLike[AnyStr]]) -> Literal[""] | AnyStr:
    """Return the longest path prefix that is a prefix of all paths.

    See Also
    --------
    * `os.path.commonprefix`.

    Version
    -------
    * Python 3.13.
    """
    if not m:
        return ""

    paths = tuple(map(os.fspath, m))

    p1 = min(paths)
    p2 = max(paths)

    for index, character in enumerate(p1):
        if character != p2[index]:
            return p1[:index]

    return p1


def getatime(filename: FileDescriptorOrPath) -> float:
    """Return the time of last access of `path`.

    See Also
    --------
    * `os.path.getatime`.

    Version
    -------
    * Python 3.13.
    """
    return os.stat(filename).st_atime


def getctime(filename: FileDescriptorOrPath) -> float:
    """Return the system's ctime which is the creation time for `path`.

    See Also
    --------
    * `os.path.getctime`.

    Version
    -------
    * Python 3.13.
    """
    return os.stat(filename).st_ctime


def getmtime(filename: FileDescriptorOrPath) -> float:
    """Return the time of last modification of `path`.

    See Also
    --------
    * `os.path.getmtime`.

    Version
    -------
    * Python 3.13.
    """
    return os.stat(filename).st_mtime


def getsize(filename: FileDescriptorOrPath) -> int:
    """Return the size, in bytes, of `path`.

    See Also
    --------
    * `os.path.getsize`.

    Version
    -------
    * Python 3.13.
    """
    return os.stat(filename).st_size


def samestat(s1: os.stat_result, s2: os.stat_result) -> bool:
    """Return `True` if the stat tuples `stat1` and `stat2` refer to the same file.

    See Also
    --------
    * `os.path.samestat`.

    Version
    -------
    * Python 3.13.
    """
    return s1.st_ino == s2.st_ino and s1.st_dev == s2.st_dev


def samefile(f1: FileDescriptorOrPath, f2: FileDescriptorOrPath) -> bool:
    """Return `True` if both pathname arguments refer to the same file or directory.

    See Also
    --------
    * `os.path.samefile`.

    Version
    -------
    * Python 3.13.
    """
    s1 = os.stat(f1)
    s2 = os.stat(f2)
    return samestat(s1, s2)


def sameopenfile(fp1: int, fp2: int) -> bool:
    """Return `True` if the file descriptors `fp1` and `fp2` refer to the same file.

    See Also
    --------
    * `os.path.sameopenfile`.

    Version
    -------
    * Python 3.13.
    """
    s1 = os.fstat(fp1)
    s2 = os.fstat(fp2)
    return samestat(s1, s2)


def isdir(s: FileDescriptorOrPath) -> bool:
    """Return `True` if `path` is an existing directory.

    See Also
    --------
    * `os.path.isdir`.

    Version
    -------
    * Python 3.13.
    """
    try:
        st = os.stat(s)
    except (OSError, ValueError):
        return False
    return S_ISDIR(st.st_mode)


def isfile(path: FileDescriptorOrPath) -> bool:
    """Return `True` if `path` is an existing regular file.

    See Also
    --------
    * `os.path.isfile`.

    Version
    -------
    * Python 3.13.
    """
    try:
        st = os.stat(path)
    except (OSError, ValueError):
        return False
    return S_ISREG(st.st_mode)


def islink(path: StrOrBytesPath) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a symbolic link.

    See Also
    --------
    * `os.path.islink`.

    Version
    -------
    * Python 3.13.
    """
    try:
        st = os.lstat(path)
    except (OSError, ValueError, AttributeError):
        return False
    return S_ISLNK(st.st_mode)


def exists(path: FileDescriptorOrPath) -> bool:
    """Return `True` if `path` refers to an existing path or an open file descriptor.

    See Also
    --------
    * `os.path.exists`.

    Version
    -------
    * Python 3.13.
    """
    try:
        os.stat(path)
    except (OSError, ValueError):
        return False
    return True


def lexists(path: StrOrBytesPath) -> bool:
    """Return `True` if `path` refers to an existing path, including broken symbolic links.

    See Also
    --------
    * `os.path.lexists`.

    Version
    -------
    * Python 3.13.
    """
    try:
        os.lstat(path)
    except (OSError, ValueError):
        return False
    return True
