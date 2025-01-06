import re

from collections.abc import Callable
from typing import Any


__all__ = ["make_scanner"]


NUMBER_RE = re.compile(
    r"(-?(?:0|[1-9][0-9]*))(\.[0-9]+)?([eE][-+]?[0-9]+)?",
    (re.VERBOSE | re.MULTILINE | re.DOTALL),
)


def make_scanner(context) -> Callable[[str, int], tuple[Any, int]]:  # noqa: C901
    parse_object = context.parse_object
    parse_array = context.parse_array
    parse_string = context.parse_string
    match_number = NUMBER_RE.match
    strict = context.strict
    parse_float = context.parse_float
    parse_int = context.parse_int
    parse_constant = context.parse_constant
    object_hook = context.object_hook
    object_pairs_hook = context.object_pairs_hook
    memo = context.memo

    def _scan_once(string: str, idx: int) -> tuple[Any, int]:  # noqa: C901, PLR0911, PLR0912
        try:
            nextchar = string[idx]
        except IndexError:
            raise StopIteration(idx) from None

        if nextchar == '"':
            return parse_string(string, idx + 1, strict)
        if nextchar == "{":
            return parse_object((string, idx + 1), strict,
                _scan_once, object_hook, object_pairs_hook, memo)
        if nextchar == "[":
            return parse_array((string, idx + 1), _scan_once)
        if nextchar == "n" and string[idx:idx + 4] == "null":
            return None, idx + 4
        if nextchar == "t" and string[idx:idx + 4] == "true":
            return True, idx + 4
        if nextchar == "f" and string[idx:idx + 5] == "false":
            return False, idx + 5

        m = match_number(string, idx)
        if m is not None:
            integer, frac, exp = m.groups()
            if frac or exp:
                res = parse_float(integer + (frac or "") + (exp or ""))
            else:
                res = parse_int(integer)
            return res, m.end()
        if nextchar == "N" and string[idx:idx + 3] == "NaN":
            return parse_constant("NaN"), idx + 3
        if nextchar == "I" and string[idx:idx + 8] == "Infinity":
            return parse_constant("Infinity"), idx + 8
        if nextchar == "-" and string[idx:idx + 9] == "-Infinity":
            return parse_constant("-Infinity"), idx + 9
        raise StopIteration(idx)

    def scan_once(string: str, idx: int) -> tuple[Any, int]:
        try:
            return _scan_once(string, idx)
        finally:
            memo.clear()

    return scan_once
