import sys

from backlib.internal.backports.py311.os_path import (
    abspath,
    basename,
    commonpath,
    commonprefix,
    dirname,
    exists,
    expanduser,
    expandvars,
    getatime,
    getctime,
    getmtime,
    getsize,
    isabs,
    isdir,
    isfile,
    islink,
    ismount,
    join,
    lexists,
    normcase,
    normpath,
    realpath,
    relpath,
    samefile,
    sameopenfile,
    split,
    splitdrive,
    splitext,
    supports_unicode_filenames,
)
from backlib.internal.backports.py312.os_path.internal.os_path import isdevdrive, samestat


if sys.version_info >= (3, 12):
    from os.path import isjunction, splitroot
else:
    from backlib.internal.backports.py312.os_path.internal.os_path import isjunction, splitroot


__all__: list[str] = [
    "abspath",
    "basename",
    "commonpath",
    "commonprefix",
    "dirname",
    "exists",
    "expanduser",
    "expandvars",
    "getatime",
    "getctime",
    "getmtime",
    "getsize",
    "isabs",
    "isdevdrive",
    "isdir",
    "isfile",
    "isjunction",
    "islink",
    "ismount",
    "join",
    "lexists",
    "normcase",
    "normpath",
    "realpath",
    "relpath",
    "samefile",
    "sameopenfile",
    "samestat",
    "split",
    "splitdrive",
    "splitext",
    "splitroot",
    "supports_unicode_filenames",
]
