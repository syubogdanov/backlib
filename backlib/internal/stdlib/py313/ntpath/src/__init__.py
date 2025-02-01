from __future__ import annotations

from typing import TYPE_CHECKING, Final, Literal

from backlib.internal.linters.decorators import techdebt
from backlib.internal.stdlib.py313.os import (
    PathLike,
    fsdecode,
    fsencode,
    fspath,
    fstat,
    lstat,
    stat,
    stat_result,
)
from backlib.internal.stdlib.py313.stat import IO_REPARSE_TAG_MOUNT_POINT, S_ISDIR, S_ISLNK, S_ISREG
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
    "isreserved",
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


supports_unicode_filenames: Final[bool] = True


def commonprefix(m: Sequence[AnyStr | PathLike[AnyStr]]) -> Literal[""] | AnyStr:
    """Return the longest path prefix that is a prefix of all paths.

    See Also
    --------
    * `ntpath.commonprefix`.

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
    * `ntpath.getatime`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_atime


def getctime(filename: int | AnyStr | PathLike[AnyStr]) -> float:
    """Return the system's ctime which is the creation time for `path`.

    See Also
    --------
    * `ntpath.getctime`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_ctime


def getmtime(filename: int | AnyStr | PathLike[AnyStr]) -> float:
    """Return the time of last modification of `path`.

    See Also
    --------
    * `ntpath.getmtime`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_mtime


def getsize(filename: int | AnyStr | PathLike[AnyStr]) -> int:
    """Return the size, in bytes, of `path`.

    See Also
    --------
    * `ntpath.getsize`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_size


def samestat(s1: stat_result, s2: stat_result) -> bool:
    """Return `True` if the stat tuples `stat1` and `stat2` refer to the same file.

    See Also
    --------
    * `ntpath.samestat`.

    Version
    -------
    * Python 3.13.
    """
    return s1.st_ino == s2.st_ino and s1.st_dev == s2.st_dev


def samefile(f1: int | AnyStr | PathLike[AnyStr], f2: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if both pathname arguments refer to the same file or directory.

    See Also
    --------
    * `ntpath.samefile`.

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
    * `ntpath.sameopenfile`.

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
    * `ntpath.isdir`.

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
    * `ntpath.isfile`.

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
    * `ntpath.islink`.

    Version
    -------
    * Python 3.13.
    """
    try:
        st = lstat(path)
    except (OSError, ValueError):
        return False
    return S_ISLNK(st.st_mode)


def exists(path: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing path or an open file descriptor.

    See Also
    --------
    * `ntpath.exists`.

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
    * `ntpath.lexists`.

    Version
    -------
    * Python 3.13.
    """
    try:
        lstat(path)
    except (OSError, ValueError):
        return False
    return True


def isjunction(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a junction.

    See Also
    --------
    * `ntpath.isjunction`.

    Version
    -------
    * Python 3.13.
    """
    try:
        st = lstat(path)
    except (OSError, ValueError):
        return False
    return st.st_reparse_tag == IO_REPARSE_TAG_MOUNT_POINT


@techdebt
def isabs(s: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an absolute pathname.

    See Also
    --------
    * `ntpath.isabs`.

    Version
    -------
    * Python 3.13.
    """
    s = fspath(s)

    sep = b"\\" if isinstance(s, bytes) else "\\"
    altsep = b"/" if isinstance(s, bytes) else "/"
    colon_sep = b":\\" if isinstance(s, bytes) else ":\\"
    double_sep = b"\\\\" if isinstance(s, bytes) else "\\\\"

    prefix = s[:3].replace(altsep, sep)
    return prefix.startswith(colon_sep, 1) or prefix.startswith(double_sep)


@techdebt
def isdevdrive(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if pathname `path` is located on a Windows Dev Drive.

    See Also
    --------
    * `ntpath.isdevdrive`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * The functionality has been reduced.
    """
    fspath(path)
    return False


@techdebt
def normcase(s: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Normalize the case of a pathname.

    See Also
    --------
    * `ntpath.normcase`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * The functionality has been reduced.
    """
    s = fspath(s)

    if not isinstance(s, bytes):
        return s.replace("/", "\\").lower()

    return fsencode(fsdecode(s).replace("/", "\\").lower())


def splitext(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]:
    """Split the pathname `path` into a pair `(root, ext)`.

    See Also
    --------
    * `ntpath.splitext`.

    Version
    -------
    * Python 3.13.
    """
    p = fspath(p)

    if isinstance(p, bytes):
        sep = b"\\"
        altsep = b"/"
        extsep = b"."

    else:
        sep = "\\"
        altsep = "/"
        extsep = "."

    sep_index = max(p.rfind(sep), p.rfind(altsep))
    extsep_index = p.rfind(extsep)

    if extsep_index <= sep_index:
        return (p, p[:0])

    starts_with_extseps = all(
        p[index] == extsep
        for index in range(sep_index + 1, extsep_index + 1)
    )

    if starts_with_extseps:
        return (p, p[:0])

    return (p[:extsep_index], p[extsep_index:])
