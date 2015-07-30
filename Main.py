#!/usr/bin/env python
"""Final Project for CS391 Intro to GameDev with Python and Pygame"""

from GameLoop import *
import pygame


__author__ = "Joshua Sonnenberg and Ethan Richardson"


pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
winSurf = pygame.display.set_mode((800, 600))
game_loop = GameLoop(winSurf)
game_loop.draw()