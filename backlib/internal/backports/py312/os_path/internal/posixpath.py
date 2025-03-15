from __future__ import annotations

from typing import TypeVar

from backlib.internal.backports.py312 import os


AnyStr = TypeVar("AnyStr", str, bytes)


def isjunction(path: str | bytes | os.PathLike[str] | os.PathLike[bytes]) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a junction.

    See Also
    --------
    * `posixpath.isjunction`.
    """
    os.fspath(path)
    return False


def splitroot(path: AnyStr | os.PathLike[AnyStr]) -> tuple[AnyStr, AnyStr, AnyStr]:
    """Split the pathname `path` into a 3-item tuple `(drive, root, tail)`.

    See Also
    --------
    * `posixpath.splitroot`.
    """
    fspath = os.fspath(path)

    sep = b"/" if isinstance(fspath, bytes) else "/"

    if fspath[:1] != sep:
        return (fspath[:0], fspath[:0], fspath)

    if fspath[1:2] != sep or fspath[2:3] == sep:
        return (fspath[:0], sep, fspath[1:])

    return (fspath[:0], fspath[:2], fspath[2:])
