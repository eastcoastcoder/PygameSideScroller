#!/usr/bin/env python
"""CollisionManager module: handles collision detection and resolution."""

from typing import List
import pygame

__author__ = "Joshua Sonnenberg and Ethan Richardson"


class CollisionManager:
    """Manages collision detection between game entities."""

    def check_hit_direction(self, one: pygame.Rect, two: pygame.Rect) -> List[int]:
        """Determine the direction of collision between two rectangles.
        
        Args:
            one: The first rectangle.
            two: The second rectangle.
            
        Returns:
            A list [x_direction, y_direction] indicating collision direction.
        """
        result = [0,0]
        dTop = abs(one.y - (two.y + two.height))
        dBot = abs((one.y+one.height) - two.y)
        dRight = abs((one.x + one.width) - two.x)
        dLeft = abs(one.x - (two.x+two.width))
        if((dTop <= dRight) and (dTop <= dLeft) and (dTop < dBot)):
            # Top
            if(dTop == dRight): # Right Corner
                result[0] = 1                
            elif(dTop == dLeft): # Left Corner
                result[0] = -1
            result[1] = -1
            
        elif((dBot <= dRight) and (dBot <= dLeft)):
            # Bottom
            if(dBot == dRight): # Right Corner
                result[0] = 1                
            elif(dBot == dLeft): # Left Corner
                result[0] = -1
            result[1] = 1
            
        elif(dRight < dLeft):
            # Right
            result[0] = 1
        else:
            # Left   
            result[0] = -1
            
        return result
    
    def handleBoxHit(self, one: pygame.Rect, two: pygame.Rect, hit: List[int]) -> None:
        """Handle collision response between two boxes.
        
        Args:
            one: The first rectangle.
            two: The second rectangle.
            hit: The collision direction from check_hit_direction.
            
        Note:
            Direction grid:
            1,1   0,1   -1,1
            1,0         -1,0
            1,-1  0,-1  -1,-1
        """
        if(one.facing != 'LSTOP' or one.facing != 'RSTOP'):
            # Right Edge - hit the left side of terrain while moving right
            if(hit[0] == -1):
                one.x = two.x + two.width
                one.x += 1
            # Left Edge - hit the right side of terrain while moving left
            elif(hit[0] == 1):
                one.x = two.x - one.width
                one.x -= 1
            # Bottom Edge
            if(hit[1] == -1):
                one.y = two.y + two.height
                one.y += 5
            # Top Edge - landed on terrain from above
            elif(hit[1] == 1):
                one.y = two.y - one.height

        
    def check_collision(self, one: pygame.Rect, two: pygame.Rect) -> bool:
        """Check if two rectangles are colliding.
        
        Args:
            one: The first rectangle.
            two: The second rectangle.
            
        Returns:
            True if rectangles are colliding, False otherwise.
        """
        if(one.x <= (two.x+two.width)) and (two.x <= (one.x+one.width)):
            if(one.y <= (two.y+two.height)) and (two.y <= (one.y+one.height)):
                return True
            else:
                return False
        else:
            return False
            
