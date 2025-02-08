from __future__ import annotations

from typing import TypeVar

from backlib.internal.markers import techdebt
from backlib.internal.utils.platform import (
    is_darwin,
    is_nt,
    is_posix,
    is_solaris,
    is_sunos,
    is_unix,
    is_vxworks,
)


T = TypeVar("T")


class Undefined:
    """An undefined value.

    Notes
    -----
    * This is not the same as `None`.
    """


def or_platform(  # noqa: PLR0911, PLR0913
    object_: object,
    name: str,
    *,
    darwin: T | type[Undefined] = Undefined,
    nt: T | type[Undefined] = Undefined,
    posix: T | type[Undefined] = Undefined,
    solaris: T | type[Undefined] = Undefined,
    sunos: T | type[Undefined] = Undefined,
    unix: T | type[Undefined] = Undefined,
    vxworks: T | type[Undefined] = Undefined,
    otherwise: T | type[Undefined] = Undefined,
) -> T:
    """Get a named attribute if exists, otherwise the platform default value.

    Notes
    -----
    * Platforms that are supersets over others are prioritized;
    * For example, *Darwin* is selected over *POSIX*.
    """
    if (value := getattr(object_, name, Undefined)) is not Undefined:
        return techdebt(value)

    if nt is not Undefined and is_nt():
        return techdebt(nt)

    if darwin is not Undefined and is_darwin():
        return techdebt(darwin)

    if solaris is not Undefined and is_solaris():
        return techdebt(solaris)

    if sunos is not Undefined and is_sunos():
        return techdebt(sunos)

    if vxworks is not Undefined and is_vxworks():
        return techdebt(vxworks)

    if unix is not Undefined and is_unix():
        return techdebt(unix)

    if posix is not Undefined and is_posix():
        return techdebt(posix)

    if otherwise is not Undefined:
        return techdebt(otherwise)

    detail = "The platform is not supported..."
    raise NotImplementedError(detail)


def or_default(
    object_: object,
    name: str,
    otherwise: T,
) -> T:
    """Get a named attribute if exists, otherwise the default value."""
    return getattr(object_, name, otherwise)
