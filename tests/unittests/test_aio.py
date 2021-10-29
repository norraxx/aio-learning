import pytest


@pytest.mark.asyncio
@pytest.mark.timeout(0.5)
async def test_server(client, server):
    """
    Test TCP komunikace mezi klientem a serverem.
    """
    client_read, client_write = client

