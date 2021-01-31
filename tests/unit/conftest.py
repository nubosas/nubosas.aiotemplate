from unittest.mock import AsyncMock, MagicMock

import pytest


@pytest.fixture
def pg_mocking(mocker):

    query_proxy = MagicMock()
    query_proxy.get = MagicMock(return_value=[])
    proxy_found = AsyncMock()
    proxy_found.fetchall = AsyncMock(return_value=query_proxy)

    conn_found = AsyncMock()
    conn_found.execute = AsyncMock(return_value=proxy_found)

    engine_mock = AsyncMock()
    engine_mock.acquire = AsyncMock(return_value=conn_found)
    mocker.patch('aiopg.sa.create_engine', engine_mock)

    return {
        'mocker': mocker,
    }
