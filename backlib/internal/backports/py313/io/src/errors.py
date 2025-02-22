import builtins

from backlib.internal.stdlib.typing import TypeAlias


__all__: list[str] = ["BlockingIOError", "UnsupportedOperation"]


BlockingIOError: TypeAlias = builtins.BlockingIOError  # noqa: A001


class UnsupportedOperation(OSError, ValueError):  # noqa: N818
    """Raised when an unsupported operation is called on a stream.

    See Also
    --------
    * `io.UnsupportedOperation`.

    Version
    -------
    * Python 3.13.
    """
