from backlib.py313.internal.stdlib.os import (
    SEEK_CUR,
    SEEK_END,
    SEEK_SET,
    PathLike,
    altsep,
    curdir,
    defpath,
    devnull,
    error,
    extsep,
    fspath,
    linesep,
    name,
    pardir,
    pathsep,
    sep,
)


__all__: list[str] = [
    "SEEK_CUR",
    "SEEK_END",
    "SEEK_SET",
    "PathLike",
    "altsep",
    "curdir",
    "defpath",
    "devnull",
    "error",
    "extsep",
    "fspath",
    "linesep",
    "name",
    "pardir",
    "pathsep",
    "sep",
]


SEEK_CUR.__module__ = __name__
SEEK_END.__module__ = __name__
SEEK_SET.__module__ = __name__

# NOTE: `error` is just an alias to `OSError`
# error.__module__ = __name__  # noqa: ERA001

curdir.__module__ = __name__
pardir.__module__ = __name__
extsep.__module__ = __name__

name.__module__ = __name__
linesep.__module__ = __name__

sep.__module__ = __name__
pathsep.__module__ = __name__
defpath.__module__ = __name__
altsep.__module__ = __name__
devnull.__module__ = __name__

PathLike.__module__ = __name__

fspath.__module__ = __name__


_detail = "The 'backlib.py313.os' is being developed"
raise NotImplementedError(_detail)
