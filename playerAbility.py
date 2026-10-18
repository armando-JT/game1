import pygame

class PlayerAbility:

    def __init__(self, duration = 0):
        self.duration = duration
        self.start_time = 0
        self.active = False

    def start(self, player):
        if self.active:
            return
        self.start_time = pygame.time.get_ticks()
        self.active = True
        self.on_start(player)

    def update(self, player):
        if not self.active:
            return

        if self.duration > 0:
            elapsed = pygame.time.get_ticks() - self.start_time
            if elapsed >= self.duration:
                self.end(player)
                return

        self.on_update(player)


    def end(self, player):
        if not self.active:
            return
        self.active = False
        self.on_end(player)

    def on_start(self, player): pass
    def on_update(self, player) : pass
    def on_end(self, player): pass


