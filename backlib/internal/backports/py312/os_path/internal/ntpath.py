from __future__ import annotations

from typing import TypeVar

from backlib.internal.backports.py312 import os, stat


AnyStr = TypeVar("AnyStr", str, bytes)


def isjunction(path: str | bytes | os.PathLike[str] | os.PathLike[bytes]) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a junction.

    See Also
    --------
    * `ntpath.isjunction`.
    """
    try:
        st = os.lstat(path)
    except (OSError, ValueError):
        return False
    return st.st_reparse_tag == stat.IO_REPARSE_TAG_MOUNT_POINT


def splitroot(path: AnyStr | os.PathLike[AnyStr]) -> tuple[AnyStr, AnyStr, AnyStr]:
    """Split the pathname `path` into a 3-item tuple `(drive, root, tail)`.

    See Also
    --------
    * `ntpath.splitroot`.
    """
    fspath = os.fspath(path)

    sep = b"\\" if isinstance(fspath, bytes) else "\\"
    double_sep = b"\\\\" if isinstance(fspath, bytes) else "\\\\"
    altsep = b"/" if isinstance(fspath, bytes) else "/"
    colon = b":" if isinstance(fspath, bytes) else ":"
    unc_prefix = b"\\\\?\\UNC\\" if isinstance(fspath, bytes) else "\\\\?\\UNC\\"

    normalized = fspath.replace(altsep, sep)

    if normalized.startswith(double_sep):
        prefix = normalized[: len(unc_prefix)]
        start = 8 if prefix.upper() == unc_prefix else 2

        if ((index1 := normalized.find(sep, start)) == -1) or (
            (index2 := normalized.find(sep, index1 + 1)) == -1
        ):
            return (fspath, fspath[:0], fspath[:0])

        return (fspath[:index2], fspath[index2 : index2 + 1], fspath[index2 + 1 :])

    if normalized.startswith(sep):
        return (fspath[:0], fspath[:1], fspath[1:])

    if normalized[1:2] != colon:
        return (fspath[:0], fspath[:0], fspath)

    if normalized[2:3] == sep:
        return (fspath[:2], fspath[2:3], fspath[3:])

    return fspath[:2], fspath[:0], fspath[2:]
