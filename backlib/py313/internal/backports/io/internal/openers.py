from __future__ import annotations

from typing import TYPE_CHECKING, Any, BinaryIO
from warnings import warn


if TYPE_CHECKING:
    from collections.abc import Callable

    from backlib.py313.internal.backports.os import PathLike


def open(
    file: int | bytes | str | PathLike[bytes] | PathLike[str],
    mode: str = "r",
    buffering: int = -1,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> Any:
    """Open `file` and return a corresponding file object.

    See Also
    --------
    * `io.open`.

    Version
    -------
    * Python 3.13.
    """
    raise NotImplementedError


def open_code(path: str) -> BinaryIO:
    """Open the provided file with mode `"rb"`.

    See Also
    --------
    * `io.open_code`.

    Version
    -------
    * Python 3.13.
    """
    message = "'backlib.py313.io.open_code()' may not be using hooks"
    warn(message, RuntimeWarning, stacklevel=2)
    return open(path, mode="rb")
