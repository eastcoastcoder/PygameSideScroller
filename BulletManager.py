__author__ = 'Joshua and Ethan'

from Bullets import *
from Constants import *

pygame.mixer.init(44100, -16, 2, 2048)
enemy_death_sound = pygame.mixer.Sound('Enemy_Death.wav')


class BulletManager:

    def __init__(self):
        """Constructor"""
        self.bullets = []

    def clean_bullets(self, level):
        for bullet in self.bullets:
                if level.check_collisions(bullet, True) or bullet.x < SIZE_BLOCK or bullet.x > SIZE_SCREEN_X-SIZE_BLOCK:
                    self.bullets.pop(self.bullets.index(bullet))
                    
    def update_bullets(self, surface):
        """Updates bullet positions"""
        for bullet in self.bullets:
            if bullet.direction == 'RIGHT' or bullet.direction == 'RSTOP':
                bullet.x += 20
            elif bullet.direction == 'LEFT' or bullet.direction == 'LSTOP':
                bullet.x -= 20
            pygame.draw.rect(surface, COLOR_BULLET, bullet, 0)

    def check_hit(self, enemy_manager):
        """Checks to see if any bullets hit their mark"""
        for enemy in enemy_manager.enemies:
            for bullet in self.bullets:
                if bullet.colliderect(enemy):
                    enemy_death_sound.play()
                    enemy.health -= 1
                    print("TAKING DAMAGE")
                    if enemy.health == 0:
                        print("DYING")
                        enemy_manager.enemies.pop(enemy_manager.enemies.index(enemy))
                    self.bullets.pop(self.bullets.index(bullet))
                    enemy.rgb = RED