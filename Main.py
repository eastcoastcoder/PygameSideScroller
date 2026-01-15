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
        
        # Display "Click to Start" message for browser compatibility
        try:
            font = pygame.font.Font(None, 48)
            small_font = pygame.font.Font(None, 24)
            print("Fonts loaded")
        except Exception as e:
            print(f"Font error: {e}")
            font = None
            small_font = None
        
        print("Waiting for user interaction...")
        # Wait for user click (required for browser audio/input)
        waiting = True
        frame_count = 0
        while waiting:
            frame_count += 1
            if frame_count % 60 == 0:  # Log every 60 frames (~1 second)
                print(f"Still waiting... frame {frame_count}")
            
            win_surf.fill((0, 0, 0))
            
            if font and small_font:
                title = font.render("Pygame Side Scroller", True, (74, 144, 226))
                prompt = small_font.render("Click anywhere to start", True, (255, 255, 255))
                win_surf.blit(title, (800//2 - title.get_width()//2, 250))
                win_surf.blit(prompt, (800//2 - prompt.get_width()//2, 320))
            else:
                # Fallback if fonts don't load - draw a white rectangle
                pygame.draw.rect(win_surf, (255, 255, 255), (300, 250, 200, 100))
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quit event received")
                    return
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                    print(f"User interaction detected: {event.type}")
                    waiting = False
            
            await asyncio.sleep(0)  # Yield to browser
        
        print("Starting game loop...")
        # Now start the actual game
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
