from __future__ import annotations

from typing import TypeVar

from backlib.internal.backports.py310 import errno, os, stat
from backlib.internal.markers import techdebt


AnyStr = TypeVar("AnyStr", bytes, str)


@techdebt.refactor
def realpath(  # noqa: C901, PLR0915
    filename: AnyStr | os.PathLike[AnyStr],
    *,
    strict: bool = False,
) -> AnyStr:
    """Return the canonical path of the specified filename.

    See Also
    --------
    * `posixpath.realpath`.
    """
    filename = os.fspath(filename)

    sep = b"/" if isinstance(filename, bytes) else "/"
    curdir = b"." if isinstance(filename, bytes) else "."
    pardir = b".." if isinstance(filename, bytes) else ".."
    getcwd = os.getcwdb if isinstance(filename, bytes) else os.getcwd

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
                    raise OSError(  # noqa: TRY301
                        errno.ENOTDIR,
                        os.strerror(errno.ENOTDIR),
                        newpath,
                    )
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
                    # Raise OSError(errno.ELOOP)
                    os.stat(newpath)
                path = newpath
                continue
            target = os.readlink(newpath)
        except OSError:
            if strict:
                raise
            path = newpath
            continue
        # Resolve the symbolic link
        seen[newpath] = None  # not resolved symlink
        if target.startswith(sep):
            # Symlink target is absolute; reset resolved path.
            path = sep
        # Push the symlink path onto the stack, and signal its specialness by
        # also pushing None. When these entries are popped, we'll record the
        # fully-resolved symlink target in the 'seen' mapping.
        rest.append(newpath)
        rest.append(None)  # type: ignore[arg-type]
        # Push the unresolved symlink target parts onto the stack.
        target_parts = target.split(sep)[::-1]
        rest.extend(target_parts)
        part_count += len(target_parts)

    return path
