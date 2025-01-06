from functools import cache
from sys import builtin_module_names


__all__: list[str] = ["is_nt", "is_posix"]


@cache
def is_nt() -> bool:
    """Check if the platform is `nt`."""
    return "nt" in builtin_module_names


@cache
def is_posix() -> bool:
    """Check if the platform is `POSIX`."""
    return "posix" in builtin_module_names
