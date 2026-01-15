#!/usr/bin/env python
"""GunPowerup module: represents a gun ammunition powerup."""

import pygame

__author__ = "Joshua Sonnenberg and Ethan Richardson"


class GunPowerup(pygame.Rect):
    """Represents a gun ammunition powerup collectible."""

    def __init__(self, x: int, y: int) -> None:
        """Initialize a gun powerup.
        
        Args:
            x: The x-coordinate position.
            y: The y-coordinate position.
        """
        super(GunPowerup, self).__init__(x, y+30, 10, 10)