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

#### builtins

For more, see the [documentation][docs/builtins] (*latest*).

```python
from backlib.py310 import builtins

assert issubclass(builtins.EncodingWarning, Warning)
```

#### errno

For more, see the [documentation][docs/errno] (*latest*).

```python
from backlib.py311 import errno

assert errno.ENOTCAPABLE == 93
```

#### json

For more, see the [documentation][docs/json] (*latest*).

```python
from backlib.py310 import json

data = json.loads("{\"backlib\": \"pypi\"}")

assert data == {"backlib": "pypi"}
```

#### operator

For more, see the [documentation][docs/operator] (*latest*).

```python
from backlib.py311 import operator

value = operator.__call__(abs, -42)

assert value == 42
```

#### os

For more, see the [documentation][docs/os] (*latest*).

```python
from backlib.py312 import os

st = os.stat("pyproject.toml")

assert st.st_birthtime_ns > 0
```

#### stat

For more, see the [documentation][docs/stat] (*latest*).

```python
from backlib.py313 import stat

assert stat.SF_SYNTHETIC == 0xC0000000
```

#### tomllib

For more, see the [documentation][docs/tomllib] (*latest*).

```python
from backlib.py311 import tomllib

data = tomllib.loads("\"backlib\" = \"pypi\"")

assert data == {"backlib": "pypi"}
```

## License

MIT License, Copyright (c) 2025 Sergei Y. Bogdanov. See [LICENSE][github/license] file.

<!-- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- -->

[docs/builtins]: https://backlib.readthedocs.io/en/latest/backports/python313/builtins.html
[docs/errno]: https://backlib.readthedocs.io/en/latest/backports/python313/errno.html
[docs/json]: https://backlib.readthedocs.io/en/latest/backports/python313/json.html
[docs/operator]: https://backlib.readthedocs.io/en/latest/backports/python313/operator.html
[docs/os]: https://backlib.readthedocs.io/en/latest/backports/python313/os.html
[docs/stat]: https://backlib.readthedocs.io/en/latest/backports/python313/stat.html
[docs/tomllib]: https://backlib.readthedocs.io/en/latest/backports/python313/tomllib.html

[github/license]: https://github.com/syubogdanov/backlib/tree/main/LICENSE

[pypi/homepage]: https://pypi.org/project/backlib/

[shields/pypi/downloads]: https://img.shields.io/pypi/dm/backlib.svg?color=green
[shields/pypi/license]: https://img.shields.io/pypi/l/backlib.svg?color=green
[shields/pypi/version]: https://img.shields.io/pypi/v/backlib.svg?color=green
[shields/python/version]: https://img.shields.io/pypi/pyversions/backlib.svg?color=green
