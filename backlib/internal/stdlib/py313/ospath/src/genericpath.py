from __future__ import annotations

from typing import TYPE_CHECKING, Literal, overload

from backlib.internal.stdlib.py313.os import fspath, fstat, stat, stat_result
from backlib.internal.stdlib.py313.ospath.src.typing import FileDescriptorOrPath
from backlib.internal.typing import AnyStr


if TYPE_CHECKING:
    from collections.abc import Sequence

    from backlib.internal.stdlib.py313.os import PathLike


__all__: list[str] = [
    "commonprefix",
    "getatime",
    "getctime",
    "getmtime",
    "getsize",
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

    paths = tuple(map(fspath, m))

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
    return stat(filename).st_atime


def getctime(filename: FileDescriptorOrPath) -> float:
    """Return the system's ctime which is the creation time for `path`.

    See Also
    --------
    * `os.path.getctime`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_ctime


def getmtime(filename: FileDescriptorOrPath) -> float:
    """Return the time of last modification of `path`.

    See Also
    --------
    * `os.path.getmtime`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_mtime


def getsize(filename: FileDescriptorOrPath) -> int:
    """Return the size, in bytes, of `path`.

    See Also
    --------
    * `os.path.getsize`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_size


def samestat(s1: stat_result, s2: stat_result) -> bool:
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
    s1 = stat(f1)
    s2 = stat(f2)
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
    s1 = fstat(fp1)
    s2 = fstat(fp2)
    return samestat(s1, s2)
