from typing import Final

from backlib.internal.stdlib.py313.json.src import (
    JSONDecodeError,
    JSONDecoder,
    JSONEncoder,
    dump,
    dumps,
    load,
    loads,
)


__all__: list[str] = [
    "JSONDecodeError",
    "JSONDecoder",
    "JSONEncoder",
    "dump",
    "dumps",
    "load",
    "loads",
]


MODULE: Final[str] = "backlib.py313.json"


JSONDecodeError.__module__ = MODULE

JSONDecoder.__module__ = MODULE
JSONEncoder.__module__ = MODULE

dump.__module__ = MODULE
dumps.__module__ = MODULE
load.__module__ = MODULE
loads.__module__ = MODULE
