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

__backlib__: str = "backlib.py313.json"


JSONDecodeError.__module__ = __backlib__

JSONDecoder.__module__ = __backlib__
JSONEncoder.__module__ = __backlib__

dump.__module__ = __backlib__
dumps.__module__ = __backlib__
load.__module__ = __backlib__
loads.__module__ = __backlib__
