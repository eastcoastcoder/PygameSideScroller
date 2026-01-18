#!/usr/bin/env python
"""EnemyManager module: manages all enemy entities."""

from typing import List
import pygame
from Enemy import Enemy
from Constants import GREEN, LIGHT_GREY

__author__ = "Joshua Sonnenberg and Ethan Richardson"

# Lazy load sound to avoid blocking browser initialization
enemy_death_sound = None

def _get_enemy_death_sound():
    """Lazily load enemy death sound."""
    global enemy_death_sound
    if enemy_death_sound is None:
        try:
            enemy_death_sound = pygame.mixer.Sound('Enemy_Death.wav')
        except:
            enemy_death_sound = type('obj', (object,), {'play': lambda: None})()
    return enemy_death_sound


class EnemyManager:
    """Manages all enemy entities in the game."""

    def __init__(self, surface: pygame.Surface) -> None:
        """Initialize the enemy manager.
        
        Args:
            surface: The pygame surface to draw on.
        """
        self.enemies = []
        self.surface = surface
        self.clock = pygame.time.Clock()

    def remove(self, index: int) -> None:
        """Remove an enemy by index.
        
        Args:
            index: The index of the enemy to remove.
        """
        self.enemies.pop(index)

    def spawn(self, x_coord: int, y_coord: int) -> None:
        """Spawn a new enemy at the specified coordinates.
        
        Args:
            x_coord: The x-coordinate position.
            y_coord: The y-coordinate position.
        """
        self.enemies.append(Enemy(x_coord, y_coord))

    def update(self, player) -> None:
        """Update all enemy behaviors and AI.
        
        Args:
            player: The player instance for AI targeting.
        """
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
    
    def update_sword(self, player) -> None:
        """Handle sword collision detection between player and enemies.
        
        Args:
            player: The player instance.
        """
        for enemy in self.enemies:
            # Parry
            if player.sword.colliderect(enemy.sword):
                if player.facing == 'LEFT' or player.facing == 'LSTOP':
                    enemy.x -= 10
                elif player.facing == 'RIGHT' or player.facing == 'RSTOP':
                    enemy.x += 10
            if player.sword.colliderect(enemy) and player.sword.stab:
                _get_enemy_death_sound().play()
                self.enemies.pop(self.enemies.index(enemy))
            if enemy.sword.colliderect(player) and enemy.stab and player.lives != 0:
                player.die()
                
    def draw(self) -> None:
        """Render all enemies and their swords."""
        for enemy in self.enemies:
            pygame.draw.rect(self.surface, GREEN, enemy, 0)
            enemy.sword.update()
            pygame.draw.rect(self.surface, LIGHT_GREY, enemy.sword, 0)

    def level_shift(self, shift: int) -> None:
        """Shift all enemies when the level scrolls.
        
        Args:
            shift: The amount to shift enemies by.
        """
        for enemy in self.enemies:
            enemy.x -= shift