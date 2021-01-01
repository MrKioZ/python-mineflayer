class Bot():

    def __init__(self, data):
        self.username = data.get('username')
        self._password = data.get('password')
        self.address = str(data.get('address'))
        self.port = int(data.get('port'))

    def event_listener(self, *args, **kwargs): 
        def inner(func):
            events[func.__name__] = func
            return func
        return inner