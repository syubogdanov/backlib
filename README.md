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

#### errno

For more, see the [documentation][docs/errno].

```python
from backlib.py313 import errno

assert errno.ENOTCAPABLE == 93
```

#### json

For more, see the [documentation][docs/json].

```python
from backlib.py313 import json

data = json.loads("{\"backlib\": \"pypi\"}")

assert data == {"backlib": "pypi"}
```

#### stat

For more, see the [documentation][docs/stat].

```python
from backlib.py313 import stat

assert stat.SF_SYNTHETIC == 0xC0000000
```

#### tomllib

For more, see the [documentation][docs/tomllib].

```python
from backlib.py313 import tomllib

data = tomllib.loads("\"backlib\" = \"pypi\"")

assert data == {"backlib": "pypi"}
```

## License

MIT License, Copyright (c) 2025 Sergei Y. Bogdanov. See [LICENSE][github/license] file.

<!-- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- -->

[docs/errno]: https://backlib.readthedocs.io/en/latest/backports/python313/errno.html
[docs/json]: https://backlib.readthedocs.io/en/latest/backports/python313/json.html
[docs/stat]: https://backlib.readthedocs.io/en/latest/backports/python313/stat.html
[docs/tomllib]: https://backlib.readthedocs.io/en/latest/backports/python313/tomllib.html

[github/license]: https://github.com/syubogdanov/backlib/tree/main/LICENSE

[pypi/homepage]: https://pypi.org/project/backlib/

[shields/pypi/downloads]: https://img.shields.io/pypi/dm/backlib.svg?color=green
[shields/pypi/license]: https://img.shields.io/pypi/l/backlib.svg?color=green
[shields/pypi/version]: https://img.shields.io/pypi/v/backlib.svg?color=green
[shields/python/version]: https://img.shields.io/pypi/pyversions/backlib.svg?color=green
