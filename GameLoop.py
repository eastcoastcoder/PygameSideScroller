#!/usr/bin/env python
"""GameLoop Class"""

from Player import *
from LevelLoader import *
from EnemyManager import *
from Controller import Controller

__author__ = "Joshua Sonnenberg and Ethan Richardson"

game_font = pygame.font.SysFont("monospace", 42)
lose_message = game_font.render("You Lose", 1, (0, 0, 0))
lives_message = game_font.render("Lives: ", 1, (255, 255, 255))

class GameLoop:
    """Game Loop"""

    def __init__(self, surface):
        """Constructor"""
        self.surface = surface
        self.clock = pygame.time.Clock()
        self.lives = 3
        self.current_level = 1
        self.is_alive = True
        self.is_paused = False
        self.level = 1
        
    def new_game(self):
        """Resets the Game"""
        if self.lives > 0:
            self.is_alive = True
            self.draw()

    def draw(self):
        """Contains main game loop"""
        background = pygame.image.load(os.path.join("sky.jpg"))
        controller = Controller()
        collide = CollisionManager()
        player = Player(self.surface)
        enemy_manager = EnemyManager(self.surface)
        level = LevelLoader.LevelLoader(self.surface, enemy_manager)
        level.load(1)

        while self.is_alive:
            self.clock.tick(FPS)
            self.surface.blit(background, (0, 0))

            controller.get_input(pygame.key.get_pressed(), player, level, player.sword)

            if player.lives > 0:
                player.move(level)
                player.update_jump()
                pygame.draw.rect(self.surface, BLUE, player, 0)
                player.bullet_manager.update_bullets(self.surface)
                player.bullet_manager.check_hit(enemy_manager)
                player.bullet_manager.clean_bullets(level)
                
                player.update()

            enemy_manager.update(player)
            enemy_manager.draw()

            level.draw_terrain()
            
            health_count = game_font.render(str(player.lives), 1, (255, 255, 255))
            self.surface.blit(lives_message, (0, 0))
            self.surface.blit(health_count, (150, 0))
            
            if player.lives <= 0:
                self.surface.blit(lose_message, (200, 200))

            pygame.display.flip()