from typing import Any


ASCII_CONTROL_CHARS = {chr(code) for code in range(32)}
VISIBLE_RESERVED_CHARS = {'"', "*", ":", "<", ">", "?", "|", "/", "\\"}

DOS_RESERVED_NAMES = {"CON", "PRN", "AUX", "NUL", "CONIN$", "CONOUT$"}

COM_RESERVED_NAMES = {f"COM{char}" for char in "123456789\xb9\xb2\xb3"}
LPT_RESERVED_NAMES = {f"LPT{char}" for char in "123456789\xb9\xb2\xb3"}

RESERVED_CHARS = ASCII_CONTROL_CHARS | VISIBLE_RESERVED_CHARS
RESERVED_NAMES = DOS_RESERVED_NAMES | COM_RESERVED_NAMES | LPT_RESERVED_NAMES


def is_reserved_name(name: str) -> bool:
    """Return `True` if `name` is reserved by the system."""
    if name.endswith((".", " ")):
        return name not in (".", "..")

    if RESERVED_CHARS.intersection(name):
        return True

    prefix, _, _ = name.partition(".")
    prefix = prefix.rstrip(" ").upper()

    return prefix in RESERVED_NAMES


def check_arg_types(funcname: str, *args: Any) -> None:
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
