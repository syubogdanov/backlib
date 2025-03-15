from __future__ import annotations

import os.path as py_os_path

from typing import TYPE_CHECKING, TypeVar

from backlib.internal.backports.py312.os_path.internal import genericpath, ntpath, posixpath
from backlib.internal.utils.platform import is_nt


if TYPE_CHECKING:
    from backlib.internal.backports.py312 import os


__all__: list[str] = ["isdevdrive", "isjunction", "splitroot"]


AnyStr = TypeVar("AnyStr", str, bytes)


def isjunction(path: str | bytes | os.PathLike[str] | os.PathLike[bytes]) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a junction.

    See Also
    --------
    * `os.path.isjunction`.
    """
    os_isjunction = ntpath.isjunction if is_nt() else posixpath.isjunction
    return os_isjunction(path)


def isdevdrive(path: str | bytes | os.PathLike[str] | os.PathLike[bytes]) -> bool:
    """Return True if pathname path is located on a Windows Dev Drive.

    See Also
    --------
    * `os.path.isdevdrive`.
    """
    if hasattr(py_os_path, "isdevdrive"):
        return py_os_path.isdevdrive(path)
    return genericpath.isdevdrive(path)


def splitroot(path: AnyStr | os.PathLike[AnyStr]) -> tuple[AnyStr, AnyStr, AnyStr]:
    """Split the pathname `path` into a 3-item tuple `(drive, root, tail)`.

    See Also
    --------
    * `os.path.splitroot`.
    """
    os_splitroot = ntpath.splitroot if is_nt() else posixpath.splitroot
    return os_splitroot(path)
