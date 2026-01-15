#!/usr/bin/env python
"""Player Class"""

from typing import List
import pygame
from Constants import (
    PLAYER_X, PLAYER_Y, PLAYER_WID, PLAYER_HT, PLAYER_SPEED,
    SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_HEIGHT, PLAYER_GRAVITY,
    PLAYER_JUMP_HT, LIGHT_GREY, BLUE
)
from BulletManager import BulletManager
from Sword import Sword
from Gun import Gun

__author__ = "Joshua Sonnenberg and Ethan Richardson"

# Lazy load sound to avoid blocking browser initialization
player_death_sound = None

def _get_death_sound():
    """Lazily load death sound."""
    global player_death_sound
    if player_death_sound is None:
        try:
            player_death_sound = pygame.mixer.Sound('Player_Death.wav')
        except:
            player_death_sound = type('obj', (object,), {'play': lambda: None})()
    return player_death_sound


class Player(pygame.Rect):
    """Handles player input, logic, and display"""
    
    def __init__(self, surface: pygame.Surface) -> None:
        """Initialize the player.
        
        Args:
            surface: The pygame surface to draw on.
        """
        super(Player, self).__init__(PLAYER_X, PLAYER_Y, PLAYER_WID, PLAYER_HT)
        self.surface = surface
        self.bullet_manager = BulletManager()
        self.gun = Gun(self, surface)
        self.sword = Sword(self)

        self.speed = 10
        self.ammo = 6
        self.status = 'GROUND'
        self.facing = 'RSTOP'
        self.current_weapon = 'GUN'
        self.lives = 3
        self.hit = [0, 0]
        self.jump_offset = 200

    def move(self, levelloader) -> None:
        """Handle x movement and collisions.
        
        Args:
            levelloader: The level loader instance for collision detection.
        """
        self.hit = levelloader.check_collisions(self, False)

        if self.facing == 'LEFT':
            if self.x > PLAYER_WID:
                self.x -= PLAYER_SPEED
        if self.facing == 'RIGHT':
            if self.x < SCREEN_WIDTH/2:
                self.x += PLAYER_SPEED
            elif self.x >= SCREEN_WIDTH/2 and not levelloader.end_of_level:
                levelloader.shift(self.speed)
            else:
                self.x += PLAYER_SPEED
         
    def update_jump(self) -> None:
        """Update player jumping physics and state."""
        if self.status == 'RISE' and self.y > PLAYER_JUMP_HT-self.jump_offset:
            self.y -= PLAYER_GRAVITY
        elif self.status == 'FALL' and self.y < SCREEN_HEIGHT-PLAYER_HT-GROUND_HEIGHT and self.status != 'GROUND':
            self.y += PLAYER_GRAVITY
        else:
            self.status = 'GROUND'
        
    def die(self) -> None:
        """Handle player death, decrement lives, and reset position."""
        _get_death_sound().play()
        self.lives -= 1
        self.x = PLAYER_X
        self.y = PLAYER_Y
        
    def update(self) -> None:
        """Update and draw the current weapon."""
        if self.current_weapon == 'GUN':
            self.gun.draw()
        elif self.current_weapon == 'SWORD':
            self.sword.update()
            pygame.draw.rect(self.surface, LIGHT_GREY, self.sword, 0)