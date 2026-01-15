#!/usr/bin/env python
"""Terrain module: represents terrain blocks."""

import os
import pygame
from Constants import TERRAIN_WD_HT

__author__ = "Joshua Sonnenberg and Ethan Richardson"


class Terrain(pygame.Rect):
    """Represents a terrain block with texture."""

    def __init__(self, x_coord: int, y_coord: int) -> None:
        """Initialize a terrain block.
        
        Args:
            x_coord: The x-coordinate position.
            y_coord: The y-coordinate position.
        """
        super(Terrain, self).__init__(x_coord, y_coord, TERRAIN_WD_HT, TERRAIN_WD_HT)
        self.tile = pygame.image.load(os.path.join("stone.jpg"))