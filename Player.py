#!/usr/bin/env python
"""Player Class"""

import pygame
from Constants import *
from BulletManager import *
from LevelLoader import *
from Sword import Sword
from Gun import Gun

__author__ = "Joshua Sonnenberg and Ethan Richardson"

pygame.mixer.init(44100, -16, 2, 2048)
player_death_sound = pygame.mixer.Sound('Player_Death.wav')


class Player(pygame.Rect):
    """Handles player input, logic, and display"""
    
    def __init__(self, surface):
        """Constructor"""
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

    def move(self, levelloader):
        """Handles x movement and collisions"""
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
         
    def update_jump(self):
        """Updates game based on player input"""
        if self.status == 'RISE' and self.y > PLAYER_JUMP_HT-self.jump_offset:
            self.y -= PLAYER_GRAVITY
        elif self.status == 'FALL' and self.y < SCREEN_HEIGHT-PLAYER_HT-GROUND_HEIGHT and self.status != 'GROUND':
            self.y += PLAYER_GRAVITY
        else:
            self.status = 'GROUND'
        
    def die(self):
        """Handles player death"""
        player_death_sound.play()
        self.lives -= 1
        self.x = PLAYER_X
        self.y = PLAYER_Y
        
    def update(self):
        if self.current_weapon == 'GUN':
            self.gun.draw()
        elif self.current_weapon == 'SWORD':
            self.sword.update()
            pygame.draw.rect(self.surface, LIGHT_GREY, self.sword, 0)