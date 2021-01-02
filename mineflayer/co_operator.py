import asyncio, signal, websockets, json, signal
from events import events
import threading

class GracefulExit(SystemExit):
    code = 1

def raise_graceful_exit(*args):
    loop.stop()
    print("Gracefully shutdown")
    raise GracefulExit()

class Operator:

    port = None
    host = None

    def __init__(self, host, port):
        if (not self.host) and (not self.port):
            self.host, self.port = host, port
            self.loop = asyncio.get_event_loop()

            self.stop = self.loop.create_future()

            self.server_thread = threading.Thread(target=self.loop.run_until_complete, name='Server', args=(self.server(),))

            try:
                self.server_thread.start()
            except GracefulExit:
                pass
            # finally:
            #     self.loop.close()

        else:
            return None

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