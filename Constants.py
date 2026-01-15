#!/usr/bin/env python
"""Constants module: handles game constants and configuration."""

import pygame
from sys import platform as _platform
from typing import Final, Tuple

__author__ = "Joshua Sonnenberg and Ethan Richardson"


# Game settings
FPS: Final[int] = 60

# Colors (RGB tuples)
BLACK: Final[Tuple[int, int, int]] = (0, 0, 0)
WHITE: Final[Tuple[int, int, int]] = (255, 255, 255)
RED: Final[Tuple[int, int, int]] = (255, 0, 0)
GREEN: Final[Tuple[int, int, int]] = (34, 111, 2)
MAGENTA: Final[Tuple[int, int, int]] = (255, 0, 255)
CYAN: Final[Tuple[int, int, int]] = (0, 255, 255)
BLUE: Final[Tuple[int, int, int]] = (34, 26, 186)
LIGHT_GREY: Final[Tuple[int, int, int]] = (166, 165, 162)
COLOR_TERRAIN: Final[Tuple[int, int, int]] = (75, 81, 82)
COLOR_BULLET: Final[Tuple[int, int, int]] = (92, 90, 86)

pygame.font.init()
FONT: pygame.font.Font = pygame.font.Font(None, 20)

# Player settings
PLAYER_SPEED: Final[int] = 5
PLAYER_WID: Final[int] = 20
PLAYER_HT: Final[int] = 40
PLAYER_X: Final[int] = 60
PLAYER_GRAVITY: Final[int] = 10
PLAYER_JUMP_HT: Final[int] = 250  # Maximum jump height

# Screen settings
SCREEN_WIDTH: Final[int] = 800
SCREEN_HEIGHT: Final[int] = 600
GROUND_HEIGHT: Final[int] = 40
SCREEN_WID_HT: Final[int] = 800
CENTER: Final[float] = SCREEN_WID_HT / 2

# Calculated player position
PLAYER_Y: Final[int] = SCREEN_HEIGHT - PLAYER_HT - GROUND_HEIGHT

# Weapon settings
SWORD_WID: Final[int] = 40
SWORD_HT: Final[int] = 5
STAB_OFFSET: Final[int] = 10
BLOCK_OFFSET: Final[int] = 17

# Terrain and projectile settings
TERRAIN_WD_HT: Final[int] = 40
BULLET_WD_HT: Final[int] = 5

# Level settings
SIZE_BLOCK: Final[int] = 40
SIZE_SCREEN_X: Final[int] = 2400
SIZE_SCREEN_Y: Final[int] = 800