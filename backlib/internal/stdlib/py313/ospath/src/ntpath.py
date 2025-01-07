from stat import IO_REPARSE_TAG_MOUNT_POINT

from backlib.internal.stdlib.py313.os import fspath, lstat, stat_result
from backlib.internal.stdlib.py313.ospath.src.typing import StrOrBytesPath


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
