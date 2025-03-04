from builtins import BlockingIOError

from backlib.py313.internal.backports.io import (
    DEFAULT_BUFFER_SIZE,
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
    UnsupportedOperation,
    open,
    open_code,
    text_encoding,
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
