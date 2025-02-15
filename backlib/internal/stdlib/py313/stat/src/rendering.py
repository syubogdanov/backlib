from backlib.internal.stdlib.py313.stat.src.flags import (
    S_IFBLK,
    S_IFCHR,
    S_IFDIR,
    S_IFIFO,
    S_IFLNK,
    S_IFREG,
    S_IFSOCK,
    S_IRGRP,
    S_IROTH,
    S_IRUSR,
    S_ISGID,
    S_ISUID,
    S_ISVTX,
    S_IWGRP,
    S_IWOTH,
    S_IWUSR,
    S_IXGRP,
    S_IXOTH,
    S_IXUSR,
)


__all__: list[str] = ["filemode"]


_filemode_table = (
    # File type chars according to:
    # http://en.wikibooks.org/wiki/C_Programming/POSIX_Reference/sys/stat.h
    ((S_IFLNK,         "l"),
     (S_IFSOCK,        "s"),  # Must appear before IFREG and IFDIR as IFSOCK == IFREG | IFDIR
     (S_IFREG,         "-"),
     (S_IFBLK,         "b"),
     (S_IFDIR,         "d"),
     (S_IFCHR,         "c"),
     (S_IFIFO,         "p")),

    ((S_IRUSR,         "r"),),
    ((S_IWUSR,         "w"),),
    ((S_IXUSR|S_ISUID, "s"),
     (S_ISUID,         "S"),
     (S_IXUSR,         "x")),

    ((S_IRGRP,         "r"),),
    ((S_IWGRP,         "w"),),
    ((S_IXGRP|S_ISGID, "s"),
     (S_ISGID,         "S"),
     (S_IXGRP,         "x")),

    ((S_IROTH,         "r"),),
    ((S_IWOTH,         "w"),),
    ((S_IXOTH|S_ISVTX, "t"),
     (S_ISVTX,         "T"),
     (S_IXOTH,         "x")),
)


def filemode(mode: int) -> str:
    """Convert a file's mode to a string of the form `'-rwxrwxrwx'`.

    See Also
    --------
    * `stat.filemode`.

    Version
    -------
    * Python 3.13.
    """
    perms: list[str] = []

    for index, table in enumerate(_filemode_table):
        perm = "-" if index != 0 else "?"

        for bit, char in table:
            if mode & bit == bit:
                perm = char
                break

        perms.append(perm)

    return "".join(perms)
