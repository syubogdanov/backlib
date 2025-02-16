from functools import cache
from sys import builtin_module_names, platform

from backlib.internal.markers import todo


__all__: list[str] = [
    "is_darwin",
    "is_freebsd",
    "is_linux",
    "is_nt",
    "is_posix",
    "is_solaris",
    "is_sunos",
    "is_unix",
    "is_vxworks",
]


@cache
def is_nt() -> bool:
    """Check if the platform is `nt`."""
    return "nt" in builtin_module_names


@cache
def is_posix() -> bool:
    """Check if the platform is `POSIX`."""
    return "posix" in builtin_module_names


@todo.restore
@cache
def is_unix() -> bool:
    """Check if the platform is `Unix`.

    Tecnical Debt
    -------------
    * This is an alias to `is_posix`.
    """
    return is_posix()


@cache
def is_darwin() -> bool:
    """Check if the platform is `Darwin`."""
    return platform == "darwin"


@cache
def is_vxworks() -> bool:
    """Check if the platform is `VxWorks`."""
    return platform == "vxworks"


@cache
def is_solaris() -> bool:
    """Check if the platform is `Solaris`."""
    return platform.startswith("solaris")


@cache
def is_sunos() -> bool:
    """Check if the platform is `SunOS`."""
    return platform.startswith("sunos")


@cache
def is_freebsd() -> bool:
    """Check if the platform is `FreeBSD`."""
    return platform.startswith("freebsd")


@cache
def is_linux() -> bool:
    """Check if the platform is `Linux`."""
    return platform == "linux"
