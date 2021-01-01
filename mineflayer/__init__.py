from pprint import pprint
from datetime import datetime
import json, time

loaded_players = {}
actions_table = []

import asyncio
import websockets

async def operator(websocket, path):
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

start_server = websockets.serve(operator, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()