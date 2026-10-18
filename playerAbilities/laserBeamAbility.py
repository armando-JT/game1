import pygame
from playerAbility import PlayerAbility
from player import Player

class LaserBeamAbility(PlayerAbility):
    def __init__(self, player : Player, duration=0,):
        super().__init__(500)
        self.laser = pygame.Rect(player.rect.x , player.rect.y , 900 , player.rect.height + 10)

    def on_start(self, player : Player):
        self.laser.x = player.rect.x
        self.laser.y = player.rect.y
        self.laser.h = player.rect.height + 10
        self.active = True
        

    def on_update(self, player : Player):

        if self.laser.h > 0:
            self.laser.h = self.laser.h - 10
            self.laser.y += 4

    def on_end(self, player : Player):
        
        self.active = False
        
    
    