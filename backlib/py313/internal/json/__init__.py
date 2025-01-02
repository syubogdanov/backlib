from __future__ import annotations

import codecs

from backlib.py313.internal.json.decoder import JSONDecodeError, JSONDecoder
from backlib.py313.internal.json.encoder import JSONEncoder


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


def dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kwargs):
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


def dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kwargs):
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


def detect_encoding(b: bytes | bytearray):
    bstartswith = b.startswith
    if bstartswith((codecs.BOM_UTF32_BE, codecs.BOM_UTF32_LE)):
        return "utf-32"
    if bstartswith((codecs.BOM_UTF16_BE, codecs.BOM_UTF16_LE)):
        return "utf-16"
    if bstartswith(codecs.BOM_UTF8):
        return "utf-8-sig"

    if len(b) >= 4:
        if not b[0]:
            # 00 00 -- -- - utf-32-be
            # 00 XX -- -- - utf-16-be
            return "utf-16-be" if b[1] else "utf-32-be"
        if not b[1]:
            # XX 00 00 00 - utf-32-le
            # XX 00 00 XX - utf-16-le
            # XX 00 XX -- - utf-16-le
            return "utf-16-le" if b[2] or b[3] else "utf-32-le"
    elif len(b) == 2:
        if not b[0]:
            # 00 XX - utf-16-be
            return "utf-16-be"
        if not b[1]:
            # XX 00 - utf-16-le
            return "utf-16-le"
    # default
    return "utf-8"


def load(fp, *, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kwargs):
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


def loads(s, *, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kwargs):
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

    if (cls is None and object_hook is None and
            parse_int is None and parse_float is None and
            parse_constant is None and object_pairs_hook is None and not kwargs):
        decoder = JSONDecoder(object_hook=None, object_pairs_hook=None)
        return decoder.decode(s)
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
