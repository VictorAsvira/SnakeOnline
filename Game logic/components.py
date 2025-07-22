class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Event:
    def __init__(self, event_class=None):
        self.event_class = event_class

    def event(self, target_object):
        if self.event_class:
            self.event_class(target_object)

class Image:
    def __init__(self, image: str):
        self.image = image 
