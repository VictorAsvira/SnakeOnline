import entities, components

class World:
    def __init__(self, world_size: tuple = (20, 20)):
        self.fields = {}
        self.entities = []
        self.systems = []
        self.world_size = world_size

    def create_world(self):
        for x in range(self.world_size[0]):
            for y in range(self.world_size[1]):
                self.fields[(x, y)] = entities.Field()

        for y in range(-1,1):
            for x in range(self.world_size[0]):
                self.fields[(x, y)] = entities.Wall(x, y)
            
        for x in range(-1, 1):
            for y in range(self.world_size[1]):
                self.fields[(x, y)] = entities.Wall(x, y)

    def update_world(self):

        for entity in self.entities:
            live_component = entity.get_component(components.Live)
            if live_component:
                if not live_component.is_alive() or live_component.owner is None:
                    self.remove_entity(entity)

        for field in self.fields.values():
            field.entities.clear()
        
        for entity in self.entities:
            pos = entity.get_component(components.Position)
            if pos:
                field_key = (pos.x, pos.y)
                if field_key in self.fields:
                    self.fields[field_key].entities.append(entity)

    def add_entity(self, entity: entities.Entity):
        self.entities.append(entity)
        entity_pos = entity.get_component(components.Position)
        field = self.fields[entity_pos.get_position()]
        field.entities.append(entity)

    def spawn_player(self, x: int, y: int, length: int = 3, starting_direction: str = "UP"):
        player = entities.Player(x, y, length, starting_direction)
        player.spawn_body()
        self.add_entity(player)

        for block in player.get_component(components.Body).blocks:
            self.add_entity(block)

    def remove_entity(self, entity: entities.Entity):
        self.entities.remove(entity)

    def add_system(self, system):
        self.systems.append(system)

    def update(self):
        for system in self.systems:
            if isinstance(system, CollisionSystem):
                system.update(self.fields)
            else:
                system.update(self.entities)
            
        self.update_world()



class MovementSystem:
    def update(self, entities):
        for entity in entities:
            move_direction = entity.get_component(components.Direction)
            pos_entity = entity.get_component(components.Position)
            if move_direction and pos_entity:
                dx, dy = move_direction.get_vector()
                pos_entity.x += dx
                pos_entity.y += dy

class CollisionSystem:
    def update(self, fields):
        for field in fields.values():
            if len(field.entities) > 1:
                for i in range(len(field.entities)):
                    for j in range(i + 1, len(field.entities)):
                        entity_a = field.entities[i]
                        entity_b = field.entities[j]
                        event_a = entity_a.get_component(components.Event)
                        event_b = entity_b.get_component(components.Event)
                        if event_a:
                            event_a.event(entity_b)
                        if event_b:
                            event_b.event(entity_a)
                
class SnakeFollowSystem:
    def update(self, entities):
        for entity in entities:
            body = entity.get_component(components.Body)
            if body:
                for i in range(1, len(body.blocks)):
                    prev_dir = body.blocks[i - 1].get_component(components.Direction)
                    curr_dir = body.blocks[i].get_component(components.Direction)
                    if prev_dir and curr_dir:
                        curr_dir.set_direction(prev_dir.direction)

class InputSystem:
    pass

class RenderSystem:
    def render(self, fields, world_size):
        width, height = world_size
        for y in range(height):
            row = ""
            for x in range(width):
                field = fields.get((x, y))
                if field and field.entities:
                    image = field.entities[0].get_component(components.Image)
                    row += image.image if image else "?"
                else:
                    row += " "
            print(row)
        
            

