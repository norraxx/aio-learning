import asyncio

import pytest

from config import HOST, PORT

__all__ = ('server',)


async def pong(reader: asyncio.streams.StreamReader, writer: asyncio.streams.StreamWriter):
    """
    This function will return anything, that has been send on server.
    """
    writer.write("wtf".encode())
    await writer.drain()
    writer.close()


@pytest.fixture
async def server(event_loop):
    server = await asyncio.start_server(pong, host=HOST, port=PORT, loop=event_loop)

    async with server:
        await server.serve_forever()
        yield server
        await asyncio.sleep(.1, event_loop)

