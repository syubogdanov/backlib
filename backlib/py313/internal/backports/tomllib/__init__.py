import sys


if sys.version_info >= (3, 11):
    from tomllib import TOMLDecodeError, load, loads
else:
    from backlib.py313.internal.backports.tomllib.internal.tomllib import (
        TOMLDecodeError,
        load,
        loads,
    )


__all__: list[str] = ["TOMLDecodeError", "load", "loads"]
