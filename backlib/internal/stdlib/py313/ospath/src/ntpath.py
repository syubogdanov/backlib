"""Backports for the `os.path` module on Windows NT.

Notes
-----
* `os.path.isreserved` is not implemented as it is not cross-platform.

See Also
--------
* `ntpath`.
"""

from __future__ import annotations

from os.path import abspath as py_abspath
from stat import IO_REPARSE_TAG_MOUNT_POINT
from string import ascii_letters, digits
from typing import TYPE_CHECKING, Final

from backlib.internal.stdlib.py313.os import (
    PathLike,
    environ,
    fsdecode,
    fsencode,
    fspath,
    lstat,
)
from backlib.internal.stdlib.py313.ospath.src.utils import check_arg_types
from backlib.internal.typing import AnyStr
from backlib.internal.utils.lint import techdebt


if TYPE_CHECKING:
    from collections.abc import Iterable


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


def isjunction(path: AnyStr | PathLike[AnyStr]) -> bool:
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

    return bool(st.st_reparse_tag == IO_REPARSE_TAG_MOUNT_POINT)


@techdebt("See the 'Notes' section...")
def isdevdrive(path: AnyStr | PathLike[AnyStr]) -> bool:
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


@techdebt("This function should be refactored...")
def join(path: AnyStr | PathLike[AnyStr], *paths: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Join one or more path segments intelligently.

    See Also
    --------
    * `os.path.join`.

    Version
    -------
    * Python 3.13.
    """
    path = fspath(path)
    if isinstance(path, bytes):
        sep = b"\\"
        seps = b"\\/"
        colon_seps = b":\\/"
    else:
        sep = "\\"
        seps = "\\/"
        colon_seps = ":\\/"
    try:
        result_drive, result_root, result_path = splitroot(path)
        for p in paths:
            p_drive, p_root, p_path = splitroot(p)
            if p_root:
                # Second path is absolute
                if p_drive or not result_drive:
                    result_drive = p_drive
                result_root = p_root
                result_path = p_path
                continue
            if p_drive and p_drive != result_drive:
                if p_drive.lower() != result_drive.lower():
                    # Different drives => ignore the first path entirely
                    result_drive = p_drive
                    result_root = p_root
                    result_path = p_path
                    continue
                # Same drive in different case
                result_drive = p_drive
            # Second path is relative to the first
            if result_path and result_path[-1] not in seps:
                result_path = result_path + sep
            result_path = result_path + p_path
        ## add separator between UNC and non-absolute path
        if (result_path and not result_root and
            result_drive and result_drive[-1] not in colon_seps):
            return result_drive + sep + result_path
        return result_drive + result_root + result_path
    except (TypeError, AttributeError, BytesWarning):
        check_arg_types("join", path, *paths)
        raise


@techdebt("This function should be refactored...")
def expanduser(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Replace an initial component of `~` or `~user` by that user's home directory.

    See Also
    --------
    * `os.path.expanduser`.

    Version
    -------
    * Python 3.13.
    """
    path = fspath(path)
    if isinstance(path, bytes):
        seps = b"\\/"
        tilde = b"~"
    else:
        seps = "\\/"
        tilde = "~"
    if not path.startswith(tilde):
        return path
    i, n = 1, len(path)
    while i < n and path[i] not in seps:
        i += 1

    if "USERPROFILE" in environ:
        userhome = environ["USERPROFILE"]
    elif "HOMEPATH" not in environ:
        return path
    else:
        drive = environ.get("HOMEDRIVE", "")
        userhome = join(drive, environ["HOMEPATH"])

    if i != 1: #~user
        target_user = fsdecode(path[1:i]) if isinstance(path, bytes) else path[1:i]
        current_user = environ.get("USERNAME")

        if target_user != current_user:
            # Try to guess user home directory.  By default all user
            # profile directories are located in the same place and are
            # named by corresponding usernames.  If userhome isn't a
            # normal profile directory, this guess is likely wrong,
            # so we bail out.
            if current_user != basename(userhome):
                return path
            userhome = join(dirname(userhome), target_user)

    if isinstance(path, bytes):
        return fsencode(userhome) + path[i:]

    return userhome + path[i:]


@techdebt("[!] This function is not a real backport...")
def abspath(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Return a normalized absolutized version of the pathname `path`.

    See Also
    --------
    * `os.path.abspath`.

    Version
    -------
    * Python 3.13.
    """
    return py_abspath(path)  # noqa: PTH100


@techdebt("This function should be refactored...")
def commonpath(paths: Iterable[AnyStr | PathLike[AnyStr]]) -> AnyStr:
    """Return the longest common sub-path of each pathname in the iterable paths.

    See Also
    --------
    * `os.path.commonpath`.

    Version
    -------
    * Python 3.13.
    """
    fspaths = tuple(map(fspath, paths))
    if not fspaths:
        detail = "commonpath() arg is an empty iterable"
        raise ValueError(detail)

    if isinstance(fspaths[0], bytes):
        sep = b"\\"
        altsep = b"/"
        curdir = b"."
    else:
        sep = "\\"
        altsep = "/"
        curdir = "."

    try:
        drivesplits = [splitroot(p.replace(altsep, sep).lower()) for p in fspaths]
        split_paths = [p.split(sep) for _, _, p in drivesplits]

        # Check that all drive letters or UNC paths match. The check is made only
        # now otherwise type errors for mixing strings and bytes would not be
        # caught.
        if len({d for d, _, _ in drivesplits}) != 1:
            detail = "Paths don't have the same drive"
            raise ValueError(detail)

        drive, root, path = splitroot(fspaths[0].replace(altsep, sep))
        if len({r for _, r, _ in drivesplits}) != 1:
            if drive:
                detail = "Can't mix absolute and relative paths"
                raise ValueError(detail)
            detail = "Can't mix rooted and not-rooted paths"
            raise ValueError(detail)

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
            common = common[:len(s1)]

        return drive + root + sep.join(common)
    except (TypeError, AttributeError):
        check_arg_types("commonpath", *fspaths)
        raise


def ismount(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if pathname `path` is a mount point.

    See Also
    --------
    * `os.path.ismount`.

    Version
    -------
    * Python 3.13.
    """
    path = fspath(path)

    sep = b"\\" if isinstance(path, bytes) else "\\"
    altsep = b"/" if isinstance(path, bytes) else "/"

    path = abspath(path)
    drive, root, tail = splitroot(path)

    if drive.startswith((sep, altsep)):
        return not tail

    return bool(root and not tail)


@techdebt("This function should be refactored...")
def relpath(
    path: AnyStr | PathLike[AnyStr],
    start: AnyStr | PathLike[AnyStr] | None = None,
) -> AnyStr:
    """Return a relative filepath to `path`.

    See Also
    --------
    * `os.path.relpath`.

    Version
    -------
    * Python 3.13.
    """
    path = fspath(path)
    if not path:
        detail = "no path specified"
        raise ValueError(detail)

    if isinstance(path, bytes):
        sep = b"\\"
        curdir = b"."
        pardir = b".."
    else:
        sep = "\\"
        curdir = "."
        pardir = ".."

    start = curdir if start is None else fspath(start)

    try:
        start_abs = abspath(start)
        path_abs = abspath(path)
        start_drive, _, start_rest = splitroot(start_abs)
        path_drive, _, path_rest = splitroot(path_abs)
        if normcase(start_drive) != normcase(path_drive):
            detail = f"path is on mount {path_drive!r}, start on mount {start_drive!r}"
            raise ValueError(detail)  # noqa: TRY301

        start_list = start_rest.split(sep) if start_rest else []
        path_list = path_rest.split(sep) if path_rest else []
        # Work out how much of the filepath is shared by start and path.
        i = 0
        for e1, e2 in zip(start_list, path_list):
            if normcase(e1) != normcase(e2):
                break
            i += 1

        rel_list = [pardir] * (len(start_list)-i) + path_list[i:]
        if not rel_list:
            return curdir
        return sep.join(rel_list)
    except (TypeError, ValueError, AttributeError, BytesWarning, DeprecationWarning):
        check_arg_types("relpath", path, start)
        raise


@techdebt("See the 'Notes' section...")
def realpath(path: AnyStr | PathLike[AnyStr], *, strict: bool = False) -> AnyStr:  # noqa: ARG001
    """Return the canonical path of the specified filename.

    Notes
    -----
    * The `strict` parameter is always ignored. It will be fixed in the future;
    * The function is just an alias to `abspath`. It will be fixed in the future.

    See Also
    --------
    * `os.path.realpath`.

    Version
    -------
    * Python 3.13.
    """
    return abspath(path)
