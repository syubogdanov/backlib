from backlib.internal.stdlib.py313.io.src import (
    BufferedIOBase,
    BufferedRandom,
    BufferedReader,
    BufferedRWPair,
    BufferedWriter,
    BytesIO,
    FileIO,
    IOBase,
    RawIOBase,
    StringIO,
    TextIOBase,
    TextIOWrapper,
    open,  # noqa: A004
    open_code,
)
from backlib.internal.stdlib.py313.io.src.constants import DEFAULT_BUFFER_SIZE
from backlib.internal.stdlib.py313.io.src.encoding import text_encoding
from backlib.internal.stdlib.py313.io.src.errors import (
    BlockingIOError,  # noqa: A004
    UnsupportedOperation,
)


__all__: list[str] = [
    "DEFAULT_BUFFER_SIZE",
    "BlockingIOError",
    "BufferedIOBase",
    "BufferedRWPair",
    "BufferedRandom",
    "BufferedReader",
    "BufferedWriter",
    "BytesIO",
    "FileIO",
    "IOBase",
    "RawIOBase",
    "StringIO",
    "TextIOBase",
    "TextIOWrapper",
    "UnsupportedOperation",
    "open",
    "open_code",
    "text_encoding",
]

__backlib__: str = "backlib.py313.io"


UnsupportedOperation.__module__ = __backlib__

BufferedIOBase.__module__ = __backlib__
BufferedRWPair.__module__ = __backlib__
BufferedRandom.__module__ = __backlib__
BufferedReader.__module__ = __backlib__
BufferedWriter.__module__ = __backlib__
BytesIO.__module__ = __backlib__
FileIO.__module__ = __backlib__
IOBase.__module__ = __backlib__
RawIOBase.__module__ = __backlib__
StringIO.__module__ = __backlib__
TextIOBase.__module__ = __backlib__
TextIOWrapper.__module__ = __backlib__

open.__module__ = __backlib__
open_code.__module__ = __backlib__
text_encoding.__module__ = __backlib__
