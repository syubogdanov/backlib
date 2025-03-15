__all__: list[str] = ["EncodingWarning"]

__backlib__: str = "backlib.py310.builtins"


class EncodingWarning(Warning):
    """Base class for warnings related to encodings.

    See Also
    --------
    * `builtins.EncodingWarning`.
    """


EncodingWarning.__module__ = __backlib__
