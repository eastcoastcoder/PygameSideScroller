#!/usr/bin/env python
"""Player Class"""

import pygame
from Constants import *
from BulletManager import *
from LevelLoader import *
from Player import *
__author__ = "Joshua Sonnenberg and Ethan Richardson"


class Sword(pygame.Rect):
    def __init__(self, entity):
        super(Sword, self).__init__(entity.x+10, entity.y+10, SWORD_WID, SWORD_HT)
        self.entity = entity
        self.stab = False
        self.sword_position = 'UP'
        
    def update(self):
        """Updates sword location on screen"""
        if self.entity.facing == 'RIGHT' or self.entity.facing == 'RSTOP':
            self.x = self.entity.x+10
            if self.stab:
                self.x += STAB_OFFSET
        elif self.entity.facing == 'LEFT' or self.entity.facing == 'LSTOP':
            self.x = self.entity.x-30
            if self.stab:
                self.x -= STAB_OFFSET
        
        if self.sword_position == 'UP':
                self.y = self.entity.y+10
        elif self.sword_position == 'DOWN':    
                self.y = self.entity.y+20