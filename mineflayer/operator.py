import asyncio, signal, websockets, json
from events import events

class Operator(object):

    def __init__(self, host, port):
        self.host, self.port = host, port
        self.loop = asyncio.get_event_loop()

        self.stop = self.loop.create_future()
        self.loop.add_signal_handler(signal.SIGINT, self.stop.set_result, None)

        self.loop.run_until_complete(self.server())

    async def server(self):
        async with websockets.serve(self.ws_handler, self.host, self.port):
            await self.stop

    async def ws_handler(self, websocket, path):
        while True:
            try:
                name = await websocket.recv()
            except websockets.ConnectionClosed:
                print(f"Terminated")
                break

            print(f"< {name}")
            greeting = f"Hello {name}!"

            await websocket.send(greeting)
            print(f"> {greeting}")

if __name__ == '__main__':
    server = Operator(host='localhost', port=6789)