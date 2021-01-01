class Position:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_distance(self, x,y,z):
        pass
        # should get the distance between two coordinates

class Entity:

    def __init__(self, id, type, displayName, position: Position):
        self.displayName = displayName
        self.position = position
        self.type = type
        self.id = id
