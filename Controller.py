#!/usr/bin/env python
"""Controller module: handles user input."""

import sys
from typing import Any
import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_ESCAPE, K_w, K_UP, K_f, K_SPACE, K_g, K_a, K_LEFT, K_d, K_RIGHT

__author__ = "Joshua Sonnenberg and Ethan Richardson"

# Sounds will be loaded lazily to avoid blocking browser initialization
jump_sound = None
shoot_sound = None
sword_sound = None

def _get_jump_sound():
    """Lazily load jump sound."""
    global jump_sound
    if jump_sound is None:
        try:
            jump_sound = pygame.mixer.Sound('Jump.wav')
        except:
            jump_sound = type('obj', (object,), {'play': lambda: None})()
    return jump_sound

def _get_shoot_sound():
    """Lazily load shoot sound."""
    global shoot_sound
    if shoot_sound is None:
        try:
            shoot_sound = pygame.mixer.Sound('Gun.wav')
        except:
            shoot_sound = type('obj', (object,), {'play': lambda: None})()
    return shoot_sound

def _get_sword_sound():
    """Lazily load sword sound."""
    global sword_sound
    if sword_sound is None:
        # Sword sound causes freezing in browser, skip loading
        print("Skipping sword sound to avoid browser freeze")
        sword_sound = type('obj', (object,), {'play': lambda: None})()
    return sword_sound


class Controller:
    """Handles keyboard input and game controls."""

    def get_input(self, key: Any, player: Any, levelloader: Any, sword: Any) -> None:
        """Process keyboard input and update game state.
        
        Args:
            key: The current key state from pygame.key.get_pressed().
            player: The player instance.
            levelloader: The level loader instance.
            sword: The sword instance.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
                if player.lives > 0:
                    if (event.key == K_w or event.key == K_UP):
                        if player.status == 'GROUND' or player.status == 'FALL':
                            if jump_sound is not None:
                                jump_sound.play()
                            player.status = 'RISE'
                    if event.key == K_f:
                        if sword.sword_position == 'UP':
                            sword.sword_position = 'DOWN'
                        else:
                            sword.sword_position = 'UP'
                    if event.key == K_SPACE:
                        if player.current_weapon == 'GUN':
                            if player.ammo > 0 and shoot_sound is not None:
                                shoot_sound.play()
                            player.gun.shoot()
                        elif player.current_weapon == 'SWORD':
                            # Sword sound disabled to prevent browser freezing
                            player.sword.stab = True
                    if event.key == K_g:
                        if player.current_weapon == 'SWORD' and player.ammo > 0:
                            player.current_weapon = 'GUN'
                        else:
                            player.current_weapon = 'SWORD'
                    if event.key == K_a or event.key == K_LEFT:
                        player.facing = 'LEFT'
                    if event.key == K_d or event.key == K_RIGHT:
                        player.facing = 'RIGHT'
                    
                        
            elif event.type == KEYUP and player.lives > 0:
                if event.key == K_w or event.key == K_UP:
                    player.status = 'FALL'
                if event.key == K_SPACE:
                    player.sword.stab = False
                if event.key == K_a or event.key == K_LEFT:
                    player.facing = 'LSTOP'
                if event.key == K_d or event.key == K_RIGHT:
                    player.facing = 'RSTOP'