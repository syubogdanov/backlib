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

with io.open_code("backlib.py") as file:
    data = file.read()
```

#### json

```python
from backlib.py313 import json

with open("./backlib.json", mode="w") as file:
    json.dump(["backlib"], file)
```

#### os [SOON]

```python
from backlib.py313 import os

if not os.access("backlib.txt", os.R_OK):
    detail = "Something went wrong..."
    raise RuntimeError(detail)
```

#### pathlib [SOON]

```python
from backlib.py313 import pathlib

if not pathlib.Path("./backlib.txt").exists():
    detail = "Something went wrong..."
    raise RuntimeError(detail)
```

#### shutil [SOON]

```python
from backlib.py313 import shutil

shutil.rmtree("/tmp/backlib/")
```

#### tarfile [SOON]

```python
from backlib.py313 import tarfile

if not tarfile.is_tarfile("./backlib.tar.gz"):
    detail = "Something went wrong..."
    raise RuntimeError(detail)
```

#### tomllib

```python
from backlib.py313 import tomllib

with open("./backlib.toml", mode="rb") as file:
    data = tomllib.load(file)
```

#### zipfile [SOON]

```python
from backlib.py313 import zipfile

if not zipfile.is_zipfile("./backlib.zip"):
    detail = "Something went wrong..."
    raise RuntimeError(detail)
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
