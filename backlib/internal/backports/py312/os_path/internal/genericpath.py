from __future__ import annotations

from backlib.internal.backports.py312 import os


def isdevdrive(path: str | bytes | os.PathLike[str] | os.PathLike[bytes]) -> bool:
    """Return True if pathname path is located on a Windows Dev Drive.

    See Also
    --------
    * `genericpath.isdevdrive`.
    """
    os.fspath(path)
    return False
