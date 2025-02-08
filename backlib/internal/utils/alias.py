from __future__ import annotations

from typing import TypeVar

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
    darwin: T | Undefined = Undefined,
    nt: T | Undefined = Undefined,
    posix: T | Undefined = Undefined,
    solaris: T | Undefined = Undefined,
    sunos: T | Undefined = Undefined,
    unix: T | Undefined = Undefined,
    vxworks: T | Undefined = Undefined,
    otherwise: T | Undefined = Undefined,
) -> T:
    """Get a named attribute if exists, otherwise the platform default value.

    Notes
    -----
    * Platforms that are supersets over others are prioritized;
    * For example, *Darwin* is selected over *POSIX*.
    """
    if (value := getattr(object_, name, Undefined)) is not Undefined:
        return value

    if nt is not Undefined and is_nt():
        return nt

    if darwin is not Undefined and is_darwin():
        return darwin

    if solaris is not Undefined and is_solaris():
        return solaris

    if sunos is not Undefined and is_sunos():
        return sunos

    if vxworks is not Undefined and is_vxworks():
        return vxworks

    if unix is not Undefined and is_unix():
        return unix

    if posix is not Undefined and is_posix():
        return posix

    if otherwise is not Undefined:
        return otherwise

    detail = "The platform is not supported..."
    raise NotImplementedError(detail)
