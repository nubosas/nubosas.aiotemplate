from unittest.mock import AsyncMock, MagicMock

import pytest


@pytest.fixture
def pg_mocking(mocker, bt_credit_card_create_mock):

    query_proxy = MagicMock()
    query_proxy.get = MagicMock(return_value=bt_credit_card_create_mock['token'])
    proxy_found = AsyncMock()
    proxy_found.fetchone = AsyncMock(return_value=query_proxy)
    conn_found = AsyncMock()
    conn_found.execute = AsyncMock(return_value=proxy_found)

    proxy_not_found = AsyncMock()
    proxy_not_found.fetchone = AsyncMock(return_value=None)
    conn_not_found = AsyncMock()
    conn_not_found.execute = AsyncMock(return_value=proxy_not_found)

    proxy_insert = AsyncMock()
    conn_not_found_and_created = AsyncMock()
    conn_not_found_and_created.execute = AsyncMock(side_effect=[proxy_not_found, proxy_insert, proxy_found])

    engine_mock = AsyncMock()
    engine_mock.acquire = AsyncMock(return_value=conn_found)
    mocker.patch('aiopg.sa.create_engine', engine_mock)

    return {
        'mocker': mocker,
        'conn_found': conn_found,
        'conn_not_found': conn_not_found,
        'conn_not_found_and_created': conn_not_found_and_created,
    }
