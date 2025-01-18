from __future__ import annotations

import os as py_os

from contextlib import suppress
from typing import Final

from backlib.internal.typing import TypeAlias
from backlib.internal.utils.lint import techdebt
from backlib.internal.utils.sys import is_nt, is_posix
from backlib.internal.utils.typing import ReadableBuffer


__all__: list[str] = [
    "F_OK",
    "O_APPEND",
    "O_CREAT",
    "O_EXCL",
    "O_RDONLY",
    "O_RDWR",
    "O_TRUNC",
    "O_WRONLY",
    "R_OK",
    "SEEK_CUR",
    "SEEK_END",
    "SEEK_SET",
    "W_OK",
    "X_OK",
    "altsep",
    "close",
    "closerange",
    "curdir",
    "defpath",
    "devnull",
    "error",
    "extsep",
    "linesep",
    "name",
    "pardir",
    "pathsep",
    "read",
    "sep",
    "write",
]


if not is_nt() and not is_posix():
    detail = "no os specific module found"
    raise ImportError(detail)


error: TypeAlias = OSError


curdir: Final[str] = "."
pardir: Final[str] = ".."
extsep: Final[str] = "."

name: Final[str] = "posix" if is_posix() else "nt"
linesep: Final[str] = "\n" if is_posix() else "\r\n"

sep: Final[str] = "/" if is_posix() else "\\"
pathsep: Final[str] = ":" if is_posix() else ";"
altsep: Final[str | None] = None if is_posix() else "/"

defpath: Final[str] = "/bin:/usr/bin" if is_posix() else ".;C:\\bin"
devnull: Final[str] = "/dev/null" if is_posix() else "nul"


SEEK_SET: Final[int] = 0
SEEK_CUR: Final[int] = 1
SEEK_END: Final[int] = 2


F_OK: Final[int] = techdebt(py_os.F_OK)
R_OK: Final[int] = techdebt(py_os.R_OK)
W_OK: Final[int] = techdebt(py_os.W_OK)
X_OK: Final[int] = techdebt(py_os.X_OK)


O_APPEND: Final[int] = techdebt(py_os.O_APPEND)
O_CREAT: Final[int] = techdebt(py_os.O_CREAT)
O_EXCL: Final[int] = techdebt(py_os.O_EXCL)
O_RDONLY: Final[int] = techdebt(py_os.O_RDONLY)
O_RDWR: Final[int] = techdebt(py_os.O_RDWR)
O_TRUNC: Final[int] = techdebt(py_os.O_TRUNC)
O_WRONLY: Final[int] = techdebt(py_os.O_WRONLY)


@techdebt
def close(fd: int) -> None:
    """Close file descriptor `fd`.

    See Also
    --------
    * `os.close`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.close(fd)


def closerange(fd_low: int, fd_high: int, /) -> None:
    """Close all descriptors from `fd_low` (inclusive) to `fd_high` (exclusive), ignoring errors.

    See Also
    --------
    * `os.closerange`.

    Version
    -------
    * Python 3.13.
    """
    for fd in range(fd_low, fd_high):
        with suppress(OSError):
            close(fd)


@techdebt
def read(fd: int, length: int, /) -> bytes:
    """Read at most `length` bytes from file descriptor `fd`.

    See Also
    --------
    * `os.read`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.read(fd, length)


@techdebt
def write(fd: int, data: ReadableBuffer, /) -> int:
    """Write the bytestring in `data` to file descriptor `fd`.

    See Also
    --------
    * `os.write`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This function is not a real backport.
    """
    return py_os.write(fd, data)
