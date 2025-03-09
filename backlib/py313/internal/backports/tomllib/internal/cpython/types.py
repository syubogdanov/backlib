# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2021 Taneli Hukkinen
# Licensed to PSF under a Contributor Agreement.

from __future__ import annotations

from typing import Any, Callable


# Type annotations
ParseFloat = Callable[[str], Any]
Key = tuple[str, ...]
Pos = int
