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
from string import ascii_letters, digits
from typing import Final

from backlib.internal.stdlib.py313.os import (
    PathLike,
    environ,
    fsdecode,
    fsencode,
    fspath,
    lstat,
    stat_result,
)
from backlib.internal.stdlib.py313.ospath.src.typing import StrOrBytesPath
from backlib.internal.typing import AnyStr
from backlib.internal.utils.lint import techdebt


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


@techdebt("See the 'Notes' section...")
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

    sep_index = max(p.rfind(sep), p.rfind(altsep))
    extsep_index = p.rfind(extsep)

    if extsep_index <= sep_index:
        return (p, p[:0])

    starts_with_extseps = all(
        p[index] == extsep
        for index in range(sep_index + 1, extsep_index + 1)
    )

    if starts_with_extseps:
        return (p, p[:0])

    return (p[:extsep_index], p[extsep_index:])


@techdebt("This function should be refactored...")
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


@techdebt("This function should be refactored...")
def expandvars(path: AnyStr | PathLike[AnyStr]) -> AnyStr:  # noqa: C901, PLR0912, PLR0915
    """Return the argument with environment variables expanded.

    See Also
    --------
    * `os.path.expandvars`.

    Version
    -------
    * Python 3.13.
    """
    path = fspath(path)
    if isinstance(path, bytes):
        if b"$" not in path and b"%" not in path:
            return path
        varchars = bytes(ascii_letters + digits + "_-", "ascii")
        quote = b"'"
        percent = b"%"
        brace = b"{"
        rbrace = b"}"
        dollar = b"$"
    else:
        if "$" not in path and "%" not in path:
            return path
        varchars = ascii_letters + digits + "_-"
        quote = "'"
        percent = "%"
        brace = "{"
        rbrace = "}"
        dollar = "$"
    res = path[:0]
    index = 0
    pathlen = len(path)
    while index < pathlen:
        c = path[index:index+1]
        if c == quote:   # no expansion within single quotes
            path = path[index + 1:]
            pathlen = len(path)
            try:
                index = path.index(c)
                res += c + path[:index + 1]
            except ValueError:
                res += c + path
                index = pathlen - 1
        elif c == percent:  # variable or '%'
            if path[index + 1:index + 2] == percent:
                res += c
                index += 1
            else:
                path = path[index+1:]
                pathlen = len(path)
                try:
                    index = path.index(percent)
                except ValueError:
                    res += percent + path
                    index = pathlen - 1
                else:
                    var = path[:index]
                    try:
                        if isinstance(var, bytes):  # 'os.environb' is not supported on Windows
                            value = fsencode(environ[fsdecode(var)])
                        else:
                            value = environ[var]
                    except KeyError:
                        value = percent + var + percent
                    res += value
        elif c == dollar:  # variable or '$$'
            if path[index + 1:index + 2] == dollar:
                res += c
                index += 1
            elif path[index + 1:index + 2] == brace:
                path = path[index+2:]
                pathlen = len(path)
                try:
                    index = path.index(rbrace)
                except ValueError:
                    res += dollar + brace + path
                    index = pathlen - 1
                else:
                    var = path[:index]
                    try:
                        if isinstance(var, bytes):  # 'os.environb' is not supported on Windows
                            value = fsencode(environ[fsdecode(var)])
                        else:
                            value = environ[var]
                    except KeyError:
                        value = dollar + brace + var + rbrace
                    res += value
            else:
                var = path[:0]
                index += 1
                c = path[index:index + 1]
                while c and c in varchars:
                    var += c
                    index += 1
                    c = path[index:index + 1]
                try:
                    if isinstance(var, bytes):  # 'os.environb' is not supported on Windows
                        value = fsencode(environ[fsdecode(var)])
                    else:
                        value = environ[var]
                except KeyError:
                    value = dollar + var
                res += value
                if c:
                    index -= 1
        else:
            res += c
        index += 1
    return res


@techdebt("This function should be refactored...")
def normpath(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Normalize a pathname by collapsing redundant separators and up-level references.

    See Also
    --------
    * `os.path.normpath`.

    Version
    -------
    * Python 3.13.
    """
    path = fspath(path)
    if isinstance(path, bytes):
        sep = b"\\"
        altsep = b"/"
        curdir = b"."
        pardir = b".."
    else:
        sep = "\\"
        altsep = "/"
        curdir = "."
        pardir = ".."
    path = path.replace(altsep, sep)
    drive, root, path = splitroot(path)
    prefix = drive + root
    comps = path.split(sep)
    i = 0
    while i < len(comps):
        if not comps[i] or comps[i] == curdir:
            del comps[i]
        elif comps[i] == pardir:
            if i > 0 and comps[i-1] != pardir:
                del comps[i-1:i+1]
                i -= 1
            elif i == 0 and root:
                del comps[i]
            else:
                i += 1
        else:
            i += 1
    # If the path is now empty, substitute '.'
    if not prefix and not comps:
        comps.append(curdir)
    return prefix + sep.join(comps)
