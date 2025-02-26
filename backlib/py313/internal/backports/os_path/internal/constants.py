from __future__ import annotations

from typing import Final

from backlib.py313.internal.backports.ntpath import (
    supports_unicode_filenames as nt_supports_unicode_filenames,
)
from backlib.py313.internal.backports.posixpath import (
    supports_unicode_filenames as posix_supports_unicode_filenames,
)
from backlib.py313.internal.utils.platform import is_nt, is_posix


if not is_nt() and not is_posix():
    detail = "no os specific module found"
    raise ImportError(detail)


supports_unicode_filenames: Final[bool] = (
    nt_supports_unicode_filenames if is_nt() else posix_supports_unicode_filenames
)
