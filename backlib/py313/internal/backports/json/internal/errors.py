import sys


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


class JSONDecodeError(ValueError):
    """Subclass of `ValueError` with additional properties.

    See Also
    --------
    * `json.JSONDecodeError`.

    Version
    -------
    * Python 3.13.
    """

    def __init__(self: Self, msg: str, doc: str, pos: int) -> None:
        """Initialize the object.

        See Also
        --------
        * `json.JSONDecodeError.__init__`.

        Version
        -------
        * Python 3.13.
        """
        lineno = doc.count("\n", 0, pos) + 1
        colno = pos - doc.rfind("\n", 0, pos)
        errmsg = f"{msg}: line {lineno} column {colno} (char {pos})"
        ValueError.__init__(self, errmsg)
        self.msg = msg
        self.doc = doc
        self.pos = pos
        self.lineno = lineno
        self.colno = colno

    def __reduce__(self: Self) -> tuple[type[Self], tuple[str, str, int]]:
        """Return a `tuple` for pickling.

        See Also
        --------
        * `json.JSONDecodeError.__reduce__`.

        Version
        -------
        * Python 3.13.
        """
        return self.__class__, (self.msg, self.doc, self.pos)
