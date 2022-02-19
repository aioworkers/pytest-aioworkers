async def test_make_coro(make_coro):
    coro = make_coro(1)
    assert 1 == await coro()
