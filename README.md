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
* Dependency-free.

## Getting Started

### Installation

The library is available as [`backlib`][pypi/homepage] on PyPI:

```shell
pip install backlib
```

### Usage

#### builtins [SOON]

For more, see the [documentation][docs/builtins].

```python
from backlib.py313 import builtins

message = "This is a backported warning!"
warn(message, builtins.EncodingWarning, stacklevel=2)
```

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

[docs/builtins]: https://backlib.readthedocs.io/en/latest/backports/python313/builtins.html
[docs/errno]: https://backlib.readthedocs.io/en/latest/backports/python313/errno.html
[docs/io]: https://backlib.readthedocs.io/en/latest/backports/python313/io.html
[docs/json]: https://backlib.readthedocs.io/en/latest/backports/python313/json.html
[docs/os]: https://backlib.readthedocs.io/en/latest/backports/python313/os.html
[docs/os.path]: https://backlib.readthedocs.io/en/latest/backports/python313/os.path.html
[docs/pathlib]: https://backlib.readthedocs.io/en/latest/backports/python313/pathlib.html
[docs/shutil]: https://backlib.readthedocs.io/en/latest/backports/python313/shutil.html
[docs/stat]: https://backlib.readthedocs.io/en/latest/backports/python313/stat.html
[docs/tarfile]: https://backlib.readthedocs.io/en/latest/backports/python313/tarfile.html
[docs/tomllib]: https://backlib.readthedocs.io/en/latest/backports/python313/tomllib.html
[docs/zipfile]: https://backlib.readthedocs.io/en/latest/backports/python313/zipfile.html

[github/license]: https://github.com/syubogdanov/backlib/tree/main/LICENSE

[pypi/homepage]: https://pypi.org/project/backlib/

[shields/pypi/downloads]: https://img.shields.io/pypi/dm/backlib.svg?color=green
[shields/pypi/license]: https://img.shields.io/pypi/l/backlib.svg?color=green
[shields/pypi/version]: https://img.shields.io/pypi/v/backlib.svg?color=green
[shields/python/version]: https://img.shields.io/pypi/pyversions/backlib.svg?color=green
