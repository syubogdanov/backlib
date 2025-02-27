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

errno
^^^^^

For more, see the `documentation <https://youtu.be/dQw4w9WgXcQ>`__.

.. code:: python

   from backlib.py313 import errno

   assert errno.ENOTCAPABLE == 93

io
^^

For more, see the `documentation <https://youtu.be/dQw4w9WgXcQ>`__.

.. code:: python

   from backlib.py313 import io

   encoding = io.text_encoding(None)

   assert encoding == "utf-8"

json
^^^^

For more, see the `documentation <https://youtu.be/dQw4w9WgXcQ>`__.

.. code:: python

   from backlib.py313 import json

   data = json.loads("{\"backlib\": \"pypi\"}")

   assert data == {"backlib": "pypi"}

ntpath
^^^^^^

For more, see the `documentation <https://youtu.be/dQw4w9WgXcQ>`__.

.. code:: python

   from backlib.py313 import ntpath

   is_reserved = ntpath.isreserved("./backlib")

   assert not is_reserved

os
^^

For more, see the `documentation <https://youtu.be/dQw4w9WgXcQ>`__.

.. code:: python

   from backlib.py313 import os

   st = os.stat("./pyproject.toml")

   assert st.st_birthtime_ns > 0

os.path
^^^^^^^

For more, see the `documentation <https://youtu.be/dQw4w9WgXcQ>`__.

.. code:: python

   from backlib.py313 import os

   is_reserved = os.path.isreserved("./backlib")

   assert not is_reserved

pathlib
^^^^^^^

For more, see the `documentation <https://youtu.be/dQw4w9WgXcQ>`__.

.. code:: python

   from backlib.py313 import pathlib

   path = pathlib.Path("./backlib")

   if not path.exists():
       path.mkdir(exist_ok=True)

posixpath
^^^^^^^^^

For more, see the `documentation <https://youtu.be/dQw4w9WgXcQ>`__.

.. code:: python

   from backlib.py313 import posixpath

   is_reserved = posixpath.isreserved("./backlib")

   assert not is_reserved

shutil
^^^^^^

For more, see the `documentation <https://youtu.be/dQw4w9WgXcQ>`__.

.. code:: python

   from backlib.py313 import shutil

   source = "./0.0.0/backlib.py"
   target = "./0.1.0/backlib.py"

   shutil.copy(source, target) 

stat
^^^^

For more, see the `documentation <https://youtu.be/dQw4w9WgXcQ>`__.

.. code:: python

   from backlib.py313 import stat

   assert stat.SF_SYNTHETIC == 0xC0000000

tarfile
^^^^^^^

For more, see the `documentation <https://youtu.be/dQw4w9WgXcQ>`__.

.. code:: python

   from backlib.py313 import tarfile

   if not tarfile.is_tarfile("./backlib.tar.gz"):
       detail = "Visit the documentation!"
       raise RuntimeError(detail)

tomllib
^^^^^^^

For more, see the `documentation <https://youtu.be/dQw4w9WgXcQ>`__.

.. code:: python

   from backlib.py313 import tomllib

   data = tomllib.loads("\"backlib\" = \"pypi\"")

   assert data == {"backlib": "pypi"}

zipfile
^^^^^^^

For more, see the `documentation <https://youtu.be/dQw4w9WgXcQ>`__.

.. code:: python

   from backlib.py313 import zipfile

   if not zipfile.is_zipfile("./backlib.zip"):
       detail = "Visit the documentation!"
       raise RuntimeError(detail)

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
