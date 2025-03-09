from backlib.py313.internal.backports.tomllib.internal import cpython as py_tomllib


__all__: list[str] = ["TOMLDecodeError", "load", "loads"]

__backlib__: str = "backlib.py313.tomllib"


# ---
# Version: Python 3.11+
# Explain: Added in Python 3.11.
# ---

TOMLDecodeError = py_tomllib.TOMLDecodeError

load = py_tomllib.load
loads = py_tomllib.loads


TOMLDecodeError.__module__ = __backlib__

load.__module__ = __backlib__
loads.__module__ = __backlib__
