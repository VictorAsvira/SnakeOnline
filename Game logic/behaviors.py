import components

class KillBehavior:
    def __call__(self, target):
        live_component = target.get_component(components.Live)
        if live_component:
            live_component.kill()

class AddBlockBehavior:
    def __init__(self, block_factory=None):
        self.block_factory = block_factory or components.SnakeBody

    def __call__(self, target, owner=None, direction=None):
        body = target.get_component(components.Body)
        pos = target.get_component(components.Position)
        live = target.get_component(components.Live)

        if not body or not pos or not live or not live.is_alive():
            return

        if body.blocks:
            last_block = body.blocks[-1]
            last_pos = last_block.get_component(components.Position)
            direction_component = last_block.get_component(components.Direction)
            dx, dy = direction_component.get_vector()
            x, y = last_pos.get_position()
            x -= dx
            y -= dy

        else:
            x, y = pos.get_position()

        new_block = self.block_factory(x, y, owner = owner, direction=direction.direction)
        body.blocks.append(new_block)
