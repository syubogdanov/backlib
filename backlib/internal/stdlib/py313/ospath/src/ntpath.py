"""Backports for the `os.path` module on Windows NT.

Notes
-----
* `os.path.isreserved` is not implemented as it is not cross-platform.

See Also
--------
* `ntpath`.
"""

from __future__ import annotations

from stat import IO_REPARSE_TAG_MOUNT_POINT
from typing import Final

from backlib.internal.stdlib.py313.os import (
    PathLike,
    fsdecode,
    fsencode,
    fspath,
    lstat,
    stat_result,
)
from backlib.internal.stdlib.py313.ospath.src import utils
from backlib.internal.stdlib.py313.ospath.src.typing import StrOrBytesPath
from backlib.internal.typing import AnyStr
from backlib.internal.utils.lint import todo


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


supports_unicode_filenames: Final[bool] = True


def isjunction(path: StrOrBytesPath) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a junction.

    See Also
    --------
    * `os.path.isjunction`.

    Version
    -------
    * Python 3.13.
    """
    try:
        st = lstat(path)

    except (AttributeError, OSError, ValueError):
        return False

    if not hasattr(stat_result, "st_reparse_tag"):
        return False

    return bool(st.st_reparse_tag == IO_REPARSE_TAG_MOUNT_POINT)


@todo("See the 'Notes' section...")
def isdevdrive(path: StrOrBytesPath) -> bool:
    """Return `True` if pathname `path` is located on a Windows Dev Drive.

    Notes
    -----
    * Always returns `False`. It will be fixed in the future.

    See Also
    --------
    * `os.path.isdevdrive`.

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
    * `os.path.normcase`.

    Version
    -------
    * Python 3.13.
    """
    s = fspath(s)

    if not isinstance(s, bytes):
        return s.replace("/", "\\").lower()

    filename = fsdecode(s).replace("/", "\\").lower()
    return fsencode(filename)


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

    if isinstance(s, bytes):
        sep = b"\\"
        altsep = b"/"
        colon_sep = b":\\"
        double_sep = b"\\\\"

    else:
        sep = "\\"
        altsep = "/"
        colon_sep = ":\\"
        double_sep = "\\\\"

    prefix = s[:3].replace(altsep, sep)
    return prefix.startswith(colon_sep, 1) or prefix.startswith(double_sep)


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
        sep = b"\\"
        altsep = b"/"
        extsep = b"."

    else:
        sep = "\\"
        altsep = "/"
        extsep = "."

    return utils.splitext(p, sep, altsep, extsep)


@todo("This function should be refactored...")
def splitroot(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr, AnyStr]:  # noqa: PLR0911
    """Split the pathname `path` into a 3-item tuple `(drive, root, tail)`.

    See Also
    --------
    * `os.path.splitdrive`.

    Version
    -------
    * Python 3.13.
    """
    p = fspath(p)

    if isinstance(p, bytes):
        sep = b"\\"
        altsep = b"/"
        colon = b":"
        unc_prefix = b"\\\\?\\UNC\\"
        empty = b""

    else:
        sep = "\\"
        altsep = "/"
        colon = ":"
        unc_prefix = "\\\\?\\UNC\\"
        empty = ""

    normp = p.replace(altsep, sep)
    if normp[:1] == sep:
        if normp[1:2] == sep:
            # UNC drives, e.g. \\server\share or \\?\UNC\server\share
            # Device drives, e.g. \\.\device or \\?\device
            start = 8 if normp[:8].upper() == unc_prefix else 2
            index = normp.find(sep, start)
            if index == -1:
                return p, empty, empty
            index2 = normp.find(sep, index + 1)
            if index2 == -1:
                return p, empty, empty
            return p[:index2], p[index2:index2 + 1], p[index2 + 1:]
        # Relative path with root, e.g. \Windows
        return empty, p[:1], p[1:]
    if normp[1:2] == colon:
        if normp[2:3] == sep:
            # Absolute drive-letter path, e.g. X:\Windows
            return p[:2], p[2:3], p[3:]
        # Relative path with drive, e.g. X:Windows
        return p[:2], empty, p[2:]
    # Relative path, e.g. Windows
    return empty, empty, p


def splitdrive(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]:
    """Split the pathname `path` into a pair `(drive, tail)`.

    See Also
    --------
    * `os.path.splitdrive`.

    Version
    -------
    * Python 3.13.
    """
    drive, root, tail = splitroot(p)
    return (drive, root + tail)


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

    sep = b"\\" if isinstance(p, bytes) else "\\"
    altsep = b"/" if isinstance(p, bytes) else "/"

    drive, root, tail = splitroot(p)

    sep_index = p.rfind(sep)
    altsep_index = p.rfind(altsep)

    index = max(sep_index + 1, altsep_index + 1)
    head, tail = p[:index], p[index:]

    return (drive + root + head.rstrip(sep + altsep), tail)


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
