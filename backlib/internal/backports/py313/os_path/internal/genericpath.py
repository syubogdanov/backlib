from typing import Any


def check_arg_types(funcname: str, *args: Any) -> None:
    """Check that all the arguments are `str` or `bytes`."""
    has_bytes = False
    has_str = False

    for arg in args:
        if isinstance(arg, bytes):
            has_bytes = True
        elif isinstance(arg, str):
            has_str = True
        else:
            detail = (
                f"{funcname}() argument must be str, bytes, or "
                f"os.PathLike object, not {arg.__class__.__name__!r}"
            )
            raise TypeError(detail) from None

        has_bytes = has_bytes or isinstance(arg, bytes)
        has_str = has_str or isinstance(arg, str)

    if has_bytes and has_str:
        detail = "Can't mix strings and bytes in path components"
        raise TypeError(detail) from None
