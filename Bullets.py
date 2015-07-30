__author__ = 'Joshua and Ethan'

import pygame
from Constants import CYAN, BULLET_WD_HT, COLOR_BULLET


class Bullets(pygame.Rect):

    def __init__(self, x, y, direction, surface):
        """Constructor"""
        super(Bullets, self).__init__(x, y, BULLET_WD_HT, BULLET_WD_HT)
        self.direction = direction
        