__author__ = 'Joshua and Ethan'

import pygame


class GunPowerup(pygame.rect):

    def __init__(self, x, y):
        super(GunPowerup, self).__init__(x, y+30, 10, 10)