import pytest


@pytest.fixture
def aioworkers(aioworkers):
    aioworkers.plugins.default = True
    aioworkers.plugins.append("pytest")
    return aioworkers


def test_context(context):
    assert context
