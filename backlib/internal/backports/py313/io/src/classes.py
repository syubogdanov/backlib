from __future__ import annotations

from abc import ABC
from threading import Lock
from typing import TYPE_CHECKING, Any, Generic, NoReturn

from backlib.internal.backports.py313.errno import EAGAIN
from backlib.internal.backports.py313.io.src.constants import DEFAULT_BUFFER_SIZE
from backlib.internal.backports.py313.io.src.errors import UnsupportedOperation
from backlib.internal.backports.py313.os import SEEK_CUR, SEEK_DATA, SEEK_END, SEEK_HOLE, SEEK_SET
from backlib.internal.markers import aware, todo
from backlib.internal.stdlib.typing import AnyStr, Self
from backlib.internal.utils.typing import ReadableBuffer, WriteableBuffer


if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator
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


SEEK_FLAGS = {SEEK_SET, SEEK_CUR, SEEK_END, SEEK_DATA, SEEK_HOLE}


class IOBase(ABC, Generic[AnyStr]):
    """The abstract base class for all I/O classes.

    Notes
    -----
    * As opposed to `io.IOBase`:
        - is generic with `AnyStr` constraint;
        - has `read` and `write` methods defined.

    See Also
    --------
    * `io.IOBase`.

    Version
    -------
    * Python 3.13.
    """

    _is_closed: bool = False

    def seek(self: Self, pos: int, whence: int = SEEK_SET, /) -> int:
        """Change the stream position to the given byte offset.

        See Also
        --------
        * `io.IOBase.seek`.

        Version
        -------
        * Python 3.13.
        """
        aware.unused(pos, whence)
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

    def truncate(self: Self, pos: int | None = None, /) -> int:
        """Resize the stream to the given size in bytes.

        See Also
        --------
        * `io.IOBase.truncate`.

        Version
        -------
        * Python 3.13.
        """
        aware.unused(pos)
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

    def readline(self: Self, size: int | None = None, /) -> AnyStr:
        """Read and return one line from the stream.

        See Also
        --------
        * `io.IOBase.readline`.

        Version
        -------
        * Python 3.13.
        """
        aware.unused(size)
        self._unsupported("readline")

    def readlines(self: Self, hint: int | None = None, /) -> list[AnyStr]:
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

        lines: list[AnyStr] = []
        length: int = 0

        for line in self:
            lines.append(line)
            length += len(line)
            if length >= hint:
                break

        return lines

    def writelines(self: Self, lines: Iterable[AnyStr], /) -> None:
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
            self.write(line)

    def read(self: Self, size: int | None = None, /) -> AnyStr | None:
        """Read and return up to `size` bytes.

        See Also
        --------
        * `io.IOBase.read`.

        Version
        -------
        * Python 3.13.
        """
        aware.unused(size)
        self._unsupported("read")

    def write(self: Self, buffer: AnyStr, /) -> int | None:
        """Write the given object to the underlying raw stream.

        See Also
        --------
        * `io.IOBase.write`.

        Version
        -------
        * Python 3.13.
        """
        aware.unused(buffer)
        self._unsupported("write")

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

    def __iter__(self: Self) -> Iterator[AnyStr]:
        """Return self.

        See Also
        --------
        * `io.IOBase.__iter__`.

        Version
        -------
        * Python 3.13.
        """
        self._check_closed()
        return self

    def __next__(self: Self) -> AnyStr:
        """Return the next line.

        See Also
        --------
        * `io.IOBase.__next__`.

        Version
        -------
        * Python 3.13.
        """
        if line := self.readline():
            return line
        raise StopIteration

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


class BinaryIOBase(IOBase[bytes]):
    """Base class for binary I/O."""

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
            if not (char := self.read(1)):
                break

            buffer += char

            if char == b"\n":
                break

        return bytes(buffer)


class RawIOBase(BinaryIOBase):
    """Base class for raw binary streams.

    Notes
    -----
    * As opposed to `io.RawIOBase`, has `name` and `mode` properties defined.


    See Also
    --------
    * `io.RawIOBase`.

    Version
    -------
    * Python 3.13.
    """

    def read(self: Self, size: int | None = None, /) -> bytes | None:
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

    def readall(self: Self) -> bytes | None:
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
            return data

        return bytes(buffer)

    def readinto(self: Self, buffer: WriteableBuffer, /) -> int | None:
        """Read bytes into a pre-allocated, writable bytes-like object.

        See Also
        --------
        * `io.RawIOBase.readinto`.

        Version
        -------
        * Python 3.13.
        """
        aware.unused(buffer)
        self._unsupported("readinto")

    def write(self: Self, buffer: ReadableBuffer, /) -> int | None:
        """Write the given bytes-like object to the underlying raw stream.

        See Also
        --------
        * `io.RawIOBase.write`.

        Version
        -------
        * Python 3.13.
        """
        aware.unused(buffer)
        self._unsupported("write")

    @property
    def name(self: Self) -> int | str | bytes:
        """The file name.

        See Also
        --------
        * `io.RawIOBase.name`.

        Version
        -------
        * Python 3.13.
        """
        self._unsupported("name")

    @property
    def mode(self: Self) -> str:
        """The mode as given in the constructor.

        See Also
        --------
        * `io.RawIOBase.mode`.

        Version
        -------
        * Python 3.13.
        """
        self._unsupported("mode")


class BufferedIOBase(BinaryIOBase):
    """Base class for binary streams that support some kind of buffering.

    See Also
    --------
    * `io.BufferedIOBase`.

    Version
    -------
    * Python 3.13.
    """

    def read(self: Self, size: int | None = None, /) -> bytes | None:
        """Read and return up to `size` bytes.

        See Also
        --------
        * `io.BufferedIOBase.read`.

        Version
        -------
        * Python 3.13.
        """
        aware.unused(size)
        self._unsupported("read")

    def read1(self: Self, size: int | None = None, /) -> bytes | None:
        """Read and return up to `size` bytes, with at most one call.

        See Also
        --------
        * `io.BufferedIOBase.read1`.

        Version
        -------
        * Python 3.13.
        """
        aware.unused(size)
        self._unsupported("read1")

    def readinto(self: Self, buffer: WriteableBuffer, /) -> int | None:
        """Read bytes into a pre-allocated, writable bytes-like object.

        See Also
        --------
        * `io.BufferedIOBase.readinto`.

        Version
        -------
        * Python 3.13.
        """
        return self._readinto(buffer, read1=False)

    def readinto1(self: Self, buffer: WriteableBuffer, /) -> int | None:
        """Read bytes into a pre-allocated, writable bytes-like object, with at most one call.

        See Also
        --------
        * `io.BufferedIOBase.readinto1`.

        Version
        -------
        * Python 3.13.
        """
        return self._readinto(buffer, read1=True)

    def write(self: Self, buffer: ReadableBuffer, /) -> int:
        """Write the given bytes-like object.

        See Also
        --------
        * `io.BufferedIOBase.write`.

        Version
        -------
        * Python 3.13.
        """
        aware.unused(buffer)
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

    def _readinto(self: Self, buffer: WriteableBuffer, *, read1: bool) -> int | None:
        """Read bytes into a pre-allocated, writable bytes-like object."""
        if not isinstance(buffer, memoryview):
            buffer = memoryview(buffer)

        buffer = buffer.cast("B")

        reader = self.read1 if read1 else self.read
        data = reader(len(buffer))

        if data is None:
            return None

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
        if self.raw is None:
            detail = "seek() on a detached stream"
            raise AttributeError(detail)

        offset = self.raw.seek(pos, whence)

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
        if self.raw is None:
            detail = "tell() on a detached stream"
            raise AttributeError(detail)

        offset = self.raw.tell()

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
        if self.raw is None:
            detail = "truncate() on a detached stream"
            raise AttributeError(detail)

        self._check_closed()
        self._check_writable()

        self.flush()

        if pos is None:
            pos = self.tell()

        return self.raw.truncate(pos)

    def flush(self: Self) -> None:
        """Flush the write buffers of the stream if applicable.

        See Also
        --------
        * `io._BufferedIOMixin.flush`.

        Version
        -------
        * Python 3.13.
        """
        if self.raw is None:
            detail = "flush() on a detached stream"
            raise AttributeError(detail)

        if self.closed:
            detail = "flush on closed file"
            raise ValueError(detail)

        self.raw.flush()

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
        if self.raw is None:
            detail = "raw stream already detached"
            raise ValueError(detail)

        self.flush()

        raw = self.raw
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
        if self.raw is None:
            detail = "seekable() on a detached stream"
            raise AttributeError(detail)

        return self.raw.seekable()

    def fileno(self: Self) -> int:
        """Return the underlying file descriptor (an integer) of the stream if it exists.

        See Also
        --------
        * `io._BufferedIOMixin.fileno`.

        Version
        -------
        * Python 3.13.
        """
        if self.raw is None:
            detail = "fileno() on a detached stream"
            raise AttributeError(detail)

        return self.raw.fileno()

    def isatty(self: Self) -> bool:
        """Return `True` if the stream is interactive.

        See Also
        --------
        * `io._BufferedIOMixin.isatty`.

        Version
        -------
        * Python 3.13.
        """
        if self.raw is None:
            detail = "isatty() on a detached stream"
            raise AttributeError(detail)

        return self.raw.isatty()

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
        if self.raw is None:
            detail = "accessing 'closed' on a detached stream"
            raise AttributeError(detail)

        return self.raw.closed

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
        if self.raw is None:
            detail = "accessing 'name' on a detached stream"
            raise AttributeError(detail)

        return self.raw.name

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
        if self.raw is None:
            detail = "accessing 'mode' on a detached stream"
            raise AttributeError(detail)

        return self.raw.mode

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

    def __init__(self: Self, initial_bytes: ReadableBuffer | None = None) -> None:
        """Initialize the object.

        See Also
        --------
        * `io.BytesIO.__init__`.

        Version
        -------
        * Python 3.13.
        """
        self._buffer = bytearray()
        self._pos: int = 0

        if initial_bytes is not None:
            self._buffer += initial_bytes

    def getvalue(self: Self) -> bytes:
        """Return `bytes` containing the entire contents of the buffer.

        See Also
        --------
        * `io.BytesIO.getvalue`.

        Version
        -------
        * Python 3.13.
        """
        if self.closed:
            detail = "getvalue on closed file"
            raise ValueError(detail)

        return bytes(self._buffer)

    def getbuffer(self: Self) -> memoryview:
        """Return a readable and writable view of the buffer.

        See Also
        --------
        * `io.BytesIO.getbuffer`.

        Version
        -------
        * Python 3.13.
        """
        if self.closed:
            detail = "getbuffer on closed file"
            raise ValueError(detail)

        return memoryview(self._buffer)

    def close(self: Self) -> None:
        """Flush and close this stream.

        See Also
        --------
        * `io.BytesIO.close`.

        Version
        -------
        * Python 3.13.
        """
        self._buffer.clear()
        super().close()

    def read(self: Self, size: int | None = None, /) -> bytes:
        """Read and return up to `size` bytes.

        See Also
        --------
        * `io.BytesIO.read`.

        Version
        -------
        * Python 3.13.
        """
        if self.closed:
            detail = "read from closed file"
            raise ValueError(detail)

        if size is None:
            size = -1

        if not hasattr(size, "__index__"):
            detail = f"{size!r} is not an integer"
            raise TypeError(detail)

        size = size.__index__()

        if size < 0:
            size = len(self._buffer)

        if len(self._buffer) <= self._pos:
            return b""

        offset = min(len(self._buffer), self._pos + size)
        buffer = self._buffer[self._pos : offset]
        self._pos = offset

        return bytes(buffer)

    def read1(self: Self, size: int | None = None, /) -> bytes:
        """Read and return up to `size` bytes, with at most one call.

        See Also
        --------
        * `io.BytesIO.read1`.

        Version
        -------
        * Python 3.13.
        """
        return self.read(size)

    def write(self: Self, buffer: ReadableBuffer, /) -> int:
        """Write the given bytes-like object.

        See Also
        --------
        * `io.BytesIO.write`.

        Version
        -------
        * Python 3.13.
        """
        if self.closed:
            detail = "write to closed file"
            raise ValueError(detail)

        if isinstance(buffer, str):
            detail = "can't write str to binary stream"
            raise TypeError(detail)

        with memoryview(buffer) as view:
            nbytes = view.nbytes

        if not nbytes:
            return 0

        if self._pos > len(self._buffer):
            length = self._pos - len(self._buffer)
            padding = b"\x00" * length
            self._buffer += padding

        self._buffer[self._pos:self._pos + nbytes] = bytes(buffer)
        self._pos += nbytes

        return nbytes

    def seek(self: Self, pos: int, whence: int = SEEK_SET, /) -> int:
        """Change the stream position to the given byte offset.

        See Also
        --------
        * `io.BytesIO.seek`.

        Version
        -------
        * Python 3.13.
        """
        if self.closed:
            detail = "seek on closed file"
            raise ValueError(detail)

        if not hasattr(pos, "__index__"):
            detail = f"{pos!r} is not an integer"
            raise TypeError(detail)

        pos = pos.__index__()

        if whence == SEEK_SET and pos < 0:
            detail = f"negative seek position {pos!r}"
            raise ValueError(detail)

        if whence == SEEK_SET:
            self._pos = pos
            return self._pos

        if whence == SEEK_CUR:
            self._pos = max(0, self._pos + pos)
            return self._pos

        if whence == SEEK_END:
            self._pos = max(0, len(self._buffer) + pos)
            return self._pos

        detail = "unsupported whence value"
        raise ValueError(detail)

    def tell(self: Self) -> int:
        """Return the current stream position.

        See Also
        --------
        * `io.BytesIO.tell`.

        Version
        -------
        * Python 3.13.
        """
        if self.closed:
            detail = "tell on closed file"
            raise ValueError(detail)

        return self._pos

    def truncate(self: Self, pos: int | None = None, /) -> int:
        """Resize the stream to the given size in bytes.

        See Also
        --------
        * `io.BytesIO.truncate`.

        Version
        -------
        * Python 3.13.
        """
        if self.closed:
            detail = "truncate on closed file"
            raise ValueError(detail)

        if pos is None:
            pos = self._pos

        if not hasattr(pos, "__index__"):
            detail = f"{pos!r} is not an integer"
            raise TypeError(detail)

        pos = pos.__index__()

        if pos < 0:
            detail = f"negative truncate position {pos!r}"
            raise ValueError(detail)

        del self._buffer[pos:]
        return pos

    def readable(self: Self) -> bool:
        """Return `True` if the stream can be read from.

        See Also
        --------
        * `io.BytesIO.readable`.

        Version
        -------
        * Python 3.13.
        """
        if self.closed:
            detail = "I/O operation on closed file."
            raise ValueError(detail)

        return True

    def writable(self: Self) -> bool:
        """Return `True` if the stream supports writing.

        See Also
        --------
        * `io.BytesIO.writable`.

        Version
        -------
        * Python 3.13.
        """
        if self.closed:
            detail = "I/O operation on closed file."
            raise ValueError(detail)

        return True

    def seekable(self: Self) -> bool:
        """Return `True` if the stream supports random access.

        See Also
        --------
        * `io.BytesIO.seekable`.

        Version
        -------
        * Python 3.13.
        """
        if self.closed:
            detail = "I/O operation on closed file."
            raise ValueError(detail)

        return True

    def __getstate__(self: Self) -> dict[str, Any]:
        """Return the state of the object.

        See Also
        --------
        * `io.BytesIO.__getstate__`.

        Version
        -------
        * Python 3.13.
        """
        if self.closed:
            detail = "__getstate__ on closed file"
            raise ValueError(detail)

        return self.__dict__.copy()


class BufferedReader(BufferedIOMixin):
    """A buffered binary stream.

    See Also
    --------
    * `io.BufferedReader`.

    Version
    -------
    * Python 3.13.
    """

    def __init__(self: Self, raw: RawIOBase, buffer_size: int = DEFAULT_BUFFER_SIZE) -> None:
        """Initialize the object.

        See Also
        --------
        * `io.BufferedReader.__init__`.

        Version
        -------
        * Python 3.13.
        """
        if not raw.readable():
            detail = '"raw" argument must be readable.'
            raise OSError(detail)

        BufferedIOMixin.__init__(self, raw)

        if buffer_size <= 0:
            detail = "invalid buffer size"
            raise ValueError(detail)

        self.buffer_size = buffer_size
        self._read_lock = Lock()

        self._read_buf = b""
        self._read_pos = 0

    def readable(self: Self) -> bool:
        """Return `True` if the stream can be read from.

        See Also
        --------
        * `io.BufferedReader.readable`.

        Version
        -------
        * Python 3.13.
        """
        if self.raw is None:
            detail = "readable() on a detached stream"
            raise AttributeError(detail)

        return self.raw.readable()

    def read(self: Self, size: int | None = None, /) -> bytes | None:
        """Read and return up to `size` bytes.

        See Also
        --------
        * `io.BufferedReader.read`.

        Version
        -------
        * Python 3.13.
        """
        if size is not None and size < -1:
            detail = "invalid number of bytes to read"
            raise ValueError(detail)

        with self._read_lock:
            return self._read_unlocked(size)

    def peek(self: Self, size: int = 0, /) -> bytes:
        """Return bytes from the stream without advancing the position.

        See Also
        --------
        * `io.BufferedReader.peek`.

        Version
        -------
        * Python 3.13.
        """
        self._check_closed("peek of closed file")
        with self._read_lock:
            return self._peek_unlocked(size)

    def read1(self: Self, size: int | None = None, /) -> bytes | None:
        """Read and return up to `size` bytes, with at most one call.

        See Also
        --------
        * `io.BufferedReader.read1`.

        Version
        -------
        * Python 3.13.
        """
        self._check_closed("read of closed file")

        if size is None or size < 0:
            size = self.buffer_size

        if size == 0:
            return b""

        with self._read_lock:
            self._peek_unlocked(n=1)

            size = min(size, len(self._read_buf) - self._read_pos)
            return self._read_unlocked(size)

    def tell(self: Self) -> int:
        """Return the current stream position.

        See Also
        --------
        * `io.BufferedReader.tell`.

        Version
        -------
        * Python 3.13.
        """
        offset = BufferedIOMixin.tell(self)
        return max(offset - len(self._read_buf) + self._read_pos, 0)

    def seek(self: Self, pos: int, whence: int = SEEK_SET, /) -> int:
        """Change the stream position to the given byte offset.

        See Also
        --------
        * `io.BufferedReader.seek`.

        Version
        -------
        * Python 3.13.
        """
        if whence not in SEEK_FLAGS:
            detail = "invalid whence value"
            raise ValueError(detail)

        self._check_closed("seek of closed file")

        with self._read_lock:
            if whence == SEEK_CUR:
                pos -= len(self._read_buf) - self._read_pos

            pos = BufferedIOMixin.seek(self, pos, whence)
            self._reset_read_buf()

            return pos

    def _peek_unlocked(self: Self, n: int = 0) -> bytes:
        """Read and return up to `n` bytes without advancing the position."""
        if self.raw is None:
            detail = "peek() on a detached stream"
            raise AttributeError(detail)

        want = min(n, self.buffer_size)
        have = len(self._read_buf) - self._read_pos

        if have < want or have <= 0:
            to_read = self.buffer_size - have
            current = self.raw.read(to_read)

            if current:
                self._read_buf = self._read_buf[self._read_pos:] + current
                self._read_pos = 0

        return self._read_buf[self._read_pos:]

    @todo.refactor
    def _read_unlocked(self: Self, n: int | None = None) -> bytes | None:
        """Read and return up to `n` bytes."""
        if self.raw is None:
            detail = "read() on a detached stream"
            raise AttributeError(detail)

        nodata_val = b""
        empty_values = (b"", None)
        buf = self._read_buf
        pos = self._read_pos

        # Special case for when the number of bytes to read is unspecified.
        if n is None or n == -1:
            self._reset_read_buf()
            if hasattr(self.raw, "readall"):
                chunk = self.raw.readall()
                if chunk is None:
                    return buf[pos:] or None
                return buf[pos:] + chunk
            chunks = [buf[pos:]]  # Strip the consumed bytes.
            current_size = 0
            while True:
                # Read until EOF or until read() would block.
                chunk = self.raw.read()
                if chunk in empty_values:
                    nodata_val = chunk  # type: ignore[assignment]
                    break
                current_size += len(chunk)  # type: ignore[arg-type]
                chunks.append(chunk)  # type: ignore[arg-type]
            return b"".join(chunks) or nodata_val

        # The number of bytes to read is specified, return at most n bytes.
        avail = len(buf) - pos  # Length of the available buffered data.
        if n <= avail:
            # Fast path: the data to read is fully buffered.
            self._read_pos += n
            return buf[pos:pos+n]
        # Slow path: read from the stream until enough bytes are read,
        # or until an EOF occurs or until read() would block.
        chunks = [buf[pos:]]
        wanted = max(self.buffer_size, n)
        while avail < n:
            chunk = self.raw.read(wanted)
            if chunk in empty_values:
                nodata_val = chunk  # type: ignore[assignment]
                break
            avail += len(chunk)  # type: ignore[arg-type]
            chunks.append(chunk)  # type: ignore[arg-type]
        # n is more than avail only when an EOF occurred or when
        # read() would have blocked.
        n = min(n, avail)
        out = b"".join(chunks)
        self._read_buf = out[n:]  # Save the extra data in the buffer.
        self._read_pos = 0
        return out[:n] if out else nodata_val

    @todo.refactor
    def _readinto(self: Self, buffer: WriteableBuffer, *, read1: bool) -> int:  # noqa: C901
        """Read bytes into a pre-allocated, writable bytes-like object."""
        if self.raw is None:
            detail = "readinto() on a detached stream"
            raise AttributeError(detail)

        self._check_closed("readinto of closed file")

        if not isinstance(buffer, memoryview):
            buffer = memoryview(buffer)

        if buffer.nbytes == 0:
            return 0

        buffer = buffer.cast("B")
        written: int = 0

        with self._read_lock:
            while written < len(buffer):
                if avail := min(len(self._read_buf) - self._read_pos, len(buffer)):
                    buffer[written:written+avail] = \
                        self._read_buf[self._read_pos:self._read_pos+avail]
                    self._read_pos += avail
                    written += avail
                    if written == len(buffer):
                        break

                if len(buffer) - written > self.buffer_size:
                    n = self.raw.readinto(buffer[written:])
                    if not n:
                        break
                    written += n

                elif not (read1 and written):
                    if not self._peek_unlocked(1):
                        break # eof

                if read1 and written:
                    break

        return written

    def _reset_read_buf(self: Self) -> None:
        """Reset the read buffer."""
        self._read_buf = b""
        self._read_pos = 0


class BufferedWriter(BufferedIOMixin):
    """A buffered binary stream.

    See Also
    --------
    * `io.BufferedWriter`.

    Version
    -------
    * Python 3.13.
    """

    def __init__(self: Self, raw: RawIOBase, buffer_size: int = DEFAULT_BUFFER_SIZE) -> None:
        """Initialize the object.

        See Also
        --------
        * `io.BufferedWriter.__init__`.

        Version
        -------
        * Python 3.13.
        """
        if not raw.writable():
            detail = '"raw" argument must be writable.'
            raise OSError(detail)

        BufferedIOMixin.__init__(self, raw)

        if buffer_size <= 0:
            detail = "invalid buffer size"
            raise ValueError(detail)

        self.buffer_size = buffer_size

        self._write_buf = bytearray()
        self._write_lock = Lock()

    def writable(self: Self) -> bool:
        """Return `True` if the stream supports writing.

        See Also
        --------
        * `io.BufferedWriter.writable`.

        Version
        -------
        * Python 3.13.
        """
        if self.raw is None:
            detail = "writable() on a detached stream"
            raise AttributeError(detail)

        return self.raw.writable()

    def write(self: Self, buffer: ReadableBuffer, /) -> int:
        """Write the given bytes-like object.

        See Also
        --------
        * `io.BufferedWriter.write`.

        Version
        -------
        * Python 3.13.
        """
        if isinstance(buffer, str):
            detail = "can't write str to binary stream"
            raise TypeError(detail)

        with self._write_lock:
            if self.closed:
                detail = "write to closed file"
                raise ValueError(detail)

            if len(self._write_buf) > self.buffer_size:
                self._flush_unlocked()

            before = len(self._write_buf)
            self._write_buf.extend(bytes(buffer))
            written = len(self._write_buf) - before

            if len(self._write_buf) <= self.buffer_size:
                return written

            try:
                self._flush_unlocked()

            except BlockingIOError as exception:
                if len(self._write_buf) > self.buffer_size:
                    overage = len(self._write_buf) - self.buffer_size
                    written -= overage
                    self._write_buf = self._write_buf[:self.buffer_size]
                    raise BlockingIOError(exception.errno, exception.strerror, written) from None

            return written

    def truncate(self: Self, pos: int | None = None, /) -> int:
        """Resize the stream to the given size in bytes.

        See Also
        --------
        * `io.BufferedWriter.truncate`.

        Version
        -------
        * Python 3.13.
        """
        if self.raw is None:
            detail = "truncate() on a detached stream"
            raise AttributeError(detail)

        with self._write_lock:
            self._flush_unlocked()
            if pos is None:
                pos = self.raw.tell()
            return self.raw.truncate(pos)

    def flush(self: Self) -> None:
        """Flush the write buffers of the stream if applicable.

        See Also
        --------
        * `io.BufferedWriter.flush`.

        Version
        -------
        * Python 3.13.
        """
        with self._write_lock:
            self._flush_unlocked()

    def tell(self: Self) -> int:
        """Return the current stream position.

        See Also
        --------
        * `io.BufferedWriter.tell`.

        Version
        -------
        * Python 3.13.
        """
        return BufferedIOMixin.tell(self) + len(self._write_buf)

    def seek(self: Self, pos: int, whence: int = SEEK_SET, /) -> int:
        """Change the stream position to the given byte offset.

        See Also
        --------
        * `io.BufferedWriter.seek`.

        Version
        -------
        * Python 3.13.
        """
        if whence not in SEEK_FLAGS:
            detail = "invalid whence value"
            raise ValueError(detail)

        with self._write_lock:
            self._flush_unlocked()
            return BufferedIOMixin.seek(self, pos, whence)

    def close(self: Self) -> None:
        """Flush and close this stream.

        See Also
        --------
        * `io.BufferedWriter.close`.

        Version
        -------
        * Python 3.13.
        """
        with self._write_lock:
            if self.raw is None or self.closed:
                return

        try:
            self.flush()

        finally:
            with self._write_lock:
                self.raw.close()

    def _flush_unlocked(self) -> None:
        """Flush the write buffers of the stream if applicable."""
        if self.raw is None:
            detail = "flush() on a detached stream"
            raise AttributeError(detail)

        if self.closed:
            detail = "flush on closed file"
            raise ValueError(detail)

        while self._write_buf:
            try:
                count = self.raw.write(self._write_buf)

            except BlockingIOError:
                detail = "self.raw should implement RawIOBase: it should not raise BlockingIOError"
                raise RuntimeError(detail) from None

            if count is None:
                detail = "write could not complete without blocking"
                raise BlockingIOError(EAGAIN, detail, 0)

            if count > len(self._write_buf) or count < 0:
                detail = "write() returned incorrect number of bytes"
                raise OSError(detail)

            del self._write_buf[:count]


class BufferedRWPair(BufferedIOBase):
    """A buffered binary stream.

    See Also
    --------
    * `io.BufferedRWPair`.

    Version
    -------
    * Python 3.13.
    """

    def __init__(
        self: Self,
        reader: RawIOBase,
        writer: RawIOBase,
        buffer_size: int = DEFAULT_BUFFER_SIZE,
    ) -> None:
        """Initialize the object.

        See Also
        --------
        * `io.BufferedRWPair.__init__`.

        Version
        -------
        * Python 3.13.
        """
        if not reader.readable():
            detail = '"reader" argument must be readable.'
            raise OSError(detail)

        if not writer.writable():
            detail = '"writer" argument must be writable.'
            raise OSError(detail)

        self.reader = BufferedReader(reader, buffer_size)
        self.writer = BufferedWriter(writer, buffer_size)

    def read(self: Self, size: int | None = None, /) -> bytes | None:
        """Read and return up to `size` bytes.

        See Also
        --------
        * `io.BufferedRWPair.read`.

        Version
        -------
        * Python 3.13.
        """
        if size is None:
            size = -1
        return self.reader.read(size)

    def readinto(self: Self, buffer: WriteableBuffer, /) -> int | None:
        """Read bytes into a pre-allocated, writable bytes-like object.

        See Also
        --------
        * `io.BufferedRWPair.readinto`.

        Version
        -------
        * Python 3.13.
        """
        return self.reader.readinto(buffer)

    def write(self: Self, buffer: ReadableBuffer, /) -> int:
        """Write the given bytes-like object.

        See Also
        --------
        * `io.BufferedRWPair.write`.

        Version
        -------
        * Python 3.13.
        """
        return self.writer.write(buffer)

    def peek(self: Self, size: int = 0, /) -> bytes:
        """Return bytes from the stream without advancing the position.

        See Also
        --------
        * `io.BufferedRWPair.peek`.

        Version
        -------
        * Python 3.13.
        """
        return self.reader.peek(size)

    def read1(self: Self, size: int | None = None, /) -> bytes | None:
        """Read and return up to `size` bytes, with at most one call.

        See Also
        --------
        * `io.BufferedRWPair.read1`.

        Version
        -------
        * Python 3.13.
        """
        return self.reader.read1(size)

    def readinto1(self: Self, buffer: WriteableBuffer, /) -> int | None:
        """Read bytes into a pre-allocated, writable bytes-like object, with at most one call.

        See Also
        --------
        * `io.BufferedRWPair.readinto1`.

        Version
        -------
        * Python 3.13.
        """
        return self.reader.readinto1(buffer)

    def readable(self: Self) -> bool:
        """Return `True` if the stream can be read from.

        See Also
        --------
        * `io.BufferedRWPair.readable`.

        Version
        -------
        * Python 3.13.
        """
        return self.reader.readable()

    def writable(self: Self) -> bool:
        """Return `True` if the stream supports writing.

        See Also
        --------
        * `io.BufferedRWPair.writable`.

        Version
        -------
        * Python 3.13.
        """
        return self.writer.writable()

    def flush(self: Self) -> None:
        """Flush the write buffers of the stream if applicable.

        See Also
        --------
        * `io.BufferedRWPair.flush`.

        Version
        -------
        * Python 3.13.
        """
        return self.writer.flush()

    def close(self: Self) -> None:
        """Flush and close this stream.

        See Also
        --------
        * `io.BufferedRWPair.close`.

        Version
        -------
        * Python 3.13.
        """
        try:
            self.writer.close()
        finally:
            self.reader.close()

    def isatty(self: Self) -> bool:
        """Return `True` if the stream is interactive.

        See Also
        --------
        * `io.BufferedRWPair.isatty`.

        Version
        -------
        * Python 3.13.
        """
        return self.reader.isatty() or self.writer.isatty()

    @property
    def closed(self: Self) -> bool:
        """`True` if the underlying stream is closed.

        See Also
        --------
        * `io.BufferedRWPair.closed`.

        Version
        -------
        * Python 3.13.
        """
        return self.writer.closed


class BufferedRandom(BufferedWriter, BufferedReader):
    """A buffered binary stream.

    See Also
    --------
    * `io.BufferedRandom`.

    Version
    -------
    * Python 3.13.
    """

    def __init__(self: Self, raw: RawIOBase, buffer_size: int = DEFAULT_BUFFER_SIZE) -> None:
        """Initialize the object.

        See Also
        --------
        * `io.BufferedRandom.__init__`.

        Version
        -------
        * Python 3.13.
        """
        if not raw.seekable():
            detail = "File or stream is not seekable."
            raise UnsupportedOperation(detail)

        BufferedReader.__init__(self, raw, buffer_size)
        BufferedWriter.__init__(self, raw, buffer_size)

    def seek(self: Self, pos: int, whence: int = SEEK_SET, /) -> int:
        """Change the stream position to the given byte offset.

        See Also
        --------
        * `io.BufferedWriter.seek`.

        Version
        -------
        * Python 3.13.
        """
        if whence not in SEEK_FLAGS:
            detail = "invalid whence value"
            raise ValueError(detail)

        if self.raw is None:
            detail = "seek() on a detached stream"
            raise AttributeError(detail)

        self.flush()

        if self._read_buf:
            with self._read_lock:
                offset = self._read_pos - len(self._read_buf)
                self.raw.seek(offset, SEEK_CUR)

        pos = self.raw.seek(pos, whence)

        with self._read_lock:
            self._reset_read_buf()

        if pos < 0:
            detail = "seek() returned invalid position"
            raise OSError(detail)

        return pos

    def tell(self: Self) -> int:
        """Return the current stream position.

        See Also
        --------
        * `io.BufferedRandom.tell`.

        Version
        -------
        * Python 3.13.
        """
        base = BufferedWriter if self._write_buf else BufferedReader
        return base.tell(self)

    def truncate(self: Self, pos: int | None = None, /) -> int:
        """Resize the stream to the given size in bytes.

        See Also
        --------
        * `io.BufferedRandom.truncate`.

        Version
        -------
        * Python 3.13.
        """
        if pos is None:
            pos = self.tell()

        return BufferedWriter.truncate(self, pos)

    def read(self: Self, size: int | None = None, /) -> bytes | None:
        """Read and return up to `size` bytes.

        See Also
        --------
        * `io.BufferedRandom.read`.

        Version
        -------
        * Python 3.13.
        """
        if size is None:
            size = -1

        self.flush()
        return BufferedReader.read(self, size)

    def readinto(self: Self, buffer: WriteableBuffer, /) -> int | None:
        """Read bytes into a pre-allocated, writable bytes-like object.

        See Also
        --------
        * `io.BufferedRandom.readinto`.

        Version
        -------
        * Python 3.13.
        """
        self.flush()
        return BufferedReader.readinto(self, buffer)

    def peek(self: Self, size: int = 0, /) -> bytes:
        """Return bytes from the stream without advancing the position.

        See Also
        --------
        * `io.BufferedRandom.peek`.

        Version
        -------
        * Python 3.13.
        """
        self.flush()
        return BufferedReader.peek(self, size)

    def read1(self: Self, size: int | None = None, /) -> bytes | None:
        """Read and return up to `size` bytes, with at most one call.

        See Also
        --------
        * `io.BufferedRandom.read1`.

        Version
        -------
        * Python 3.13.
        """
        self.flush()
        return BufferedReader.read1(self, size)

    def readinto1(self: Self, buffer: WriteableBuffer, /) -> int | None:
        """Read bytes into a pre-allocated, writable bytes-like object, with at most one call.

        See Also
        --------
        * `io.BufferedRandom.readinto1`.

        Version
        -------
        * Python 3.13.
        """
        self.flush()
        return BufferedReader.readinto1(self, buffer)

    def write(self: Self, buffer: ReadableBuffer, /) -> int:
        """Write the given bytes-like object.

        See Also
        --------
        * `io.BufferedRandom.write`.

        Version
        -------
        * Python 3.13.
        """
        if self.raw is None:
            detail = "write() on a detached stream"
            raise AttributeError(detail)

        if self._read_buf:
            with self._read_lock:
                offset = self._read_pos - len(self._read_buf)
                self.raw.seek(offset, SEEK_CUR)
                self._reset_read_buf()

        return BufferedWriter.write(self, buffer)


class FileIO(RawIOBase):
    pass


class TextIOBase(IOBase[str]):
    pass


class TextIOWrapper(TextIOBase):
    pass


class StringIO(TextIOWrapper):
    pass
