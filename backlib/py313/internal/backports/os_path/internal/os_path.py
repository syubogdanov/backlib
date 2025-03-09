from __future__ import annotations

import os.path as py_os_path
import sys

from typing import TYPE_CHECKING, TypeVar
from warnings import warn

from backlib.py313.internal.backports import os
from backlib.py313.internal.backports.os_path.internal.cpython import ntpath, posixpath
from backlib.py313.internal.markers import techdebt
from backlib.py313.internal.utils.platform import is_nt, is_posix


if TYPE_CHECKING:
    from collections.abc import Iterable

    from backlib.py313.internal.backports.os import PathLike


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

__backlib__: str = "backlib.py313.os.path"


AnyStr = TypeVar("AnyStr", str, bytes)


# ---
# Version: Python 3.10.
# Explain: Changed in Python 3.10.
# ---


@techdebt.simplified
def realpath(path: AnyStr | PathLike[AnyStr], *, strict: bool = False) -> AnyStr:
    """Return the canonical path of the specified filename.

    See Also
    --------
    * `os.path.realpath`

    Technical Debt
    --------------
    * This may be an alias to `backlib.py313.os.path.abspath` (Windows, Python 3.9).
    """
    if sys.version_info >= (3, 10):
        return py_os_path.realpath(path, strict=strict)

    if is_posix():
        return posixpath.realpath(path, strict=strict)

    detail = f"{__backlib__}.realpath() is an alias to {__backlib__}.abspath()"
    warn(detail, RuntimeWarning, stacklevel=2)

    return py_os_path.abspath(path)  # noqa: PTH100


realpath.__module__ = __backlib__


# ---
# Version: Python 3.12.
# Explain: Added in Python 3.12.
# ---


def isjunction(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a junction.

    See Also
    --------
    * `os.path.isjunction`.
    """
    os_isjunction = posixpath.isjunction if is_posix() else ntpath.isjunction
    return os_isjunction(path)


@techdebt.simplified
def isdevdrive(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if pathname `path` is located on a Windows Dev Drive.

    See Also
    --------
    * `os.path.isdevdrive`.

    Technical Debt
    --------------
    * Always returns `False` on Windows.
    """
    if sys.version_info >= (3, 12):
        return py_os_path.isdevdrive(path)

    if is_nt():
        detail = f"{__backlib__}.isdevdrive() is returned as False"
        warn(detail, RuntimeWarning, stacklevel=2)

    os.fspath(path)
    return False


def splitroot(path: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr, AnyStr]:
    """Split the pathname `path` into a 3-item tuple `(drive, root, tail)`.

    See Also
    --------
    * `os.path.splitroot`.
    """
    os_splitroot = posixpath.splitroot if is_posix() else ntpath.splitroot
    return os_splitroot(path)


isdevdrive.__module__ = __backlib__
isjunction.__module__ = __backlib__
splitroot.__module__ = __backlib__


# ---
# Version: Python 3.13.
# Explain: Added in Python 3.13.
# ---


def isreserved(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is a reserved pathname on the current system.

    See Also
    --------
    * `os.path.isreserved`.
    """
    os_isreserved = posixpath.isreserved if is_posix() else ntpath.isreserved
    return os_isreserved(path)


isreserved.__module__ = __backlib__


# ---
# Version: Python 3.13.
# Explain: Changed in Python 3.13.
# ---


def commonpath(paths: Iterable[AnyStr | PathLike[AnyStr]]) -> AnyStr:
    """Return the longest common sub-path of each pathname in the iterable paths.

    See Also
    --------
    * `os.path.commonpath`.
    """
    os_commonpath = posixpath.commonpath if is_posix() else ntpath.commonpath
    return os_commonpath(paths)


def isabs(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an absolute pathname.

    See Also
    --------
    * `os.path.isabs`.
    """
    os_isabs = posixpath.isabs if is_posix() else ntpath.isabs
    return os_isabs(path)


commonpath.__module__ = __backlib__
isabs.__module__ = __backlib__


# ---
# Version: Python 3.9+
# Explain: No changes required.
# ---

abspath = py_os_path.abspath
basename = py_os_path.basename
commonprefix = py_os_path.commonprefix
dirname = py_os_path.dirname
exists = py_os_path.exists
expanduser = py_os_path.expanduser
expandvars = py_os_path.expandvars
getatime = py_os_path.getatime
getctime = py_os_path.getctime
getmtime = py_os_path.getmtime
getsize = py_os_path.getsize
isdir = py_os_path.isdir
isfile = py_os_path.isfile
islink = py_os_path.islink
ismount = py_os_path.ismount
join = py_os_path.join
lexists = py_os_path.lexists
normcase = py_os_path.normcase
normpath = py_os_path.normpath
relpath = py_os_path.relpath
samefile = py_os_path.samefile
sameopenfile = py_os_path.sameopenfile
samestat = py_os_path.samestat
split = py_os_path.split
splitdrive = py_os_path.splitdrive
splitext = py_os_path.splitext
supports_unicode_filenames = py_os_path.supports_unicode_filenames
