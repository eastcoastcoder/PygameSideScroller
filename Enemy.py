#!/usr/bin/env python
"""Enemy"""

import pygame
from Sword import Sword
from random import randrange

__author__ = "Joshua Sonnenberg and Ethan Richardson"


class Enemy(pygame.Rect):
    """Handles enemy entities"""

    def __init__(self, x, y):
        """Constructor"""
        super(Enemy, self).__init__(x, y, 20, 40)
        self.facing = 'LEFT'
        self.health = 2
        self.sword = Sword(self)
        self.seed1 = randrange(11, 33)
        self.seed2 = randrange(11, 33)
        
        self.stab = True
        
    def move(self):
        """Checks and updates enemy movement"""
        if self.facing == 'LEFT':
            self.x -= 3
        elif self.facing == 'RIGHT':
            self.x += 3
