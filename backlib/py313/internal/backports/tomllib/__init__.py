from backlib.py313.internal.backports.tomllib.internal.tomllib import TOMLDecodeError, load, loads


__all__: list[str] = ["TOMLDecodeError", "load", "loads"]

__backlib__: str = "backlib.py313.tomllib"


TOMLDecodeError.__module__ = __backlib__

load.__module__ = __backlib__
loads.__module__ = __backlib__
