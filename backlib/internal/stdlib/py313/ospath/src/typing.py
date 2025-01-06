from __future__ import annotations

from typing import Union

from backlib.internal.stdlib.py313.os import PathLike
from backlib.internal.typing import TypeAlias


__all__: list[str] = ["FileDescriptorOrPath", "StrOrBytesPath"]


StrOrBytesPath: TypeAlias = Union[str, bytes, PathLike[str], PathLike[bytes]]
FileDescriptorOrPath: TypeAlias = Union[int, StrOrBytesPath]
