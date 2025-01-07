from __future__ import annotations

from backlib.internal.typing import AnyStr


def splitext(
    path: AnyStr,
    sep: AnyStr,
    altsep: AnyStr | None,
    extsep: AnyStr,
) -> tuple[AnyStr, AnyStr]:
    """Split the pathname `path` into a pair `(root, ext)`.

    Notes
    -----
    * `sep`, `altsep` and `extsep` must be characters.
    """
    sep_index = path.rfind(sep)
    if altsep is not None:
        altsep_index = path.rfind(altsep)
        sep_index = max(sep_index, altsep_index)

    extsep_index = path.rfind(extsep)
    if extsep_index <= sep_index:
        return (path, path[:0])

    starts_with_extseps = all(
        path[index] == extsep
        for index in range(sep_index + 1, extsep_index + 1)
    )

    if starts_with_extseps:
        return (path, path[:0])

    return (path[:extsep_index], path[extsep_index:])
