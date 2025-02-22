from __future__ import annotations

from typing import IO, TYPE_CHECKING, Any, BinaryIO, Literal, overload
from warnings import warn

from backlib.internal.utils.typing import (
    OpenBinaryModeReading,
    OpenBinaryModeUpdating,
    OpenBinaryModeWriting,
    OpenTextModeReading,
    OpenTextModeUpdating,
    OpenTextModeWriting,
)


if TYPE_CHECKING:
    from collections.abc import Callable

    from backlib.internal.backports.py313.io.src.classes import (
        BufferedRandom,
        BufferedReader,
        BufferedWriter,
        FileIO,
        TextIOWrapper,
    )
    from backlib.internal.backports.py313.os import PathLike


@overload
def open(  # noqa: A001
    file: int | bytes | str | PathLike[bytes] | PathLike[str],
    mode: OpenTextModeUpdating | OpenTextModeWriting | OpenTextModeReading = "r",
    buffering: int = -1,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> TextIOWrapper: ...


@overload
def open(  # noqa: A001
    file: int | bytes | str | PathLike[bytes] | PathLike[str],
    mode: OpenBinaryModeUpdating | OpenBinaryModeReading | OpenBinaryModeWriting,
    buffering: Literal[0],
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> FileIO: ...


@overload
def open(  # noqa: A001
    file: int | bytes | str | PathLike[bytes] | PathLike[str],
    mode: OpenBinaryModeUpdating,
    buffering: Literal[-1, 1] = -1,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> BufferedRandom: ...


@overload
def open(  # noqa: A001
    file: int | bytes | str | PathLike[bytes] | PathLike[str],
    mode: OpenBinaryModeWriting,
    buffering: Literal[-1, 1] = -1,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> BufferedWriter: ...


@overload
def open(  # noqa: A001
    file: int | bytes | str | PathLike[bytes] | PathLike[str],
    mode: OpenBinaryModeReading,
    buffering: Literal[-1, 1] = -1,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> BufferedReader: ...


@overload
def open(  # noqa: A001
    file: int | bytes | str | PathLike[bytes] | PathLike[str],
    mode: OpenBinaryModeUpdating | OpenBinaryModeReading | OpenBinaryModeWriting,
    buffering: int = -1,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> BinaryIO: ...


@overload
def open(  # noqa: A001
    file: int | bytes | str | PathLike[bytes] | PathLike[str],
    mode: str,
    buffering: int = -1,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> IO[Any]: ...


def open(  # noqa: A001
    file: int | bytes | str | PathLike[bytes] | PathLike[str],
    mode: str = "r",
    buffering: int = -1,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> IO[Any]:
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
