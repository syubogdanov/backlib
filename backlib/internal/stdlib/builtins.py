import sys


__all__: list[str] = ["EncodingWarning"]


if sys.version_info >= (3, 10):
    from builtins import EncodingWarning

else:
    class EncodingWarning(Warning):
        """Base class for warnings related to encodings.

        See Also
        --------
        * `builtins.EncodingWarning`.
        """
