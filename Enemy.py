#!/usr/bin/env python
"""Enemy module: enemy entity behavior."""

import pygame
from Sword import Sword
from random import randrange

__author__ = "Joshua Sonnenberg and Ethan Richardson"


class Enemy(pygame.Rect):
    """Represents an enemy entity with movement and combat."""

    def __init__(self, x: int, y: int) -> None:
        """Initialize an enemy.
        
        Args:
            x: The x-coordinate position.
            y: The y-coordinate position.
        """
        super(Enemy, self).__init__(x, y, 20, 40)
        self.facing = 'LEFT'
        self.health = 2
        self.sword = Sword(self)
        self.seed1 = randrange(11, 33)
        self.seed2 = randrange(11, 33)
        
        self.stab = True
        
    def move(self) -> None:
        """Update enemy movement based on facing direction."""
        if self.facing == 'LEFT':
            self.x -= 3
        elif self.facing == 'RIGHT':
            self.x += 3
