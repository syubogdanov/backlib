import backlib.py313.internal.backports.tomllib.internal.cpython as tomllib


__all__: list[str] = ["TOMLDecodeError", "load", "loads"]

__backlib__: str = "backlib.py313.tomllib"


# ---
# Version: Python 3.11+
# Explain: Added in Python 3.11.
# ---

TOMLDecodeError = tomllib.TOMLDecodeError
TOMLDecodeError.__module__ = __backlib__

load = tomllib.load
load.__module__ = __backlib__

loads = tomllib.loads
loads.__module__ = __backlib__
