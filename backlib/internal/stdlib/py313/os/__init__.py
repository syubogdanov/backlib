from backlib.internal.stdlib.py313.os.src.abc import PathLike
from backlib.internal.stdlib.py313.os.src.env import environ, environb, supports_bytes_environ
from backlib.internal.stdlib.py313.os.src.impl import (
    F_OK,
    O_APPEND,
    O_CREAT,
    O_EXCL,
    O_RDONLY,
    O_RDWR,
    O_TRUNC,
    O_WRONLY,
    R_OK,
    SEEK_CUR,
    SEEK_END,
    SEEK_SET,
    W_OK,
    X_OK,
    access,
    altsep,
    chdir,
    close,
    closerange,
    curdir,
    defpath,
    devnull,
    error,
    extsep,
    fsdecode,
    fsencode,
    fspath,
    fstat,
    ftruncate,
    get_inheritable,
    get_terminal_size,
    getcwd,
    getcwdb,
    isatty,
    linesep,
    link,
    lseek,
    lstat,
    mkdir,
    name,
    open,  # noqa: A004
    pardir,
    pathsep,
    read,
    readlink,
    rename,
    replace,
    rmdir,
    sep,
    set_inheritable,
    stat,
    strerror,
    symlink,
    unlink,
    write,
)
from backlib.internal.stdlib.py313.os.src.structs import stat_result, terminal_size


__all__: list[str] = [
    "F_OK",
    "O_APPEND",
    "O_CREAT",
    "O_EXCL",
    "O_RDONLY",
    "O_RDWR",
    "O_TRUNC",
    "O_WRONLY",
    "R_OK",
    "SEEK_CUR",
    "SEEK_END",
    "SEEK_SET",
    "W_OK",
    "X_OK",
    "PathLike",
    "access",
    "altsep",
    "chdir",
    "close",
    "closerange",
    "curdir",
    "defpath",
    "devnull",
    "environ",
    "environb",
    "error",
    "extsep",
    "fsdecode",
    "fsencode",
    "fspath",
    "fstat",
    "ftruncate",
    "get_inheritable",
    "get_terminal_size",
    "getcwd",
    "getcwdb",
    "isatty",
    "linesep",
    "link",
    "lseek",
    "lstat",
    "mkdir",
    "name",
    "open",
    "pardir",
    "pathsep",
    "read",
    "readlink",
    "rename",
    "replace",
    "rmdir",
    "sep",
    "set_inheritable",
    "stat",
    "stat_result",
    "strerror",
    "supports_bytes_environ",
    "symlink",
    "terminal_size",
    "unlink",
    "write",
]

__backlib__: str = "backlib.py313.os"


PathLike.__module__ = __backlib__

stat_result.__module__ = __backlib__
terminal_size.__module__ = __backlib__

# [!] environ.__module__ = __backlib__
# [!] environb.__module__ = __backlib__

access.__module__ = __backlib__
chdir.__module__ = __backlib__
close.__module__ = __backlib__
closerange.__module__ = __backlib__
fsdecode.__module__ = __backlib__
fsencode.__module__ = __backlib__
fspath.__module__ = __backlib__
fstat.__module__ = __backlib__
ftruncate.__module__ = __backlib__
get_inheritable.__module__ = __backlib__
get_terminal_size.__module__ = __backlib__
getcwd.__module__ = __backlib__
getcwdb.__module__ = __backlib__
isatty.__module__ = __backlib__
link.__module__ = __backlib__
lseek.__module__ = __backlib__
lstat.__module__ = __backlib__
mkdir.__module__ = __backlib__
open.__module__ = __backlib__
read.__module__ = __backlib__
readlink.__module__ = __backlib__
rename.__module__ = __backlib__
replace.__module__ = __backlib__
rmdir.__module__ = __backlib__
set_inheritable.__module__ = __backlib__
stat.__module__ = __backlib__
strerror.__module__ = __backlib__
symlink.__module__ = __backlib__
unlink.__module__ = __backlib__
write.__module__ = __backlib__
