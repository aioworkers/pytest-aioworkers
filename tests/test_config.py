import pytest


@pytest.fixture
def config_yaml(config_yaml):
    return config_yaml + """---
    s: 2
    """


def test_cfg1(config):
    assert config.s == 2
