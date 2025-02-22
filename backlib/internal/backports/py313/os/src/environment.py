from __future__ import annotations

import os as py_os

from backlib.internal.utils import alias
from backlib.internal.utils.platform import is_nt, is_posix


__all__: list[str] = ["environ", "environb", "supports_bytes_environ"]


if not is_nt() and not is_posix():
    detail = "no os specific module found"
    raise ImportError(detail)


supports_bytes_environ = not is_nt()

environ = alias.to(py_os.environ)
environb: dict[bytes, bytes] = alias.or_default(py_os, "environb", {})
