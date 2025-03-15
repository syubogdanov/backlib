import errno as py_errno

from typing import Final

from backlib.internal.backports.py310 import errno as py310_errno
from backlib.internal.backports.py311.errno.internal import darwin1, freebsd13
from backlib.internal.utils import alias


__all__: list[str] = ["ENOTCAPABLE", "EQFULL", "errorcode"]


ENOTCAPABLE: Final[int] = alias.or_platform(
    py_errno,
    "ENOTCAPABLE",
    freebsd=freebsd13.ENOTCAPABLE,
    otherwise=freebsd13.ENOTCAPABLE,
)

EQFULL: Final[int] = alias.or_platform(
    py_errno,
    "EQFULL",
    darwin=darwin1.EQFULL,
    otherwise=darwin1.EQFULL,
)


errorcode = {
    ENOTCAPABLE: "ENOTCAPABLE",
    EQFULL: "EQFULL",
    **py310_errno.errorcode,
}
