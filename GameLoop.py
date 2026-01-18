#!/usr/bin/env python
"""GameLoop module: main game loop and state management."""

import asyncio
import os
import pygame
from Player import Player
from LevelLoader import LevelLoader
from EnemyManager import EnemyManager
from CollisionManager import CollisionManager
from Controller import Controller
from Constants import FPS, BLUE

__author__ = "Joshua Sonnenberg and Ethan Richardson"

game_font = pygame.font.SysFont("monospace", 42)
lose_message = game_font.render("You Lose", 1, (0, 0, 0))
lives_message = game_font.render("Lives: ", 1, (255, 255, 255))
ammo_message = game_font.render("Ammo: ", 1, (255, 255, 255))

class GameLoop:
    """Main game loop and state management."""

    def __init__(self, surface: pygame.Surface) -> None:
        """Initialize the game loop.
        
        Args:
            surface: The pygame surface to draw on.
        """
        self.surface = surface
        self.clock = pygame.time.Clock()
        self.lives = 3
        self.current_level = 1
        self.is_alive = True
        self.is_paused = False
        self.level = 1
        
    async def new_game(self) -> None:
        """Reset and restart the game."""
        if self.lives > 0:
            self.is_alive = True
            await self.draw()

    async def draw(self) -> None:
        """Run the main game loop."""
        print("GameLoop.draw() started")
        
        try:
            background = pygame.image.load(os.path.join("sky.jpg"))
            print("Background loaded successfully")
        except Exception as e:
            print(f"Warning: Could not load background image: {e}")
            # Create a fallback gradient background
            background = pygame.Surface((800, 600))
            background.fill((135, 206, 235))  # Sky blue
        
        controller = Controller()
        collide = CollisionManager()
        player = Player(self.surface)
        enemy_manager = EnemyManager(self.surface)
        level = LevelLoader(self.surface, enemy_manager)
        level.load(1)
        
        print("Game objects initialized, entering main loop")

        while self.is_alive:
            self.clock.tick(FPS)
            self.surface.blit(background, (0, 0))

            controller.get_input(pygame.key.get_pressed(), player, level, player.sword)

            if player.lives > 0:
                # Update jump before collision detection to get correct position
                player.update_jump()
                player.move(level)
                pygame.draw.rect(self.surface, BLUE, player, 0)
                player.bullet_manager.update_bullets(self.surface)
                player.bullet_manager.check_hit(enemy_manager)
                player.bullet_manager.clean_bullets(level)
                
                player.update()

            enemy_manager.update(player)
            enemy_manager.draw()

            level.draw_terrain()
            
            health_count = game_font.render(str(player.lives), 1, (255, 255, 255))
            ammo_count = game_font.render(str(player.ammo), 1, (255, 255, 255))
            self.surface.blit(lives_message, (0, 0))
            self.surface.blit(ammo_message, (0, 50))
            self.surface.blit(health_count, (150, 0))
            self.surface.blit(ammo_count, (150, 50))
            
            if player.lives <= 0:
                self.surface.blit(lose_message, (200, 200))

            pygame.display.flip()
            
            # Yield control to browser event loop (critical for Pygbag)
            await asyncio.sleep(0)