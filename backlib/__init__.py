import sys as _sys


__author__ = "Sergei Y. Bogdanov <syubogdanov@outlook.com>"
__version__ = "0.1.0-rc"


if not ((3, 8) < _sys.version_info < (3, 14)):
    detail = f"Python {_sys.version_info} is not supported"
    raise NotImplementedError(detail)
