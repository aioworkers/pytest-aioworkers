from unittest import mock

import pytest


@pytest.fixture
def config_yaml():
    return ''


@pytest.fixture
def config(config_yaml):
    from aioworkers.core.config import Config

    c = Config()
    if config_yaml:
        import yaml
        loader = getattr(yaml, 'CLoader', yaml.Loader)
        c.update(yaml.load(config_yaml, loader))
    return c


@pytest.fixture
def context(loop, config):
    from aioworkers.core.context import Context

    with Context(config, loop=loop) as ctx:
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
