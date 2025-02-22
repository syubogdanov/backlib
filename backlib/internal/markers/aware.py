from typing import Any


def unused(*_: Any, **__: Any) -> None:  # noqa: ANN401
    """Ignore the unused arguments.

    See Also
    --------
    * `ARG002`.
    """
