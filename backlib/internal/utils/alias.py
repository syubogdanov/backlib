from __future__ import annotations

from enum import Enum, auto
from typing import Any, TypeVar

from backlib.internal.utils.platform import (
    is_darwin,
    is_freebsd,
    is_linux,
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


def or_platform(  # noqa: C901, PLR0911, PLR0913
    container: Any,
    attribute_name: str,
    /,
    *,
    darwin: T | Undefined = Undefined.DEFAULT,
    freebsd: T | Undefined = Undefined.DEFAULT,
    linux: T | Undefined = Undefined.DEFAULT,
    nt: T | Undefined = Undefined.DEFAULT,
    posix: T | Undefined = Undefined.DEFAULT,
    solaris: T | Undefined = Undefined.DEFAULT,
    sunos: T | Undefined = Undefined.DEFAULT,
    unix: T | Undefined = Undefined.DEFAULT,
    vxworks: T | Undefined = Undefined.DEFAULT,
    otherwise: T,
) -> T:
    """Get an attribute if exists, otherwise the platform-specific default value.

    Notes
    -----
    * If several OS options are suitable, the most specific (or narrowest) one is selected. For
      example, *FreeBSD* is chosen over *POSIX* because it provides a more precise match for the
      target environment.
    """
    value = getattr(container, attribute_name, Undefined.DEFAULT)

    if not isinstance(value, Undefined):
        return value

    if not isinstance(nt, Undefined) and is_nt():
        return nt

    if not isinstance(darwin, Undefined) and is_darwin():
        return darwin

    if not isinstance(solaris, Undefined) and is_solaris():
        return solaris

    if not isinstance(sunos, Undefined) and is_sunos():
        return sunos

    if not isinstance(vxworks, Undefined) and is_vxworks():
        return vxworks

    if not isinstance(freebsd, Undefined) and is_freebsd():
        return freebsd

    if not isinstance(linux, Undefined) and is_linux():
        return linux

    if not isinstance(unix, Undefined) and is_unix():
        return unix

    if not isinstance(posix, Undefined) and is_posix():
        return posix

    return otherwise


def or_default(
    container: object,
    attribute_name: str,
    /,
    otherwise: T,
) -> T:
    """Get a named attribute if exists, otherwise the default value."""
    return getattr(container, attribute_name, otherwise)
