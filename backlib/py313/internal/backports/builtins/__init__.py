import sys


__all__: list[str] = ["EncodingWarning"]


if sys.version_info >= (3, 10):
    from builtins import EncodingWarning
else:
    from backlib.py313.internal.backports.builtins import EncodingWarning
