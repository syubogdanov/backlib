from __future__ import annotations

import os as py_os

from backlib.internal.utils import alias
from backlib.internal.utils.platform import is_nt


__all__: list[str] = ["environ", "environb", "supports_bytes_environ"]


supports_bytes_environ = not is_nt()

environ = alias.to(py_os.environ)
environb: dict[bytes, bytes] = alias.or_default(py_os, "environb", {})
