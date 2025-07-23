import components, behaviors
class Entity:
    def __init__(self):
        self.components = {}

    def add_component(self, component):
        self.components[type(component)] = component

    def get_component(self, component_type):
        return self.components.get(component_type)
    
class Wall(Entity):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.add_component(components.Position(x, y))
        self.add_component(components.Image("#"))
        self.add_component(components.Event(behaviors.KillBehavior()))

class Apple(Entity):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.add_component(components.Position(x, y))
        self.add_component(components.Image("*"))
        self.add_component(components.Event(behaviors.AddBlockBehavior()))
        self.add_component(components.Live(owner=self))

class Field(Entity):
    def __init__(self):
        super().__init__()
        self.add_component(components.Image(" "))
        self.entities = []

class SnakeBody(Entity):
    def __init__(self, x: int, y: int, direction: str = "UP", owner=None):
        super().__init__()
        self.add_component(components.Position(x, y))
        self.add_component(components.Image("O"))
        self.add_component(components.Event(behaviors.KillBehavior()))
        self.add_component(components.Direction(direction))
        self.add_component(components.Live(owner = owner))

class Player(Entity):
    def __init__(self, x: int, y: int, length: int = 3, starting_direction: str = "UP"):
        super().__init__()
        self.add_component(components.Position(x, y))
        self.add_component(components.Body(length))
        self.add_component(components.Direction(starting_direction))
        self.add_component(components.Live(self))

    def spawn_body(self):
        body = self.get_component(components.Body)
        if body:
            for i in range(body.length):
                addBlock = behaviors.AddBlockBehavior()
                direction = self.get_component(components.Direction)
                addBlock(self, owner=self, direction=direction)

    


                