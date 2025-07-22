class KillBehavior:
    def __call__(self, target):
        target.live = False

class AddBlokeBehavior:
    def __call__(self, target):
        target.add_bloke()