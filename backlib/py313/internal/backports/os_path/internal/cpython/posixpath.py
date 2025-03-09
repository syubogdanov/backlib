from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from backlib.py313.internal.backports import errno, os, stat
from backlib.py313.internal.backports.os_path.internal.cpython import genericpath
from backlib.py313.internal.markers import techdebt


if TYPE_CHECKING:
    from collections.abc import Callable, Iterable


AnyStr = TypeVar("AnyStr", str, bytes)


def realpath(path: AnyStr | os.PathLike[AnyStr], *, strict: bool = False) -> AnyStr:
    """Return the canonical path of the specified filename.

    See Also
    --------
    * posixpath.realpath
    """
    filename = os.fspath(path)

    sep = b"/" if isinstance(filename, bytes) else "/"
    curdir = b"." if isinstance(filename, bytes) else "."
    pardir = b".." if isinstance(filename, bytes) else ".."
    getcwd = os.getcwdb if isinstance(filename, bytes) else os.getcwd

    return _realpath(filename, sep, curdir, pardir, getcwd, strict=strict)


@techdebt.refactor
def _realpath(  # noqa: C901
    filename: AnyStr,
    sep: AnyStr,
    curdir: AnyStr,
    pardir: AnyStr,
    getcwd: Callable[[], AnyStr],
    *,
    strict: bool,
) -> AnyStr:
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
    seen = {}  # type: ignore[var-annotated]

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
        newpath = path + name if path == sep else path + sep + name
        try:
            st_mode = os.lstat(newpath).st_mode
            if not stat.S_ISLNK(st_mode):
                if strict and part_count and not stat.S_ISDIR(st_mode):
                    message = os.strerror(errno.ENOTDIR)
                    raise OSError(errno.ENOTDIR, message, newpath)  # noqa: TRY301
                path = newpath
                continue

            if newpath in seen:
                # Already seen this path
                path = seen[newpath]
                if path is not None:
                    # use cached value
                    continue
                # The symlink is not resolved, so we must have a symlink loop.
                if strict:
                    raise OSError(errno.ELOOP, os.strerror(errno.ELOOP), newpath)  # noqa: TRY301
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
        rest.append(None)  # type: ignore[arg-type]
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
    fspath = os.fspath(path)

    sep = b"/" if isinstance(fspath, bytes) else "/"

    if fspath[:1] != sep:
        return (fspath[:0], fspath[:0], fspath)

    if fspath[1:2] != sep or fspath[2:3] == sep:
        return (fspath[:0], sep, fspath[1:])

    return (fspath[:0], fspath[:2], fspath[2:])


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
    fspaths = [os.fspath(path) for path in paths]

    if not fspaths:
        detail = "commonpath() arg is an empty sequence"
        raise ValueError(detail)

    first_fspath = fspaths[0]

    sep = b"/" if isinstance(first_fspath, bytes) else "/"
    curdir = b"." if isinstance(first_fspath, bytes) else "."

    try:
        split_paths: list[list[AnyStr]] = [fspath.split(sep) for fspath in fspaths]

        has_absolute = any(fspath.startswith(sep) for fspath in fspaths)
        all_absolute = all(fspath.startswith(sep) for fspath in fspaths)

        if has_absolute and not all_absolute:
            detail = "Can't mix absolute and relative paths"
            raise ValueError(detail) from None

        split_paths = [
            [component for component in split_path if component and component != curdir]
            for split_path in split_paths
        ]

        s1 = min(split_paths)
        s2 = max(split_paths)

        common = s1

        for index, component in enumerate(s1):
            if component != s2[index]:
                common = s1[:index]
                break

        prefix = sep if all_absolute else sep[:0]
        return prefix + sep.join(common)

    except (TypeError, AttributeError):
        genericpath.check_arg_types("commonpath", *fspaths)
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
