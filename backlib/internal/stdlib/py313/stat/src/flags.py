import stat as py_stat

from typing import Final

from backlib.internal.utils import alias


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
    "S_IFPORT",
    "S_IFREG",
    "S_IFSOCK",
    "S_IFWHT",
    "S_IREAD",
    "S_IRGRP",
    "S_IROTH",
    "S_IRUSR",
    "S_IRWXG",
    "S_IRWXO",
    "S_IRWXU",
    "S_ISGID",
    "S_ISUID",
    "S_ISVTX",
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
]


ST_MODE: Final[int] = 0
ST_INO: Final[int] = 1
ST_DEV: Final[int] = 2
ST_NLINK: Final[int] = 3
ST_UID: Final[int] = 4
ST_GID: Final[int] = 5
ST_SIZE: Final[int] = 6
ST_ATIME: Final[int] = 7
ST_MTIME: Final[int] = 8
ST_CTIME: Final[int] = 9

S_IFDIR: Final[int]  = 0o040000
S_IFCHR: Final[int]  = 0o020000
S_IFBLK: Final[int]  = 0o060000
S_IFREG: Final[int]  = 0o100000
S_IFIFO: Final[int]  = 0o010000
S_IFLNK: Final[int]  = 0o120000
S_IFSOCK: Final[int] = 0o140000

S_IFDOOR: Final[int] = alias.to(py_stat.S_IFDOOR)
S_IFPORT: Final[int] = alias.to(py_stat.S_IFPORT)
S_IFWHT: Final[int] = alias.to(py_stat.S_IFWHT)

S_ISUID: Final[int] = 0o4000
S_ISGID: Final[int] = 0o2000
S_ENFMT: Final[int] = S_ISGID
S_ISVTX: Final[int] = 0o1000
S_IREAD: Final[int] = 0o0400
S_IWRITE: Final[int] = 0o0200
S_IEXEC: Final[int] = 0o0100
S_IRWXU: Final[int] = 0o0700
S_IRUSR: Final[int] = 0o0400
S_IWUSR: Final[int] = 0o0200
S_IXUSR: Final[int] = 0o0100
S_IRWXG: Final[int] = 0o0070
S_IRGRP: Final[int] = 0o0040
S_IWGRP: Final[int] = 0o0020
S_IXGRP: Final[int] = 0o0010
S_IRWXO: Final[int] = 0o0007
S_IROTH: Final[int] = 0o0004
S_IWOTH: Final[int] = 0o0002
S_IXOTH: Final[int] = 0o0001

UF_SETTABLE: Final[int] = 0x0000ffff
UF_NODUMP: Final[int] = 0x00000001
UF_IMMUTABLE: Final[int] = 0x00000002
UF_APPEND: Final[int] = 0x00000004
UF_OPAQUE: Final[int] = 0x00000008
UF_NOUNLINK: Final[int] = 0x00000010
UF_COMPRESSED: Final[int] = 0x00000020
UF_TRACKED: Final[int] = 0x00000040
UF_DATAVAULT: Final[int] = 0x00000080
UF_HIDDEN: Final[int] = 0x00008000

SF_SETTABLE: Final[int] = 0xffff0000
SF_ARCHIVED: Final[int] = 0x00010000
SF_IMMUTABLE: Final[int] = 0x00020000
SF_APPEND: Final[int] = 0x00040000
SF_RESTRICTED: Final[int] = 0x00080000
SF_NOUNLINK: Final[int] = 0x00100000
SF_SNAPSHOT: Final[int] = 0x00200000
SF_FIRMLINK: Final[int] = 0x00800000
SF_DATALESS: Final[int] = 0x40000000

SF_SUPPORTED: Final[int] = 0x9F0000
SF_SYNTHETIC: Final[int] = 0xC0000000

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

IO_REPARSE_TAG_SYMLINK: Final[int] = 0xA000000C
IO_REPARSE_TAG_MOUNT_POINT: Final[int] = 0xA0000003
IO_REPARSE_TAG_APPEXECLINK: Final[int] = 0x8000001B
