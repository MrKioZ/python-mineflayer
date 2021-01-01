from entity import Entity

class Player(Entity):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = kwargs['username']

    def __str__(self):
        return self.username