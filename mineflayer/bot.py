from co_operator import Operator
from subprocess import Popen
import json, random

class Bot():

    def __init__(self, username, password=None, host=None, port=None, operator_address=None, operator_port=None):
        
        self.username = username
        self._password = password
        self.host = host
        self.port = int(port)

        self.events_listener = {}

        self.operator_address = '127.0.0.1'        
        self.operator_port = int(''.join([str(random.randint(1,6)), str(random.randint(1,5)), str(random.randint(1,5)), str(random.randint(1,3)), str(random.randint(1,5))]))

        self.operator = Operator(self.operator_address, self.operator_port)


        data = {
            "username": self.username,
            "host": self.host,
            "port": self.port
        }

        if self._password:
            data.update({
                "password": self.password
            })        
        p = Popen(['js_end/IPC.js', json.dumps(data)])

    # async def start(self):

    def event_listener(self, *args, **kwargs): 
        def inner(func):
            self.events_listener[func.__name__] = func
            return func
        return inner

if __name__ == "__main__":
    bot = Bot(**{
        "username": 'pablo',
        "host": '127.0.0.1',
        "port": '51458'
    })
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(bot.start())