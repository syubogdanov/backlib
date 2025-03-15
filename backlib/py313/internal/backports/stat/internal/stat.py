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
    "SF_DATALESS",
    "SF_FIRMLINK",
    "SF_RESTRICTED",
    "SF_SETTABLE",
    "SF_SUPPORTED",
    "SF_SYNTHETIC",
    "S_IFDOOR",
    "S_IFPORT",
    "S_IFWHT",
    "UF_DATAVAULT",
    "UF_SETTABLE",
    "UF_TRACKED",
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
