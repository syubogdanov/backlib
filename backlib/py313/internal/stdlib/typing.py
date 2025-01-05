import sys

from typing import TypeVar


__all__: list[str] = ["AnyStr", "Self"]


AnyStr = TypeVar("AnyStr", str, bytes)


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self
