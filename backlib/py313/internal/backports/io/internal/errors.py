class UnsupportedOperation(OSError, ValueError):  # noqa: N818
    """Raised when an unsupported operation is called on a stream.

    See Also
    --------
    * `io.UnsupportedOperation`.

    Version
    -------
    * Python 3.13.
    """
