import builtins
import sys


if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


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
