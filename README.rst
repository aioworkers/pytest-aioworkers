=================
pytest-aioworkers
=================

.. image:: https://github.com/aioworkers/pytest-aioworkers/workflows/Tests/badge.svg
  :target: https://github.com/aioworkers/pytest-aioworkers/actions?query=workflow%3ATests

.. image:: https://codecov.io/gh/aioworkers/pytest-aioworkers/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/aioworkers/pytest-aioworkers

.. image:: https://img.shields.io/pypi/v/pytest-aioworkers.svg
  :target: https://pypi.org/project/pytest-aioworkers
  :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-aioworkers.svg
  :target: https://pypi.org/project/pytest-aioworkers
  :alt: Python versions

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

To run tests::

    hatch run pytest

or::

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
