from collections import namedtuple
from typing import Dict, Iterable
from unittest import mock

import pytest


try:
    import yaml
except ImportError:
    _yaml_loader = None
else:
    _yaml_loader = getattr(yaml, 'CLoader', yaml.Loader)


def _yaml_import_error(s: str) -> Iterable[Dict]:
    import yaml  # noqa
    return yaml_load_all(s)


def _yaml_load_all(s: str) -> Iterable[Dict]:
    yield from yaml.load_all(s, Loader=_yaml_loader)


if _yaml_loader is None:
    yaml_load_all = _yaml_import_error
else:
    yaml_load_all = _yaml_load_all


AioWorkers = namedtuple('AioWorkers', 'plugins groups')
Groups = namedtuple('Groups', 'include exclude')


class Plugins(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.default = False


@pytest.fixture
def groups():
    return Groups(set(), set())


@pytest.fixture
def aioworkers(groups):
    return AioWorkers(Plugins(), groups)


@pytest.fixture
def config_yaml():
    return ''


@pytest.fixture
def config(aioworkers, config_yaml):
    from aioworkers.core.config import Config

    c = Config()
    if aioworkers.plugins.default:
        c.load_plugins()
    if aioworkers.plugins:
        c.load_plugins(*aioworkers.plugins)
    for data in yaml_load_all(config_yaml):
        c.update(data)
    return c


@pytest.fixture
def context(loop, groups, config):
    from aioworkers.core.context import Context
    from aioworkers.core.context import GroupResolver

    gr = GroupResolver(
        include=groups.include,
        exclude=groups.exclude,
    )
    with Context(config, group_resolver=gr, loop=loop) as ctx:
        yield ctx


@pytest.fixture
def make_coro():
    def make_coro(result=None, exception=None):
        async def coro(*args, **kwargs):
            if exception is not None:
                raise exception
            return result
        return mock.Mock(wraps=coro)
    return make_coro
