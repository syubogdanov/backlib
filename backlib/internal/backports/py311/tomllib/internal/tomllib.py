import backlib.internal.backports.py311.tomllib.internal.cpython as backport


__all__: list[str] = ["TOMLDecodeError", "load", "loads"]

__backlib__: str = "backlib.py311.tomllib"


# ---
# Version: Python 3.11+
# Explain: Added in Python 3.11.
# ---

TOMLDecodeError = backport.TOMLDecodeError
TOMLDecodeError.__module__ = __backlib__

load = backport.load
load.__module__ = __backlib__

loads = backport.loads
loads.__module__ = __backlib__
