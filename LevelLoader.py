#!/usr/bin/env python
"""Final Project for CS391 Intro to GameDev with Python and Pygame"""
import pygame, random
from Constants import *
from Terrain import *
from EnemyManager import *
from CollisionManager import *

__author__ = "Joshua Sonnenberg and Ethan Richardson"


class LevelLoader:
    """Handles loading in maps"""

    def __init__(self, surface, enemy_manager):
        """Constructor"""
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

    def load(self, level):
        """Loads in level based on ASCII values"""
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

    def shift(self, speed):
        """Updates map coordinates"""
        for terrain in self.terrain_objects:
            terrain.x -= speed
        self.enemy_manager.level_shift(speed)
        self.counter += speed
        if self.counter == 1600:
            self.end_of_level = True
            
    def check_collisions(self, rect_object, is_bullet):
        """Checks collisions with terrain"""
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
                
    def draw_terrain(self):
        for terrain in self.terrain_objects:
            pygame.draw.rect(self.surface, COLOR_TERRAIN, terrain, 0)
            self.surface.blit(terrain.tile, (terrain.x, terrain.y))