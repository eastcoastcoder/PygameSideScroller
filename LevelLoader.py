#!/usr/bin/env python
"""LevelLoader module: handles level loading and terrain management."""

from typing import List, Tuple
import pygame
from Constants import SIZE_BLOCK, SIZE_SCREEN_X, SIZE_SCREEN_Y, COLOR_TERRAIN
from Terrain import Terrain
from EnemyManager import EnemyManager
from CollisionManager import CollisionManager

__author__ = "Joshua Sonnenberg and Ethan Richardson"


class LevelLoader:
    """Handles loading and managing game levels."""

    def __init__(self, surface: pygame.Surface, enemy_manager: EnemyManager) -> None:
        """Initialize the level loader.
        
        Args:
            surface: The pygame surface to draw on.
            enemy_manager: The enemy manager instance.
        """
        self.surface = surface
        self.enemy_manager = enemy_manager
        self.terrain_objects = []
        self.gun_objects = []
        self.enemies = []
        self.end_of_level = False
        self.collide_flag = False
        self.counter = 0
        self.collide = CollisionManager()
        
        # Level ASCII keys
        self.level_one_key = "////////////////////////////////////////////////////////////" \
                             "///////////////////////////SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS/" \
                             "///////////////////////////SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS/" \
                             "///////////////////////////SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS/" \
                             "///////////////////////////SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS/" \
                             "///////////////////////////SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS/" \
                             "/SSSSSSSSSSSSSSSSSSSSS/////SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS/" \
                             "/SSSSSSSSSSXSSSSSSSSSS/////SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS/" \
                             "/SSSSSSSS///////SSSSSS/////SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS/" \
                             "/SXSSSSSS///////SSSSSS/////SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS/" \
                             "//////SSS///////SSSSSS/////SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS/" \
                             "/SSSSSSSS///////SSSSSS/////SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS/" \
                             "/SSSSSSSS///////SSSSSSSSSSSSSSSS///SSSSS//SSSSS////SSSSSSSS/" \
                             "/SSSSSS//SSSSSSSSSSSSSSSXSSSSSSSSXSSSSSSSXSSSSSSXSSSXSSSSSS/" \
                             "////////////////////////////////////////////////////////////"

    def load(self, level: int) -> None:
        """Load a level from ASCII map representation.
        
        Args:
            level: The level number to load.
        """
        count_x = 0
        count_y = 0
        if level == 1:
            ascii_map = self.level_one_key
        elif level == 2:
            ascii_map = self.level_two_key
        elif level == 3:
            ascii_map = self.level_three_key

        for i in ascii_map:
            if i == '/':
                self.terrain_objects.append(Terrain(count_x, count_y))
            elif i == 'S':
                pass
            elif i == 'X':
                self.enemy_manager.spawn(count_x, count_y)
            elif i == 'G':
                # self.objects.append(Gun(count_x, count_y, self.surface)
                pass
            count_x += SIZE_BLOCK
            if count_x == SIZE_SCREEN_X:
                count_x = 0
                count_y += SIZE_BLOCK
            if count_y == SIZE_SCREEN_Y:
                break

    def shift(self, speed: int) -> None:
        """Shift terrain and enemies as the level scrolls.
        
        Args:
            speed: The amount to shift by.
        """
        for terrain in self.terrain_objects:
            terrain.x -= speed
        self.enemy_manager.level_shift(speed)
        self.counter += speed
        if self.counter == 1600:
            self.end_of_level = True
            
    def check_collisions(self, rect_object: pygame.Rect, is_bullet: bool):
        """Check for collisions between an object and terrain.
        
        Args:
            rect_object: The rectangle to check for collisions.
            is_bullet: Whether the object is a bullet (returns bool) or not (returns list).
            
        Returns:
            For bullets: True if collision detected, False otherwise.
            For other objects: List [x_direction, y_direction] of collision.
        """
        if not is_bullet:
            hit = [0, 0]
            for terrain in self.terrain_objects:
                if self.collide.check_collision(rect_object, terrain):
                    hit = self.collide.check_hit_direction(rect_object, terrain)
                    self.collide.handleBoxHit(rect_object, terrain, hit)
            return hit
        else:
            flag = False
            for terrain in self.terrain_objects:
                if self.collide.check_collision(rect_object, terrain):
                    flag = True
            return flag
                
    def draw_terrain(self) -> None:
        """Render all terrain blocks to the screen."""
        for terrain in self.terrain_objects:
            pygame.draw.rect(self.surface, COLOR_TERRAIN, terrain, 0)
            self.surface.blit(terrain.tile, (terrain.x, terrain.y))