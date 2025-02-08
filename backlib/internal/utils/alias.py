from __future__ import annotations

from enum import Enum, auto
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


class Undefined(Enum):
    """An undefined value."""

    DEFAULT = auto()


def or_platform(  # noqa: PLR0911, PLR0913
    object_: object,
    name: str,
    *,
    darwin: T | Undefined = Undefined.DEFAULT,
    nt: T | Undefined = Undefined.DEFAULT,
    posix: T | Undefined = Undefined.DEFAULT,
    solaris: T | Undefined = Undefined.DEFAULT,
    sunos: T | Undefined = Undefined.DEFAULT,
    unix: T | Undefined = Undefined.DEFAULT,
    vxworks: T | Undefined = Undefined.DEFAULT,
    otherwise: T | Undefined = Undefined.DEFAULT,
) -> T:
    """Get a named attribute if exists, otherwise the platform default value.

    Notes
    -----
    * Platforms that are supersets over others are prioritized;
    * For example, *Darwin* is selected over *POSIX*.
    """
    value = getattr(object_, name, Undefined.DEFAULT)

    if not isinstance(value, Undefined):
        return techdebt(value)

    if not isinstance(nt, Undefined) and is_nt():
        return techdebt(nt)

    if not isinstance(darwin, Undefined) and is_darwin():
        return techdebt(darwin)

    if not isinstance(solaris, Undefined) and is_solaris():
        return techdebt(solaris)

    if not isinstance(sunos, Undefined) and is_sunos():
        return techdebt(sunos)

    if not isinstance(vxworks, Undefined) and is_vxworks():
        return techdebt(vxworks)

    if not isinstance(unix, Undefined) and is_unix():
        return techdebt(unix)

    if not isinstance(posix, Undefined) and is_posix():
        return techdebt(posix)

    if not isinstance(otherwise, Undefined):
        return techdebt(otherwise)

    detail = "The platform is not supported..."
    raise NotImplementedError(detail)


def or_default(
    object_: object,
    name: str,
    otherwise: T,
) -> T:
    """Get a named attribute if exists, otherwise the default value."""
    return or_platform(object_, name, otherwise=otherwise)


def to(object_: T) -> T:
    """Mark an object as an alias."""
    return techdebt(object_)
