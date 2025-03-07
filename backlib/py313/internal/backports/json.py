import json as py_json

from backlib.py313.internal.utils import alias


__all__: list[str] = [
    "JSONDecodeError",
    "JSONDecoder",
    "JSONEncoder",
    "dump",
    "dumps",
    "load",
    "loads",
]


# Python 3.9+
JSONDecodeError = alias.to(py_json.JSONDecodeError)
JSONDecoder = alias.to(py_json.JSONDecoder)
JSONEncoder = alias.to(py_json.JSONEncoder)
dump = alias.to(py_json.dump)
dumps = alias.to(py_json.dumps)
load = alias.to(py_json.load)
loads = alias.to(py_json.loads)
