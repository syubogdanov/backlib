import stat as py_stat

from typing import Final


__all__: list[str] = [
    "FILE_ATTRIBUTE_ARCHIVE",
    "FILE_ATTRIBUTE_COMPRESSED",
    "FILE_ATTRIBUTE_DEVICE",
    "FILE_ATTRIBUTE_DIRECTORY",
    "FILE_ATTRIBUTE_ENCRYPTED",
    "FILE_ATTRIBUTE_HIDDEN",
    "FILE_ATTRIBUTE_INTEGRITY_STREAM",
    "FILE_ATTRIBUTE_NORMAL",
    "FILE_ATTRIBUTE_NOT_CONTENT_INDEXED",
    "FILE_ATTRIBUTE_NO_SCRUB_DATA",
    "FILE_ATTRIBUTE_OFFLINE",
    "FILE_ATTRIBUTE_READONLY",
    "FILE_ATTRIBUTE_REPARSE_POINT",
    "FILE_ATTRIBUTE_SPARSE_FILE",
    "FILE_ATTRIBUTE_SYSTEM",
    "FILE_ATTRIBUTE_TEMPORARY",
    "FILE_ATTRIBUTE_VIRTUAL",
    "IO_REPARSE_TAG_APPEXECLINK",
    "IO_REPARSE_TAG_MOUNT_POINT",
    "IO_REPARSE_TAG_SYMLINK",
    "SF_APPEND",
    "SF_ARCHIVED",
    "SF_DATALESS",
    "SF_FIRMLINK",
    "SF_IMMUTABLE",
    "SF_NOUNLINK",
    "SF_RESTRICTED",
    "SF_SETTABLE",
    "SF_SNAPSHOT",
    "SF_SUPPORTED",
    "SF_SYNTHETIC",
    "ST_ATIME",
    "ST_CTIME",
    "ST_DEV",
    "ST_GID",
    "ST_INO",
    "ST_MODE",
    "ST_MTIME",
    "ST_NLINK",
    "ST_SIZE",
    "ST_UID",
    "S_ENFMT",
    "S_IEXEC",
    "S_IFBLK",
    "S_IFCHR",
    "S_IFDIR",
    "S_IFDOOR",
    "S_IFIFO",
    "S_IFLNK",
    "S_IFMT",
    "S_IFPORT",
    "S_IFREG",
    "S_IFSOCK",
    "S_IFWHT",
    "S_IMODE",
    "S_IREAD",
    "S_IRGRP",
    "S_IROTH",
    "S_IRUSR",
    "S_IRWXG",
    "S_IRWXO",
    "S_IRWXU",
    "S_ISBLK",
    "S_ISCHR",
    "S_ISDIR",
    "S_ISDOOR",
    "S_ISFIFO",
    "S_ISGID",
    "S_ISLNK",
    "S_ISPORT",
    "S_ISREG",
    "S_ISSOCK",
    "S_ISUID",
    "S_ISVTX",
    "S_ISWHT",
    "S_IWGRP",
    "S_IWOTH",
    "S_IWRITE",
    "S_IWUSR",
    "S_IXGRP",
    "S_IXOTH",
    "S_IXUSR",
    "UF_APPEND",
    "UF_COMPRESSED",
    "UF_DATAVAULT",
    "UF_HIDDEN",
    "UF_IMMUTABLE",
    "UF_NODUMP",
    "UF_NOUNLINK",
    "UF_OPAQUE",
    "UF_SETTABLE",
    "UF_TRACKED",
    "filemode",
]


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

FILE_ATTRIBUTE_ARCHIVE: Final[int] = 32
FILE_ATTRIBUTE_COMPRESSED: Final[int] = 2048
FILE_ATTRIBUTE_DEVICE: Final[int] = 64
FILE_ATTRIBUTE_DIRECTORY: Final[int] = 16
FILE_ATTRIBUTE_ENCRYPTED: Final[int] = 16384
FILE_ATTRIBUTE_HIDDEN: Final[int] = 2
FILE_ATTRIBUTE_INTEGRITY_STREAM: Final[int] = 32768
FILE_ATTRIBUTE_NORMAL: Final[int] = 128
FILE_ATTRIBUTE_NOT_CONTENT_INDEXED: Final[int] = 8192
FILE_ATTRIBUTE_NO_SCRUB_DATA: Final[int] = 131072
FILE_ATTRIBUTE_OFFLINE: Final[int] = 4096
FILE_ATTRIBUTE_READONLY: Final[int] = 1
FILE_ATTRIBUTE_REPARSE_POINT: Final[int] = 1024
FILE_ATTRIBUTE_SPARSE_FILE: Final[int] = 512
FILE_ATTRIBUTE_SYSTEM: Final[int] = 4
FILE_ATTRIBUTE_TEMPORARY: Final[int] = 256
FILE_ATTRIBUTE_VIRTUAL: Final[int] = 65536


# ---
# Version: Python 3.9+
# Explain: Available on Windows.
# ---

IO_REPARSE_TAG_SYMLINK: Final[int] = 0xA000000C
IO_REPARSE_TAG_MOUNT_POINT: Final[int] = 0xA0000003
IO_REPARSE_TAG_APPEXECLINK: Final[int] = 0x8000001B


# ---
# Version: Python 3.13+
# Explain: Available on macOS.
# ---

SF_SUPPORTED: Final[int] = 0x9F0000
SF_SYNTHETIC: Final[int] = 0xC0000000


# ---
# Version: Python 3.13+
# Explain: Added in Python 3.13.
# ---

SF_DATALESS: Final[int] = 0x40000000
SF_FIRMLINK: Final[int] = 0x00800000
SF_RESTRICTED: Final[int] = 0x00080000
SF_SETTABLE: Final[int] = 0xFFFF0000

UF_DATAVAULT: Final[int] = 0x00000080
UF_SETTABLE: Final[int] = 0x0000FFFF
UF_TRACKED: Final[int] = 0x00000040


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
