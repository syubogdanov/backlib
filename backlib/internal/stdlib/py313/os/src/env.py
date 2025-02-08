from __future__ import annotations

import os as py_os

from backlib.internal.markers import py_alias, techdebt
from backlib.internal.utils.platform import is_nt


__all__: list[str] = ["environ", "environb", "supports_bytes_environ"]


supports_bytes_environ = not is_nt()

environ = py_alias(py_os.environ)
environb = techdebt(getattr(py_os, "environb", {}))
