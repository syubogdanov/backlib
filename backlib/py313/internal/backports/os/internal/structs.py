from __future__ import annotations

from typing import NamedTuple

from backlib.py313.internal.markers import techdebt


@techdebt.simplified
class stat_result(NamedTuple):  # noqa: N801
    """Object whose attributes correspond roughly to the members of the `stat` structure.

    See Also
    --------
    * `os.stat_result`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This class is a `NamedTuple`, not `structeq[float]`.
    """

    st_mode: int
    st_ino: int
    st_dev: int
    st_nlink: int
    st_uid: int
    st_gid: int
    st_size: int

    st_atime: float
    st_mtime: float
    st_ctime: float

    st_atime_ns: int
    st_mtime_ns: int
    st_ctime_ns: int

    st_birthtime: float
    st_birthtime_ns: int

    # Unix
    st_blocks: int
    st_blksize: int
    st_rdev: int
    st_flags: int

    # FreeBSD
    st_gen: int

    # Solaris
    st_fstype: str

    # macOS
    st_rsize: int
    st_creator: int
    st_type: int

    # Windows
    st_file_attributes: int
    st_reparse_tag: int


@techdebt.simplified
class terminal_size(NamedTuple):  # noqa: N801
    """A subclass of tuple, holding `(columns, lines)` of the terminal window size.

    See Also
    --------
    * `os.terminal_size`.

    Version
    -------
    * Python 3.13.

    Technical Debt
    --------------
    * This class is a `NamedTuple`, not `structeq[int]`.
    """

    columns: int
    lines: int
