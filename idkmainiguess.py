import pygame
import random
from enemy import Enemy
from bonus import Bonus
from player import Player

from playerAbilities.shrinkAbility import ShrinkAbility
from playerAbilities.laserBeamAbility import LaserBeamAbility


def main():


    pygame.init()
    
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 20)
    
    pygame.display.set_caption("unoptimized barely put together piece of garbage")
    
    clock = pygame.time.Clock()
    running = True
    state = "PLAYING"

  

    player : Player = Player(0 , 0, 100, 100, 5)
    
    bonuses : list[Bonus] = []
    
    enemies : list[Enemy] = []
    
    shrAb = ShrinkAbility()
    laserAb = LaserBeamAbility(player)

    

    def start_game():
        enemies.clear()
        bonuses.clear()
        player.respawn()
        

        for _ in range(5):
            new_enemy = Enemy(769 , random.randint(0, 570), random.randint(3,8) )
            enemies.append(new_enemy)
            
        for _ in range(3):
            new_bonus = Bonus()
            bonuses.append(new_bonus)

        

    start_game()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q:
                    player.activate_ability(laserAb)
    
                

                if event.key == pygame.K_r and state == "GAME_OVER":
                    state = "PLAYING"
                    start_game()
    
        if state == "PLAYING":
            
            player.update()
            keys = pygame.key.get_pressed()
        
            if keys[pygame.K_a]:
                player.moveLeft()
            if keys[pygame.K_d]:
                player.moveRight()
            if keys[pygame.K_w]:
                player.moveUP()
            if keys[pygame.K_s]:
                player.moveDown()

            # HOLD ABILITIES
            if keys[pygame.K_SPACE]:

                player.activate_ability(shrAb)
            else:
                player.deactivate_ability(shrAb)
            


        
        
            
        
            for enemy_object in enemies:
                enemy_object.update()

                if enemy_object.rect.x < 0 :
                    enemy_object.respawn()
        

                if laserAb.laser.colliderect(enemy_object.rect):
                    enemy_object.respawn()
                if player.rect.colliderect(enemy_object.rect):
                    player.take_damage(1)
                    enemy_object.respawn()
                    if player.hp <= 0:

                        state = "GAME_OVER"


        
        
                    
        
            for bonus_object in bonuses:
                
                if player.rect.colliderect(bonus_object.rect):
                    bonus_object.despawn()
                    if player.speed > 8:
                        player.heal(1)
                    else:
                        player.speed += 1

                else:
                    if bonus_object.rect.x == 1200 and random.randint(1, 500) == 100:
                        bonus_object.spawn()
                
        
            hp_bar = pygame.Rect(10, 10, 200 * (player.hp / player.max_hp) , 10)
            screen.fill([255,255,255])

            if laserAb.active:
                pygame.draw.rect(screen, (255,0,0), laserAb.laser )
        
            pygame.draw.rect(screen, (0,0,0), player)
            
        
            for enemy_object in enemies:
                enemy_object.draw(screen)

        
            for bonus_object in bonuses:
                bonus_object.draw(screen)

            
            text_surface = font.render( f"speed: {str(player.speed)}", False , (0,0,0))
            pygame.draw.rect(screen, [0, 153, 76] ,hp_bar )
            screen.blit(text_surface, (10,30))
            pygame.display.flip()
        
        
        
        elif state == "GAME_OVER":
            screen.fill([0,0,0])
            text_surface = font.render("GET REKT BRO", False, (255,255,255))
            screen.blit(text_surface, (800 // 2, 600 // 2))
            pygame.display.flip()

        clock.tick(60)
    pygame.quit()

main()