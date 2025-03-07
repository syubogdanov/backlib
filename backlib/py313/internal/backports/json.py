import json as py_json


__all__: list[str] = [
    "JSONDecodeError",
    "JSONDecoder",
    "JSONEncoder",
    "dump",
    "dumps",
    "load",
    "loads",
]


# ---
# Version: Python 3.9+
# Explain: No changes required.
# ---

JSONDecodeError = py_json.JSONDecodeError
JSONDecoder = py_json.JSONDecoder
JSONEncoder = py_json.JSONEncoder
dump = py_json.dump
dumps = py_json.dumps
load = py_json.load
loads = py_json.loads
