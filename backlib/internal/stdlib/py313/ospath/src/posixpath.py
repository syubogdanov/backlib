from __future__ import annotations

from backlib.internal.stdlib.py313.os import PathLike, fspath
from backlib.internal.stdlib.py313.ospath.src import utils
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
    fspath(path)
    return False


def isdevdrive(path: StrOrBytesPath) -> bool:
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
        altsep = None

    else:
        sep = "/"
        extsep = "."
        altsep = None

    return utils.splitext(p, sep, altsep, extsep)
