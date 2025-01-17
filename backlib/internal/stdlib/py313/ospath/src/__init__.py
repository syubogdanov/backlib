from __future__ import annotations

from typing import TYPE_CHECKING, Final, Literal

from backlib.internal.stdlib.py313.ntpath import abspath as nt_abspath
from backlib.internal.stdlib.py313.ntpath import basename as nt_basename
from backlib.internal.stdlib.py313.ntpath import commonpath as nt_commonpath
from backlib.internal.stdlib.py313.ntpath import commonprefix as nt_commonprefix
from backlib.internal.stdlib.py313.ntpath import dirname as nt_dirname
from backlib.internal.stdlib.py313.ntpath import exists as nt_exists
from backlib.internal.stdlib.py313.ntpath import expanduser as nt_expanduser
from backlib.internal.stdlib.py313.ntpath import expandvars as nt_expandvars
from backlib.internal.stdlib.py313.ntpath import getatime as nt_getatime
from backlib.internal.stdlib.py313.ntpath import getctime as nt_getctime
from backlib.internal.stdlib.py313.ntpath import getmtime as nt_getmtime
from backlib.internal.stdlib.py313.ntpath import getsize as nt_getsize
from backlib.internal.stdlib.py313.ntpath import isabs as nt_isabs
from backlib.internal.stdlib.py313.ntpath import isdevdrive as nt_isdevdrive
from backlib.internal.stdlib.py313.ntpath import isdir as nt_isdir
from backlib.internal.stdlib.py313.ntpath import isfile as nt_isfile
from backlib.internal.stdlib.py313.ntpath import isjunction as nt_isjunction
from backlib.internal.stdlib.py313.ntpath import islink as nt_islink
from backlib.internal.stdlib.py313.ntpath import ismount as nt_ismount
from backlib.internal.stdlib.py313.ntpath import isreserved as nt_isreserved
from backlib.internal.stdlib.py313.ntpath import join as nt_join
from backlib.internal.stdlib.py313.ntpath import lexists as nt_lexists
from backlib.internal.stdlib.py313.ntpath import normcase as nt_normcase
from backlib.internal.stdlib.py313.ntpath import normpath as nt_normpath
from backlib.internal.stdlib.py313.ntpath import realpath as nt_realpath
from backlib.internal.stdlib.py313.ntpath import relpath as nt_relpath
from backlib.internal.stdlib.py313.ntpath import samefile as nt_samefile
from backlib.internal.stdlib.py313.ntpath import sameopenfile as nt_sameopenfile
from backlib.internal.stdlib.py313.ntpath import samestat as nt_samestat
from backlib.internal.stdlib.py313.ntpath import split as nt_split
from backlib.internal.stdlib.py313.ntpath import splitdrive as nt_splitdrive
from backlib.internal.stdlib.py313.ntpath import splitext as nt_splitext
from backlib.internal.stdlib.py313.ntpath import splitroot as nt_splitroot
from backlib.internal.stdlib.py313.ntpath import (
    supports_unicode_filenames as nt_supports_unicode_filenames,
)
from backlib.internal.stdlib.py313.posixpath import abspath as posix_abspath
from backlib.internal.stdlib.py313.posixpath import basename as posix_basename
from backlib.internal.stdlib.py313.posixpath import commonpath as posix_commonpath
from backlib.internal.stdlib.py313.posixpath import commonprefix as posix_commonprefix
from backlib.internal.stdlib.py313.posixpath import dirname as posix_dirname
from backlib.internal.stdlib.py313.posixpath import exists as posix_exists
from backlib.internal.stdlib.py313.posixpath import expanduser as posix_expanduser
from backlib.internal.stdlib.py313.posixpath import expandvars as posix_expandvars
from backlib.internal.stdlib.py313.posixpath import getatime as posix_getatime
from backlib.internal.stdlib.py313.posixpath import getctime as posix_getctime
from backlib.internal.stdlib.py313.posixpath import getmtime as posix_getmtime
from backlib.internal.stdlib.py313.posixpath import getsize as posix_getsize
from backlib.internal.stdlib.py313.posixpath import isabs as posix_isabs
from backlib.internal.stdlib.py313.posixpath import isdevdrive as posix_isdevdrive
from backlib.internal.stdlib.py313.posixpath import isdir as posix_isdir
from backlib.internal.stdlib.py313.posixpath import isfile as posix_isfile
from backlib.internal.stdlib.py313.posixpath import isjunction as posix_isjunction
from backlib.internal.stdlib.py313.posixpath import islink as posix_islink
from backlib.internal.stdlib.py313.posixpath import ismount as posix_ismount
from backlib.internal.stdlib.py313.posixpath import isreserved as posix_isreserved
from backlib.internal.stdlib.py313.posixpath import join as posix_join
from backlib.internal.stdlib.py313.posixpath import lexists as posix_lexists
from backlib.internal.stdlib.py313.posixpath import normcase as posix_normcase
from backlib.internal.stdlib.py313.posixpath import normpath as posix_normpath
from backlib.internal.stdlib.py313.posixpath import realpath as posix_realpath
from backlib.internal.stdlib.py313.posixpath import relpath as posix_relpath
from backlib.internal.stdlib.py313.posixpath import samefile as posix_samefile
from backlib.internal.stdlib.py313.posixpath import sameopenfile as posix_sameopenfile
from backlib.internal.stdlib.py313.posixpath import samestat as posix_samestat
from backlib.internal.stdlib.py313.posixpath import split as posix_split
from backlib.internal.stdlib.py313.posixpath import splitdrive as posix_splitdrive
from backlib.internal.stdlib.py313.posixpath import splitext as posix_splitext
from backlib.internal.stdlib.py313.posixpath import splitroot as posix_splitroot
from backlib.internal.stdlib.py313.posixpath import (
    supports_unicode_filenames as posix_supports_unicode_filenames,
)
from backlib.internal.typing import AnyStr
from backlib.internal.utils.sys import is_nt, is_posix


if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence

    from backlib.internal.stdlib.py313.os import PathLike, stat_result


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


if not is_nt() and not is_posix():
    detail = "no os specific module found"
    raise ImportError(detail)


supports_unicode_filenames: Final[bool] = (
    nt_supports_unicode_filenames if is_nt() else posix_supports_unicode_filenames
)


def commonprefix(m: Sequence[AnyStr | PathLike[AnyStr]]) -> Literal[""] | AnyStr:
    """Return the longest path prefix that is a prefix of all paths.

    See Also
    --------
    * `os.path.commonprefix`.

    Version
    -------
    * Python 3.13.
    """
    os_commonprefix = nt_commonprefix if is_nt() else posix_commonprefix
    return os_commonprefix(m)


def getatime(filename: int | AnyStr | PathLike[AnyStr]) -> float:
    """Return the time of last access of `path`.

    See Also
    --------
    * `os.path.getatime`.

    Version
    -------
    * Python 3.13.
    """
    os_getatime = nt_getatime if is_nt() else posix_getatime
    return os_getatime(filename)


def getctime(filename: int | AnyStr | PathLike[AnyStr]) -> float:
    """Return the system's ctime which is the creation time for `path`.

    See Also
    --------
    * `os.path.getctime`.

    Version
    -------
    * Python 3.13.
    """
    os_getctime = nt_getctime if is_nt() else posix_getctime
    return os_getctime(filename)


def getmtime(filename: int | AnyStr | PathLike[AnyStr]) -> float:
    """Return the time of last modification of `path`.

    See Also
    --------
    * `os.path.getmtime`.

    Version
    -------
    * Python 3.13.
    """
    os_getmtime = nt_getmtime if is_nt() else posix_getmtime
    return os_getmtime(filename)


def getsize(filename: int | AnyStr | PathLike[AnyStr]) -> int:
    """Return the size, in bytes, of `path`.

    See Also
    --------
    * `os.path.getsize`.

    Version
    -------
    * Python 3.13.
    """
    os_getsize = nt_getsize if is_nt() else posix_getsize
    return os_getsize(filename)


def samestat(s1: stat_result, s2: stat_result) -> bool:
    """Return `True` if the stat tuples `stat1` and `stat2` refer to the same file.

    See Also
    --------
    * `os.path.samestat`.

    Version
    -------
    * Python 3.13.
    """
    os_samestat = nt_samestat if is_nt() else posix_samestat
    return os_samestat(s1, s2)


def samefile(f1: int | AnyStr | PathLike[AnyStr], f2: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if both pathname arguments refer to the same file or directory.

    See Also
    --------
    * `os.path.samefile`.

    Version
    -------
    * Python 3.13.
    """
    os_samefile = nt_samefile if is_nt() else posix_samefile
    return os_samefile(f1, f2)


def sameopenfile(fp1: int, fp2: int) -> bool:
    """Return `True` if the file descriptors `fp1` and `fp2` refer to the same file.

    See Also
    --------
    * `os.path.sameopenfile`.

    Version
    -------
    * Python 3.13.
    """
    os_sameopenfile = nt_sameopenfile if is_nt() else posix_sameopenfile
    return os_sameopenfile(fp1, fp2)


def isdir(s: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an existing directory.

    See Also
    --------
    * `os.path.isdir`.

    Version
    -------
    * Python 3.13.
    """
    os_isdir = nt_isdir if is_nt() else posix_isdir
    return os_isdir(s)


def isfile(path: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an existing regular file.

    See Also
    --------
    * `os.path.isfile`.

    Version
    -------
    * Python 3.13.
    """
    os_isfile = nt_isfile if is_nt() else posix_isfile
    return os_isfile(path)


def islink(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a symbolic link.

    See Also
    --------
    * `os.path.islink`.

    Version
    -------
    * Python 3.13.
    """
    os_islink = nt_islink if is_nt() else posix_islink
    return os_islink(path)


def exists(path: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing path or an open file descriptor.

    See Also
    --------
    * `os.path.exists`.

    Version
    -------
    * Python 3.13.
    """
    os_exists = nt_exists if is_nt() else posix_exists
    return os_exists(path)


def lexists(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing path, including broken symbolic links.

    See Also
    --------
    * `os.path.lexists`.

    Version
    -------
    * Python 3.13.
    """
    os_lexists = nt_lexists if is_nt() else posix_lexists
    return os_lexists(path)


def isjunction(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a junction.

    See Also
    --------
    * `os.path.isjunction`.

    Version
    -------
    * Python 3.13.
    """
    os_isjunction = nt_isjunction if is_nt() else posix_isjunction
    return os_isjunction(path)


def isdevdrive(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if pathname `path` is located on a Windows Dev Drive.

    See Also
    --------
    * `os.path.isdevdrive`.

    Version
    -------
    * Python 3.13.
    """
    os_isdevdrive = nt_isdevdrive if is_nt() else posix_isdevdrive
    return os_isdevdrive(path)


def normcase(s: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Normalize the case of a pathname.

    See Also
    --------
    * `os.path.normcase`.

    Version
    -------
    * Python 3.13.
    """
    os_normcase = nt_normcase if is_nt() else posix_normcase
    return os_normcase(s)


def isabs(s: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an absolute pathname.

    See Also
    --------
    * `os.path.isabs`.

    Version
    -------
    * Python 3.13.
    """
    os_isabs = nt_isabs if is_nt() else posix_isabs
    return os_isabs(s)


def splitext(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]:
    """Split the pathname `path` into a pair `(root, ext)`.

    See Also
    --------
    * `os.path.splitext`.

    Version
    -------
    * Python 3.13.
    """
    os_splitext = nt_splitext if is_nt() else posix_splitext
    return os_splitext(p)


def splitroot(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr, AnyStr]:
    """Split the pathname `path` into a 3-item tuple `(drive, root, tail)`.

    See Also
    --------
    * `os.path.splitroot`.

    Version
    -------
    * Python 3.13.
    """
    os_splitroot = nt_splitroot if is_nt() else posix_splitroot
    return os_splitroot(p)


def splitdrive(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]:
    """Split the pathname `path` into a pair `(drive, tail)`.

    See Also
    --------
    * `os.path.splitdrive`.

    Version
    -------
    * Python 3.13.
    """
    os_splitdrive = nt_splitdrive if is_nt() else posix_splitdrive
    return os_splitdrive(p)


def split(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]:
    """Split the pathname `path` into a pair `(head, tail)`.

    See Also
    --------
    * `os.path.split`.

    Version
    -------
    * Python 3.13.
    """
    os_split = nt_split if is_nt() else posix_split
    return os_split(p)


def basename(p: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Return the base name of pathname path.

    See Also
    --------
    * `os.path.basename`.

    Version
    -------
    * Python 3.13.
    """
    os_basename = nt_basename if is_nt() else posix_basename
    return os_basename(p)


def dirname(p: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Return the directory name of pathname `path`.

    See Also
    --------
    * `os.path.dirname`.

    Version
    -------
    * Python 3.13.
    """
    os_dirname = nt_dirname if is_nt() else posix_dirname
    return os_dirname(p)


def expandvars(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Return the argument with environment variables expanded.

    See Also
    --------
    * `os.path.expandvars`.

    Version
    -------
    * Python 3.13.
    """
    os_expandvars = nt_expandvars if is_nt() else posix_expandvars
    return os_expandvars(path)


def normpath(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Normalize a pathname by collapsing redundant separators and up-level references.

    See Also
    --------
    * `os.path.normpath`.

    Version
    -------
    * Python 3.13.
    """
    os_normpath = nt_normpath if is_nt() else posix_normpath
    return os_normpath(path)


def join(path: AnyStr | PathLike[AnyStr], *paths: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Join one or more path segments intelligently.

    See Also
    --------
    * `os.path.join`.

    Version
    -------
    * Python 3.13.
    """
    os_join = nt_join if is_nt() else posix_join
    return os_join(path, *paths)


def expanduser(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Replace an initial component of `~` or `~user` by that user's home directory.

    See Also
    --------
    * `os.path.expanduser`.

    Version
    -------
    * Python 3.13.
    """
    os_expanduser = nt_expanduser if is_nt() else posix_expanduser
    return os_expanduser(path)


def abspath(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Return a normalized absolutized version of the pathname `path`.

    See Also
    --------
    * `os.path.abspath`.

    Version
    -------
    * Python 3.13.
    """
    os_abspath = nt_abspath if is_nt() else posix_abspath
    return os_abspath(path)


def commonpath(paths: Iterable[AnyStr | PathLike[AnyStr]]) -> AnyStr:
    """Return the longest common sub-path of each pathname in the iterable paths.

    See Also
    --------
    * `os.path.commonpath`.

    Version
    -------
    * Python 3.13.
    """
    os_commonpath = nt_commonpath if is_nt() else posix_commonpath
    return os_commonpath(paths)


def ismount(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if pathname `path` is a mount point.

    See Also
    --------
    * `os.path.ismount`.

    Version
    -------
    * Python 3.13.
    """
    os_ismount = nt_ismount if is_nt() else posix_ismount
    return os_ismount(path)


def relpath(
    path: AnyStr | PathLike[AnyStr],
    start: AnyStr | PathLike[AnyStr] | None = None,
) -> AnyStr:
    """Return a relative filepath to `path`.

    See Also
    --------
    * `os.path.relpath`.

    Version
    -------
    * Python 3.13.
    """
    os_relpath = nt_relpath if is_nt() else posix_relpath
    return os_relpath(path, start)


def realpath(path: AnyStr | PathLike[AnyStr], *, strict: bool = False) -> AnyStr:  # noqa: ARG001
    """Return the canonical path of the specified filename.

    See Also
    --------
    * `os.path.realpath`.

    Version
    -------
    * Python 3.13.
    """
    os_realpath = nt_realpath if is_nt() else posix_realpath
    return os_realpath(path)


def isreserved(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is a reserved pathname on the current system.

    Notes
    -----
    * On POSIX `False` is always returned.

    See Also
    --------
    * `os.path.isreserved`.

    Version
    -------
    * Python 3.13.
    """
    os_isreserved = nt_isreserved if is_nt() else posix_isreserved
    return os_isreserved(path)
