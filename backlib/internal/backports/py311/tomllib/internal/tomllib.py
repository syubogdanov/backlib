import backlib.internal.backports.py311.tomllib.internal.cpython as backport


__all__: list[str] = ["TOMLDecodeError", "load", "loads"]

__backlib__: str = "backlib.py311.tomllib"


TOMLDecodeError = backport.TOMLDecodeError

load = backport.load
loads = backport.loads


TOMLDecodeError.__module__ = __backlib__
load.__module__ = __backlib__
loads.__module__ = __backlib__
