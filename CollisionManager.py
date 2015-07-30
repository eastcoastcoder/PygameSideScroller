'''
Created on Feb 6, 2015

@author: SIU853541579
'''
import pygame
import random
from Constants import *

class CollisionManager:

    def check_hit_direction(self, one, two):
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
    
    def handleBoxHit(self, one, two, hit):
        """
        1,1   0,1   -1,1
        
        1,0         -1,0
        
        1,-1  0,-1  -1,-1
        """
        if(one.facing != 'LSTOP' or one.facing != 'RSTOP'):
            # Right Edge
            if(hit[0] == -1):
                one.x = two.x + two.width
                one.x += 1
            # Left Edge
            elif(hit[0] == 1):
                one.x = two.x - one.width
                one.x -= 1
            # Bottom Edge
            if(hit[1] == -1):
                one.y = two.y + two.height
                one.y += 5
            # Top Edge
            elif(hit[1] == 1):
                one.y = two.y - one.height

        
    def check_collision(self, one, two):
        if(one.x <= (two.x+two.width)) and (two.x <= (one.x+one.width)):
            if(one.y <= (two.y+two.height)) and (two.y <= (one.y+one.height)):
                return True
            else:
                return False
        else:
            return False
            
