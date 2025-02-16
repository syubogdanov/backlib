from typing import BinaryIO
from warnings import warn


def open():
    ...


def open_code(path: str) -> BinaryIO:
    """Open the provided file with mode `"rb"`.

    See Also
    --------
    * `io.open_code`.

    Version
    -------
    * Python 3.13.
    """
    message = "'backlib.py313.io.open_code()' may not be using hooks"
    warn(message, RuntimeWarning, stacklevel=2)
    return open(path, mode="rb")
