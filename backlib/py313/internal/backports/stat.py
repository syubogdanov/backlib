import stat as py_stat

from typing import Final

from backlib.py313.internal.utils import alias


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

# Python 3.9+, May be defined as `0`
S_IFDOOR: Final[int] = alias.to(py_stat.S_IFDOOR) or 0o150000
S_IFPORT: Final[int] = alias.to(py_stat.S_IFPORT) or 0o160000
S_IFWHT: Final[int] = alias.to(py_stat.S_IFWHT) or 0o160000

# Python 3.9+, Windows
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

# Python 3.9+, Windows
IO_REPARSE_TAG_SYMLINK: Final[int] = 0xA000000C
IO_REPARSE_TAG_MOUNT_POINT: Final[int] = 0xA0000003
IO_REPARSE_TAG_APPEXECLINK: Final[int] = 0x8000001B

# Python 3.13+, macOS
SF_SUPPORTED: Final[int] = 0x9F0000
SF_SYNTHETIC: Final[int] = 0xC0000000

# Python 3.13+
SF_DATALESS: Final[int] = 0x40000000
SF_FIRMLINK: Final[int] = 0x00800000
SF_RESTRICTED: Final[int] = 0x00080000
SF_SETTABLE: Final[int] = 0xFFFF0000

# Python 3.13+
UF_DATAVAULT: Final[int] = 0x00000080
UF_SETTABLE: Final[int] = 0x0000FFFF
UF_TRACKED: Final[int] = 0x00000040

# Python 3.9+
SF_APPEND = alias.to(py_stat.SF_APPEND)
SF_ARCHIVED = alias.to(py_stat.SF_ARCHIVED)
SF_IMMUTABLE = alias.to(py_stat.SF_IMMUTABLE)
SF_NOUNLINK = alias.to(py_stat.SF_NOUNLINK)
SF_SNAPSHOT = alias.to(py_stat.SF_SNAPSHOT)

ST_ATIME = alias.to(py_stat.ST_ATIME)
ST_CTIME = alias.to(py_stat.ST_CTIME)
ST_DEV = alias.to(py_stat.ST_DEV)
ST_GID = alias.to(py_stat.ST_GID)
ST_INO = alias.to(py_stat.ST_INO)
ST_MODE = alias.to(py_stat.ST_MODE)
ST_MTIME = alias.to(py_stat.ST_MTIME)
ST_NLINK = alias.to(py_stat.ST_NLINK)
ST_SIZE = alias.to(py_stat.ST_SIZE)
ST_UID = alias.to(py_stat.ST_UID)

S_ENFMT = alias.to(py_stat.S_ENFMT)
S_IEXEC = alias.to(py_stat.S_IEXEC)
S_IFBLK = alias.to(py_stat.S_IFBLK)
S_IFCHR = alias.to(py_stat.S_IFCHR)
S_IFDIR = alias.to(py_stat.S_IFDIR)
S_IFIFO = alias.to(py_stat.S_IFIFO)
S_IFLNK = alias.to(py_stat.S_IFLNK)
S_IFMT = alias.to(py_stat.S_IFMT)
S_IFREG = alias.to(py_stat.S_IFREG)
S_IFSOCK = alias.to(py_stat.S_IFSOCK)
S_IMODE = alias.to(py_stat.S_IMODE)
S_IREAD = alias.to(py_stat.S_IREAD)
S_IRGRP = alias.to(py_stat.S_IRGRP)
S_IROTH = alias.to(py_stat.S_IROTH)
S_IRUSR = alias.to(py_stat.S_IRUSR)
S_IRWXG = alias.to(py_stat.S_IRWXG)
S_IRWXO = alias.to(py_stat.S_IRWXO)
S_IRWXU = alias.to(py_stat.S_IRWXU)
S_ISBLK = alias.to(py_stat.S_ISBLK)
S_ISCHR = alias.to(py_stat.S_ISCHR)
S_ISDIR = alias.to(py_stat.S_ISDIR)
S_ISDOOR = alias.to(py_stat.S_ISDOOR)
S_ISFIFO = alias.to(py_stat.S_ISFIFO)
S_ISGID = alias.to(py_stat.S_ISGID)
S_ISLNK = alias.to(py_stat.S_ISLNK)
S_ISPORT = alias.to(py_stat.S_ISPORT)
S_ISREG = alias.to(py_stat.S_ISREG)
S_ISSOCK = alias.to(py_stat.S_ISSOCK)
S_ISUID = alias.to(py_stat.S_ISUID)
S_ISVTX = alias.to(py_stat.S_ISVTX)
S_ISWHT = alias.to(py_stat.S_ISWHT)
S_IWGRP = alias.to(py_stat.S_IWGRP)
S_IWOTH = alias.to(py_stat.S_IWOTH)
S_IWRITE = alias.to(py_stat.S_IWRITE)
S_IWUSR = alias.to(py_stat.S_IWUSR)
S_IXGRP = alias.to(py_stat.S_IXGRP)
S_IXOTH = alias.to(py_stat.S_IXOTH)
S_IXUSR = alias.to(py_stat.S_IXUSR)

UF_APPEND = alias.to(py_stat.UF_APPEND)
UF_COMPRESSED = alias.to(py_stat.UF_COMPRESSED)
UF_HIDDEN = alias.to(py_stat.UF_HIDDEN)
UF_IMMUTABLE = alias.to(py_stat.UF_IMMUTABLE)
UF_NODUMP = alias.to(py_stat.UF_NODUMP)
UF_NOUNLINK = alias.to(py_stat.UF_NOUNLINK)
UF_OPAQUE = alias.to(py_stat.UF_OPAQUE)

filemode = alias.to(py_stat.filemode)
