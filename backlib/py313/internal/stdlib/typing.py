import sys

from typing import TypeVar


__all__: list[str] = ["AnyStr", "Self", "TypeAlias"]


AnyStr = TypeVar("AnyStr", str, bytes)


if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self
