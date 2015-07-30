_author_ = 'Joshua and Ethan'

import sys
import pygame
from pygame.locals import *
from Constants import *

pygame.mixer.init(44100, -16, 2, 2048)
jump_sound = pygame.mixer.Sound('Jump.wav')
shoot_sound = pygame.mixer.Sound('Gun.wav')
sword_sound = pygame.mixer.Sound('Sword.wav')


class Controller:

    def get_input(self, key, player, levelloader, sword):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
                if player.lives > 0:
                    if (event.key == K_w or event.key == K_UP):
                        if player.status == 'GROUND' or player.status == 'FALL':
                            jump_sound.play()
                            player.status = 'RISE'
                    if event.key == K_f:
                        if sword.sword_position == 'UP':
                            sword.sword_position = 'DOWN'
                        else:
                            sword.sword_position = 'UP'
                    if event.key == K_SPACE:
                        if player.current_weapon == 'GUN':
                            shoot_sound.play()
                            player.gun.shoot()
                        if player.current_weapon == 'SWORD':
                            sword_sound.play()
                            player.sword.stab = True
                    if event.key == K_g:
                        if player.current_weapon == 'SWORD' and player.ammo > 0:
                            player.current_weapon = 'GUN'
                        else:
                            player.current_weapon = 'SWORD'
                    if event.key == K_a or event.key == K_LEFT:
                        player.facing = 'LEFT'
                    if event.key == K_d or event.key == K_RIGHT:
                        player.facing = 'RIGHT'
                    
                        
            elif event.type == KEYUP and player.lives > 0:
                if event.key == K_w or event.key == K_UP:
                    player.status = 'FALL'
                if event.key == K_SPACE:
                    player.sword.stab = False
                if event.key == K_a or event.key == K_LEFT:
                    player.facing = 'LSTOP'
                if event.key == K_d or event.key == K_RIGHT:
                    player.facing = 'RSTOP'