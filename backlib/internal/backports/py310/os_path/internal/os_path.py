from __future__ import annotations

import os.path as py_os_path
import sys

from typing import TYPE_CHECKING, TypeVar
from warnings import warn

from backlib.internal.backports.py310.os_path.internal import posixpath
from backlib.internal.markers import techdebt
from backlib.internal.utils.platform import is_posix


if TYPE_CHECKING:
    from backlib.internal.backports.py310 import os


__all__: list[str] = ["realpath"]

__backlib__: str = "backlib.py313.os.path"


AnyStr = TypeVar("AnyStr", bytes, str)


@techdebt.refactor
def realpath(
    filename: AnyStr | os.PathLike[AnyStr],
    *,
    strict: bool = False,
) -> AnyStr:
    """Return the canonical path of the specified filename.

    See Also
    --------
    * `os.path.realpath`.
    """
    if sys.version_info >= (3, 10):
        return py_os_path.realpath(filename, strict=strict)

    if is_posix():
        return posixpath.realpath(filename, strict=strict)

    detail = f"{__backlib__}.realpath() is an alias to {__backlib__}.abspath()"
    warn(detail, RuntimeWarning, stacklevel=2)

    return py_os_path.abspath(filename)


realpath.__module__ = __name__
