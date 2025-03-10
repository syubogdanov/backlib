from __future__ import annotations

import io as py_io
import sys

from typing import IO, TYPE_CHECKING, Any, BinaryIO, Literal, TextIO, TypeVar, overload
from warnings import warn

from backlib.py313.internal.backports import os
from backlib.py313.internal.backports.builtins import EncodingWarning
from backlib.py313.internal.utils import alias


if TYPE_CHECKING:
    from collections.abc import Callable

    from backlib.py313.internal.backports.io.internal.typing import (
        OpenBinaryModeReading,
        OpenBinaryModeUpdating,
        OpenBinaryModeWriting,
        OpenTextModeReading,
        OpenTextModeUpdating,
        OpenTextModeWriting,
    )


__all__: list[str] = [
    "DEFAULT_BUFFER_SIZE",
    "BlockingIOError",
    "BufferedIOBase",
    "BufferedRWPair",
    "BufferedRandom",
    "BufferedReader",
    "BufferedWriter",
    "BytesIO",
    "FileIO",
    "IOBase",
    "RawIOBase",
    "StringIO",
    "TextIOBase",
    "TextIOWrapper",
    "UnsupportedOperation",
    "open",
    "open_code",
    "text_encoding",
]

__backlib__: str = "backlib.py313.io"


AnyStr = TypeVar("AnyStr", str, bytes)


# ---
# Version: Python 3.9+
# Explain: No changes required.
# ---

DEFAULT_BUFFER_SIZE = py_io.DEFAULT_BUFFER_SIZE

BlockingIOError = py_io.BlockingIOError
UnsupportedOperation = py_io.UnsupportedOperation

BufferedIOBase = py_io.BufferedIOBase
BufferedRWPair = py_io.BufferedRWPair
BufferedRandom = py_io.BufferedRandom
BufferedReader = py_io.BufferedReader
BufferedWriter = py_io.BufferedWriter
BytesIO = py_io.BytesIO
FileIO = py_io.FileIO
IOBase = py_io.IOBase
RawIOBase = py_io.RawIOBase
TextIOBase = py_io.TextIOBase


# ---
# Version: Python 3.11+
# Explain: Changed in Python 3.11.
# ---


def text_encoding(encoding: str | None, stacklevel: int = 2) -> str:
    """Select the encoding for text I/O.

    See Also
    --------
    * `io.text_encoding`.
    """
    if encoding is not None:
        return encoding

    warn_from_env = "PYTHONWARNDEFAULTENCODING" in os.environ
    warn_from_sys = alias.or_default(sys.flags, "warn_default_encoding", otherwise=False)

    if warn_from_env or warn_from_sys:
        message = "'encoding' argument not specified."
        warn(message, EncodingWarning, stacklevel=(stacklevel + 1))

    return "utf-8" if sys.flags.utf8_mode else "locale"


@overload
def open(
    file: int | AnyStr | os.PathLike[AnyStr],
    mode: OpenTextModeUpdating | OpenTextModeWriting | OpenTextModeReading = "r",
    buffering: int = -1,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> TextIOWrapper: ...


@overload
def open(
    file: int | AnyStr | os.PathLike[AnyStr],
    mode: OpenBinaryModeUpdating | OpenBinaryModeReading | OpenBinaryModeWriting,
    buffering: Literal[0],
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> FileIO: ...


@overload
def open(
    file: int | AnyStr | os.PathLike[AnyStr],
    mode: OpenBinaryModeUpdating,
    buffering: Literal[-1, 1] = -1,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> BufferedRandom: ...


@overload
def open(
    file: int | AnyStr | os.PathLike[AnyStr],
    mode: OpenBinaryModeWriting,
    buffering: Literal[-1, 1] = -1,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> BufferedWriter: ...


@overload
def open(
    file: int | AnyStr | os.PathLike[AnyStr],
    mode: OpenBinaryModeReading,
    buffering: Literal[-1, 1] = -1,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> BufferedReader: ...


@overload
def open(
    file: int | AnyStr | os.PathLike[AnyStr],
    mode: OpenBinaryModeUpdating | OpenBinaryModeReading | OpenBinaryModeWriting,
    buffering: int = -1,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> BinaryIO: ...


def open(
    file: int | AnyStr | os.PathLike[AnyStr],
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
    """
    raise NotImplementedError


def open_code(path: str) -> BinaryIO:
    """Open the provided file with mode `"rb"`.

    See Also
    --------
    * `io.open_code`.
    """
    message = f"'{__backlib__}.open_code()' may not be using hooks"
    warn(message, RuntimeWarning, stacklevel=2)
    return open(path, mode="rb")


class TextIOWrapper(TextIOBase, TextIO): ...


class StringIO(TextIOWrapper): ...
