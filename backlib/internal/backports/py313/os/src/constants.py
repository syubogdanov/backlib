from __future__ import annotations

from typing import Final

from backlib.internal.utils.platform import is_nt, is_posix


__all__: list[str] = [
    "altsep",
    "curdir",
    "defpath",
    "devnull",
    "extsep",
    "linesep",
    "name",
    "pardir",
    "pathsep",
    "sep",
]


if not is_nt() and not is_posix():
    detail = "no os specific module found"
    raise ImportError(detail)


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
