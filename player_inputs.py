import pygame, sys
from pygame.locals import *
from consts import *

def player_position():
    plpos = spritepos + movecommand

movecommand = (0,0)

def inputs():
    movecommand = (0,0)
    for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_s:
                            movecommand[1] -= 1
                            