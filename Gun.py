#!/usr/bin/env python
"""Player Class"""

import pygame
from Constants import *
from BulletManager import *
from LevelLoader import *
from Player import *

__author__ = "Joshua Sonnenberg and Ethan Richardson"


class Gun(pygame.Rect):
    
    def __init__(self, entity, surface):
        self.entity = entity
        super(Gun, self).__init__(entity.x+20, entity.y+10, 10, 5)
        self.ammoSideX = entity.x+30
        self.ammoSideY = entity.y+10
        self.surface = surface
        self.entity = entity
    
    def draw(self):
        """Draws gun to screen"""
        if self.entity.facing == 'RIGHT' or self.entity.facing == 'RSTOP':
            self.x = self.entity.x+20
        elif self.entity.facing == 'LEFT' or self.entity.facing == 'LSTOP':
            self.x = self.entity.x-10
        
        self.y = self.entity.y+10           
        pygame.draw.rect(self.surface, (55, 55, 59), self, 0)
        
    def shoot(self):
        """Gun type attack function"""
        if self.entity.ammo > 0:
            if self.entity.facing == 'RIGHT' or self.entity.facing == 'RSTOP':
                self.ammoSideX = self.entity.x+30
            elif self.entity.facing == 'LEFT' or self.entity.facing == 'LSTOP':
                self.ammoSideX = self.entity.x-10
            
            self.ammoSideY = self.entity.y+10
            
            # Fires rounds and adds bullet objects to list
            self.entity.bullet_manager.bullets.append(Bullets(self.ammoSideX, self.ammoSideY, self.entity.facing, self.surface))
            self.entity.ammo -= 1
        else:
            self.entity.current_weapon = 'SWORD'