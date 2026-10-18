import pygame
import random

class Bonus:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(30, 770), random.randint(30, 570), 30, 30)

    def spawn(self):
        self.rect.x = random.randint(30, 770)
        self.rect.y = random.randint(30, 570)

    def despawn(self):
        self.rect.x = 1200
    def draw(self, surface):
        pygame.draw.rect(surface , (0, 255, 26), self.rect)