from __future__ import annotations

import sys

from warnings import warn

from backlib.internal.stdlib.builtins import EncodingWarning
from backlib.internal.utils import alias


__all__: list[str] = ["text_encoding"]


def text_encoding(encoding: str | None, stacklevel: int = 2) -> str:
    """Select the encoding for text I/O.

    See Also
    --------
    * `io.text_encoding`.

    Version
    -------
    * Python 3.13.
    """
    if encoding is not None:
        return encoding

    if alias.or_default(sys.flags, "warn_default_encoding", otherwise=False):
        message = "'encoding' argument not specified."
        warn(message, EncodingWarning, stacklevel=(stacklevel + 1))

    return "utf-8" if sys.flags.utf8_mode else "locale"
