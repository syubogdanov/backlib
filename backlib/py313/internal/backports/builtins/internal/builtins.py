import builtins

from backlib.py313.internal.backports.builtins.internal import warnings
from backlib.py313.internal.utils import alias


EncodingWarning: type[Warning] = alias.or_default(
    builtins,
    "EncodingWarning",
    otherwise=warnings.EncodingWarning,
)
