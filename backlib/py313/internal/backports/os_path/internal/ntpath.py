from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from backlib.py313.internal.backports import os, stat
from backlib.py313.internal.backports.os_path.internal import genericpath


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
    path = os.fspath(path)
    if isinstance(path, bytes):
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
    normp = path.replace(altsep, sep)
    if normp[:1] == sep:
        if normp[1:2] == sep:
            # UNC drives, e.g. \\server\share or \\?\UNC\server\share
            # Device drives, e.g. \\.\device or \\?\device
            start = 8 if normp[:8].upper() == unc_prefix else 2
            index = normp.find(sep, start)
            if index == -1:
                return path, empty, empty
            index2 = normp.find(sep, index + 1)
            if index2 == -1:
                return path, empty, empty
            return path[:index2], path[index2 : index2 + 1], path[index2 + 1 :]
        else:
            # Relative path with root, e.g. \Windows
            return empty, path[:1], path[1:]
    elif normp[1:2] == colon:
        if normp[2:3] == sep:
            # Absolute drive-letter path, e.g. X:\Windows
            return path[:2], path[2:3], path[3:]
        else:
            # Relative path with drive, e.g. X:Windows
            return path[:2], empty, path[2:]
    else:
        # Relative path, e.g. Windows
        return empty, empty, path


_reserved_chars = frozenset(
    {chr(i) for i in range(32)} | {'"', "*", ":", "<", ">", "?", "|", "/", "\\"}
)

_reserved_names = frozenset(
    {"CON", "PRN", "AUX", "NUL", "CONIN$", "CONOUT$"}
    | {f"COM{c}" for c in "123456789\xb9\xb2\xb3"}
    | {f"LPT{c}" for c in "123456789\xb9\xb2\xb3"}
)


def isreserved(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is a reserved pathname on the current system.

    See Also
    --------
    * `ntpath.isreserved`.
    """
    # Refer to "Naming Files, Paths, and Namespaces":
    # https://docs.microsoft.com/en-us/windows/win32/fileio/naming-a-file
    path = os.fsdecode(splitroot(path)[2]).replace("/", "\\")
    return any(_isreservedname(name) for name in reversed(path.split("\\")))


def _isreservedname(name):
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
    paths = tuple(map(os.fspath, paths))
    if not paths:
        raise ValueError("commonpath() arg is an empty iterable")

    if isinstance(paths[0], bytes):
        sep = b"\\"
        altsep = b"/"
        curdir = b"."
    else:
        sep = "\\"
        altsep = "/"
        curdir = "."

    try:
        drivesplits = [splitroot(p.replace(altsep, sep).lower()) for p in paths]
        split_paths = [p.split(sep) for d, r, p in drivesplits]

        # Check that all drive letters or UNC paths match. The check is made only
        # now otherwise type errors for mixing strings and bytes would not be
        # caught.
        if len({d for d, r, p in drivesplits}) != 1:
            raise ValueError("Paths don't have the same drive")

        drive, root, path = splitroot(paths[0].replace(altsep, sep))
        if len({r for d, r, p in drivesplits}) != 1:
            if drive:
                raise ValueError("Can't mix absolute and relative paths")
            else:
                raise ValueError("Can't mix rooted and not-rooted paths")

        common = path.split(sep)
        common = [c for c in common if c and c != curdir]

        split_paths = [[c for c in s if c and c != curdir] for s in split_paths]
        s1 = min(split_paths)
        s2 = max(split_paths)
        for i, c in enumerate(s1):
            if c != s2[i]:
                common = common[:i]
                break
        else:
            common = common[: len(s1)]

        return drive + root + sep.join(common)
    except (TypeError, AttributeError):
        genericpath.check_arg_types("commonpath", *paths)
        raise


def isabs(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an absolute pathname.

    See Also
    --------
    * `ntpath.isabs`.
    """
    s = os.fspath(path)
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
    s = s[:3].replace(altsep, sep)
    # Absolute: UNC, device, and paths with a drive and root.
    return s.startswith(colon_sep, 1) or s.startswith(double_sep)
