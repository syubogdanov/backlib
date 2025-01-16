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

#### io [SOON]

```python
from backlib.py313 import io

...
```

#### json

```python
from backlib.py313 import json

data = json.loads("{\"backlib\": \"pypi\"}")

assert data == {"backlib": "pypi"}
```

#### ntpath [SOON]

```python
from backlib.py313 import ntpath

...
```

#### os [SOON]

```python
from backlib.py313 import os

...
```

#### os.path [SOON]

```python
from backlib.py313 import ospath

...
```

#### pathlib [SOON]

```python
from backlib.py313 import pathlib

...
```

#### posixpath [SOON]

```python
from backlib.py313 import posixpath

...
```

#### shutil [SOON]

```python
from backlib.py313 import shutil

...
```

#### stat

```python
from backlib.py313 import stat

...
```

#### tarfile [SOON]

```python
from backlib.py313 import tarfile

...
```

#### tomllib

```python
from backlib.py313 import tomllib

data = tomllib.loads("\"backlib\" = \"pypi\"")

assert data == {"backlib": "pypi"}
```

#### zipfile [SOON]

```python
from backlib.py313 import zipfile

...
```

## Documentation

The `backlib` API is the same as the standard library, so you can refer to the official documentation:

* [Python 3.13][docs/3.13]

## License

MIT License, Copyright (c) 2025 Sergei Bogdanov. See [LICENSE][github/license] file.

<!-- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- -->

[docs/3.13]: https://docs.python.org/3.13/library/index.html

[github/license]: https://github.com/syubogdanov/backlib/tree/main/LICENSE

[pypi/homepage]: https://pypi.org/project/backlib/

[shields/pypi/downloads]: https://img.shields.io/pypi/dm/backlib.svg?color=green
[shields/pypi/license]: https://img.shields.io/pypi/l/backlib.svg?color=green
[shields/pypi/version]: https://img.shields.io/pypi/v/backlib.svg?color=green
[shields/python/version]: https://img.shields.io/pypi/pyversions/backlib.svg?color=green
