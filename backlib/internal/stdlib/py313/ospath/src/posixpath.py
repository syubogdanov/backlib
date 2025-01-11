from __future__ import annotations

from typing import TYPE_CHECKING, Final

from backlib.internal.stdlib.py313.os import PathLike, fspath, getcwd, getcwdb
from backlib.internal.stdlib.py313.ospath.src.utils import check_arg_types
from backlib.internal.typing import AnyStr
from backlib.internal.utils.lint import techdebt
from backlib.internal.utils.sys import is_darwin


if TYPE_CHECKING:
    from collections.abc import Iterable


__all__: list[str] = [
    "abspath",
    "basename",
    "commonpath",
    "dirname",
    "expanduser",
    "expandvars",
    "isabs",
    "isdevdrive",
    "isjunction",
    "ismount",
    "join",
    "normcase",
    "normpath",
    "realpath",
    "relpath",
    "split",
    "splitdrive",
    "splitext",
    "splitroot",
    "supports_unicode_filenames",
]


supports_unicode_filenames: Final[bool] = is_darwin()


def isjunction(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a junction.

    See Also
    --------
    * `os.path.isjunction`.

    Version
    -------
    * Python 3.13.
    """
    fspath(path)
    return False


def isdevdrive(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if pathname `path` is located on a Windows Dev Drive.

    See Also
    --------
    * `os.path.isdevdrive`.

    Version
    -------
    * Python 3.13.
    """
    fspath(path)
    return False


def splitext(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]:
    """Split the pathname `path` into a pair `(root, ext)`.

    See Also
    --------
    * `os.path.splitext`.

    Version
    -------
    * Python 3.13.
    """
    p = fspath(p)

    if isinstance(p, bytes):
        sep = b"/"
        extsep = b"."

    else:
        sep = "/"
        extsep = "."

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


def normcase(s: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Normalize the case of a pathname.

    See Also
    --------
    * `os.path.normcase`.

    Version
    -------
    * Python 3.13.
    """
    return fspath(s)


def isabs(s: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an absolute pathname.

    See Also
    --------
    * `os.path.isabs`.

    Version
    -------
    * Python 3.13.
    """
    s = fspath(s)
    sep = b"/" if isinstance(s, bytes) else "/"
    return s.startswith(sep)


def splitdrive(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]:
    """Split the pathname `path` into a pair `(drive, tail)`.

    See Also
    --------
    * `os.path.splitdrive`.

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
    * `os.path.split`.

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
    * `os.path.basename`.

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
    * `os.path.dirname`.

    Version
    -------
    * Python 3.13.
    """
    head, _ = split(p)
    return head


def abspath(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Return a normalized absolutized version of the pathname `path`.

    See Also
    --------
    * `os.path.abspath`.

    Version
    -------
    * Python 3.13.
    """
    path = fspath(path)

    if isinstance(path, bytes) and not path.startswith(b"/"):
        path = join(getcwdb(), path)

    elif isinstance(path, str) and not path.startswith("/"):
        path = join(getcwd(), path)

    return normpath(path)


def splitroot(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr, AnyStr]:
    """Split the pathname `path` into a 3-item tuple `(drive, root, tail)`.

    See Also
    --------
    * `os.path.splitroot`.

    Version
    -------
    * Python 3.13.
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


@techdebt("This function should be refactored...")
def normpath(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Normalize a pathname by collapsing redundant separators and up-level references.

    See Also
    --------
    * `os.path.normpath`.

    Version
    -------
    * Python 3.13.
    """
    path = fspath(path)
    if isinstance(path, bytes):
        sep = b"/"
        dot = b"."
        dotdot = b".."
    else:
        sep = "/"
        dot = "."
        dotdot = ".."
    if not path:
        return dot
    _, initial_slashes, path = splitroot(path)
    comps = path.split(sep)
    new_comps = []
    for comp in comps:
        if not comp or comp == dot:
            continue
        if (comp != dotdot or (not initial_slashes and not new_comps) or
             (new_comps and new_comps[-1] == dotdot)):
            new_comps.append(comp)
        elif new_comps:
            new_comps.pop()
    comps = new_comps
    path = initial_slashes + sep.join(comps)
    return path or dot
