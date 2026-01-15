#!/usr/bin/env python
"""Sword module: melee weapon entity."""

import pygame
from Constants import SWORD_WID, SWORD_HT, STAB_OFFSET

__author__ = "Joshua Sonnenberg and Ethan Richardson"


class Sword(pygame.Rect):
    """Represents a sword weapon attached to an entity."""
    
    def __init__(self, entity) -> None:
        """Initialize the sword.
        
        Args:
            entity: The entity (player or enemy) that owns this sword.
        """
        super(Sword, self).__init__(entity.x+10, entity.y+10, SWORD_WID, SWORD_HT)
        self.entity = entity
        self.stab = False
        self.sword_position = 'UP'
        
    def update(self) -> None:
        """Update sword position based on entity position and facing direction."""
        if self.entity.facing == 'RIGHT' or self.entity.facing == 'RSTOP':
            self.x = self.entity.x+10
            if self.stab:
                self.x += STAB_OFFSET
        elif self.entity.facing == 'LEFT' or self.entity.facing == 'LSTOP':
            self.x = self.entity.x-30
            if self.stab:
                self.x -= STAB_OFFSET
        
        if self.sword_position == 'UP':
                self.y = self.entity.y+10
        elif self.sword_position == 'DOWN':    
                self.y = self.entity.y+20