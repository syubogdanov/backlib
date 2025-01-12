from backlib.internal.stdlib.py313.os.src import (
    EX_OK,
    F_OK,
    O_APPEND,
    O_CREAT,
    O_EXCL,
    O_RDONLY,
    O_RDWR,
    O_TRUNC,
    O_WRONLY,
    P_NOWAIT,
    P_NOWAITO,
    P_WAIT,
    R_OK,
    SEEK_CUR,
    SEEK_END,
    SEEK_SET,
    TMP_MAX,
    W_OK,
    X_OK,
    DirEntry,
    PathLike,
    _exit,
    abort,
    access,
    altsep,
    chdir,
    chmod,
    close,
    closerange,
    cpu_count,
    curdir,
    defpath,
    device_encoding,
    devnull,
    dup,
    dup2,
    environ,
    environb,
    error,
    execl,
    execle,
    execlp,
    execlpe,
    execv,
    execve,
    execvp,
    execvpe,
    extsep,
    fchmod,
    fdopen,
    fsdecode,
    fsencode,
    fspath,
    fstat,
    fsync,
    ftruncate,
    get_blocking,
    get_exec_path,
    get_inheritable,
    get_terminal_size,
    getcwd,
    getcwdb,
    getenv,
    getenvb,
    getlogin,
    getpid,
    getppid,
    isatty,
    kill,
    linesep,
    link,
    listdir,
    lseek,
    lstat,
    makedirs,
    mkdir,
    name,
    open,  # noqa: A004
    pardir,
    path,
    pathsep,
    pipe,
    popen,
    process_cpu_count,
    putenv,
    read,
    readlink,
    remove,
    removedirs,
    rename,
    renames,
    replace,
    rmdir,
    scandir,
    sep,
    set_blocking,
    set_inheritable,
    spawnl,
    spawnle,
    spawnv,
    spawnve,
    stat,
    stat_result,
    strerror,
    supports_bytes_environ,
    supports_dir_fd,
    supports_effective_ids,
    supports_fd,
    supports_follow_symlinks,
    symlink,
    system,
    terminal_size,
    times,
    times_result,
    truncate,
    umask,
    unlink,
    unsetenv,
    urandom,
    utime,
    waitpid,
    waitstatus_to_exitcode,
    walk,
    write,
)


__all__: list[str] = [
    "EX_OK",
    "F_OK",
    "O_APPEND",
    "O_CREAT",
    "O_EXCL",
    "O_RDONLY",
    "O_RDWR",
    "O_TRUNC",
    "O_WRONLY",
    "P_NOWAIT",
    "P_NOWAITO",
    "P_WAIT",
    "R_OK",
    "SEEK_CUR",
    "SEEK_END",
    "SEEK_SET",
    "TMP_MAX",
    "W_OK",
    "X_OK",
    "DirEntry",
    "PathLike",
    "_exit",
    "abort",
    "access",
    "altsep",
    "chdir",
    "chmod",
    "close",
    "closerange",
    "cpu_count",
    "curdir",
    "defpath",
    "device_encoding",
    "devnull",
    "dup",
    "dup2",
    "environ",
    "environb",
    "error",
    "execl",
    "execle",
    "execlp",
    "execlpe",
    "execv",
    "execve",
    "execvp",
    "execvpe",
    "extsep",
    "fchmod",
    "fdopen",
    "fsdecode",
    "fsencode",
    "fspath",
    "fstat",
    "fsync",
    "ftruncate",
    "get_blocking",
    "get_exec_path",
    "get_inheritable",
    "get_terminal_size",
    "getcwd",
    "getcwdb",
    "getenv",
    "getenvb",
    "getlogin",
    "getpid",
    "getppid",
    "isatty",
    "kill",
    "linesep",
    "link",
    "listdir",
    "lseek",
    "lstat",
    "makedirs",
    "mkdir",
    "name",
    "open",
    "pardir",
    "path",
    "pathsep",
    "pipe",
    "popen",
    "process_cpu_count",
    "putenv",
    "read",
    "readlink",
    "remove",
    "removedirs",
    "rename",
    "renames",
    "replace",
    "rmdir",
    "scandir",
    "sep",
    "set_blocking",
    "set_inheritable",
    "spawnl",
    "spawnle",
    "spawnv",
    "spawnve",
    "stat",
    "stat_result",
    "strerror",
    "supports_bytes_environ",
    "supports_dir_fd",
    "supports_effective_ids",
    "supports_fd",
    "supports_follow_symlinks",
    "symlink",
    "system",
    "terminal_size",
    "times",
    "times_result",
    "truncate",
    "umask",
    "unlink",
    "unsetenv",
    "urandom",
    "utime",
    "waitpid",
    "waitstatus_to_exitcode",
    "walk",
    "write",
]

__backlib__: str = "backlib.py313.os"


environ.__module__ = __backlib__
environb.__module__ = __backlib__

# `os.error` is an alias to `OSError`
# error.__module__ = __backlib__  # noqa: ERA001

DirEntry.__module__ = __backlib__
PathLike.__module__ = __backlib__
stat_result.__module__ = __backlib__
terminal_size.__module__ = __backlib__
times_result.__module__ = __backlib__

_exit.__module__ = __backlib__
abort.__module__ = __backlib__
access.__module__ = __backlib__
chdir.__module__ = __backlib__
chmod.__module__ = __backlib__
close.__module__ = __backlib__
closerange.__module__ = __backlib__
cpu_count.__module__ = __backlib__
device_encoding.__module__ = __backlib__
dup.__module__ = __backlib__
dup2.__module__ = __backlib__
execl.__module__ = __backlib__
execle.__module__ = __backlib__
execlp.__module__ = __backlib__
execlpe.__module__ = __backlib__
execv.__module__ = __backlib__
execve.__module__ = __backlib__
execvp.__module__ = __backlib__
execvpe.__module__ = __backlib__
fchmod.__module__ = __backlib__
fdopen.__module__ = __backlib__
fsdecode.__module__ = __backlib__
fsencode.__module__ = __backlib__
fspath.__module__ = __backlib__
fstat.__module__ = __backlib__
fsync.__module__ = __backlib__
ftruncate.__module__ = __backlib__
get_blocking.__module__ = __backlib__
get_exec_path.__module__ = __backlib__
get_inheritable.__module__ = __backlib__
get_terminal_size.__module__ = __backlib__
getcwd.__module__ = __backlib__
getcwdb.__module__ = __backlib__
getenv.__module__ = __backlib__
getenvb.__module__ = __backlib__
getlogin.__module__ = __backlib__
getpid.__module__ = __backlib__
getppid.__module__ = __backlib__
isatty.__module__ = __backlib__
kill.__module__ = __backlib__
link.__module__ = __backlib__
listdir.__module__ = __backlib__
lseek.__module__ = __backlib__
lstat.__module__ = __backlib__
makedirs.__module__ = __backlib__
mkdir.__module__ = __backlib__
open.__module__ = __backlib__
pipe.__module__ = __backlib__
popen.__module__ = __backlib__
process_cpu_count.__module__ = __backlib__
putenv.__module__ = __backlib__
read.__module__ = __backlib__
readlink.__module__ = __backlib__
remove.__module__ = __backlib__
removedirs.__module__ = __backlib__
rename.__module__ = __backlib__
renames.__module__ = __backlib__
replace.__module__ = __backlib__
rmdir.__module__ = __backlib__
scandir.__module__ = __backlib__
set_blocking.__module__ = __backlib__
set_inheritable.__module__ = __backlib__
spawnl.__module__ = __backlib__
spawnle.__module__ = __backlib__
spawnv.__module__ = __backlib__
spawnve.__module__ = __backlib__
stat.__module__ = __backlib__
strerror.__module__ = __backlib__
symlink.__module__ = __backlib__
system.__module__ = __backlib__
times.__module__ = __backlib__
truncate.__module__ = __backlib__
umask.__module__ = __backlib__
unlink.__module__ = __backlib__
unsetenv.__module__ = __backlib__
urandom.__module__ = __backlib__
utime.__module__ = __backlib__
waitpid.__module__ = __backlib__
waitstatus_to_exitcode.__module__ = __backlib__
walk.__module__ = __backlib__
write.__module__ = __backlib__
