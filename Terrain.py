__author__ = 'Joshua and Ethan'

import pygame
import os
from Constants import TERRAIN_WD_HT


class Terrain(pygame.Rect):
    """Handles Terrain"""

    def __init__(self, x_coord, y_coord):
        """Constructor"""
        super(Terrain, self).__init__(x_coord, y_coord, TERRAIN_WD_HT, TERRAIN_WD_HT)
        self.tile = pygame.image.load(os.path.join("stone.jpg"))