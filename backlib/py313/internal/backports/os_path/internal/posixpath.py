from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from backlib.py313.internal.backports import errno, os
from backlib.py313.internal.backports.os_path.internal import genericpath


if TYPE_CHECKING:
    from collections.abc import Iterable


AnyStr = TypeVar("AnyStr", str, bytes)


def realpath(path: AnyStr | os.PathLike[AnyStr], *, strict: bool = False) -> AnyStr:
    """Return the canonical path of the specified filename.

    See Also
    --------
    * posixpath.realpath
    """
    filename = os.fspath(path)
    if isinstance(filename, bytes):
        sep = b"/"
        curdir = b"."
        pardir = b".."
        getcwd = os.getcwdb
    else:
        sep = "/"
        curdir = "."
        pardir = ".."
        getcwd = os.getcwd
    return _realpath(filename, strict, sep, curdir, pardir, getcwd)


def _realpath(filename, strict, sep, curdir, pardir, getcwd):
    # The stack of unresolved path parts. When popped, a special value of None
    # indicates that a symlink target has been resolved, and that the original
    # symlink path can be retrieved by popping again. The [::-1] slice is a
    # very fast way of spelling list(reversed(...)).
    rest = filename.split(sep)[::-1]

    # Number of unprocessed parts in 'rest'. This can differ from len(rest)
    # later, because 'rest' might contain markers for unresolved symlinks.
    part_count = len(rest)

    # The resolved path, which is absolute throughout this function.
    # Note: getcwd() returns a normalized and symlink-free path.
    path = sep if filename.startswith(sep) else getcwd()

    # Mapping from symlink paths to *fully resolved* symlink targets. If a
    # symlink is encountered but not yet resolved, the value is None. This is
    # used both to detect symlink loops and to speed up repeated traversals of
    # the same links.
    seen = {}

    # Number of symlinks traversed. When the number of traversals is limited
    # by *maxlinks*, this is used instead of *seen* to detect symlink loops.
    link_count = 0

    while part_count:
        name = rest.pop()
        if name is None:
            # resolved symlink target
            seen[rest.pop()] = path
            continue
        part_count -= 1
        if not name or name == curdir:
            # current dir
            continue
        if name == pardir:
            # parent dir
            path = path[: path.rindex(sep)] or sep
            continue
        if path == sep:
            newpath = path + name
        else:
            newpath = path + sep + name
        try:
            st_mode = os.lstat(newpath).st_mode
            if not os.stat.S_ISLNK(st_mode):
                if strict and part_count and not os.stat.S_ISDIR(st_mode):
                    raise OSError(errno.ENOTDIR, os.strerror(errno.ENOTDIR), newpath)
                path = newpath
                continue

            elif newpath in seen:
                # Already seen this path
                path = seen[newpath]
                if path is not None:
                    # use cached value
                    continue
                # The symlink is not resolved, so we must have a symlink loop.
                if strict:
                    raise OSError(errno.ELOOP, os.strerror(errno.ELOOP), newpath)
                path = newpath
                continue
            target = os.readlink(newpath)
        except OSError:
            if strict:
                raise
            path = newpath
            continue
        # Resolve the symbolic link
        if target.startswith(sep):
            # Symlink target is absolute; reset resolved path.
            path = sep

        # Mark this symlink as seen but not fully resolved.
        seen[newpath] = None
        # Push the symlink path onto the stack, and signal its specialness
        # by also pushing None. When these entries are popped, we'll
        # record the fully-resolved symlink target in the 'seen' mapping.
        rest.append(newpath)
        rest.append(None)
        # Push the unresolved symlink target parts onto the stack.
        target_parts = target.split(sep)[::-1]
        rest.extend(target_parts)
        part_count += len(target_parts)

    return path


def isjunction(path: AnyStr | os.PathLike[AnyStr]) -> bool:
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
    path = os.fspath(path)
    if isinstance(path, bytes):
        sep = b"/"
        empty = b""
    else:
        sep = "/"
        empty = ""
    if path[:1] != sep:
        # Relative path, e.g.: 'foo'
        return empty, empty, path
    elif path[1:2] != sep or path[2:3] == sep:
        # Absolute path, e.g.: '/foo', '///foo', '////foo', etc.
        return empty, sep, path[1:]
    else:
        # Precisely two leading slashes, e.g.: '//foo'. Implementation defined per POSIX, see
        # https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap04.html#tag_04_13
        return empty, path[:2], path[2:]


def isreserved(path: AnyStr | os.PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is a reserved pathname on the current system.

    See Also
    --------
    * `posixpath.isreserved`.
    """
    os.fspath(path)
    return False


def commonpath(paths: Iterable[AnyStr | os.PathLike[AnyStr]]) -> AnyStr:
    """Return the longest common sub-path of each pathname in the iterable paths.

    See Also
    --------
    * `posixpath.commonpath`.
    """
    paths = tuple(map(os.fspath, paths))

    if not paths:
        raise ValueError("commonpath() arg is an empty sequence")

    if isinstance(paths[0], bytes):
        sep = b"/"
        curdir = b"."
    else:
        sep = "/"
        curdir = "."

    try:
        split_paths = [path.split(sep) for path in paths]

        try:
            (isabs,) = {p.startswith(sep) for p in paths}
        except ValueError:
            raise ValueError("Can't mix absolute and relative paths") from None

        split_paths = [[c for c in s if c and c != curdir] for s in split_paths]
        s1 = min(split_paths)
        s2 = max(split_paths)
        common = s1
        for i, c in enumerate(s1):
            if c != s2[i]:
                common = s1[:i]
                break

        prefix = sep if isabs else sep[:0]
        return prefix + sep.join(common)
    except (TypeError, AttributeError):
        genericpath.check_arg_types("commonpath", *paths)
        raise


def isabs(path: AnyStr | os.PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an absolute pathname.

    See Also
    --------
    * `posixpath.isabs`.
    """
    path = os.fspath(path)
    sep = b"/" if isinstance(path, bytes) else "/"
    return path.startswith(sep)
