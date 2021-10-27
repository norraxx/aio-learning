import asyncio

import pytest


@pytest.fixture
def sleep():
    return asyncio.sleep
