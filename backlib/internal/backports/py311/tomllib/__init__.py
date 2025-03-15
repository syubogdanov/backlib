import sys


if sys.version_info >= (3, 11):
    from tomllib import TOMLDecodeError, load, loads
else:
    from backlib.internal.backports.py311.tomllib.internal.tomllib import (
        TOMLDecodeError,
        load,
        loads,
    )


__all__: list[str] = ["TOMLDecodeError", "load", "loads"]
