from __future__ import annotations

from typing import IO, TYPE_CHECKING, BinaryIO, Literal, overload
from warnings import warn

from backlib.internal.typing import AnyStr
from backlib.internal.utils.typing import (
    OpenBinaryMode,
    OpenBinaryModeReading,
    OpenBinaryModeUpdating,
    OpenBinaryModeWriting,
    OpenTextMode,
)


if TYPE_CHECKING:
    from collections.abc import Callable

    from backlib.internal.stdlib.py313.io.src.classes import (
        BufferedRandom,
        BufferedReader,
        BufferedWriter,
        FileIO,
        TextIOWrapper,
    )
    from backlib.internal.stdlib.py313.os import PathLike


@overload
def open(  # noqa: A001
    file: int | AnyStr | PathLike[AnyStr],
    mode: OpenTextMode = "r",
    buffering: int = -1,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> TextIOWrapper: ...


@overload
def open(  # noqa: A001
    file: int | AnyStr | PathLike[AnyStr],
    mode: OpenBinaryMode,
    buffering: Literal[0],
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> FileIO: ...


@overload
def open(  # noqa: A001
    file: int | AnyStr | PathLike[AnyStr],
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
    file: int | AnyStr | PathLike[AnyStr],
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
    file: int | AnyStr | PathLike[AnyStr],
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
    file: int | AnyStr | PathLike[AnyStr],
    mode: OpenBinaryMode,
    buffering: int = -1,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> BinaryIO: ...


@overload
def open(  # noqa: A001
    file: int | AnyStr | PathLike[AnyStr],
    mode: str,
    buffering: int = -1,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> IO[AnyStr]: ...


def open(  # noqa: A001
    file: int | AnyStr | PathLike[AnyStr],
    mode: str = "r",
    buffering: int = -1,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> IO[AnyStr]:
    """Open `file` and return a corresponding file object.

    See Also
    --------
    * `io.open`.

    Version
    -------
    * Python 3.13.
    """


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
