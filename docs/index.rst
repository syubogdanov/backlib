backlib
=======

|PyPI Version| |PyPI Downloads| |License| |Python Version|

Key Features
------------

-  Provides backports for the standard library;
-  Compatible with Python 3.9+;
-  Almost dependency-free.

Getting Started
---------------

Installation
~~~~~~~~~~~~

The library is available as `backlib <https://pypi.org/project/backlib/>`__ on PyPI:

.. code:: shell

   pip install backlib

Usage
~~~~~

builtins
^^^^^^^^

For more, see the `documentation <https://backlib.readthedocs.io/en/latest/backports/python313/builtins.html>`__ (*latest*).

.. code:: python

   from backlib.py310 import builtins

   assert issubclass(builtins.EncodingWarning, Warning)

errno
^^^^^

For more, see the `documentation <https://backlib.readthedocs.io/en/latest/backports/python313/errno.html>`__ (*latest*).

.. code:: python

   from backlib.py311 import errno

   assert errno.ENOTCAPABLE == 93

json
^^^^

For more, see the `documentation <https://backlib.readthedocs.io/en/latest/backports/python313/json.html>`__ (*latest*).

.. code:: python

   from backlib.py310 import json

   data = json.loads("{\"backlib\": \"pypi\"}")

   assert data == {"backlib": "pypi"}

operator
^^^^^^^^

For more, see the `documentation <https://backlib.readthedocs.io/en/latest/backports/python313/operator.html>`__ (*latest*).

.. code:: python

   from backlib.py311 import operator

   value = operator.__call__(abs, -42)

   assert value == 42

os
^^

For more, see the `documentation <https://backlib.readthedocs.io/en/latest/backports/python313/os.html>`__ (*latest*).

.. code:: python

   from backlib.py312 import os

   st = os.stat("pyproject.toml")

   assert st.st_birthtime_ns > 0

stat
^^^^

For more, see the `documentation <https://backlib.readthedocs.io/en/latest/backports/python313/stat.html>`__ (*latest*).

.. code:: python

   from backlib.py313 import stat

   assert stat.SF_SYNTHETIC == 0xC0000000

tomllib
^^^^^^^

For more, see the `documentation <https://backlib.readthedocs.io/en/latest/backports/python313/tomllib.html>`__ (*latest*).

.. code:: python

   from backlib.py311 import tomllib

   data = tomllib.loads("\"backlib\" = \"pypi\"")

   assert data == {"backlib": "pypi"}

Documentation
-------------

.. toctree::
    :maxdepth: 3

    backports/index

License
-------

MIT License, Copyright (c) 2025 Sergei Y. Bogdanov. See
`LICENSE <https://github.com/syubogdanov/backlib/tree/main/LICENSE>`__
file.


.. |PyPI Version| image:: https://img.shields.io/pypi/v/backlib.svg?color=green
   :target: https://pypi.org/project/backlib/

.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/backlib.svg?color=green
   :target: https://pypi.org/project/backlib/

.. |License| image:: https://img.shields.io/pypi/l/backlib.svg?color=green
   :target: https://github.com/syubogdanov/backlib/tree/main/LICENSE

.. |Python Version| image:: https://img.shields.io/pypi/pyversions/backlib.svg?color=green
   :target: https://pypi.org/project/backlib/
