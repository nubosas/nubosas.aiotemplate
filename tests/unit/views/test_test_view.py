

async def test_test_get(aiohttp_client, pg_mocking):
    """Validates the testing top level GET."""

    from nubosas.aiotemplate.main import app

    client = await aiohttp_client(app())

    resp = await client.get('/')

    assert resp.status == 200
