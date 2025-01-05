from backlib.py313.internal.stdlib.os import SEEK_CUR, SEEK_END, SEEK_SET, PathLike, error, fspath


__all__: list[str] = ["SEEK_CUR", "SEEK_END", "SEEK_SET", "PathLike", "error", "fspath"]


SEEK_CUR.__module__ = __name__
SEEK_END.__module__ = __name__
SEEK_SET.__module__ = __name__

# NOTE: `error` is just an alias to `OSError`
# error.__module__ = __name__  # noqa: ERA001

PathLike.__module__ = __name__

fspath.__module__ = __name__


_detail = "The 'backlib.py313.os' is being developed"
raise NotImplementedError(_detail)
