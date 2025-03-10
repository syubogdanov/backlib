import stat as py_stat

from typing import Final

from backlib.py313.internal.utils import alias


# ---
# Version: Python 3.9+
# Explain: May be defined as `0`.
# ---

S_IFDOOR: Final[int] = py_stat.S_IFDOOR or 0o150000
S_IFPORT: Final[int] = py_stat.S_IFPORT or 0o160000
S_IFWHT: Final[int] = py_stat.S_IFWHT or 0o160000


# ---
# Version: Python 3.9+
# Explain: Available on Windows.
# ---

FILE_ATTRIBUTE_ARCHIVE: Final[int] = alias.or_default(
    py_stat,
    "FILE_ATTRIBUTE_ARCHIVE",
    otherwise=32,
)
FILE_ATTRIBUTE_COMPRESSED: Final[int] = alias.or_default(
    py_stat,
    "FILE_ATTRIBUTE_COMPRESSED",
    otherwise=2048,
)
FILE_ATTRIBUTE_DEVICE: Final[int] = alias.or_default(
    py_stat,
    "FILE_ATTRIBUTE_DEVICE",
    otherwise=64,
)
FILE_ATTRIBUTE_DIRECTORY: Final[int] = alias.or_default(
    py_stat,
    "FILE_ATTRIBUTE_DIRECTORY",
    otherwise=16,
)
FILE_ATTRIBUTE_ENCRYPTED: Final[int] = alias.or_default(
    py_stat,
    "FILE_ATTRIBUTE_ENCRYPTED",
    otherwise=16384,
)
FILE_ATTRIBUTE_HIDDEN: Final[int] = alias.or_default(
    py_stat,
    "FILE_ATTRIBUTE_HIDDEN",
    otherwise=2,
)
FILE_ATTRIBUTE_INTEGRITY_STREAM: Final[int] = alias.or_default(
    py_stat,
    "FILE_ATTRIBUTE_INTEGRITY_STREAM",
    otherwise=32768,
)
FILE_ATTRIBUTE_NORMAL: Final[int] = alias.or_default(
    py_stat,
    "FILE_ATTRIBUTE_NORMAL",
    otherwise=128,
)
FILE_ATTRIBUTE_NOT_CONTENT_INDEXED: Final[int] = alias.or_default(
    py_stat,
    "FILE_ATTRIBUTE_NOT_CONTENT_INDEXED",
    otherwise=8192,
)
FILE_ATTRIBUTE_NO_SCRUB_DATA: Final[int] = alias.or_default(
    py_stat,
    "FILE_ATTRIBUTE_NO_SCRUB_DATA",
    otherwise=131072,
)
FILE_ATTRIBUTE_OFFLINE: Final[int] = alias.or_default(
    py_stat,
    "FILE_ATTRIBUTE_OFFLINE",
    otherwise=4096,
)
FILE_ATTRIBUTE_READONLY: Final[int] = alias.or_default(
    py_stat,
    "FILE_ATTRIBUTE_READONLY",
    otherwise=1,
)
FILE_ATTRIBUTE_REPARSE_POINT: Final[int] = alias.or_default(
    py_stat,
    "FILE_ATTRIBUTE_REPARSE_POINT",
    otherwise=1024,
)
FILE_ATTRIBUTE_SPARSE_FILE: Final[int] = alias.or_default(
    py_stat,
    "FILE_ATTRIBUTE_SPARSE_FILE",
    otherwise=512,
)
FILE_ATTRIBUTE_SYSTEM: Final[int] = alias.or_default(
    py_stat,
    "FILE_ATTRIBUTE_SYSTEM",
    otherwise=4,
)
FILE_ATTRIBUTE_TEMPORARY: Final[int] = alias.or_default(
    py_stat,
    "FILE_ATTRIBUTE_TEMPORARY",
    otherwise=256,
)
FILE_ATTRIBUTE_VIRTUAL: Final[int] = alias.or_default(
    py_stat,
    "FILE_ATTRIBUTE_VIRTUAL",
    otherwise=65536,
)


# ---
# Version: Python 3.9+
# Explain: Available on Windows.
# ---

IO_REPARSE_TAG_SYMLINK: Final[int] = alias.or_default(
    py_stat,
    "IO_REPARSE_TAG_SYMLINK",
    0xA000000C,
)
IO_REPARSE_TAG_MOUNT_POINT: Final[int] = alias.or_default(
    py_stat,
    "IO_REPARSE_TAG_MOUNT_POINT",
    0xA0000003,
)
IO_REPARSE_TAG_APPEXECLINK: Final[int] = alias.or_default(
    py_stat,
    "IO_REPARSE_TAG_APPEXECLINK",
    0x8000001B,
)


# ---
# Version: Python 3.13+
# Explain: Available on macOS.
# ---

SF_SUPPORTED: Final[int] = alias.or_default(
    py_stat,
    "SF_SUPPORTED",
    otherwise=0x9F0000,
)
SF_SYNTHETIC: Final[int] = alias.or_default(
    py_stat,
    "SF_SYNTHETIC",
    otherwise=0xC0000000,
)


# ---
# Version: Python 3.13+
# Explain: Added in Python 3.13.
# ---

SF_DATALESS: Final[int] = alias.or_default(
    py_stat,
    "SF_DATALESS",
    otherwise=0x40000000,
)
SF_FIRMLINK: Final[int] = alias.or_default(
    py_stat,
    "SF_FIRMLINK",
    otherwise=0x00800000,
)
SF_RESTRICTED: Final[int] = alias.or_default(
    py_stat,
    "SF_RESTRICTED",
    otherwise=0x00080000,
)
SF_SETTABLE: Final[int] = alias.or_default(
    py_stat,
    "SF_SETTABLE",
    otherwise=0xFFFF0000,
)

UF_DATAVAULT: Final[int] = alias.or_default(
    py_stat,
    "UF_DATAVAULT",
    otherwise=0x00000080,
)
UF_SETTABLE: Final[int] = alias.or_default(
    py_stat,
    "UF_SETTABLE",
    otherwise=0x0000FFFF,
)
UF_TRACKED: Final[int] = alias.or_default(
    py_stat,
    "UF_TRACKED",
    otherwise=0x00000040,
)


# ---
# Version: Python 3.9+
# Explain: No changes required.
# ---

SF_APPEND = py_stat.SF_APPEND
SF_ARCHIVED = py_stat.SF_ARCHIVED
SF_IMMUTABLE = py_stat.SF_IMMUTABLE
SF_NOUNLINK = py_stat.SF_NOUNLINK
SF_SNAPSHOT = py_stat.SF_SNAPSHOT

ST_ATIME = py_stat.ST_ATIME
ST_CTIME = py_stat.ST_CTIME
ST_DEV = py_stat.ST_DEV
ST_GID = py_stat.ST_GID
ST_INO = py_stat.ST_INO
ST_MODE = py_stat.ST_MODE
ST_MTIME = py_stat.ST_MTIME
ST_NLINK = py_stat.ST_NLINK
ST_SIZE = py_stat.ST_SIZE
ST_UID = py_stat.ST_UID

S_ENFMT = py_stat.S_ENFMT
S_IEXEC = py_stat.S_IEXEC
S_IFBLK = py_stat.S_IFBLK
S_IFCHR = py_stat.S_IFCHR
S_IFDIR = py_stat.S_IFDIR
S_IFIFO = py_stat.S_IFIFO
S_IFLNK = py_stat.S_IFLNK
S_IFMT = py_stat.S_IFMT
S_IFREG = py_stat.S_IFREG
S_IFSOCK = py_stat.S_IFSOCK
S_IMODE = py_stat.S_IMODE
S_IREAD = py_stat.S_IREAD
S_IRGRP = py_stat.S_IRGRP
S_IROTH = py_stat.S_IROTH
S_IRUSR = py_stat.S_IRUSR
S_IRWXG = py_stat.S_IRWXG
S_IRWXO = py_stat.S_IRWXO
S_IRWXU = py_stat.S_IRWXU
S_ISBLK = py_stat.S_ISBLK
S_ISCHR = py_stat.S_ISCHR
S_ISDIR = py_stat.S_ISDIR
S_ISDOOR = py_stat.S_ISDOOR
S_ISFIFO = py_stat.S_ISFIFO
S_ISGID = py_stat.S_ISGID
S_ISLNK = py_stat.S_ISLNK
S_ISPORT = py_stat.S_ISPORT
S_ISREG = py_stat.S_ISREG
S_ISSOCK = py_stat.S_ISSOCK
S_ISUID = py_stat.S_ISUID
S_ISVTX = py_stat.S_ISVTX
S_ISWHT = py_stat.S_ISWHT
S_IWGRP = py_stat.S_IWGRP
S_IWOTH = py_stat.S_IWOTH
S_IWRITE = py_stat.S_IWRITE
S_IWUSR = py_stat.S_IWUSR
S_IXGRP = py_stat.S_IXGRP
S_IXOTH = py_stat.S_IXOTH
S_IXUSR = py_stat.S_IXUSR

UF_APPEND = py_stat.UF_APPEND
UF_COMPRESSED = py_stat.UF_COMPRESSED
UF_HIDDEN = py_stat.UF_HIDDEN
UF_IMMUTABLE = py_stat.UF_IMMUTABLE
UF_NODUMP = py_stat.UF_NODUMP
UF_NOUNLINK = py_stat.UF_NOUNLINK
UF_OPAQUE = py_stat.UF_OPAQUE

filemode = py_stat.filemode
