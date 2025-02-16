"""Flags for Linux 5.10+.

See Also
--------
* https://docs.rs/crate/libc/latest
"""

from typing import Final


__all__: list[str] = [
    "CLD_CONTINUED",
    "CLD_DUMPED",
    "CLD_EXITED",
    "CLD_KILLED",
    "CLD_STOPPED",
    "CLD_TRAPPED",
    "CLONE_FILES",
    "CLONE_FS",
    "CLONE_NEWCGROUP",
    "CLONE_NEWIPC",
    "CLONE_NEWNET",
    "CLONE_NEWNS",
    "CLONE_NEWPID",
    "CLONE_NEWTIME",
    "CLONE_NEWUSER",
    "CLONE_NEWUTS",
    "CLONE_SIGHAND",
    "CLONE_SYSVSEM",
    "CLONE_THREAD",
    "CLONE_VM",
    "EFD_CLOEXEC",
    "EFD_NONBLOCK",
    "EFD_SEMAPHORE",
    "F_LOCK",
    "F_OK",
    "F_TEST",
    "F_TLOCK",
    "F_ULOCK",
    "GRND_NONBLOCK",
    "GRND_RANDOM",
    "MFD_ALLOW_SEALING",
    "MFD_CLOEXEC",
    "MFD_HUGETLB",
    "MFD_HUGE_1GB",
    "MFD_HUGE_1MB",
    "MFD_HUGE_2GB",
    "MFD_HUGE_2MB",
    "MFD_HUGE_8MB",
    "MFD_HUGE_16GB",
    "MFD_HUGE_16MB",
    "MFD_HUGE_32MB",
    "MFD_HUGE_64KB",
    "MFD_HUGE_256MB",
    "MFD_HUGE_512KB",
    "MFD_HUGE_512MB",
    "MFD_HUGE_MASK",
    "MFD_HUGE_SHIFT",
    "O_APPEND",
    "O_ASYNC",
    "O_CLOEXEC",
    "O_CREAT",
    "O_DIRECT",
    "O_DIRECTORY",
    "O_DSYNC",
    "O_EXCL",
    "O_NDELAY",
    "O_NOATIME",
    "O_NOCTTY",
    "O_NOFOLLOW",
    "O_NONBLOCK",
    "O_PATH",
    "O_RDONLY",
    "O_RDWR",
    "O_RSYNC",
    "O_SYNC",
    "O_TMPFILE",
    "O_TRUNC",
    "O_WRONLY",
    "PIDFD_NONBLOCK",
    "POSIX_FADV_DONTNEED",
    "POSIX_FADV_NOREUSE",
    "POSIX_FADV_NORMAL",
    "POSIX_FADV_RANDOM",
    "POSIX_FADV_SEQUENTIAL",
    "POSIX_FADV_WILLNEED",
    "PRIO_PGRP",
    "PRIO_PROCESS",
    "PRIO_USER",
    "P_ALL",
    "P_PGID",
    "P_PID",
    "P_PIDFD",
    "RTLD_DEEPBIND",
    "RTLD_GLOBAL",
    "RTLD_LAZY",
    "RTLD_LOCAL",
    "RTLD_NODELETE",
    "RTLD_NOLOAD",
    "RTLD_NOW",
    "RWF_APPEND",
    "RWF_DSYNC",
    "RWF_HIPRI",
    "RWF_NOWAIT",
    "RWF_SYNC",
    "R_OK",
    "SCHED_BATCH",
    "SCHED_FIFO",
    "SCHED_IDLE",
    "SCHED_OTHER",
    "SCHED_RESET_ON_FORK",
    "SCHED_RR",
    "SEEK_CUR",
    "SEEK_DATA",
    "SEEK_END",
    "SEEK_HOLE",
    "SEEK_SET",
    "SPLICE_F_MORE",
    "SPLICE_F_MOVE",
    "SPLICE_F_NONBLOCK",
    "TFD_CLOEXEC",
    "TFD_NONBLOCK",
    "TFD_TIMER_ABSTIME",
    "TFD_TIMER_CANCEL_ON_SET",
    "WCONTINUED",
    "WEXITED",
    "WNOHANG",
    "WNOWAIT",
    "WSTOPPED",
    "WUNTRACED",
    "W_OK",
    "XATTR_CREATE",
    "XATTR_REPLACE",
    "X_OK",
]

PRIO_PROCESS: Final[int] = 0
PRIO_PGRP: Final[int] = 1
PRIO_USER: Final[int] = 2

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

F_LOCK: Final[int] = 1
F_TLOCK: Final[int] = 2
F_ULOCK: Final[int] = 0
F_TEST: Final[int] = 3

SEEK_SET: Final[int] = 0
SEEK_CUR: Final[int] = 1
SEEK_END: Final[int] = 2

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

F_OK: Final[int] = 0
R_OK: Final[int] = 4
W_OK: Final[int] = 2
X_OK: Final[int] = 1

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

TFD_NONBLOCK: Final[int] = O_NONBLOCK
TFD_CLOEXEC: Final[int] = O_CLOEXEC

TFD_TIMER_ABSTIME: Final[int] = 1
TFD_TIMER_CANCEL_ON_SET: Final[int] = 2

XATTR_CREATE: Final[int] = 0x1
XATTR_REPLACE: Final[int] = 0x2

PIDFD_NONBLOCK: Final[int] = O_NONBLOCK

P_PID: Final[int] = 1
P_PGID: Final[int] = 2
P_ALL: Final[int] = 0
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
