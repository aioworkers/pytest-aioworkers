import pytest

from aioworkers.core.config import Config
from aioworkers.core.context import Context


@pytest.fixture
def config_yaml():
    return ''


@pytest.fixture
def config(config_yaml):
    c = Config()
    if config_yaml:
        import yaml
        loader = getattr(yaml, 'CLoader', yaml.Loader)
        c.update(yaml.load(config_yaml, loader))
    return c


@pytest.fixture
def context(loop, config):
    with Context(config, loop=loop) as ctx:
        yield ctx
