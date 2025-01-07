from __future__ import annotations

from stat import IO_REPARSE_TAG_MOUNT_POINT
from typing import overload

from backlib.internal.stdlib.py313.os import (
    PathLike,
    fsdecode,
    fsencode,
    fspath,
    lstat,
    stat_result,
)
from backlib.internal.stdlib.py313.ospath.src.typing import StrOrBytesPath
from backlib.internal.typing import AnyStr


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


@overload
def normcase(s: AnyStr) -> AnyStr:
    ...


@overload
def normcase(s: PathLike[AnyStr]) -> AnyStr:
    ...


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
