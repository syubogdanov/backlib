from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, Any, NoReturn

from backlib.internal.stdlib.py313.io.src.constants import DEFAULT_BUFFER_SIZE
from backlib.internal.stdlib.py313.io.src.errors import UnsupportedOperation
from backlib.internal.stdlib.py313.os import SEEK_CUR, SEEK_DATA, SEEK_END, SEEK_HOLE, SEEK_SET
from backlib.internal.typing import Self
from backlib.internal.utils.typing import ReadableBuffer, WriteableBuffer


if TYPE_CHECKING:
    from collections.abc import Iterable
    from types import TracebackType


__all__: list[str] = [
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
]


class IOBase(ABC):  # noqa: B024
    """The abstract base class for all I/O classes.

    See Also
    --------
    * `io.IOBase`.

    Version
    -------
    * Python 3.13.
    """

    _is_closed: bool = False

    def seek(self: Self, pos: int, whence: int = SEEK_SET, /) -> int:  # noqa: ARG002
        """Change the stream position to the given byte offset.

        See Also
        --------
        * `io.IOBase.seek`.

        Version
        -------
        * Python 3.13.
        """
        self._unsupported("seek")

    def tell(self: Self) -> int:
        """Return the current stream position.

        See Also
        --------
        * `io.IOBase.tell`.

        Version
        -------
        * Python 3.13.
        """
        return self.seek(0, SEEK_CUR)

    def truncate(self: Self, pos: int | None = None, /) -> int:  # noqa: ARG002
        """Resize the stream to the given size in bytes.

        See Also
        --------
        * `io.IOBase.truncate`.

        Version
        -------
        * Python 3.13.
        """
        self._unsupported("truncate")

    def flush(self: Self) -> None:
        """Flush the write buffers of the stream if applicable.

        See Also
        --------
        * `io.IOBase.flush`.

        Version
        -------
        * Python 3.13.
        """
        self._check_closed()

    def close(self: Self) -> None:
        """Flush and close this stream.

        See Also
        --------
        * `io.IOBase.close`.

        Version
        -------
        * Python 3.13.
        """
        if not self._is_closed:
            try:
                self.flush()
            finally:
                self._is_closed = True

    def seekable(self: Self) -> bool:
        """Return `True` if the stream supports random access.

        See Also
        --------
        * `io.IOBase.seekable`.

        Version
        -------
        * Python 3.13.
        """
        return False

    def readable(self: Self) -> bool:
        """Return `True` if the stream can be read from.

        See Also
        --------
        * `io.IOBase.readable`.

        Version
        -------
        * Python 3.13.
        """
        return False

    def writable(self: Self) -> bool:
        """Return `True` if the stream supports writing.

        See Also
        --------
        * `io.IOBase.writable`.

        Version
        -------
        * Python 3.13.
        """
        return False

    def fileno(self: Self) -> int:
        """Return the underlying file descriptor (an integer) of the stream if it exists.

        See Also
        --------
        * `io.IOBase.fileno`.

        Version
        -------
        * Python 3.13.
        """
        self._unsupported("fileno")

    def isatty(self: Self) -> bool:
        """Return `True` if the stream is interactive.

        See Also
        --------
        * `io.IOBase.isatty`.

        Version
        -------
        * Python 3.13.
        """
        self._check_closed()
        return False

    def readline(self: Self, size: int | None = None, /) -> bytes:
        """Read and return one line from the stream.

        See Also
        --------
        * `io.IOBase.readline`.

        Version
        -------
        * Python 3.13.
        """
        if size is None:
            size = -1

        if not hasattr(size, "__index__"):
            detail = f"{size!r} is not an integer"
            raise TypeError(detail)

        size = size.__index__()
        buffer = bytearray()

        while size < 0 or len(buffer) < size:
            if not (char := self.read(1)):  # type: ignore[attr-defined]
                break

            buffer += char

            if char == b"\n":
                break

        return bytes(buffer)

    def readlines(self: Self, hint: int | None = None, /) -> list[bytes]:
        """Read and return a list of lines from the stream.

        See Also
        --------
        * `io.IOBase.readlines`.

        Version
        -------
        * Python 3.13.
        """
        if hint is None or hint <= 0:
            return list(self)

        lines: list[bytes] = []
        length: int = 0

        for line in self:
            lines.append(line)
            length += len(line)
            if length >= hint:
                break

        return lines

    def writelines(self: Self, lines: Iterable[ReadableBuffer], /) -> None:
        """Write a list of lines to the stream.

        See Also
        --------
        * `io.IOBase.writelines`.

        Version
        -------
        * Python 3.13.
        """
        self._check_closed()
        for line in lines:
            self.write(line)  # type: ignore[attr-defined]

    @property
    def closed(self: Self) -> bool:
        """`True` if the stream is closed.

        See Also
        --------
        * `io.IOBase.closed`.

        Version
        -------
        * Python 3.13.
        """
        return self._is_closed

    def __del__(self: Self) -> None:
        """Destroy the object.

        See Also
        --------
        * `io.IOBase.__del__`.

        Version
        -------
        * Python 3.13.
        """
        try:
            is_closed = self.closed

        except AttributeError:
            return

        if not is_closed:
            self.close()

    def __enter__(self: Self) -> Self:
        """Return self.

        See Also
        --------
        * `io.IOBase.__enter__`.

        Version
        -------
        * Python 3.13.
        """
        self._check_closed()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Call `close()`.

        See Also
        --------
        * `io.IOBase.__exit__`.

        Version
        -------
        * Python 3.13.
        """
        self.close()

    def __iter__(self: Self) -> Self:
        """Return self."""
        self._check_closed()
        return self

    def __next__(self: Self) -> bytes:
        """Return the next line."""
        if not (line := self.readline()):
            raise StopIteration
        return line

    def _check_closed(self: Self, message: str | None = None) -> None:
        """Raise a ValueError if file is closed."""
        if self.closed:
            detail = "I/O operation on closed file."
            raise ValueError(detail if message is None else message)

    def _check_readable(self: Self, message: str | None = None) -> None:
        """Raise `UnsupportedOperation` if file is not readable."""
        if not self.readable():
            detail = "File or stream is not readable."
            raise UnsupportedOperation(detail if message is None else message)

    def _check_seekable(self: Self, message: str | None = None) -> None:
        """Raise `UnsupportedOperation` if file is not seekable."""
        if not self.seekable():
            detail = "File or stream is not seekable."
            raise UnsupportedOperation(detail if message is None else message)

    def _check_writable(self: Self, message: str | None = None) -> None:
        """Raise `UnsupportedOperation` if file is not writable."""
        if not self.writable():
            detail = "File or stream is not writable."
            raise UnsupportedOperation(detail if message is None else message)

    def _unsupported(self: Self, name: str) -> NoReturn:
        """Raise an `OSError` exception for unsupported operations."""
        detail = f"{self.__class__.__name__}.{name}() not supported"
        raise OSError(detail)


class RawIOBase(IOBase):
    """Base class for raw binary streams.

    See Also
    --------
    * `io.RawIOBase`.

    Version
    -------
    * Python 3.13.
    """

    def read(self: Self, size: int | None = None, /) -> bytes:
        """Read up to size bytes from the object and return them.

        See Also
        --------
        * `io.RawIOBase.read`.

        Version
        -------
        * Python 3.13.
        """
        if size is None or size < 0:
            return self.readall()

        buffer = bytearray(size.__index__())
        count = self.readinto(buffer)

        if count is None:
            return None

        return bytes(buffer[:count])

    def readall(self: Self) -> bytes:
        """Read and return all the bytes from the stream until EOF.

        See Also
        --------
        * `io.RawIOBase.readall`.

        Version
        -------
        * Python 3.13.
        """
        buffer = bytearray()

        while data := self.read(DEFAULT_BUFFER_SIZE):
            buffer += data

        if not buffer:
            return b""

        return bytes(buffer)

    def readinto(self: Self, buffer: WriteableBuffer, /) -> int:  # noqa: ARG002
        """Read bytes into a pre-allocated, writable bytes-like object.

        See Also
        --------
        * `io.RawIOBase.readinto`.

        Version
        -------
        * Python 3.13.
        """
        self._unsupported("readinto")

    def write(self: Self, buffer: ReadableBuffer, /) -> int:  # noqa: ARG002
        """Write the given bytes-like object to the underlying raw stream.

        See Also
        --------
        * `io.RawIOBase.write`.

        Version
        -------
        * Python 3.13.
        """
        self._unsupported("write")


class BufferedIOBase(IOBase):
    """Base class for binary streams that support some kind of buffering.

    See Also
    --------
    * `io.BufferedIOBase`.

    Version
    -------
    * Python 3.13.
    """

    def read(self: Self, size: int | None = None, /) -> bytes:  # noqa: ARG002
        """Read and return up to `size` bytes.

        See Also
        --------
        * `io.BufferedIOBase.read`.

        Version
        -------
        * Python 3.13.
        """
        self._unsupported("read")

    def read1(self: Self, size: int | None = None, /) -> bytes:  # noqa: ARG002
        """Read and return up to `size` bytes, with at most one call.

        See Also
        --------
        * `io.BufferedIOBase.read1`.

        Version
        -------
        * Python 3.13.
        """
        self._unsupported("read1")

    def readinto(self: Self, buffer: WriteableBuffer, /) -> int:
        """Read bytes into a pre-allocated, writable bytes-like object.

        See Also
        --------
        * `io.BufferedIOBase.readinto`.

        Version
        -------
        * Python 3.13.
        """
        return self._readinto(buffer, read1=False)

    def readinto1(self: Self, buffer: WriteableBuffer, /) -> int:
        """Read bytes into a pre-allocated, writable bytes-like object, with at most one call.

        See Also
        --------
        * `io.BufferedIOBase.readinto1`.

        Version
        -------
        * Python 3.13.
        """
        return self._readinto(buffer, read1=True)

    def write(self: Self, buffer: ReadableBuffer, /) -> int:  # noqa: ARG002
        """Write the given bytes-like object.

        See Also
        --------
        * `io.BufferedIOBase.write`.

        Version
        -------
        * Python 3.13.
        """
        self._unsupported("write")

    def detach(self: Self) -> RawIOBase:
        """Separate the underlying raw stream from the buffer and return it.

        See Also
        --------
        * `io.BufferedIOBase.detach`.

        Version
        -------
        * Python 3.13.
        """
        self._unsupported("detach")

    def _readinto(self: Self, buffer: WriteableBuffer, *, read1: bool) -> int:
        if not isinstance(buffer, memoryview):
            buffer = memoryview(buffer)

        buffer = buffer.cast("B")

        reader = self.read1 if read1 else self.read
        data = reader(len(buffer))

        count = len(data)
        buffer[:count] = data

        return count


class BufferedIOMixin(BufferedIOBase):
    """Mixin class for binary streams.

    See Also
    --------
    * `io._BufferedIOMixin`.

    Version
    -------
    * Python 3.13.
    """

    def __init__(self: Self, raw: RawIOBase) -> None:
        """Initialize the object.

        See Also
        --------
        * `io._BufferedIOMixin.__init__`.

        Version
        -------
        * Python 3.13.
        """
        self._raw: RawIOBase | None = raw

    def seek(self: Self, pos: int, whence: int = SEEK_SET, /) -> int:
        """Change the stream position to the given byte offset.

        See Also
        --------
        * `io._BufferedIOMixin.seek`.

        Version
        -------
        * Python 3.13.
        """
        offset = self.raw.seek(pos, whence)  # type: ignore[union-attr]

        if offset < 0:
            detail = "seek() returned an invalid position"
            raise OSError(detail)

        return offset

    def tell(self: Self) -> int:
        """Return the current stream position.

        See Also
        --------
        * `io._BufferedIOMixin.tell`.

        Version
        -------
        * Python 3.13.
        """
        offset = self.raw.tell()  # type: ignore[union-attr]

        if offset < 0:
            detail = "tell() returned an invalid position"
            raise OSError(detail)

        return offset

    def truncate(self: Self, pos: int | None = None, /) -> int:
        """Resize the stream to the given size in bytes.

        See Also
        --------
        * `io._BufferedIOMixin.truncate`.

        Version
        -------
        * Python 3.13.
        """
        self._check_closed()
        self._check_writable()

        self.flush()

        if pos is None:
            pos = self.tell()

        return self.raw.truncate(pos)  # type: ignore[union-attr]

    def flush(self: Self) -> None:
        """Flush the write buffers of the stream if applicable.

        See Also
        --------
        * `io._BufferedIOMixin.flush`.

        Version
        -------
        * Python 3.13.
        """
        if self.closed:
            detail = "flush on closed file"
            raise ValueError(detail)
        self.raw.flush()  # type: ignore[union-attr]

    def close(self: Self) -> None:
        """Flush and close this stream.

        See Also
        --------
        * `io._BufferedIOMixin.close`.

        Version
        -------
        * Python 3.13.
        """
        if self.raw is not None and not self.closed:
            try:
                self.flush()
            finally:
                self.raw.close()

    def detach(self: Self) -> RawIOBase:
        """Separate the underlying raw stream from the buffer and return it.

        See Also
        --------
        * `io._BufferedIOMixin.detach`.

        Version
        -------
        * Python 3.13.
        """
        raw = self._raw

        if raw is None:
            detail = "raw stream already detached"
            raise ValueError(detail)

        self.flush()
        self._raw = None

        return raw

    def seekable(self: Self) -> bool:
        """Return `True` if the stream supports random access.

        See Also
        --------
        * `io._BufferedIOMixin.seekable`.

        Version
        -------
        * Python 3.13.
        """
        return self.raw.seekable()  # type: ignore[union-attr]

    def fileno(self: Self) -> int:
        """Return the underlying file descriptor (an integer) of the stream if it exists.

        See Also
        --------
        * `io._BufferedIOMixin.fileno`.

        Version
        -------
        * Python 3.13.
        """
        return self.raw.fileno()  # type: ignore[union-attr]

    def isatty(self: Self) -> bool:
        """Return `True` if the stream is interactive.

        See Also
        --------
        * `io._BufferedIOMixin.isatty`.

        Version
        -------
        * Python 3.13.
        """
        return self.raw.isatty()  # type: ignore[union-attr]

    @property
    def raw(self: Self) -> RawIOBase | None:
        """The underlying raw stream.

        See Also
        --------
        * `io._BufferedIOMixin.raw`.

        Version
        -------
        * Python 3.13.
        """
        return self._raw

    @property
    def closed(self: Self) -> bool:
        """`True` if the underlying stream is closed.

        See Also
        --------
        * `io._BufferedIOMixin.closed`.

        Version
        -------
        * Python 3.13.
        """
        return self.raw.closed  # type: ignore[union-attr]

    @property
    def name(self: Self) -> int | str | bytes:
        """The file name.

        See Also
        --------
        * `io._BufferedIOMixin.name`.

        Version
        -------
        * Python 3.13.
        """
        return self.raw.name  # type: ignore[union-attr]

    @property
    def mode(self: Self) -> str:
        """The mode as given in the constructor.

        See Also
        --------
        * `io._BufferedIOMixin.mode`.

        Version
        -------
        * Python 3.13.
        """
        return self.raw.mode  # type: ignore[union-attr]

    def __getstate__(self: Self) -> dict[str, Any]:
        """Return the state of the object.

        See Also
        --------
        * `io._BufferedIOMixin.__getstate__`.

        Version
        -------
        * Python 3.13.
        """
        detail = f"cannot pickle {self.__class__.__name__!r} object"
        raise TypeError(detail)

    def __repr__(self: Self) -> str:
        """Return a string representation of the object.

        See Also
        --------
        * `io._BufferedIOMixin.__repr__`.

        Version
        -------
        * Python 3.13.
        """
        modname = self.__class__.__module__
        clsname = self.__class__.__qualname__

        try:
            name = self.name
        except AttributeError:
            return f"<{modname}.{clsname}>"
        else:
            return f"<{modname}.{clsname} name={name!r}>"


class BytesIO(BufferedIOBase):
    """A binary stream using an in-memory bytes buffer.

    See Also
    --------
    * `io.BytesIO`.

    Version
    -------
    * Python 3.13.
    """


class BufferedRWPair:
    pass


class BufferedRandom:
    pass


class BufferedReader:
    pass


class BufferedWriter:
    pass


class FileIO:
    pass


class StringIO:
    pass


class TextIOBase:
    pass


class TextIOWrapper:
    pass
