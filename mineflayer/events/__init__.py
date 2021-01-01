events = {}

def event_listener(*args, **kwargs): 
    def inner(func):
        events[func.__name__] = func
        return func
    return inner