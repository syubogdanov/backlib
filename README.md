# backlib

[![PyPI Version][shields/pypi/version]][pypi/homepage]
[![PyPI Downloads][shields/pypi/downloads]][pypi/homepage]
[![License][shields/pypi/license]][github/license]
[![Python Version][shields/python/version]][pypi/homepage]

> [!WARNING]
> The library is in the pre-alpha stage. Bugs may exist!

## Key Features

* Provides backports for the standard library;
* Compatible with Python 3.9+;
* Almost dependency-free.

## Getting Started

### Installation

The library is available as [`backlib`][pypi/homepage] on PyPI:

```shell
pip install backlib
```

### Usage

#### errno [UNRELEASED]

For more, see the [documentation][docs/errno].

```python
from backlib.py313 import errno

assert errno.ENOTCAPABLE == 93
```

#### io [SOON]

For more, see the [documentation][docs/io].

```python
from backlib.py313 import io

encoding = io.text_encoding(None)

assert encoding == "utf-8"
```

#### json

For more, see the [documentation][docs/json].

```python
from backlib.py313 import json

data = json.loads("{\"backlib\": \"pypi\"}")

assert data == {"backlib": "pypi"}
```

#### ntpath [UNRELEASED]

For more, see the [documentation][docs/ntpath].

```python
from backlib.py313 import ntpath

is_reserved = ntpath.isreserved("./backlib")

assert not is_reserved
```

#### os [UNRELEASED]

For more, see the [documentation][docs/os].

```python
from backlib.py313 import os

st = os.stat("./pyproject.toml")

assert st.st_birthtime_ns > 0
```

#### os.path [UNRELEASED]

For more, see the [documentation][docs/os.path].

```python
from backlib.py313 import os

is_reserved = os.path.isreserved("./backlib")

assert not is_reserved
```

#### pathlib [SOON]

For more, see the [documentation][docs/pathlib].

```python
from backlib.py313 import pathlib

path = pathlib.Path("./backlib")

if not path.exists():
    path.mkdir(exist_ok=True)
```

#### posixpath [UNRELEASED]

For more, see the [documentation][docs/posixpath].

```python
from backlib.py313 import posixpath

is_reserved = posixpath.isreserved("./backlib")

assert not is_reserved
```

#### shutil [SOON]

For more, see the [documentation][docs/shutil].

```python
from backlib.py313 import shutil

source = "./0.0.0/backlib.py"
target = "./0.1.0/backlib.py"

shutil.copy(source, target) 
```

#### stat

For more, see the [documentation][docs/stat].

```python
from backlib.py313 import stat

assert stat.SF_SYNTHETIC == 0xC0000000
```

#### tarfile [SOON]

For more, see the [documentation][docs/tarfile].

```python
from backlib.py313 import tarfile

if not tarfile.is_tarfile("./backlib.tar.gz"):
    detail = "Visit the documentation!"
    raise RuntimeError(detail)
```

#### tomllib

For more, see the [documentation][docs/tomllib].

```python
from backlib.py313 import tomllib

data = tomllib.loads("\"backlib\" = \"pypi\"")

assert data == {"backlib": "pypi"}
```

#### zipfile [SOON]

For more, see the [documentation][docs/zipfile].

```python
from backlib.py313 import zipfile

if not zipfile.is_zipfile("./backlib.zip"):
    detail = "Visit the documentation!"
    raise RuntimeError(detail)
```

## License

MIT License, Copyright (c) 2025 Sergei Y. Bogdanov. See [LICENSE][github/license] file.

<!-- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- -->

[docs/errno]: https://youtu.be/dQw4w9WgXcQ
[docs/io]: https://youtu.be/dQw4w9WgXcQ
[docs/json]: https://youtu.be/dQw4w9WgXcQ
[docs/ntpath]: https://youtu.be/dQw4w9WgXcQ
[docs/os]: https://youtu.be/dQw4w9WgXcQ
[docs/os.path]: https://youtu.be/dQw4w9WgXcQ
[docs/pathlib]: https://youtu.be/dQw4w9WgXcQ
[docs/posixpath]: https://youtu.be/dQw4w9WgXcQ
[docs/shutil]: https://youtu.be/dQw4w9WgXcQ
[docs/stat]: https://youtu.be/dQw4w9WgXcQ
[docs/tarfile]: https://youtu.be/dQw4w9WgXcQ
[docs/tomllib]: https://youtu.be/dQw4w9WgXcQ
[docs/zipfile]: https://youtu.be/dQw4w9WgXcQ

[github/license]: https://github.com/syubogdanov/backlib/tree/main/LICENSE

[pypi/homepage]: https://pypi.org/project/backlib/

[shields/pypi/downloads]: https://img.shields.io/pypi/dm/backlib.svg?color=green
[shields/pypi/license]: https://img.shields.io/pypi/l/backlib.svg?color=green
[shields/pypi/version]: https://img.shields.io/pypi/v/backlib.svg?color=green
[shields/python/version]: https://img.shields.io/pypi/pyversions/backlib.svg?color=green
