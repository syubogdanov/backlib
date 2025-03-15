"""Flags for Linux 5.10+.

See Also
--------
* https://docs.rs/libc/latest/libc/
"""

from typing import Final


PRIO_PROCESS: Final[int] = 0
PRIO_PGRP: Final[int] = 1
PRIO_USER: Final[int] = 2

F_LOCK: Final[int] = 1
F_TLOCK: Final[int] = 2
F_ULOCK: Final[int] = 0
F_TEST: Final[int] = 3

SEEK_HOLE: Final[int] = 4
SEEK_DATA: Final[int] = 3

O_RDONLY: Final[int] = 0
O_WRONLY: Final[int] = 1
O_RDWR: Final[int] = 2
O_APPEND: Final[int] = 1024
O_CREAT: Final[int] = 64
O_EXCL: Final[int] = 128
O_TRUNC: Final[int] = 512

O_DSYNC: Final[int] = 4096
O_RSYNC: Final[int] = 1052672
O_SYNC: Final[int] = 1052672
O_NONBLOCK: Final[int] = 2048
O_NOCTTY: Final[int] = 256

O_CLOEXEC: Final[int] = 0x80000
O_NDELAY: Final[int] = 0x800

O_ASYNC: Final[int] = 0x2000
O_DIRECT: Final[int] = 0x4000
O_DIRECTORY: Final[int] = 0x10000
O_NOFOLLOW: Final[int] = 0x20000

O_NOATIME: Final[int] = 0o1000000
O_PATH: Final[int] = 0o10000000
O_TMPFILE: Final[int] = 0o20000000 | O_DIRECTORY

POSIX_FADV_NORMAL: Final[int] = 0
POSIX_FADV_SEQUENTIAL: Final[int] = 2
POSIX_FADV_RANDOM: Final[int] = 1
POSIX_FADV_NOREUSE: Final[int] = 5
POSIX_FADV_WILLNEED: Final[int] = 3
POSIX_FADV_DONTNEED: Final[int] = 4

RWF_NOWAIT: Final[int] = 0x00000008
RWF_HIPRI: Final[int] = 0x00000001

RWF_DSYNC: Final[int] = 0x00000002
RWF_SYNC: Final[int] = 0x00000004
RWF_APPEND: Final[int] = 0x00000010

SPLICE_F_MOVE: Final[int] = 0x01
SPLICE_F_NONBLOCK: Final[int] = 0x02
SPLICE_F_MORE: Final[int] = 0x04

MFD_CLOEXEC: Final[int] = 0x0001
MFD_ALLOW_SEALING: Final[int] = 0x0002
MFD_HUGETLB: Final[int] = 0x0004

MFD_HUGE_SHIFT: Final[int] = 26
MFD_HUGE_MASK: Final[int] = 63

MFD_HUGE_64KB: Final[int] = 0x40000000
MFD_HUGE_512KB: Final[int] = 0x4C000000
MFD_HUGE_1MB: Final[int] = 0x50000000
MFD_HUGE_2MB: Final[int] = 0x54000000
MFD_HUGE_8MB: Final[int] = 0x5C000000
MFD_HUGE_16MB: Final[int] = 0x60000000
MFD_HUGE_32MB: Final[int] = 0x64000000
MFD_HUGE_256MB: Final[int] = 0x70000000
MFD_HUGE_512MB: Final[int] = 0x74000000
MFD_HUGE_1GB: Final[int] = 0x78000000
MFD_HUGE_2GB: Final[int] = 0x7C000000
MFD_HUGE_16GB: Final[int] = 0x88000000

EFD_CLOEXEC: Final[int] = 0x80000
EFD_NONBLOCK: Final[int] = 0x800
EFD_SEMAPHORE: Final[int] = 0x1

XATTR_CREATE: Final[int] = 0x1
XATTR_REPLACE: Final[int] = 0x2

P_ALL: Final[int] = 0
P_PID: Final[int] = 1
P_PGID: Final[int] = 2
P_PIDFD: Final[int] = 3

WCONTINUED: Final[int] = 0x00000008
WEXITED: Final[int] = 0x00000004
WUNTRACED: Final[int] = 0x00000002
WSTOPPED: Final[int] = WUNTRACED
WNOHANG: Final[int] = 0x00000001
WNOWAIT: Final[int] = 0x01000000

CLD_EXITED: Final[int] = 1
CLD_KILLED: Final[int] = 2
CLD_DUMPED: Final[int] = 3
CLD_TRAPPED: Final[int] = 4
CLD_STOPPED: Final[int] = 5
CLD_CONTINUED: Final[int] = 6

SCHED_OTHER: Final[int] = 0
SCHED_FIFO: Final[int] = 1
SCHED_RR: Final[int] = 2
SCHED_BATCH: Final[int] = 3
SCHED_IDLE: Final[int] = 5

SCHED_RESET_ON_FORK: Final[int] = 0x40000000

RTLD_LOCAL: Final[int] = 0
RTLD_LAZY: Final[int] = 1

RTLD_NOW: Final[int] = 0x2
RTLD_NOLOAD: Final[int] = 0x4
RTLD_DEEPBIND: Final[int] = 0x8
RTLD_GLOBAL: Final[int] = 0x100
RTLD_NODELETE: Final[int] = 0x1000

GRND_NONBLOCK: Final[int] = 0x0001
GRND_RANDOM: Final[int] = 0x0002
