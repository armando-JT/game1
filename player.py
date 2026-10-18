import pygame
from playerAbility import PlayerAbility
class Player:
    def __init__(self, x , y, playerSizeX, playerSizeY, speed):
        self.rect = pygame.Rect(x,y, playerSizeX, playerSizeY)
        self.speed = speed
        self.baseSpeed = speed
        self.baseSizeX = playerSizeX
        self.baseSizeY = playerSizeY 
        self.max_hp = 5
        self.hp = self.max_hp
        self.active_abilities = []

    def draw(self, surface):
        pygame.draw.rect(surface, (0,0,0), self.rect)

    def moveLeft(self):
        self.rect.x -= self.speed
    def moveRight(self):
        self.rect.x += self.speed
    def moveUP(self):
        self.rect.y -= self.speed
    def moveDown(self):
        self.rect.y += self.speed



    def activate_ability(self, ability):
        ability.start(self)
        self.active_abilities.append(ability)

    def deactivate_ability(self, ability):
        ability.end(self)
        if ability in self.active_abilities:
            self.active_abilities.remove(ability)


    def update(self):
        for ability in self.active_abilities[:]:
            ability.update(self)
            if not ability.active:
                self.active_abilities.remove(ability)

    def take_damage(self, damage):
        self.hp -= damage

    def heal(self, heal_amount):
        self.hp += heal_amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        

    def respawn(self):
        self.rect.x = 30
        self.rect.y = 600 // 2
        self.speed = 5
        self.hp = self.max_hp