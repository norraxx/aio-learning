import asyncio

import pytest

from config import HOST, PORT


__all__ = ('client',)


@pytest.fixture
def client(event_loop):
    return asyncio.open_connection(HOST, PORT, loop=event_loop)
