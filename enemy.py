import pygame
import random

class Enemy:
    def __init__(self, x, y, speed):
        self.rect = pygame.Rect(x,y, 30, 30)
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, (18, 128, 91), self.rect)

    def respawn(self):
        self.rect.x = 769
        self.rect.y = random.randint(1, 600 - 30)
        self.speed = random.randint(3, 15)
        