from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from backlib.internal.backports.py313 import os
from backlib.internal.backports.py313.os_path.internal import genericpath


if TYPE_CHECKING:
    from collections.abc import Iterable


AnyStr = TypeVar("AnyStr", str, bytes)


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


def isreserved(path: AnyStr | os.PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is a reserved pathname on the current system.

    See Also
    --------
    * `posixpath.isreserved`.
    """
    os.fspath(path)
    return False
