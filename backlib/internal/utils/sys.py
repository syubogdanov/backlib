from functools import cache
from sys import builtin_module_names, platform, stdout
from typing import Final


__all__: list[str] = ["STDOUT_FILENO", "is_darwin", "is_nt", "is_posix"]


STDOUT_FILENO: Final[int] = stdout.fileno()


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
