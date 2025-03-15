"""Flags for Linux 5.10+.

See Also
--------
* https://docs.rs/libc/latest/libc/
"""

from typing import Final


TFD_CLOEXEC: Final[int] = 0x80000

TFD_NONBLOCK: Final[int] = 2048

TFD_TIMER_ABSTIME: Final[int] = 1
TFD_TIMER_CANCEL_ON_SET: Final[int] = 2
