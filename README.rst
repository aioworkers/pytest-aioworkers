=================
pytest-aioworkers
=================

.. image:: https://img.shields.io/pypi/v/pytest-aioworkers.svg
  :target: https://pypi.org/project/pytest-aioworkers

.. image:: https://github.com/aioworkers/pytest-aioworkers/workflows/Tests/badge.svg
  :target: https://github.com/aioworkers/pytest-aioworkers/actions?query=workflow%3ATests

.. image:: https://codecov.io/gh/aioworkers/pytest-aioworkers/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/aioworkers/pytest-aioworkers
  :alt: Coverage

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v0.json
  :target: https://github.com/charliermarsh/ruff
  :alt: Code style: ruff

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
  :target: https://github.com/psf/black
  :alt: Code style: black

.. image:: https://img.shields.io/badge/types-Mypy-blue.svg
  :target: https://github.com/python/mypy
  :alt: Code style: Mypy

.. image:: https://readthedocs.org/projects/pytest-aioworkers/badge/?version=latest
  :target: https://pytest-aioworkers.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

.. image:: https://img.shields.io/pypi/pyversions/pytest-aioworkers.svg
  :target: https://pypi.org/project/pytest-aioworkers
  :alt: Python versions

.. image:: https://img.shields.io/pypi/dm/pytest-aioworkers.svg
  :target: https://pypi.org/project/pytest-aioworkers

.. image:: https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg
  :alt: Hatch project
  :target: https://github.com/pypa/hatch

A plugin to test aioworkers projects with pytest



Features
--------

* fixtures: aioworkers, context, config_yaml


Requirements
------------

* pytest
* aioworkers


Installation
------------

You can install "pytest-aioworkers" via `pip`_ from `PyPI`_::

    $ pip install pytest-aioworkers[asyncio]


Contributing
------------
Contributions are very welcome. Tests can be run with `hatch`_, please ensure
the coverage at least stays the same before you submit a pull request.

Check code:

.. code-block:: shell

    hatch run lint:all


Format code:

.. code-block:: shell

    hatch run lint:fmt


Run tests:

.. code-block:: shell

    hatch run pytest


Run tests with coverage:

.. code-block:: shell

    hatch run cov

License
-------

Distributed under the terms of the `Apache Software License 2.0`_ license, "pytest-aioworkers" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`file an issue`: https://github.com/aioworkers/pytest-aioworkers/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`hatch`: https://hatch.pypa.io/latest/environment/#scripts
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
