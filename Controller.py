#!/usr/bin/env python
"""Controller module: handles user input."""

import sys
from typing import Any
import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_ESCAPE, K_w, K_UP, K_f, K_SPACE, K_g, K_a, K_LEFT, K_d, K_RIGHT

__author__ = "Joshua Sonnenberg and Ethan Richardson"

pygame.mixer.init(44100, -16, 2, 2048)
jump_sound = pygame.mixer.Sound('Jump.wav')
shoot_sound = pygame.mixer.Sound('Gun.wav')
sword_sound = pygame.mixer.Sound('Sword.wav')


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
                            jump_sound.play()
                            player.status = 'RISE'
                    if event.key == K_f:
                        if sword.sword_position == 'UP':
                            sword.sword_position = 'DOWN'
                        else:
                            sword.sword_position = 'UP'
                    if event.key == K_SPACE:
                        if player.current_weapon == 'GUN':
                            shoot_sound.play()
                            player.gun.shoot()
                        if player.current_weapon == 'SWORD':
                            sword_sound.play()
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