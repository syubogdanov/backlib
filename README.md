# backlib

[![PyPI Version][shields/pypi/version]][pypi/homepage]
[![PyPI Downloads][shields/pypi/downloads]][pypi/homepage]
[![License][shields/pypi/license]][github/license]
[![Python Version][shields/python/version]][pypi/homepage]

> [!WARNING]
> The library is in the pre-alpha stage.

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

For more, see the [documentation][github/docs/errno].

```python
from backlib.py313 import errno

assert errno.ENOTCAPABLE == 93
```

#### io [SOON]

For more, see the [documentation][github/docs/io].

```python
from backlib.py313 import io

...
```

#### json

For more, see the [documentation][github/docs/json].

```python
from backlib.py313 import json

data = json.loads("{\"backlib\": \"pypi\"}")

assert data == {"backlib": "pypi"}
```

#### ntpath [UNRELEASED]

For more, see the [documentation][github/docs/ntpath].

```python
from backlib.py313 import ntpath

is_reserved = ntpath.isreserved("./backlib")

assert not is_reserved
```

#### os [SOON]

For more, see the [documentation][github/docs/os].

```python
from backlib.py313 import os

st = os.stat("./pyproject.toml")

assert st.st_birthtime_ns > 0
```

#### os.path [UNRELEASED]

For more, see the [documentation][github/docs/os.path].

```python
from backlib.py313 import ospath

is_reserved = ospath.isreserved("./backlib")

assert not is_reserved
```

#### posixpath [UNRELEASED]

For more, see the [documentation][github/docs/posixpath].

```python
from backlib.py313 import posixpath

is_reserved = posixpath.isreserved("./backlib")

assert not is_reserved
```

#### shutil [SOON]

For more, see the [documentation][github/docs/shutil].

```python
from backlib.py313 import shutil

...
```

#### stat

For more, see the [documentation][github/docs/stat].

```python
from backlib.py313 import stat

assert stat.SF_SYNTHETIC == 0xC0000000
```

#### tarfile [SOON]

For more, see the [documentation][github/docs/tarfile].

```python
from backlib.py313 import tarfile

...
```

#### tomllib

For more, see the [documentation][github/docs/tomllib].

```python
from backlib.py313 import tomllib

data = tomllib.loads("\"backlib\" = \"pypi\"")

assert data == {"backlib": "pypi"}
```

#### zipfile [SOON]

For more, see the [documentation][github/docs/zipfile].

```python
from backlib.py313 import zipfile

...
```

## License

MIT License, Copyright (c) 2025 Sergei Bogdanov. See [LICENSE][github/license] file.

<!-- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- -->

[github/docs/errno]: https://github.com/syubogdanov/backlib/tree/main/docs/py313/errno.md
[github/docs/io]: https://github.com/syubogdanov/backlib/tree/main/docs/py313/io.md
[github/docs/json]: https://github.com/syubogdanov/backlib/tree/main/docs/py313/json.md
[github/docs/ntpath]: https://github.com/syubogdanov/backlib/tree/main/docs/py313/ntpath.md
[github/docs/os]: https://github.com/syubogdanov/backlib/tree/main/docs/py313/os.md
[github/docs/os.path]: https://github.com/syubogdanov/backlib/tree/main/docs/py313/os.path.md
[github/docs/posixpath]: https://github.com/syubogdanov/backlib/tree/main/docs/py313/posixpath.md
[github/docs/shutil]: https://github.com/syubogdanov/backlib/tree/main/docs/py313/shutil.md
[github/docs/stat]: https://github.com/syubogdanov/backlib/tree/main/docs/py313/stat.md
[github/docs/tarfile]: https://github.com/syubogdanov/backlib/tree/main/docs/py313/tarfile.md
[github/docs/tomllib]: https://github.com/syubogdanov/backlib/tree/main/docs/py313/tomllib.md
[github/docs/zipfile]: https://github.com/syubogdanov/backlib/tree/main/docs/py313/zipfile.md
[github/license]: https://github.com/syubogdanov/backlib/tree/main/LICENSE

[pypi/homepage]: https://pypi.org/project/backlib/

[shields/pypi/downloads]: https://img.shields.io/pypi/dm/backlib.svg?color=green
[shields/pypi/license]: https://img.shields.io/pypi/l/backlib.svg?color=green
[shields/pypi/version]: https://img.shields.io/pypi/v/backlib.svg?color=green
[shields/python/version]: https://img.shields.io/pypi/pyversions/backlib.svg?color=green
