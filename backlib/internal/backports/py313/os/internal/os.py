from __future__ import annotations

import os as py_os
import sys

from typing import TYPE_CHECKING, Final
from warnings import warn

from backlib.internal.backports.py312 import os as py312_os
from backlib.internal.backports.py313.os.internal import linux5
from backlib.internal.utils import alias


if TYPE_CHECKING:
    from backlib.internal.backports.py312.os import PathLike


__all__: list[str] = [
    "TFD_CLOEXEC",
    "TFD_NONBLOCK",
    "TFD_TIMER_ABSTIME",
    "TFD_TIMER_CANCEL_ON_SET",
    "makedirs",
    "mkdir",
]

__backlib__: str = "backlib.py313.os"


TFD_CLOEXEC: Final[int] = alias.or_platform(
    py_os,
    "TFD_CLOEXEC",
    linux=linux5.TFD_CLOEXEC,
    otherwise=linux5.TFD_CLOEXEC,
)
TFD_NONBLOCK: Final[int] = alias.or_platform(
    py_os,
    "TFD_NONBLOCK",
    linux=linux5.TFD_NONBLOCK,
    otherwise=linux5.TFD_NONBLOCK,
)
TFD_TIMER_ABSTIME: Final[int] = alias.or_platform(
    py_os,
    "TFD_TIMER_ABSTIME",
    linux=linux5.TFD_TIMER_ABSTIME,
    otherwise=linux5.TFD_TIMER_ABSTIME,
)
TFD_TIMER_CANCEL_ON_SET: Final[int] = alias.or_platform(
    py_os,
    "TFD_TIMER_CANCEL_ON_SET",
    linux=linux5.TFD_TIMER_CANCEL_ON_SET,
    otherwise=linux5.TFD_TIMER_CANCEL_ON_SET,
)


def mkdir(
    path: str | bytes | PathLike[str] | PathLike[bytes],
    mode: int = 0o777,
    *,
    dir_fd: int | None = None,
) -> None:
    """Create a directory named `path` with numeric mode `mode`.

    See Also
    --------
    * `os.mkdir`.
    """
    if sys.version_info < (3, 13) and mode == 0o700:
        detail = f"{__backlib__}.mkdir() does not support mode='0o700'"
        warn(detail, RuntimeWarning, stacklevel=2)

    py312_os.mkdir(path, mode, dir_fd=dir_fd)


def makedirs(
    name: str | bytes | PathLike[str] | PathLike[bytes],
    mode: int = 0o777,
    exist_ok: bool = False,
) -> None:
    """Recursive directory creation function.

    See Also
    --------
    * `os.makedirs`.
    """
    if sys.version_info < (3, 13) and mode == 0o700:
        detail = f"{__backlib__}.makedirs() does not support mode='0o700'"
        warn(detail, RuntimeWarning, stacklevel=2)

    py312_os.makedirs(name, mode, exist_ok=exist_ok)


makedirs.__module__ = __backlib__
mkdir.__module__ = __backlib__
