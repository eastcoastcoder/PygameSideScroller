#!/usr/bin/env python
"""Bullets module: projectile entity."""

import pygame
from Constants import BULLET_WD_HT

__author__ = "Joshua Sonnenberg and Ethan Richardson"


class Bullets(pygame.Rect):
    """Represents a bullet projectile."""

    def __init__(self, x: int, y: int, direction: str, surface: pygame.Surface) -> None:
        """Initialize a bullet.
        
        Args:
            x: The x-coordinate position.
            y: The y-coordinate position.
            direction: The direction the bullet is traveling.
            surface: The pygame surface to draw on.
        """
        super(Bullets, self).__init__(x, y, BULLET_WD_HT, BULLET_WD_HT)
        self.direction = direction
        