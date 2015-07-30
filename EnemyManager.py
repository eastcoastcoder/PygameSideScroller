import LevelLoader
from Enemy import *
from Constants import *
from BulletManager import enemy_death_sound

__author__ = 'Joshua and Ethan'


class EnemyManager():
    """Handles Enemy enemies"""

    def __init__(self, surface):
        """Constructor"""
        self.enemies = []
        self.surface = surface
        self.clock = pygame.time.Clock()

    def remove(self, index):
        """Removes entity"""
        self.enemies.pop(index)

    def spawn(self, x_coord, y_coord):
        """Spawns entity"""
        self.enemies.append(Enemy(x_coord, y_coord))

    def update(self, player):
        """Updates entity movement"""
        self.clock.tick()
        for enemy in self.enemies:
            distance = enemy.x - player.x
            if distance > 0:
                enemy.facing = 'LEFT'
            elif distance < -20:
                enemy.facing = 'RIGHT'

            if distance < 400 and distance > 35 and enemy.y == player.y:
                enemy.move()
            if distance < -55 and distance > -420 and enemy.y == player.y:
                enemy.move()

            if pygame.time.get_ticks() % enemy.seed1 == 0:
                if enemy.sword.sword_position == 'UP':
                    enemy.sword.sword_position = 'DOWN'
                else:
                    enemy.sword.sword_position = 'UP'

            elif pygame.time.get_ticks() % enemy.seed2 == 0:
                if enemy.sword.stab:
                    enemy.sword.stab = False
                else:
                    enemy.sword.stab = True
        
        self.update_sword(player)
    
    def update_sword(self, player):
        for enemy in self.enemies:
            # Parry
            if player.sword.colliderect(enemy.sword):
                if player.facing == 'LEFT' or player.facing == 'LSTOP':
                    enemy.x -= 10
                elif player.facing == 'RIGHT' or player.facing == 'RSTOP':
                    enemy.x += 10
            if player.sword.colliderect(enemy) and player.sword.stab:
                enemy_death_sound.play()
                self.enemies.pop(self.enemies.index(enemy))
            if enemy.sword.colliderect(player) and enemy.stab:
                player.die()
                
    def draw(self):
        """Draws enemies"""
        for enemy in self.enemies:
            pygame.draw.rect(self.surface, GREEN, enemy, 0)
            enemy.sword.update()
            pygame.draw.rect(self.surface, LIGHT_GREY, enemy.sword, 0)

    def level_shift(self, shift):
        """Shifts enemies with level"""
        for enemy in self.enemies:
            enemy.x -= shift