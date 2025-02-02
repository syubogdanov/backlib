from functools import cache
from sys import builtin_module_names, platform

from backlib.internal.markers.decorators import techdebt


__all__: list[str] = ["is_darwin", "is_nt", "is_posix", "is_unix"]


@cache
def is_darwin() -> bool:
    """Check if the platform is `Darwin`."""
    return platform == "darwin"


@cache
def is_nt() -> bool:
    """Check if the platform is `nt`."""
    return "nt" in builtin_module_names


@cache
def is_posix() -> bool:
    """Check if the platform is `POSIX`."""
    return "posix" in builtin_module_names


@cache
@techdebt
def is_unix() -> bool:
    """Check if the platform is `Unix`.

    Tecnical Debt
    -------------
    * This is an alias to `is_posix`.
    """
    return is_posix()
