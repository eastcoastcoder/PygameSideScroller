#!/usr/bin/env python
"""Gun module: ranged weapon entity."""

import pygame
from Bullets import Bullets

__author__ = "Joshua Sonnenberg and Ethan Richardson"


class Gun(pygame.Rect):
    """Represents a gun weapon attached to an entity."""
    
    def __init__(self, entity, surface: pygame.Surface) -> None:
        """Initialize the gun.
        
        Args:
            entity: The entity (player) that owns this gun.
            surface: The pygame surface to draw on.
        """
        self.entity = entity
        super(Gun, self).__init__(entity.x+20, entity.y+10, 10, 5)
        self.ammoSideX = entity.x+30
        self.ammoSideY = entity.y+10
        self.surface = surface
        self.entity = entity
    
    def draw(self) -> None:
        """Update gun position and render it on screen."""
        if self.entity.facing == 'RIGHT' or self.entity.facing == 'RSTOP':
            self.x = self.entity.x+20
        elif self.entity.facing == 'LEFT' or self.entity.facing == 'LSTOP':
            self.x = self.entity.x-10
        
        self.y = self.entity.y+10           
        pygame.draw.rect(self.surface, (55, 55, 59), self, 0)
        
    def shoot(self) -> None:
        """Fire a bullet if ammo is available, otherwise switch to sword."""
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