from __future__ import annotations

from typing import TYPE_CHECKING, Final, Literal

from backlib.internal.linters.decorators import techdebt
from backlib.internal.stdlib.py313.os import fspath, fstat, lstat, stat, stat_result
from backlib.internal.stdlib.py313.posixpath.src.utils import check_arg_types
from backlib.internal.stdlib.py313.stat import S_ISDIR, S_ISLNK, S_ISREG
from backlib.internal.typing import AnyStr
from backlib.internal.utils.sys import is_darwin


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


supports_unicode_filenames: Final[bool] = is_darwin()


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
    except (OSError, ValueError):
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


def isreserved(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is a reserved pathname on the current system.

    Notes
    -----
    * The standard library module does not have this function;
    * `False` is always returned.

    See Also
    --------
    * `posixpath.isreserved`.

    Version
    -------
    * Python 3.13.
    """
    fspath(path)
    return False


def isabs(s: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an absolute pathname.

    See Also
    --------
    * `posixpath.isabs`.

    Version
    -------
    * Python 3.13.
    """
    s = fspath(s)
    sep = b"/" if isinstance(s, bytes) else "/"
    return s.startswith(sep)


def isdevdrive(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if pathname `path` is located on a Windows Dev Drive.

    See Also
    --------
    * `posixpath.isdevdrive`.

    Version
    -------
    * Python 3.13.
    """
    fspath(path)
    return False


def normcase(s: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Normalize the case of a pathname.

    See Also
    --------
    * `posixpath.normcase`.

    Version
    -------
    * Python 3.13.
    """
    return fspath(s)


def splitext(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]:
    """Split the pathname `path` into a pair `(root, ext)`.

    See Also
    --------
    * `posixpath.splitext`.

    Version
    -------
    * Python 3.13.
    """
    p = fspath(p)

    sep = b"/" if isinstance(p, bytes) else "/"
    extsep = b"." if isinstance(p, bytes) else "."

    sep_index = p.rfind(sep)
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


def isjunction(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a junction.

    See Also
    --------
    * `posixpath.isjunction`.

    Version
    -------
    * Python 3.13.
    """
    fspath(path)
    return False


@techdebt
def splitroot(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr, AnyStr]:
    """Split the pathname `path` into a 3-item tuple `(drive, root, tail)`.

    See Also
    --------
    * `posixpath.splitroot`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * The functionality has been reduced.
    """
    p = fspath(p)

    sep = b"/" if isinstance(p, bytes) else "/"

    double_sep = sep * 2
    triple_sep = sep * 3

    if not p.startswith(sep):
        return (p[:0], p[:0], p)

    if not p.startswith(double_sep) or p.startswith(triple_sep):
        return (p[:0], sep, p[1:])

    return (p[:0], p[:2], p[2:])


def splitdrive(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]:
    """Split the pathname `path` into a pair `(drive, tail)`.

    See Also
    --------
    * `posixpath.splitdrive`.

    Version
    -------
    * Python 3.13.
    """
    p = fspath(p)
    return (p[:0], p)


def split(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]:
    """Split the pathname `path` into a pair `(head, tail)`.

    See Also
    --------
    * `posixpath.split`.

    Version
    -------
    * Python 3.13.
    """
    p = fspath(p)

    sep = b"/" if isinstance(p, bytes) else "/"
    index = p.rfind(sep) + 1

    head, tail = p[:index], p[index:]

    if head and head != sep * len(head):
        head = head.rstrip(sep)

    return (head, tail)


def basename(p: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Return the base name of pathname path.

    See Also
    --------
    * `posixpath.basename`.

    Version
    -------
    * Python 3.13.
    """
    _, tail = split(p)
    return tail


def dirname(p: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Return the directory name of pathname `path`.

    See Also
    --------
    * `posixpath.dirname`.

    Version
    -------
    * Python 3.13.
    """
    head, _ = split(p)
    return head


def normpath(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Normalize a pathname by collapsing redundant separators and up-level references.

    See Also
    --------
    * `posixpath.normpath`.

    Version
    -------
    * Python 3.13.
    """
    path = fspath(path)

    sep = b"/" if isinstance(path, bytes) else "/"
    dot = b"." if isinstance(path, bytes) else "."
    dotdot = b".." if isinstance(path, bytes) else ".."

    if not path:
        return dot

    _, root, tail = splitroot(path)
    components: list[AnyStr] = []

    for component in tail.split(sep):
        if not component or component == dot:
            continue

        if component != dotdot:
            components.append(component)
            continue

        if not root and not components:
            components.append(component)
            continue

        if components and components[-1] == dotdot:
            components.append(component)
            continue

        if components:
            components.pop()

    path = root + sep.join(components)
    return path or dot
