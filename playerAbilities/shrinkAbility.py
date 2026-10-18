from playerAbility import PlayerAbility
import pygame

class ShrinkAbility(PlayerAbility):

    def __init__(self):
        super().__init__()

    def on_start(self, player ):
        player.rect.width = 50
        player.rect.height = 50

    def on_end(self, player):
        player.rect.width = 100
        player.rect.height = 100
