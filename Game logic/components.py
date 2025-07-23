class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y


class Event:
    def __init__(self, event_class=None):
        self.event_class = event_class

    def event(self, target_object):
        if self.event_class:
            self.event_class(target_object)


class Image:
    def __init__(self, image: str):
        self.image = image


class Direction:
    GLOBAL_DIRECTIONS = {
        "UP": (0, -1),
        "DOWN": (0, 1),
        "LEFT": (-1, 0),
        "RIGHT": (1, 0)
    }

    def __init__(self, direction: str):
        self.directions = self.GLOBAL_DIRECTIONS.copy()

        if direction not in self.directions:
            raise ValueError(f"Unknown direction: {direction}")
        
        self.direction = direction
        self.dx, self.dy = self.directions[direction]

    def set_direction(self, direction: str):
        if direction not in self.directions:
            raise ValueError(f"Unknown direction: {direction}")
        
        self.direction = direction
        self.dx, self.dy = self.directions[direction]

    def add_direction(self, name: str, dx: int, dy: int):
        if name in self.directions:
            raise ValueError(f"Direction already exists: {name}")
        
        self.directions[name] = (dx, dy)

    def get_vector(self):
        return self.dx, self.dy

class Live:
    def __init__(self, live: bool = True, owner=None):
        self.owner = owner
        self.live = live

    def is_alive(self):
        return self.live

    def kill(self):
        self.live = False

        
class Body:
    def __init__(self, length: int):
        self.length = length
        self.blocks = []