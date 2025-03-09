from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from backlib.py313.internal.backports import os, stat
from backlib.py313.internal.backports.os_path.internal.cpython import genericpath


if TYPE_CHECKING:
    from collections.abc import Iterable

    from backlib.py313.internal.backports.os import PathLike


AnyStr = TypeVar("AnyStr", str, bytes)


def isjunction(path: AnyStr | PathLike[AnyStr]) -> bool:
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


def splitroot(path: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr, AnyStr]:
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


_reserved_chars = frozenset(
    {chr(i) for i in range(32)} | {'"', "*", ":", "<", ">", "?", "|", "/", "\\"},
)

_reserved_names = frozenset(
    {"CON", "PRN", "AUX", "NUL", "CONIN$", "CONOUT$"}
    | {f"COM{c}" for c in "123456789\xb9\xb2\xb3"}
    | {f"LPT{c}" for c in "123456789\xb9\xb2\xb3"},
)


def isreserved(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is a reserved pathname on the current system.

    See Also
    --------
    * `ntpath.isreserved`.
    """
    # Refer to "Naming Files, Paths, and Namespaces":
    # https://docs.microsoft.com/en-us/windows/win32/fileio/naming-a-file
    fspath = os.fsdecode(splitroot(path)[2]).replace("/", "\\")
    return any(_isreservedname(name) for name in reversed(fspath.split("\\")))


def _isreservedname(name: str) -> bool:
    """Return true if the filename is reserved by the system."""
    # Trailing dots and spaces are reserved.
    if name[-1:] in (".", " "):
        return name not in (".", "..")
    # Wildcards, separators, colon, and pipe (*?"<>/\:|) are reserved.
    # ASCII control characters (0-31) are reserved.
    # Colon is reserved for file streams (e.g. "name:stream[:type]").
    if _reserved_chars.intersection(name):
        return True
    # DOS device names are reserved (e.g. "nul" or "nul .txt"). The rules
    # are complex and vary across Windows versions. On the side of
    # caution, return True for names that may not be reserved.
    return name.partition(".")[0].rstrip(" ").upper() in _reserved_names


def commonpath(paths: Iterable[AnyStr | PathLike[AnyStr]]) -> AnyStr:
    """Return the longest common sub-path of each pathname in the iterable paths.

    See Also
    --------
    * `ntpath.commonpath`.
    """
    fspaths = [os.fspath(path) for path in paths]

    if not fspaths:
        detail = "commonpath() arg is an empty iterable"
        raise ValueError(detail)

    first_fspath = fspaths[0]

    sep = b"\\" if isinstance(first_fspath, bytes) else "\\"
    altsep = b"/" if isinstance(first_fspath, bytes) else "/"
    curdir = b"." if isinstance(first_fspath, bytes) else "."

    try:
        drivesplits = [splitroot(fspath.replace(altsep, sep).lower()) for fspath in fspaths]
        split_paths = [fspath.split(sep) for _, _, fspath in drivesplits]

        if len({d for d, _, _ in drivesplits}) != 1:
            detail = "Paths don't have the same drive"
            raise ValueError(detail)

        drive, root, path = splitroot(fspaths[0].replace(altsep, sep))

        if len({r for _, r, _ in drivesplits}) != 1:
            type1 = "absolute" if drive else "rooted"
            type2 = "relative" if drive else "not-rooted"
            detail = f"Can't mix {type1} and {type2} paths"
            raise ValueError(detail)

        common = path.split(sep)
        common = [component for component in common if component and component != curdir]

        split_paths = [
            [common for common in split_path if common and common != curdir]
            for split_path in split_paths
        ]

        s1 = min(split_paths)
        s2 = max(split_paths)

        for index, component in enumerate(s1):
            if component != s2[index]:
                common = common[:index]
                break
        else:
            common = common[: len(s1)]

    except (TypeError, AttributeError):
        genericpath.check_arg_types("commonpath", *fspaths)
        raise

    return drive + root + sep.join(common)


def isabs(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an absolute pathname.

    See Also
    --------
    * `ntpath.isabs`.
    """
    fspath = os.fspath(path)

    sep = b"\\" if isinstance(fspath, bytes) else "\\"
    altsep = b"/" if isinstance(fspath, bytes) else "/"

    colon_sep = b":\\" if isinstance(fspath, bytes) else ":\\"
    double_sep = b"\\\\" if isinstance(fspath, bytes) else "\\\\"

    prefix = fspath[:3].replace(altsep, sep)
    return prefix.startswith(double_sep) or prefix.endswith(colon_sep)
