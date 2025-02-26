from typing import Final

from backlib.py313.internal.utils.platform import is_darwin


supports_unicode_filenames: Final[bool] = is_darwin()
