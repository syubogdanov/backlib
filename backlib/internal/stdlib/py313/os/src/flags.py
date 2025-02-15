import os as py_os

from typing import Final

from backlib.internal.utils import alias


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
]


SEEK_SET: Final[int] = 0
SEEK_CUR: Final[int] = 1
SEEK_END: Final[int] = 2

F_OK: Final[int] = alias.to(py_os.F_OK)
R_OK: Final[int] = alias.to(py_os.R_OK)
W_OK: Final[int] = alias.to(py_os.W_OK)
X_OK: Final[int] = alias.to(py_os.X_OK)

O_APPEND: Final[int] = alias.to(py_os.O_APPEND)
O_CREAT: Final[int] = alias.to(py_os.O_CREAT)
O_EXCL: Final[int] = alias.to(py_os.O_EXCL)
O_RDONLY: Final[int] = alias.to(py_os.O_RDONLY)
O_RDWR: Final[int] = alias.to(py_os.O_RDWR)
O_TRUNC: Final[int] = alias.to(py_os.O_TRUNC)
O_WRONLY: Final[int] = alias.to(py_os.O_WRONLY)
