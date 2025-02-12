from __future__ import annotations

from string import ascii_letters, digits
from typing import TYPE_CHECKING, Final, Literal

from backlib.internal.markers import techdebt
from backlib.internal.stdlib.py313.ntpath.src.utils import check_arg_types, is_reserved_name
from backlib.internal.stdlib.py313.os import (
    PathLike,
    environ,
    fsdecode,
    fsencode,
    fspath,
    fstat,
    getcwd,
    getcwdb,
    lstat,
    readlink,
    stat,
    stat_result,
)
from backlib.internal.stdlib.py313.stat import IO_REPARSE_TAG_MOUNT_POINT, S_ISDIR, S_ISLNK, S_ISREG
from backlib.internal.typing import AnyStr


if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence

    from backlib.internal.stdlib.py313.os import PathLike


__all__: list[str] = [
    "abspath",
    "basename",
    "commonpath",
    "commonprefix",
    "dirname",
    "exists",
    "expanduser",
    "expandvars",
    "getatime",
    "getctime",
    "getmtime",
    "getsize",
    "isabs",
    "isdevdrive",
    "isdir",
    "isfile",
    "isjunction",
    "islink",
    "ismount",
    "isreserved",
    "join",
    "lexists",
    "normcase",
    "normpath",
    "realpath",
    "relpath",
    "samefile",
    "sameopenfile",
    "samestat",
    "split",
    "splitdrive",
    "splitext",
    "splitroot",
    "supports_unicode_filenames",
]


supports_unicode_filenames: Final[bool] = True


def commonprefix(m: Sequence[AnyStr | PathLike[AnyStr]]) -> Literal[""] | AnyStr:
    """Return the longest path prefix that is a prefix of all paths.

    See Also
    --------
    * `ntpath.commonprefix`.

    Version
    -------
    * Python 3.13.
    """
    if not m:
        return ""

    paths = tuple(map(fspath, m))

    p1 = min(paths)
    p2 = max(paths)

    for index, character in enumerate(p1):
        if character != p2[index]:
            return p1[:index]

    return p1


def getatime(filename: int | AnyStr | PathLike[AnyStr]) -> float:
    """Return the time of last access of `path`.

    See Also
    --------
    * `ntpath.getatime`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_atime


def getctime(filename: int | AnyStr | PathLike[AnyStr]) -> float:
    """Return the system's ctime which is the creation time for `path`.

    See Also
    --------
    * `ntpath.getctime`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_ctime


def getmtime(filename: int | AnyStr | PathLike[AnyStr]) -> float:
    """Return the time of last modification of `path`.

    See Also
    --------
    * `ntpath.getmtime`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_mtime


def getsize(filename: int | AnyStr | PathLike[AnyStr]) -> int:
    """Return the size, in bytes, of `path`.

    See Also
    --------
    * `ntpath.getsize`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_size


def samestat(s1: stat_result, s2: stat_result) -> bool:
    """Return `True` if the stat tuples `stat1` and `stat2` refer to the same file.

    See Also
    --------
    * `ntpath.samestat`.

    Version
    -------
    * Python 3.13.
    """
    return s1.st_ino == s2.st_ino and s1.st_dev == s2.st_dev


def samefile(f1: int | AnyStr | PathLike[AnyStr], f2: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if both pathname arguments refer to the same file or directory.

    See Also
    --------
    * `ntpath.samefile`.

    Version
    -------
    * Python 3.13.
    """
    s1 = stat(f1)
    s2 = stat(f2)
    return samestat(s1, s2)


def sameopenfile(fp1: int, fp2: int) -> bool:
    """Return `True` if the file descriptors `fp1` and `fp2` refer to the same file.

    See Also
    --------
    * `ntpath.sameopenfile`.

    Version
    -------
    * Python 3.13.
    """
    s1 = fstat(fp1)
    s2 = fstat(fp2)
    return samestat(s1, s2)


def isdir(s: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an existing directory.

    See Also
    --------
    * `ntpath.isdir`.

    Version
    -------
    * Python 3.13.
    """
    try:
        st = stat(s)
    except (OSError, ValueError):
        return False
    return S_ISDIR(st.st_mode)


def isfile(path: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an existing regular file.

    See Also
    --------
    * `ntpath.isfile`.

    Version
    -------
    * Python 3.13.
    """
    try:
        st = stat(path)
    except (OSError, ValueError):
        return False
    return S_ISREG(st.st_mode)


def islink(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a symbolic link.

    See Also
    --------
    * `ntpath.islink`.

    Version
    -------
    * Python 3.13.
    """
    try:
        st = lstat(path)
    except (OSError, ValueError):
        return False
    return S_ISLNK(st.st_mode)


def exists(path: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing path or an open file descriptor.

    See Also
    --------
    * `ntpath.exists`.

    Version
    -------
    * Python 3.13.
    """
    try:
        stat(path)
    except (OSError, ValueError):
        return False
    return True


def lexists(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing path, including broken symbolic links.

    See Also
    --------
    * `ntpath.lexists`.

    Version
    -------
    * Python 3.13.
    """
    try:
        lstat(path)
    except (OSError, ValueError):
        return False
    return True


def isjunction(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a junction.

    See Also
    --------
    * `ntpath.isjunction`.

    Version
    -------
    * Python 3.13.
    """
    try:
        st = lstat(path)
    except (OSError, ValueError):
        return False
    return st.st_reparse_tag == IO_REPARSE_TAG_MOUNT_POINT


@techdebt
def isabs(s: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an absolute pathname.

    See Also
    --------
    * `ntpath.isabs`.

    Version
    -------
    * Python 3.13.
    """
    s = fspath(s)

    sep = b"\\" if isinstance(s, bytes) else "\\"
    altsep = b"/" if isinstance(s, bytes) else "/"
    colon_sep = b":\\" if isinstance(s, bytes) else ":\\"
    double_sep = b"\\\\" if isinstance(s, bytes) else "\\\\"

    prefix = s[:3].replace(altsep, sep)
    return prefix.startswith(colon_sep, 1) or prefix.startswith(double_sep)


@techdebt
def isdevdrive(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if pathname `path` is located on a Windows Dev Drive.

    See Also
    --------
    * `ntpath.isdevdrive`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * The functionality has been reduced.
    """
    fspath(path)
    return False


@techdebt
def normcase(s: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Normalize the case of a pathname.

    See Also
    --------
    * `ntpath.normcase`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * The functionality has been reduced.
    """
    s = fspath(s)

    if not isinstance(s, bytes):
        return s.replace("/", "\\").lower()

    return fsencode(fsdecode(s).replace("/", "\\").lower())


def splitext(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]:
    """Split the pathname `path` into a pair `(root, ext)`.

    See Also
    --------
    * `ntpath.splitext`.

    Version
    -------
    * Python 3.13.
    """
    p = fspath(p)

    sep = b"\\" if isinstance(p, bytes) else "\\"
    altsep = b"/" if isinstance(p, bytes) else "/"
    extsep = b"." if isinstance(p, bytes) else "."

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


@techdebt
def splitroot(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr, AnyStr]:  # noqa: PLR0911
    """Split the pathname `path` into a 3-item tuple `(drive, root, tail)`.

    See Also
    --------
    * `ntpath.splitroot`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * The functionality has been reduced;
    * This function should be refactored.
    """
    p = fspath(p)

    sep = b"\\" if isinstance(p, bytes) else "\\"
    altsep = b"/" if isinstance(p, bytes) else "/"
    colon = b":" if isinstance(p, bytes) else ":"
    double_sep = b"\\\\" if isinstance(p, bytes) else "\\\\"
    unc_prefix = b"\\\\?\\UNC\\" if isinstance(p, bytes) else "\\\\?\\UNC\\"

    normalized = p.replace(altsep, sep)

    if normalized.startswith(double_sep):
        start = 8 if normalized[:8].upper() == unc_prefix else 2
        index = normalized.find(sep, start)

        if index == -1:
            return (p, p[:0], p[:0])

        index2 = normalized.find(sep, index + 1)

        if index2 == -1:
            return (p, p[:0], p[:0])

        return (p[:index2], p[index2:index2 + 1], p[index2 + 1:])

    if normalized.startswith(sep):
        return (p[:0], sep, p[1:])

    if normalized[1:2] == colon:
        if normalized[2:3] == sep:
            return (p[:2], p[2:3], p[3:])
        return (p[:2], p[:0], p[2:])

    return (p[:0], p[:0], p)


def splitdrive(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]:
    """Split the pathname `path` into a pair `(drive, tail)`.

    See Also
    --------
    * `ntpath.splitdrive`.

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
    * `ntpath.split`.

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
    * `ntpath.basename`.

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
    * `ntpath.dirname`.

    Version
    -------
    * Python 3.13.
    """
    head, _ = split(p)
    return head


@techdebt
def join(path: AnyStr | PathLike[AnyStr], *paths: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Join one or more path segments intelligently.

    See Also
    --------
    * `ntpath.join`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function should be refactored.
    """
    path = fspath(path)

    sep = b"\\" if isinstance(path, bytes) else "\\"
    seps = b"\\/" if isinstance(path, bytes) else "\\/"
    colon_seps = b":\\/" if isinstance(path, bytes) else ":\\/"

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


@techdebt
def normpath(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Normalize a pathname by collapsing redundant separators and up-level references.

    See Also
    --------
    * `ntpath.normpath`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * The functionality has been reduced;
    * This function should be refactored.
    """
    path = fspath(path)

    sep = b"\\" if isinstance(path, bytes) else "\\"
    altsep = b"/" if isinstance(path, bytes) else "/"
    curdir = b"." if isinstance(path, bytes) else "."
    pardir = b".." if isinstance(path, bytes) else ".."

    path = path.replace(altsep, sep)
    drive, root, path = splitroot(path)
    prefix = drive + root
    components = path.split(sep)

    index = 0

    while index < len(components):
        if not components[index] or components[index] == curdir:
            del components[index]
            continue

        if components[index] != pardir:
            index += 1
            continue

        if index > 0 and components[index - 1] != pardir:
            del components[index - 1 : index + 1]
            index -= 1
            continue

        if index == 0 and root:
            del components[index]
            continue

        index += 1

    if not prefix and not components:
        return curdir

    return prefix + sep.join(components)


@techdebt
def abspath(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Return a normalized absolutized version of the pathname `path`.

    See Also
    --------
    * `ntpath.abspath`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * The functionality has been reduced.
    """
    path = fspath(path)

    if isabs(path):
        return normpath(path)

    cwd = getcwdb() if isinstance(path, bytes) else getcwd()
    path = join(cwd, path)

    return normpath(path)


@techdebt
def ismount(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if pathname `path` is a mount point.

    See Also
    --------
    * `ntpath.ismount`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * The functionality has been reduced.
    """
    path = fspath(path)

    sep = b"\\" if isinstance(path, bytes) else "\\"
    altsep = b"/" if isinstance(path, bytes) else "/"

    path = abspath(path)
    drive, root, tail = splitroot(path)

    if drive.startswith((sep, altsep)):
        return not tail

    return bool(root and not tail)


def realpath(path: AnyStr | PathLike[AnyStr], *, strict: bool = False) -> AnyStr:
    """Return the canonical path of the specified filename.

    See Also
    --------
    * `ntpath.realpath`.

    Version
    -------
    * Python 3.13.
    """
    path = abspath(path)

    target = path
    seen = {target}

    try:
        st = lstat(target)

        while S_ISLNK(st.st_mode):
            target = readlink(target)
            target = abspath(target)

            if target in seen:
                detail = "Symlink loop is encountered"
                raise OSError(None, detail, path)  # noqa: TRY301

            seen.add(target)
            st = lstat(target)

    except OSError:
        if strict:
            raise

    return target


def isreserved(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is a reserved pathname on the current system.

    See Also
    --------
    * `ntpath.isreserved`.

    Version
    -------
    * Python 3.13.
    """
    _, _, relative_to_root = splitroot(path)

    sep = "\\"
    altsep = "/"

    tail = fsdecode(relative_to_root)
    tail = tail.replace(altsep, sep)

    return any(is_reserved_name(name) for name in tail.split(sep))


def relpath(
    path: AnyStr | PathLike[AnyStr],
    start: AnyStr | PathLike[AnyStr] | None = None,
) -> AnyStr:
    """Return a relative filepath to `path`.

    See Also
    --------
    * `ntpath.relpath`.

    Version
    -------
    * Python 3.13.
    """
    if not (path := fspath(path)):
        detail = "no path specified"
        raise ValueError(detail)

    sep = b"\\" if isinstance(path, bytes) else "\\"
    curdir = b"." if isinstance(path, bytes) else "."
    pardir = b".." if isinstance(path, bytes) else ".."

    start = curdir if start is None else fspath(start)

    try:
        absolute_start = abspath(start)
        absolute_path = abspath(path)

        start_drive, _, start_tail = splitroot(absolute_start)
        path_drive, _, path_tail = splitroot(absolute_path)

        if normcase(start_drive) != normcase(path_drive):
            detail = f"path is on mount {path_drive!r}, start on mount {start_drive!r}"
            raise ValueError(detail)  # noqa: TRY301

        start_components = start_tail.split(sep) if start_tail else []
        path_components = path_tail.split(sep) if path_tail else []

        count = 0

        for start_component, path_component in zip(start_components, path_components):
            if normcase(start_component) != normcase(path_component):
                break
            count += 1

        components = [pardir] * (len(start_components) - count) + path_components[count:]
        return sep.join(components) if components else curdir

    except (TypeError, ValueError, AttributeError, BytesWarning, DeprecationWarning):
        check_arg_types("relpath", path, start)
        raise


@techdebt
def commonpath(paths: Iterable[AnyStr | PathLike[AnyStr]]) -> AnyStr:
    """Return the longest common sub-path of each pathname in the iterable paths.

    See Also
    --------
    * `ntpath.commonpath`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * The function should be refactored.
    """
    paths = [fspath(p) for p in paths]

    if not paths:
        detail = "commonpath() arg is an empty iterable"
        raise ValueError(detail)

    sep = b"\\" if isinstance(paths[0], bytes) else "\\"
    altsep = b"/" if isinstance(paths[0], bytes) else "/"
    curdir = b"." if isinstance(paths[0], bytes) else "."

    try:
        drivesplits = [splitroot(p.replace(altsep, sep).lower()) for p in paths]  # type: ignore[arg-type, union-attr]
        split_paths = [p.split(sep) for _, _, p in drivesplits]

        if len({d for d, _, _ in drivesplits}) != 1:
            detail = "Paths don't have the same drive"
            raise ValueError(detail)

        drive, root, path = splitroot(paths[0].replace(altsep, sep))  # type: ignore[arg-type, union-attr]

        if len({r for _, r, _ in drivesplits}) != 1:
            m1 = "absolute" if drive else "rooted"
            m2 = "relative" if drive else "not-rooted"
            detail = f"Can't mix {m1} and {m2} paths"
            raise ValueError(detail)

        common = path.split(sep)
        common = [c for c in common if c and c != curdir]

        split_paths = [[c for c in s if c and c != curdir] for s in split_paths]

        s1 = min(split_paths)
        s2 = max(split_paths)

        for index, char in enumerate(s1):
            if char != s2[index]:
                common = common[:index]
                break
        else:
            common = common[:len(s1)]

        return drive + root + sep.join(common)

    except (TypeError, AttributeError):
        check_arg_types("commonpath", *paths)
        raise


@techdebt
def expanduser(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Replace an initial component of `~` or `~user` by that user's home directory.

    See Also
    --------
    * `ntpath.expanduser`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * The function should be refactored.
    """
    path = fspath(path)

    seps = b"\\/" if isinstance(path, bytes) else "\\/"
    tilde = b"~" if isinstance(path, bytes) else "~"

    if not path.startswith(tilde):
        return path

    sep_index = 1

    while sep_index < len(path) and path[sep_index] not in seps:
        sep_index += 1

    if "USERPROFILE" in environ:
        userhome = environ["USERPROFILE"]
    elif "HOMEPATH" not in environ:
        return path
    else:
        drive = environ.get("HOMEDRIVE", "")
        userhome = join(drive, environ["HOMEPATH"])

    if sep_index > 1:
        target_user = path[1:sep_index]

        if isinstance(target_user, bytes):
            target_user = fsdecode(target_user)  # type: ignore[assignment]

        current_user = environ.get("USERNAME")

        if target_user != current_user:
            if current_user != basename(userhome):
                return path
            userhome = join(dirname(userhome), target_user)  # type: ignore[assignment,type-var]

    if isinstance(path, bytes):
        userhome = fsencode(userhome)  # type: ignore[assignment]
        return userhome + path[sep_index:]  # type: ignore[operator,return-value]

    return userhome + path[sep_index:]


@techdebt
def expandvars(path: AnyStr | PathLike[AnyStr]) -> AnyStr:  # noqa: C901, PLR0912, PLR0915
    """Return the argument with environment variables expanded.

    See Also
    --------
    * `ntpath.expandvars`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * The function should be refactored.
    """
    path = fspath(path)

    quote = b"'" if isinstance(path, bytes) else "'"
    percent = b"%" if isinstance(path, bytes) else "%"
    brace = b"{" if isinstance(path, bytes) else "{"
    rbrace = b"}" if isinstance(path, bytes) else "}"
    dollar = b"$" if isinstance(path, bytes) else "$"

    if isinstance(path, bytes):
        if b"$" not in path and b"%" not in path:
            return path
        varchars = bytes(ascii_letters + digits + "_-", "ascii")
        env = None

    else:
        if "$" not in path and "%" not in path:
            return path
        varchars = ascii_letters + digits + "_-"
        env = environ

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
                        value = fsencode(environ[fsdecode(var)]) if env is None else env[var]
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
                        value = fsencode(environ[fsdecode(var)]) if env is None else env[var]
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
                    value = fsencode(environ[fsdecode(var)]) if env is None else env[var]
                except KeyError:
                    value = dollar + var
                res += value
                if c:
                    index -= 1
        else:
            res += c
        index += 1
    return res
