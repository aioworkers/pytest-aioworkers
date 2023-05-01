import pytest


async def test_make_coro(make_coro):
    coro = make_coro(1)
    assert 1 == await coro()


async def test_make_coro_exc(make_coro):
    coro = make_coro(1, exception=KeyError("a"))
    with pytest.raises(KeyError):
        assert 1 == await coro()
