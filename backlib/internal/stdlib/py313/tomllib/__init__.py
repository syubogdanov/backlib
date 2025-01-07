from typing import Final

from backlib.internal.stdlib.py313.tomllib.src.parser import TOMLDecodeError, load, loads


__all__: list[str] = ["TOMLDecodeError", "load", "loads"]


MODULE: Final[str] = "backlib.py313.tomllib"


TOMLDecodeError.__module__ = MODULE

load.__module__ = MODULE
loads.__module__ = MODULE
