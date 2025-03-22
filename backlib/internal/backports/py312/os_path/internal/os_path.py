from __future__ import annotations

import os.path as py_os_path

from typing import TYPE_CHECKING, TypeVar

from backlib.internal.backports.py312.os_path.internal import genericpath, ntpath, posixpath
from backlib.internal.utils.platform import is_nt


if TYPE_CHECKING:
    from backlib.internal.backports.py312.os import PathLike, stat_result


__all__: list[str] = ["isdevdrive", "isjunction", "splitroot"]

__backlib__: str = "backlib.py312.os.path"


AnyStr = TypeVar("AnyStr", str, bytes)


def isjunction(path: str | bytes | PathLike[str] | PathLike[bytes]) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a junction.

    See Also
    --------
    * `os.path.isjunction`.
    """
    os_isjunction = ntpath.isjunction if is_nt() else posixpath.isjunction
    return os_isjunction(path)


def isdevdrive(path: str | bytes | PathLike[str] | PathLike[bytes]) -> bool:
    """Return True if pathname path is located on a Windows Dev Drive.

    See Also
    --------
    * `os.path.isdevdrive`.
    """
    if hasattr(py_os_path, "isdevdrive"):
        return py_os_path.isdevdrive(path)
    return genericpath.isdevdrive(path)


def splitroot(path: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr, AnyStr]:
    """Split the pathname `path` into a 3-item tuple `(drive, root, tail)`.

    See Also
    --------
    * `os.path.splitroot`.
    """
    os_splitroot = ntpath.splitroot if is_nt() else posixpath.splitroot
    return os_splitroot(path)


def samestat(s1: stat_result, s2: stat_result) -> bool:
    """Return `True` if the stat tuples `s1` and `s2` refer to the same file.

    See Also
    --------
    * `os.path.samestat`.
    """
    return s1.st_ino == s2.st_ino and s1.st_dev == s2.st_dev


isdevdrive.__module__ = __backlib__
isjunction.__module__ = __backlib__
samestat.__module__ = __backlib__
splitroot.__module__ = __backlib__
