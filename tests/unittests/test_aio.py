import pytest


@pytest.mark.asyncio
async def test_1(sleep):
    await sleep(1)
