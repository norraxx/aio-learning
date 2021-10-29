import asyncio

import pytest

__all__ = ('sleep',)


@pytest.fixture
def sleep(event_loop):
    return asyncio.sleep
