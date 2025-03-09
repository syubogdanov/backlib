# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2021 Taneli Hukkinen
# Licensed to PSF under a Contributor Agreement.

__all__: list[str] = ["TOMLDecodeError", "load", "loads"]

from backlib.py313.internal.backports.tomllib.internal.cpython.parser import (
    TOMLDecodeError,
    load,
    loads,
)


# Pretend this exception was created here.
TOMLDecodeError.__module__ = __name__
