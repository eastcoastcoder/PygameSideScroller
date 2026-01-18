#!/usr/bin/env python
"""Final Project for CS391 Intro to GameDev with Python and Pygame"""

import asyncio
import pygame
from GameLoop import GameLoop
import Controller


__author__ = "Joshua Sonnenberg and Ethan Richardson"


def preload_sounds() -> None:
    """Pre-load all sounds to avoid blocking during gameplay."""
    print("Pre-loading sounds...")
    try:
        # Pre-load all Controller sounds
        Controller._get_jump_sound()
        Controller._get_shoot_sound()
        Controller._get_sword_sound()
        print("Controller sounds pre-loaded")
    except Exception as e:
        print(f"Error pre-loading sounds: {e}")


async def main() -> None:
    """Initialize and run the game."""
    print("Starting Pygame Side Scroller...")
    
    try:
        pygame.init()
        print("Pygame initialized")
        win_surf = pygame.display.set_mode((800, 600))
        print(f"Display created: {win_surf.get_size()}")
        pygame.display.set_caption("Pygame Side Scroller")
        
        # Pre-load sounds after pygame.init() but before game starts
        preload_sounds()
        
        try:
            font = pygame.font.Font(None, 48)
            small_font = pygame.font.Font(None, 24)
            print("Fonts loaded")
        except Exception as e:
            print(f"Font error: {e}")
            font = None
            small_font = None
        
        print("Starting game loop...")
        game_loop = GameLoop(win_surf)
        await game_loop.draw()
        
    except Exception as e:
        print(f"ERROR in main: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    print("__main__ block executing")
    print("About to call asyncio.run(main())")
    asyncio.run(main())
