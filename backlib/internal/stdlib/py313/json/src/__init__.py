from __future__ import annotations

import codecs

from typing import TYPE_CHECKING, Any

from backlib.internal.stdlib.py313.json.src.decoder import JSONDecodeError, JSONDecoder
from backlib.internal.stdlib.py313.json.src.encoder import JSONEncoder
from backlib.internal.utils.typing import SupportsRead, SupportsWrite


if TYPE_CHECKING:
    from collections.abc import Callable


__author__ = "Bob Ippolito <bob@redivi.com>"
__version__ = "2.0.9"


__all__: list[str] = [
    "JSONDecodeError",
    "JSONDecoder",
    "JSONEncoder",
    "dump",
    "dumps",
    "load",
    "loads",
]


def dump(  # noqa: PLR0913
    obj: Any,  # noqa: ANN401
    fp: SupportsWrite[str],
    *,
    skipkeys: bool = False,
    ensure_ascii: bool = True,
    check_circular: bool = True,
    allow_nan: bool = True,
    cls: type[JSONEncoder] | None = None,
    indent: int | str | None = None,
    separators: tuple[str, str] | None = None,
    default: Callable[[Any], Any] | None = None,
    sort_keys: bool = False,
    **kwargs: Any,  # noqa: ANN401
) -> None:
    """Serialize `obj` as a JSON formatted stream to `fp`.

    See Also
    --------
    * `json.dump`.

    Version
    -------
    * Python 3.13.
    """
    if cls is None:
        cls = JSONEncoder

    encoder = cls(
        skipkeys=skipkeys,
        ensure_ascii=ensure_ascii,
        check_circular=check_circular,
        allow_nan=allow_nan,
        indent=indent,
        separators=separators,
        default=default,
        sort_keys=sort_keys,
        **kwargs,
    )

    for chunk in encoder.iterencode(obj):
        fp.write(chunk)


def dumps(  # noqa: PLR0913
    obj: Any,  # noqa: ANN401
    *,
    skipkeys: bool = False,
    ensure_ascii: bool = True,
    check_circular: bool = True,
    allow_nan: bool = True,
    cls: type[JSONEncoder] | None = None,
    indent: int | str | None = None,
    separators: tuple[str, str] | None = None,
    default: Callable[[Any], Any] | None = None,
    sort_keys: bool = False,
    **kwargs: Any,  # noqa: ANN401
) -> str:
    """Serialize `obj` to a JSON formatted `str`.

    See Also
    --------
    * `json.dumps`.

    Version
    -------
    * Python 3.13.
    """
    if cls is None:
        cls = JSONEncoder

    encoder = cls(
        skipkeys=skipkeys,
        ensure_ascii=ensure_ascii,
        check_circular=check_circular,
        allow_nan=allow_nan,
        indent=indent,
        separators=separators,
        default=default,
        sort_keys=sort_keys,
        **kwargs,
    )

    return encoder.encode(obj)


def detect_encoding(b: bytes | bytearray) -> str:  # noqa: PLR0911
    if b.startswith((codecs.BOM_UTF32_BE, codecs.BOM_UTF32_LE)):
        return "utf-32"

    if b.startswith((codecs.BOM_UTF16_BE, codecs.BOM_UTF16_LE)):
        return "utf-16"

    if b.startswith(codecs.BOM_UTF8):
        return "utf-8-sig"

    if len(b) >= 4:  # noqa: PLR2004
        if not b[0]:
            # 00 00 -- -- - utf-32-be
            # 00 XX -- -- - utf-16-be
            return "utf-16-be" if b[1] else "utf-32-be"
        if not b[1]:
            # XX 00 00 00 - utf-32-le
            # XX 00 00 XX - utf-16-le
            # XX 00 XX -- - utf-16-le
            return "utf-16-le" if b[2] or b[3] else "utf-32-le"
    elif len(b) == 2:  # noqa: PLR2004
        if not b[0]:
            # 00 XX - utf-16-be
            return "utf-16-be"
        if not b[1]:
            # XX 00 - utf-16-le
            return "utf-16-le"
    # default
    return "utf-8"


def load(
    fp: SupportsRead[str | bytes | bytearray],
    *,
    cls: type[JSONDecoder] | None = None,
    object_hook: Callable[[dict[Any, Any]], Any] | None = None,
    parse_float: Callable[[str], Any] | None = None,
    parse_int: Callable[[str], Any] | None = None,
    parse_constant: Callable[[str], Any] | None = None,
    object_pairs_hook: Callable[[list[tuple[Any, Any]]], Any] | None = None,
    **kwargs: Any,  # noqa: ANN401
) -> Any:  # noqa: ANN401
    """Deserialize `fp` to a Python object.

    See Also
    --------
    * `json.load`.

    Version
    -------
    * Python 3.13.
    """
    return loads(
        s=fp.read(),
        cls=cls,
        object_hook=object_hook,
        parse_float=parse_float,
        parse_int=parse_int,
        parse_constant=parse_constant,
        object_pairs_hook=object_pairs_hook,
        **kwargs,
    )


def loads(
    s: str | bytes | bytearray,
    *,
    cls: type[JSONDecoder] | None = None,
    object_hook: Callable[[dict[Any, Any]], Any] | None = None,
    parse_float: Callable[[str], Any] | None = None,
    parse_int: Callable[[str], Any] | None = None,
    parse_constant: Callable[[str], Any] | None = None,
    object_pairs_hook: Callable[[list[tuple[Any, Any]]], Any] | None = None,
    **kwargs: Any,  # noqa: ANN401
) -> Any:  # noqa: ANN401
    """Deserialize `s` to a Python object.

    See Also
    --------
    * `json.loads`.

    Version
    -------
    * Python 3.13.
    """
    if isinstance(s, str):
        if s.startswith("\ufeff"):
            detail = "Unexpected UTF-8 BOM (decode using utf-8-sig)"
            raise JSONDecodeError(detail, s, 0)
    else:
        if not isinstance(s, (bytes, bytearray)):
            detail = f"the JSON object must be str, bytes or bytearray, not {s.__class__.__name__}"
            raise TypeError(detail)

        s = s.decode(detect_encoding(s), "surrogatepass")

    if cls is None:
        cls = JSONDecoder

    if object_hook is not None:
        kwargs["object_hook"] = object_hook

    if object_pairs_hook is not None:
        kwargs["object_pairs_hook"] = object_pairs_hook

    if parse_float is not None:
        kwargs["parse_float"] = parse_float

    if parse_int is not None:
        kwargs["parse_int"] = parse_int

    if parse_constant is not None:
        kwargs["parse_constant"] = parse_constant

    return cls(**kwargs).decode(s)
