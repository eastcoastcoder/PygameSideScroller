#!/usr/bin/env python
"""BulletManager module: manages bullet lifecycle."""

from typing import List
import pygame
from Bullets import Bullets
from Constants import COLOR_BULLET, SIZE_BLOCK, SIZE_SCREEN_X, RED

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


class BulletManager:
    """Manages all bullet entities in the game."""

    def __init__(self) -> None:
        """Initialize the bullet manager."""
        self.bullets = []

    def clean_bullets(self, level) -> None:
        """Remove bullets that collide with terrain or go off-screen.
        
        Args:
            level: The level loader instance for collision detection.
        """
        for bullet in self.bullets:
                if level.check_collisions(bullet, True) or bullet.x < SIZE_BLOCK or bullet.x > SIZE_SCREEN_X-SIZE_BLOCK:
                    self.bullets.pop(self.bullets.index(bullet))
                    
    def update_bullets(self, surface: pygame.Surface) -> None:
        """Update bullet positions and render them.
        
        Args:
            surface: The pygame surface to draw on.
        """
        for bullet in self.bullets:
            if bullet.direction == 'RIGHT' or bullet.direction == 'RSTOP':
                bullet.x += 20
            elif bullet.direction == 'LEFT' or bullet.direction == 'LSTOP':
                bullet.x -= 20
            pygame.draw.rect(surface, COLOR_BULLET, bullet, 0)

    def check_hit(self, enemy_manager) -> None:
        """Check for bullet collisions with enemies.
        
        Args:
            enemy_manager: The enemy manager instance.
        """
        for enemy in enemy_manager.enemies:
            for bullet in self.bullets:
                if bullet.colliderect(enemy):
                    _get_enemy_death_sound().play()
                    enemy.health -= 1
                    print("TAKING DAMAGE")
                    if enemy.health == 0:
                        print("DYING")
                        enemy_manager.enemies.pop(enemy_manager.enemies.index(enemy))
                    self.bullets.pop(self.bullets.index(bullet))
                    enemy.rgb = RED