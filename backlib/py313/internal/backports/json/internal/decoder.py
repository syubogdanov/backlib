from __future__ import annotations

import re
import sys

from contextlib import suppress
from typing import TYPE_CHECKING, Any

from backlib.py313.internal.backports.json.internal import scanner
from backlib.py313.internal.backports.json.internal.errors import JSONDecodeError


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


if TYPE_CHECKING:
    from collections.abc import Callable


FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL

NaN = float("nan")
PosInf = float("inf")
NegInf = float("-inf")


_CONSTANTS = {
    "-Infinity": NegInf,
    "Infinity": PosInf,
    "NaN": NaN,
}


HEXDIGITS = re.compile(r"[0-9A-Fa-f]{4}", FLAGS)
STRINGCHUNK = re.compile(r'(.*?)(["\\\x00-\x1f])', FLAGS)

BACKSLASH = {
    '"': '"',
    "\\": "\\",
    "/": "/",
    "b": "\b",
    "f": "\f",
    "n": "\n",
    "r": "\r",
    "t": "\t",
}


def _decode_uXXXX(s: str, pos: int) -> int:  # noqa: N802
    if esc := HEXDIGITS.match(s, pos + 1):
        with suppress(ValueError):
            return int(esc.group(), 16)

    detail = "Invalid \\uXXXX escape"
    raise JSONDecodeError(detail, s, pos)


def scanstring(  # noqa: C901
    s: str,
    end: int,
    strict: bool = True,  # noqa: FBT001, FBT002
) -> tuple[str, int]:
    """Scan the string s for a JSON string. End is the index of the
    character in s after the quote that started the JSON string.
    Unescapes all valid JSON string escape sequences and raises ValueError
    on attempt to decode an invalid string. If strict is False then literal
    control characters are allowed in the string.

    Returns a tuple of the decoded string and the index of the character in s
    after the end quote.
    """  # noqa: D205
    chunks = []
    begin = end - 1
    while 1:
        chunk = STRINGCHUNK.match(s, end)
        if chunk is None:
            detail = "Unterminated string starting at"
            raise JSONDecodeError(detail, s, begin)
        end = chunk.end()
        content, terminator = chunk.groups()
        # Content is contains zero or more unescaped string characters
        if content:
            chunks.append(content)
        # Terminator is the end of string, a literal control character,
        # or a backslash denoting that an escape sequence follows
        if terminator == '"':
            break
        if terminator != "\\":
            if strict:
                msg = f"Invalid control character {terminator!r} at"
                raise JSONDecodeError(msg, s, end)
            chunks.append(terminator)
            continue
        try:
            esc = s[end]
        except IndexError:
            detail = "Unterminated string starting at"
            raise JSONDecodeError(detail, s, begin) from None
        # If not a unicode escape sequence, must be in the lookup table
        if esc != "u":
            try:
                char = BACKSLASH[esc]
            except KeyError:
                detail = f"Invalid \\escape: {esc!r}"
                raise JSONDecodeError(detail, s, end) from None
            end += 1
        else:
            uni = _decode_uXXXX(s, end)
            end += 5
            if 0xD800 <= uni <= 0xDBFF and s[end : end + 2] == "\\u":  # noqa: PLR2004
                uni2 = _decode_uXXXX(s, end + 1)
                if 0xDC00 <= uni2 <= 0xDFFF:  # noqa: PLR2004
                    uni = 0x10000 + (((uni - 0xD800) << 10) | (uni2 - 0xDC00))
                    end += 6
            char = chr(uni)
        chunks.append(char)
    return ("".join(chunks), end)


WHITESPACE = re.compile(r"[ \t\n\r]*", FLAGS)
WHITESPACE_STR = " \t\n\r"


def JSONObject(  # noqa: C901, D103, N802, PLR0912, PLR0915
    s_and_end: tuple[str, int],
    strict: bool,  # noqa: FBT001
    scan_once: Callable[[str, int], tuple[Any, int]],
    object_hook: Callable[[dict[str, Any]], Any] | None,
    object_pairs_hook: Callable[[list[tuple[str, Any]]], Any] | None,
    memo: dict[str, str] | None = None,
) -> Any:
    s, end = s_and_end
    pairs: list[tuple[str, Any]] = []
    pairs_append = pairs.append
    # Backwards compatibility
    if memo is None:
        memo = {}
    memo_get = memo.setdefault
    # Use a slice to prevent IndexError from being raised, the following
    # check will raise a more specific ValueError if the string is empty
    nextchar = s[end : end + 1]
    # Normally we expect nextchar == '"'
    if nextchar != '"':
        if nextchar in WHITESPACE_STR:
            end = WHITESPACE.match(s, end).end()  # type: ignore[union-attr]
            nextchar = s[end : end + 1]
        # Trivial empty object
        if nextchar == "}":
            if object_pairs_hook is not None:
                result = object_pairs_hook(pairs)
                return result, end + 1

            if object_hook is not None:
                return (object_hook({}), end + 1)

            return ({}, end + 1)

        if nextchar != '"':
            detail = "Expecting property name enclosed in double quotes"
            raise JSONDecodeError(detail, s, end)
    end += 1
    while True:
        key, end = scanstring(s, end, strict)
        key = memo_get(key, key)
        # To skip some function call overhead we optimize the fast paths where
        # the JSON key separator is ": " or just ":".
        if s[end : end + 1] != ":":
            end = WHITESPACE.match(s, end).end()  # type: ignore[union-attr]
            if s[end : end + 1] != ":":
                detail = "Expecting ':' delimiter"
                raise JSONDecodeError(detail, s, end)
        end += 1

        try:
            if s[end] in WHITESPACE_STR:
                end += 1
                if s[end] in WHITESPACE_STR:
                    end = WHITESPACE.match(s, end + 1).end()  # type: ignore[union-attr]
        except IndexError:
            pass

        try:
            value, end = scan_once(s, end)

        except StopIteration as err:
            detail = "Expecting value"
            raise JSONDecodeError(detail, s, err.value) from None

        pairs_append((key, value))

        try:
            nextchar = s[end]
            if nextchar in WHITESPACE_STR:
                end = WHITESPACE.match(s, end + 1).end()  # type: ignore[union-attr]
                nextchar = s[end]

        except IndexError:
            nextchar = ""

        end += 1

        if nextchar == "}":
            break

        if nextchar != ",":
            detail = "Expecting ',' delimiter"
            raise JSONDecodeError(detail, s, end - 1)

        comma_idx = end - 1
        end = WHITESPACE.match(s, end).end()  # type: ignore[union-attr]
        nextchar = s[end : end + 1]
        end += 1
        if nextchar != '"':
            if nextchar == "}":
                detail = "Illegal trailing comma before end of object"
                raise JSONDecodeError(detail, s, comma_idx)

            detail = "Expecting property name enclosed in double quotes"
            raise JSONDecodeError(detail, s, end - 1)

    if object_pairs_hook is not None:
        result = object_pairs_hook(pairs)
        return result, end

    as_dict = dict(pairs)

    if object_hook is not None:
        return (object_hook(as_dict), end)

    return (as_dict, end)


def JSONArray(  # noqa: C901, D103, N802
    s_and_end: tuple[str, int],
    scan_once: Callable[[str, int], tuple[Any, int]],
) -> tuple[list[Any], int]:
    s, end = s_and_end
    values: list[Any] = []
    nextchar = s[end : end + 1]

    if nextchar in WHITESPACE_STR:
        end = WHITESPACE.match(s, end + 1).end()  # type: ignore[union-attr]
        nextchar = s[end : end + 1]

    # Look-ahead for trivial empty array
    if nextchar == "]":
        return values, end + 1

    while True:
        try:
            value, end = scan_once(s, end)

        except StopIteration as err:
            detail = "Expecting value"
            raise JSONDecodeError(detail, s, err.value) from None

        values.append(value)
        nextchar = s[end : end + 1]
        if nextchar in WHITESPACE_STR:
            end = WHITESPACE.match(s, end + 1).end()  # type: ignore[union-attr]
            nextchar = s[end : end + 1]
        end += 1

        if nextchar == "]":
            break

        if nextchar != ",":
            detail = "Expecting ',' delimiter"
            raise JSONDecodeError(detail, s, end - 1)

        comma_idx = end - 1
        try:
            if s[end] in WHITESPACE_STR:
                end += 1
                if s[end] in WHITESPACE_STR:
                    end = WHITESPACE.match(s, end + 1).end()  # type: ignore[union-attr]
            nextchar = s[end : end + 1]
        except IndexError:
            pass

        if nextchar == "]":
            detail = "Illegal trailing comma before end of array"
            raise JSONDecodeError(detail, s, comma_idx)

    return values, end


class JSONDecoder:
    """Simple JSON decoder.

    See Also
    --------
    * `json.JSONDecoder`.

    Version
    -------
    * Python 3.13.
    """

    def __init__(
        self: Self,
        *,
        object_hook: Callable[[dict[str, Any]], Any] | None = None,
        parse_float: Callable[[str], Any] | None = None,
        parse_int: Callable[[str], Any] | None = None,
        parse_constant: Callable[[str], Any] | None = None,
        strict: bool = True,
        object_pairs_hook: Callable[[list[tuple[str, Any]]], Any] | None = None,
    ) -> None:
        """Initialize the object.

        See Also
        --------
        * `json.JSONDecoder.__init__`.

        Version
        -------
        * Python 3.13.
        """
        self.object_hook = object_hook
        self.parse_float = parse_float or float
        self.parse_int = parse_int or int
        self.parse_constant = parse_constant or _CONSTANTS.__getitem__
        self.strict = strict
        self.object_pairs_hook = object_pairs_hook
        self.parse_object = JSONObject
        self.parse_array = JSONArray
        self.parse_string = scanstring
        self.memo: dict[str, str] = {}
        self.scan_once = scanner.make_scanner(self)

    def decode(self: Self, s: str) -> Any:
        """Return the Python representation of `s`.

        See Also
        --------
        * `json.JSONDecoder.decode`.

        Version
        -------
        * Python 3.13.
        """
        obj, end = self.raw_decode(s, idx=WHITESPACE.match(s, 0).end())  # type: ignore[union-attr]
        end = WHITESPACE.match(s, end).end()  # type: ignore[union-attr]

        if end != len(s):
            detail = "Extra data"
            raise JSONDecodeError(detail, s, end)

        return obj

    def raw_decode(self: Self, s: str, idx: int = 0) -> tuple[Any, int]:
        """Decode a JSON document from `s`.

        See Also
        --------
        * `json.JSONDecoder.raw_decode`.

        Version
        -------
        * Python 3.13.
        """
        try:
            obj, end = self.scan_once(s, idx)

        except StopIteration as err:
            detail = "Expecting value"
            raise JSONDecodeError(detail, s, err.value) from None

        return obj, end
