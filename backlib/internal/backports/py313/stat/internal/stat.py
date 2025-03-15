import stat as py_stat

from typing import Final

from backlib.internal.utils import alias


__all__: list[str] = [
    "SF_DATALESS",
    "SF_FIRMLINK",
    "SF_RESTRICTED",
    "SF_SETTABLE",
    "SF_SUPPORTED",
    "SF_SYNTHETIC",
    "UF_DATAVAULT",
    "UF_SETTABLE",
    "UF_TRACKED",
]

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
