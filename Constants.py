#!/usr/bin/env python
"""Constants Class, handles constants and imports"""

import pygame
from sys import platform as _platform

__author__ = "Joshua Sonnenberg and Ethan Richardson"


FPS = 60
BLACK = (0, 0, 0)

pygame.font.init()
FONT = pygame.font.Font(None, 20)

if _platform == 'linux' or _platform == 'linux2' or _platform == 'linux3' or _platform == "darwin":
    # Import Linux and OS X Assets
    pass
elif _platform == "win32":
    # Import Windows Assets
    pass


WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLUE = (34, 26, 186)
GREEN = (34, 111, 2)
LIGHT_GREY = (166, 165, 162)
COLOR_TERRAIN = (75, 81, 82)
COLOR_BULLET = (92, 90, 86)

PLAYER_SPEED = 5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GROUND_HEIGHT = 40

PLAYER_WID = 20
PLAYER_HT = 40
PLAYER_X = 60
PLAYER_Y = SCREEN_HEIGHT-PLAYER_HT-GROUND_HEIGHT

PLAYER_GRAVITY = 10
PLAYER_JUMP_HT = 100
PLAYER_JUMP_HT = 250

SWORD_WID = 40
SWORD_HT = 5

TERRAIN_WD_HT = 40
BULLET_WD_HT = 5

SCREEN_WID_HT = 800
CENTER = SCREEN_WID_HT/2

STAB_OFFSET = 10
BLOCK_OFFSET = 17

SIZE_BLOCK = 40
SIZE_SCREEN_X = 2400
SIZE_SCREEN_Y = 800


'''
# Unused
 BLOCK_X = 10+30
 BLOCK_Y = 20*4
 BLOCK_WID = 32
 BLOCK_HT = 32
'''