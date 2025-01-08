from typing import Any


def check_arg_types(funcname: str, *args: Any) -> None:  # noqa: ANN401
    """Check that all arguments are `str`, `bytes`, or `os.PathLike`."""
    has_str = False
    has_bytes = False

    for arg in args:
        if isinstance(arg, str):
            has_str = True

        elif isinstance(arg, bytes):
            has_bytes = True

        else:
            detail = (
                f"{funcname}() argument must be str, bytes, or "
                f"os.PathLike object, not {arg.__class__.__name__!r}"
            )
            raise TypeError(detail) from None

    if has_str and has_bytes:
        detail = "Can't mix strings and bytes in path components"
        raise TypeError(detail) from None
