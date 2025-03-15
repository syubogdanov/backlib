"""Flags for Linux 5.10+.

See Also
--------
* https://docs.rs/libc/latest/libc/
"""

from typing import Final


CLONE_FILES: Final[int] = 0x400
CLONE_FS: Final[int] = 0x200
CLONE_NEWCGROUP: Final[int] = 0x02000000
CLONE_NEWIPC: Final[int] = 0x08000000
CLONE_NEWNET: Final[int] = 0x40000000
CLONE_NEWNS: Final[int] = 0x20000
CLONE_NEWPID: Final[int] = 0x20000000
CLONE_NEWTIME: Final[int] = 0x80
CLONE_NEWUSER: Final[int] = 0x10000000
CLONE_NEWUTS: Final[int] = 0x04000000
CLONE_SIGHAND: Final[int] = 0x800
CLONE_SYSVSEM: Final[int] = 0x40000
CLONE_THREAD: Final[int] = 0x10000
CLONE_VM: Final[int] = 0x100

PIDFD_NONBLOCK: Final[int] = 2048
