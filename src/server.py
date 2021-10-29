import asyncio

from config import PORT, HOST


async def pong(reader: asyncio.streams.StreamReader, writer: asyncio.streams.StreamWriter):
    data = await reader.readline()
    message = data.decode()

    address = writer.get_extra_info('peername')

    print(f"Received {message!r} from {address!r}")
    print(f"Send: {message!r}")

    writer.write(message.encode())
    await writer.drain()

    writer.close()


async def main():
    server = await asyncio.start_server(pong, host=HOST, port=PORT)
    async with server:
        await server.serve_forever()
        yield server


asyncio.run(main())
