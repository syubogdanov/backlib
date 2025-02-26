from __future__ import annotations

import re

from typing import TYPE_CHECKING, Literal, TypeVar

from backlib.py313.internal.backports.errno import ENOTDIR
from backlib.py313.internal.backports.os import (
    environ,
    environb,
    fsencode,
    fspath,
    fstat,
    getcwd,
    getcwdb,
    lstat,
    readlink,
    stat,
    stat_result,
    strerror,
)
from backlib.py313.internal.backports.posixpath.internal.utils import check_arg_types
from backlib.py313.internal.backports.stat import S_ISDIR, S_ISLNK, S_ISREG
from backlib.py313.internal.markers import techdebt
from backlib.py313.internal.utils.platform import is_vxworks


if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence

    from backlib.py313.internal.backports.os import PathLike


AnyStr = TypeVar("AnyStr", bytes, str)


def commonprefix(m: Sequence[AnyStr | PathLike[AnyStr]]) -> Literal[""] | AnyStr:
    """Return the longest path prefix that is a prefix of all paths.

    See Also
    --------
    * `posixpath.commonprefix`.

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
    * `posixpath.getatime`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_atime


def getctime(filename: int | AnyStr | PathLike[AnyStr]) -> float:
    """Return the system's ctime which is the creation time for `path`.

    See Also
    --------
    * `posixpath.getctime`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_ctime


def getmtime(filename: int | AnyStr | PathLike[AnyStr]) -> float:
    """Return the time of last modification of `path`.

    See Also
    --------
    * `posixpath.getmtime`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_mtime


def getsize(filename: int | AnyStr | PathLike[AnyStr]) -> int:
    """Return the size, in bytes, of `path`.

    See Also
    --------
    * `posixpath.getsize`.

    Version
    -------
    * Python 3.13.
    """
    return stat(filename).st_size


def samestat(s1: stat_result, s2: stat_result) -> bool:
    """Return `True` if the stat tuples `stat1` and `stat2` refer to the same file.

    See Also
    --------
    * `posixpath.samestat`.

    Version
    -------
    * Python 3.13.
    """
    return s1.st_ino == s2.st_ino and s1.st_dev == s2.st_dev


def samefile(f1: int | AnyStr | PathLike[AnyStr], f2: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if both pathname arguments refer to the same file or directory.

    See Also
    --------
    * `posixpath.samefile`.

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
    * `posixpath.sameopenfile`.

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
    * `posixpath.isdir`.

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
    * `posixpath.isfile`.

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
    * `posixpath.islink`.

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
    * `posixpath.exists`.

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
    * `posixpath.lexists`.

    Version
    -------
    * Python 3.13.
    """
    try:
        lstat(path)
    except (OSError, ValueError):
        return False
    return True


def isreserved(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is a reserved pathname on the current system.

    Notes
    -----
    * As opposed to `posixpath`, `isreserved` is defined.

    See Also
    --------
    * `posixpath.isreserved`.

    Version
    -------
    * Python 3.13.
    """
    fspath(path)
    return False


def isabs(s: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an absolute pathname.

    See Also
    --------
    * `posixpath.isabs`.

    Version
    -------
    * Python 3.13.
    """
    s = fspath(s)
    sep = b"/" if isinstance(s, bytes) else "/"
    return s.startswith(sep)


def isdevdrive(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if pathname `path` is located on a Windows Dev Drive.

    See Also
    --------
    * `posixpath.isdevdrive`.

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
    * `posixpath.normcase`.

    Version
    -------
    * Python 3.13.
    """
    return fspath(s)


def splitext(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]:
    """Split the pathname `path` into a pair `(root, ext)`.

    See Also
    --------
    * `posixpath.splitext`.

    Version
    -------
    * Python 3.13.
    """
    p = fspath(p)

    sep = b"/" if isinstance(p, bytes) else "/"
    extsep = b"." if isinstance(p, bytes) else "."

    sep_index = p.rfind(sep)
    extsep_index = p.rfind(extsep)

    if extsep_index <= sep_index:
        return (p, p[:0])

    starts_with_extseps = all(
        p[index] == extsep for index in range(sep_index + 1, extsep_index + 1)
    )

    if starts_with_extseps:
        return (p, p[:0])

    return (p[:extsep_index], p[extsep_index:])


def isjunction(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a junction.

    See Also
    --------
    * `posixpath.isjunction`.

    Version
    -------
    * Python 3.13.
    """
    fspath(path)
    return False


@techdebt.simplified
def splitroot(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr, AnyStr]:
    """Split the pathname `path` into a 3-item tuple `(drive, root, tail)`.

    See Also
    --------
    * `posixpath.splitroot`.

    Version
    -------
    * Python 3.13.
    """
    p = fspath(p)

    sep = b"/" if isinstance(p, bytes) else "/"

    double_sep = sep * 2
    triple_sep = sep * 3

    if not p.startswith(sep):
        return (p[:0], p[:0], p)

    if not p.startswith(double_sep) or p.startswith(triple_sep):
        return (p[:0], sep, p[1:])

    return (p[:0], p[:2], p[2:])


def splitdrive(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]:
    """Split the pathname `path` into a pair `(drive, tail)`.

    See Also
    --------
    * `posixpath.splitdrive`.

    Version
    -------
    * Python 3.13.
    """
    p = fspath(p)
    return (p[:0], p)


def split(p: AnyStr | PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]:
    """Split the pathname `path` into a pair `(head, tail)`.

    See Also
    --------
    * `posixpath.split`.

    Version
    -------
    * Python 3.13.
    """
    p = fspath(p)

    sep = b"/" if isinstance(p, bytes) else "/"
    index = p.rfind(sep) + 1

    head, tail = p[:index], p[index:]

    if head and head != sep * len(head):
        head = head.rstrip(sep)

    return (head, tail)


def basename(p: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Return the base name of pathname path.

    See Also
    --------
    * `posixpath.basename`.

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
    * `posixpath.dirname`.

    Version
    -------
    * Python 3.13.
    """
    head, _ = split(p)
    return head


def normpath(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Normalize a pathname by collapsing redundant separators and up-level references.

    See Also
    --------
    * `posixpath.normpath`.

    Version
    -------
    * Python 3.13.
    """
    path = fspath(path)

    sep = b"/" if isinstance(path, bytes) else "/"
    dot = b"." if isinstance(path, bytes) else "."
    dotdot = b".." if isinstance(path, bytes) else ".."

    if not path:
        return dot

    _, root, tail = splitroot(path)
    components: list[AnyStr] = []

    for component in tail.split(sep):
        if not component or component == dot:
            continue

        if component != dotdot:
            components.append(component)
            continue

        if not root and not components:
            components.append(component)
            continue

        if components and components[-1] == dotdot:
            components.append(component)
            continue

        if components:
            components.pop()

    path = root + sep.join(components)
    return path or dot


@techdebt.refactor
def relpath(
    path: AnyStr | PathLike[AnyStr],
    start: AnyStr | PathLike[AnyStr] | None = None,
) -> AnyStr:
    """Return a relative filepath to `path`.

    See Also
    --------
    * `posixpath.relpath`.

    Version
    -------
    * Python 3.13.
    """
    path = fspath(path)

    if not path:
        detail = "no path specified"
        raise ValueError(detail)

    curdir = b"." if isinstance(path, bytes) else "."
    sep = b"/" if isinstance(path, bytes) else "/"
    pardir = b".." if isinstance(path, bytes) else ".."

    start = curdir if start is None else fspath(start)

    try:
        start_tail = abspath(start).lstrip(sep)
        path_tail = abspath(path).lstrip(sep)

        start_list = start_tail.split(sep) if start_tail else []
        path_list = path_tail.split(sep) if path_tail else []

        index = len(commonprefix([start_list, path_list]))  # type: ignore[type-var]
        components = [pardir] * (len(start_list) - index) + path_list[index:]

        if not components:
            return curdir

        return sep.join(components)

    except (TypeError, AttributeError, BytesWarning, DeprecationWarning):
        check_arg_types("relpath", path, start)
        raise


@techdebt.refactor
def realpath(  # noqa: C901, PLR0915
    path: AnyStr | PathLike[AnyStr],
    *,
    strict: bool = False,
) -> AnyStr:
    """Return the canonical path of the specified filename.

    See Also
    --------
    * `posixpath.realpath`.

    Version
    -------
    * Python 3.13.
    """
    filename = fspath(path)

    sep = b"/" if isinstance(filename, bytes) else "/"
    curdir = b"." if isinstance(filename, bytes) else "."
    pardir = b".." if isinstance(filename, bytes) else ".."
    cwd = getcwdb() if isinstance(filename, bytes) else getcwd()

    rest = filename.split(sep)[::-1]
    part_count = len(rest)
    path = sep if filename.startswith(sep) else cwd

    seen: dict[AnyStr, AnyStr] = {}

    while part_count:
        name = rest.pop()
        if name is None:
            seen[rest.pop()] = path
            continue
        part_count -= 1
        if not name or name == curdir:
            continue
        if name == pardir:
            path = path[: path.rindex(sep)] or sep
            continue
        newpath = path + name if path == sep else path + sep + name
        try:
            st_mode = lstat(newpath).st_mode
            if not S_ISLNK(st_mode):
                if strict and part_count and not S_ISDIR(st_mode):
                    raise OSError(ENOTDIR, strerror(ENOTDIR), newpath)  # noqa: TRY301
                path = newpath
                continue
            if newpath in seen:
                # Already seen this path
                path = seen[newpath]
                if path is not None:
                    continue
                if strict:
                    stat(newpath)
                path = newpath
                continue
            target = readlink(newpath)
        except OSError:
            if strict:
                raise
            path = newpath
            continue
        seen[newpath] = None  # type: ignore[assignment]
        if target.startswith(sep):
            path = sep
        rest.append(newpath)
        rest.append(None)  # type: ignore[arg-type]
        target_parts = target.split(sep)[::-1]
        rest.extend(target_parts)
        part_count += len(target_parts)

    return path


@techdebt.refactor
def ismount(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if pathname `path` is a mount point.

    See Also
    --------
    * `posixpath.ismount`.

    Version
    -------
    * Python 3.13.
    """
    pardir = b".." if isinstance(path, bytes) else ".."

    try:
        s1 = lstat(path)
    except (OSError, ValueError):
        return False

    if S_ISLNK(s1.st_mode):
        return False

    path = fspath(path)
    parent = join(path, pardir)  # type: ignore[type-var]

    try:
        s2 = lstat(parent)  # type: ignore[type-var]

    except OSError:
        parent = realpath(parent)  # type: ignore[type-var]
        try:
            s2 = lstat(parent)  # type: ignore[type-var]
        except OSError:
            return False

    return s1.st_dev != s2.st_dev or s1.st_ino == s2.st_ino


def abspath(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Return a normalized absolutized version of the pathname `path`.

    See Also
    --------
    * `posixpath.abspath`.

    Version
    -------
    * Python 3.13.
    """
    path = fspath(path)

    sep = b"/" if isinstance(path, bytes) else "/"

    if not path.startswith(sep):
        cwd = getcwdb() if isinstance(path, bytes) else getcwd()
        path = join(cwd, path)

    return normpath(path)


@techdebt.refactor
def join(path: AnyStr | PathLike[AnyStr], *paths: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Join one or more path segments intelligently.

    See Also
    --------
    * `posixpath.join`.

    Version
    -------
    * Python 3.13.
    """
    initial_path = fspath(path)

    sep = b"/" if isinstance(initial_path, bytes) else "/"

    final_path = initial_path

    try:
        for another_path in paths:
            another_path = fspath(another_path)  # noqa: PLW2901

            if another_path.startswith(sep) or not final_path:
                final_path = another_path
            elif final_path.endswith(sep):
                final_path += another_path
            else:
                final_path += sep + another_path

    except (TypeError, AttributeError, BytesWarning):
        check_arg_types("join", initial_path, *paths)
        raise

    return final_path


@techdebt.refactor
def commonpath(paths: Iterable[AnyStr | PathLike[AnyStr]]) -> AnyStr:
    """Return the longest common sub-path of each pathname in the iterable paths.

    See Also
    --------
    * `posixpath.commonpath`.

    Version
    -------
    * Python 3.13.
    """
    paths = [fspath(p) for p in paths]

    if not paths:
        detail = "commonpath() arg is an empty sequence"
        raise ValueError(detail)

    sep = b"/" if isinstance(paths[0], bytes) else "/"
    curdir = b"." if isinstance(paths[0], bytes) else "."

    try:
        split_paths = [path.split(sep) for path in paths]  # type: ignore[arg-type,union-attr]

        try:
            (isabs,) = {p.startswith(sep) for p in paths}  # type: ignore[arg-type,union-attr]

        except ValueError:
            detail = "Can't mix absolute and relative paths"
            raise ValueError(detail) from None

        split_paths = [[c for c in s if c and c != curdir] for s in split_paths]

        s1 = min(split_paths)
        s2 = max(split_paths)

        common = s1
        for i, c in enumerate(s1):
            if c != s2[i]:
                common = s1[:i]
                break

        prefix = sep if isabs else sep[:0]
        return prefix + sep.join(common)  # type: ignore[arg-type,operator,return-value]

    except (TypeError, AttributeError):
        check_arg_types("commonpath", *paths)
        raise


@techdebt.refactor
@techdebt.simplified
def expanduser(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Replace an initial component of `~` or `~user` by that user's home directory.

    See Also
    --------
    * `posixpath.expanduser`.

    Version
    -------
    * Python 3.13.
    """
    path = fspath(path)

    sep = b"/" if isinstance(path, bytes) else "/"
    tilde = b"~" if isinstance(path, bytes) else "~"

    if not path.startswith(tilde):
        return path

    sep_index = path.find(sep, 1)
    if sep_index < 0:
        sep_index = len(path)

    if sep_index > 1:
        return path

    if "HOME" not in environ:
        return path

    if is_vxworks():
        return path

    userhome = environ["HOME"]

    if isinstance(path, bytes):
        userhome = fsencode(userhome)  # type: ignore[assignment]

    userhome = userhome.rstrip(sep)  # type: ignore[arg-type]
    return (userhome + path[sep_index:]) or sep  # type: ignore[operator,return-value]


@techdebt.refactor
def expandvars(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Return the argument with environment variables expanded.

    See Also
    --------
    * `posixpath.expandvars`.

    Version
    -------
    * Python 3.13.
    """
    path = fspath(path)

    varprog = re.compile(r"\$(\w+|\{[^}]*\})", re.ASCII)
    varprogb = re.compile(rb"\$(\w+|\{[^}]*\})", re.ASCII)

    dollar = b"$" if isinstance(path, bytes) else "$"
    start = b"{" if isinstance(path, bytes) else "{"
    end = b"}" if isinstance(path, bytes) else "}"

    if dollar not in path:
        return path

    search = varprogb.search if isinstance(path, bytes) else varprog.search
    env = environb if isinstance(path, bytes) else environ

    i = 0
    while True:
        m = search(path, i)

        if not m:
            break

        i, j = m.span(0)
        name = m.group(1)

        if name.startswith(start) and name.endswith(end):
            name = name[1:-1]

        try:
            value = env[name]

        except KeyError:
            i = j

        else:
            tail = path[j:]
            path = path[:i] + value
            i = len(path)
            path += tail

    return path
