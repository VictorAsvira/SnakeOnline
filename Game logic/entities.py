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
        self.add_component(components.Event(behaviors.AddBlokeBehavior()))
        

class SnakeBody(Entity):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.add_component(components.Position(x, y))
        self.add_component(components.Image("O"))
        self.add_component(components.Event(behaviors.KillBehavior()))