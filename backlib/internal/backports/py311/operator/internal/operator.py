import sys

from collections.abc import Callable
from typing import TypeVar


if sys.version_info >= (3, 10):
    from typing import ParamSpec
else:
    from typing_extensions import ParamSpec


__all__: list[str] = ["call"]

__backlib__: str = "backlib.py311.operator"


P = ParamSpec("P")
R = TypeVar("R")


def call(obj: Callable[P, R], /, *args: P.args, **kwargs: P.kwargs) -> R:
    """Alias to `obj(*args, **kwargs)`.

    See Also
    --------
    * `operator.call`.
    """
    return obj(*args, **kwargs)


call.__module__ = __backlib__
