from typing import Any

from backlib.internal.backports.py313.ntpath.src.constants import RESERVED_CHARS, RESERVED_NAMES


__all___: list[str] = ["check_arg_types", "is_reserved_name"]


def check_arg_types(funcname: str, *args: Any) -> None:  # noqa: ANN401
    """Check the types of the arguments to a function."""
    has_str = False
    has_bytes = False

    for arg in args:
        if isinstance(arg, str):
            has_str = True

        elif isinstance(arg, bytes):
            has_bytes = True

        else:
            detail = (
                f"{funcname}() argument must be str, bytes, or os.PathLike object, not "
                f"{arg.__class__.__name__!r}"
            )
            raise TypeError(detail)

    if has_str and has_bytes:
        detail = "Can't mix strings and bytes in path components"
        raise TypeError(detail)


def is_reserved_name(name: str) -> bool:
    """Return `True` if `name` is reserved by the system."""
    if name.endswith((".", " ")):
        return name not in (".", "..")

    if RESERVED_CHARS.intersection(name):
        return True

    prefix, _, _ = name.partition(".")
    prefix = prefix.rstrip(" ").upper()

    return prefix in RESERVED_NAMES
