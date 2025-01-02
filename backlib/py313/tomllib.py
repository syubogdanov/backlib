from backlib.py313.internal.tomllib import TOMLDecodeError, load, loads


__all__: list[str] = ["TOMLDecodeError", "load", "loads"]


TOMLDecodeError.__module__ = __name__

load.__module__ = __name__
loads.__module__ = __name__
