from __future__ import annotations

import re
import sys

from math import isnan
from typing import TYPE_CHECKING, Any


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


if TYPE_CHECKING:
    from collections.abc import Callable, Iterator


# mypy: disable-error-code="no-untyped-def"


ESCAPE = re.compile(r'[\x00-\x1f\\"\b\f\n\r\t]')
ESCAPE_ASCII = re.compile(r'([\\"]|[^\ -~])')
HAS_UTF8 = re.compile(b"[\x80-\xff]")
ESCAPE_DCT = {
    "\\": "\\\\",
    '"': '\\"',
    "\b": "\\b",
    "\f": "\\f",
    "\n": "\\n",
    "\r": "\\r",
    "\t": "\\t",
}
for i in range(0x20):
    ESCAPE_DCT.setdefault(chr(i), f"\\u{i:04x}")
del i

INFINITY = float("inf")


def encode_basestring(s: str) -> str:
    """Return a JSON representation of a Python string."""

    def replace(match: re.Match[str]) -> str:
        return ESCAPE_DCT[match.group(0)]

    return '"' + ESCAPE.sub(replace, s) + '"'


def encode_basestring_ascii(s: str) -> str:
    """Return an ASCII-only JSON representation of a Python string."""

    def replace(match: re.Match[str]) -> str:
        s = match.group(0)
        try:
            return ESCAPE_DCT[s]
        except KeyError:
            n = ord(s)
            if n < 0x10000:  # noqa: PLR2004
                return f"\\u{n:04x}"
            # surrogate pair
            n -= 0x10000
            s1 = 0xD800 | ((n >> 10) & 0x3FF)
            s2 = 0xDC00 | (n & 0x3FF)
            return f"\\u{s1:04x}\\u{s2:04x}"

    return '"' + ESCAPE_ASCII.sub(replace, s) + '"'


class JSONEncoder:
    """Simple JSON encoder.

    See Also
    --------
    * `json.JSONEncoder`.

    Version
    -------
    * Python 3.13.
    """

    item_separator: str = ", "
    key_separator: str = ": "

    def __init__(
        self: Self,
        *,
        skipkeys: bool = False,
        ensure_ascii: bool = True,
        check_circular: bool = True,
        allow_nan: bool = True,
        sort_keys: bool = False,
        indent: int | str | None = None,
        separators: tuple[str, str] | None = None,
        default: Callable[..., Any] | None = None,
    ) -> None:
        """Initialize the object.

        See Also
        --------
        * `json.JSONEncoder.__init__`.

        Version
        -------
        * Python 3.13.
        """
        self.skipkeys = skipkeys
        self.ensure_ascii = ensure_ascii
        self.check_circular = check_circular
        self.allow_nan = allow_nan
        self.sort_keys = sort_keys
        self.indent = indent
        if separators is not None:
            self.item_separator, self.key_separator = separators
        elif indent is not None:
            self.item_separator = ","
        if default is not None:
            self.default = default  # type: ignore[method-assign]

    def default(self: Self, o: Any) -> Any:
        """Add support for an arbitrary type.

        See Also
        --------
        * `json.JSONEncoder.default`.

        Version
        -------
        * Python 3.13.
        """
        detail = f"Object of type {o.__class__.__name__} is not JSON serializable"
        raise TypeError(detail)

    def encode(self: Self, o: Any) -> str:
        """Return a JSON string representation of a Python data structure.

        See Also
        --------
        * `json.JSONEncoder.encode`.

        Version
        -------
        * Python 3.13.
        """
        # This is for extremely simple cases and benchmarks.
        if isinstance(o, str):
            encoder = encode_basestring_ascii if self.ensure_ascii else encode_basestring
            return encoder(o)
        # This doesn't pass the iterator directly to ''.join() because the
        # exceptions aren't as detailed.  The list call should be roughly
        # equivalent to the PySequence_Fast that ''.join() would do.
        chunks = self.iterencode(o)
        if not isinstance(chunks, (list, tuple)):
            chunks = list(chunks)  # type: ignore[assignment]
        return "".join(chunks)

    def iterencode(self: Self, o: Any) -> Iterator[str]:
        """Encode the given object and yield each string representation as available.

        See Also
        --------
        * `json.JSONEncoder.iterencode`.

        Version
        -------
        * Python 3.13.
        """
        markers: dict[int, Any] | None = {} if self.check_circular else None
        _encoder = encode_basestring_ascii if self.ensure_ascii else encode_basestring

        def floatstr(o: float, *, allow_nan: bool = self.allow_nan) -> str:
            # Check for specials.  Note that this type of test is processor
            # and/or platform-specific, so do tests which don't depend on the
            # internals.

            if isnan(o):
                text = "NaN"
            elif o == INFINITY:
                text = "Infinity"
            elif o == -INFINITY:
                text = "-Infinity"
            else:
                encoder = float.__repr__
                return encoder(o)

            if not allow_nan:
                detail = f"Out of range float values are not JSON compliant: {o!r}"
                raise ValueError(detail)

            return text

        if self.indent is None or isinstance(self.indent, str):
            indent = self.indent
        else:
            indent = " " * self.indent

        _iterencode = _make_iterencode(
            markers=markers,
            _default=self.default,
            _encoder=_encoder,
            _indent=indent,
            _floatstr=floatstr,
            _key_separator=self.key_separator,
            _item_separator=self.item_separator,
            _sort_keys=self.sort_keys,
            _skipkeys=self.skipkeys,
        )

        return _iterencode(o, 0)


def _make_iterencode(  # noqa: C901, PLR0915
    markers: dict[int, Any] | None,
    _default: Callable[[Any], Any],
    _encoder: Callable[[str], str],
    _indent: str | None,
    _floatstr: Callable[[float], str],
    _key_separator: str,
    _item_separator: str,
    *,
    _sort_keys: bool,
    _skipkeys: bool,
) -> Callable[[Any, int], Iterator[str]]:

    def _iterencode_list(  # noqa: C901, PLR0912
        lst: list[Any] | tuple[Any],
        _current_indent_level: int,
    ) -> Iterator[str]:
        if not lst:
            yield "[]"
            return
        if markers is not None:
            markerid = id(lst)
            if markerid in markers:
                detail = "Circular reference detected"
                raise ValueError(detail)
            markers[markerid] = lst
        buf = "["
        if _indent is not None:
            _current_indent_level += 1
            newline_indent = "\n" + _indent * _current_indent_level
            separator = _item_separator + newline_indent
            buf += newline_indent
        else:
            newline_indent = None
            separator = _item_separator
        first = True
        for value in lst:
            if first:
                first = False
            else:
                buf = separator
            if isinstance(value, str):
                yield buf + _encoder(value)
            elif value is None:
                yield buf + "null"
            elif value is True:
                yield buf + "true"
            elif value is False:
                yield buf + "false"
            elif isinstance(value, int):
                # Subclasses of int/float may override __repr__, but we still
                # want to encode them as integers/floats in JSON. One example
                # within the standard library is IntEnum.
                represent = int.__repr__
                yield buf + represent(value)
            elif isinstance(value, float):
                # see comment above for int
                yield buf + _floatstr(value)
            else:
                yield buf
                if isinstance(value, (list, tuple)):
                    chunks = _iterencode_list(value, _current_indent_level)
                elif isinstance(value, dict):
                    chunks = _iterencode_dict(value, _current_indent_level)
                else:
                    chunks = _iterencode(value, _current_indent_level)
                yield from chunks
        if newline_indent is not None:
            _current_indent_level -= 1
            yield "\n" + _indent * _current_indent_level  # type: ignore[operator]
        yield "]"
        if markers is not None:
            del markers[markerid]

    def _iterencode_dict(  # noqa: C901, PLR0912, PLR0915
        dct: dict[Any, Any],
        _current_indent_level: int,
    ) -> Iterator[str]:
        if not dct:
            yield "{}"
            return
        if markers is not None:
            markerid = id(dct)
            if markerid in markers:
                detail = "Circular reference detected"
                raise ValueError(detail)
            markers[markerid] = dct
        yield "{"
        if _indent is not None:
            _current_indent_level += 1
            newline_indent = "\n" + _indent * _current_indent_level
            item_separator = _item_separator + newline_indent
            yield newline_indent
        else:
            newline_indent = None
            item_separator = _item_separator
        first = True
        items = sorted(dct.items()) if _sort_keys else dct.items()
        for key, value in items:
            if isinstance(key, str):
                pass
            # JavaScript is weakly typed for these, so it makes sense to
            # also allow them.  Many encoders seem to do something like this.
            elif isinstance(key, float):
                # see comment for int/float in _make_iterencode
                key = _floatstr(key)  # noqa: PLW2901
            elif key is True:
                key = "true"  # noqa: PLW2901
            elif key is False:
                key = "false"  # noqa: PLW2901
            elif key is None:
                key = "null"  # noqa: PLW2901
            elif isinstance(key, int):
                # see comment for int/float in _make_iterencode
                represent = int.__repr__
                key = represent(key)  # noqa: PLW2901
            elif _skipkeys:
                continue
            else:
                detail = f"keys must be str, int, float, bool or None, not {key.__class__.__name__}"
                raise TypeError(detail)
            if first:
                first = False
            else:
                yield item_separator
            yield _encoder(key)
            yield _key_separator
            if isinstance(value, str):
                yield _encoder(value)
            elif value is None:
                yield "null"
            elif value is True:
                yield "true"
            elif value is False:
                yield "false"
            elif isinstance(value, int):
                # see comment for int/float in _make_iterencode
                represent = int.__repr__
                yield represent(value)
            elif isinstance(value, float):
                # see comment for int/float in _make_iterencode
                yield _floatstr(value)
            else:
                if isinstance(value, (list, tuple)):
                    chunks = _iterencode_list(value, _current_indent_level)
                elif isinstance(value, dict):
                    chunks = _iterencode_dict(value, _current_indent_level)
                else:
                    chunks = _iterencode(value, _current_indent_level)
                yield from chunks
        if newline_indent is not None:
            _current_indent_level -= 1
            yield "\n" + _indent * _current_indent_level  # type: ignore[operator]
        yield "}"
        if markers is not None:
            del markers[markerid]

    def _iterencode(o: Any, _current_indent_level: int) -> Iterator[str]:  # noqa: C901
        if isinstance(o, str):
            yield _encoder(o)
        elif o is None:
            yield "null"
        elif o is True:
            yield "true"
        elif o is False:
            yield "false"
        elif isinstance(o, int):
            # see comment for int/float in _make_iterencode
            represent = int.__repr__
            yield represent(o)
        elif isinstance(o, float):
            # see comment for int/float in _make_iterencode
            yield _floatstr(o)
        elif isinstance(o, (list, tuple)):
            yield from _iterencode_list(o, _current_indent_level)
        elif isinstance(o, dict):
            yield from _iterencode_dict(o, _current_indent_level)
        else:
            if markers is not None:
                markerid = id(o)
                if markerid in markers:
                    detail = "Circular reference detected"
                    raise ValueError(detail)
                markers[markerid] = o
            o = _default(o)
            yield from _iterencode(o, _current_indent_level)
            if markers is not None:
                del markers[markerid]

    return _iterencode
