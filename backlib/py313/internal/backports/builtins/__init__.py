import sys

from backlib.py313.internal.backports.builtins.internal.builtins import EncodingWarning


__all__: list[str] = ["EncodingWarning"]

__backlib__: str = "backlib.py313.builtins"


if sys.version_info >= (3, 10):
    EncodingWarning.__module__ = __backlib__
