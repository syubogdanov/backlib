from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from backlib.internal.backports.py313.os_path.internal import ntpath, posixpath
from backlib.internal.utils.platform import is_nt


if TYPE_CHECKING:
    from collections.abc import Iterable

    from backlib.internal.backports.py313.os import PathLike


__all__: list[str] = ["commonpath", "isabs", "isreserved"]

__backlib__: str = "backlib.py313.os.path"


AnyStr = TypeVar("AnyStr", str, bytes)


def commonpath(paths: Iterable[AnyStr | PathLike[AnyStr]]) -> AnyStr:
    """Return the longest common sub-path of each pathname in the iterable paths.

    See Also
    --------
    * `os.path.commonpath`.
    """
    os_commonpath = ntpath.commonpath if is_nt() else posixpath.commonpath
    return os_commonpath(paths)


def isabs(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an absolute pathname.

    See Also
    --------
    * `os.path.isabs`.
    """
    os_isabs = ntpath.isabs if is_nt() else posixpath.isabs
    return os_isabs(path)


def isreserved(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is a reserved pathname on the current system.

    See Also
    --------
    * `os.path.isreserved`.
    """
    os_isreserved = ntpath.isreserved if is_nt() else posixpath.isreserved
    return os_isreserved(path)


commonpath.__module__ = __backlib__
isabs.__module__ = __backlib__
isreserved.__module__ = __backlib__
