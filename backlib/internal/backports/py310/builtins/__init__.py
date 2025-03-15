import sys


__all__: list[str] = ["EncodingWarning"]


if sys.version_info >= (3, 10):
    from builtins import EncodingWarning
else:
    from backlib.internal.backports.py310.builtins.internal.builtins import EncodingWarning
