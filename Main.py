#!/usr/bin/env python
"""Final Project for CS391 Intro to GameDev with Python and Pygame"""

import pygame
from GameLoop import GameLoop


__author__ = "Joshua Sonnenberg and Ethan Richardson"


def main() -> None:
    """Initialize and run the game."""
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    win_surf = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pygame Side Scroller")
    game_loop = GameLoop(win_surf)
    game_loop.draw()


if __name__ == "__main__":
    main()