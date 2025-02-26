from backlib.py313.internal.backports.json.internal.decoder import JSONDecoder
from backlib.py313.internal.backports.json.internal.encoder import JSONEncoder
from backlib.py313.internal.backports.json.internal.errors import JSONDecodeError
from backlib.py313.internal.backports.json.internal.io import dump, dumps, load, loads


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
