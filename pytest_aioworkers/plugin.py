import asyncio
from unittest import mock

import pytest

from . import AioWorkers, Groups, Plugins
from .utils import yaml_load_all


@pytest.fixture
def groups() -> Groups:
    return Groups(set(), set())


@pytest.fixture
def aioworkers(groups) -> AioWorkers:
    return AioWorkers(Plugins(), groups)


@pytest.fixture
def config_yaml() -> str:
    return ""


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
async def context(aioworkers, config):
    from aioworkers.core.context import Context, GroupResolver

    gr = GroupResolver(
        include=aioworkers.groups.include,
        exclude=aioworkers.groups.exclude,
    )
    async with Context(
        config,
        group_resolver=gr,
        loop=asyncio.get_running_loop(),
        sent_start=False,
    ) as ctx:
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
