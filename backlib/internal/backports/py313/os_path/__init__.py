import sys

from backlib.internal.backports.py312.os_path import (
    abspath,
    basename,
    commonprefix,
    dirname,
    exists,
    expanduser,
    expandvars,
    getatime,
    getctime,
    getmtime,
    getsize,
    isdevdrive,
    isdir,
    isfile,
    isjunction,
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
    samestat,
    split,
    splitdrive,
    splitext,
    splitroot,
    supports_unicode_filenames,
)
from backlib.internal.utils.platform import is_nt


if sys.version_info >= (3, 13):
    from os.path import commonpath, isabs
else:
    from backlib.internal.backports.py313.os_path.internal.os_path import commonpath, isabs


if sys.version_info >= (3, 13) and is_nt():
    from os.path import isreserved
else:
    from backlib.internal.backports.py313.os_path.internal.os_path import isreserved


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
    "isreserved",
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
