import pygame, sys
from pygame.locals import *
from consts import *
from emergency_stop import *

# def Player_position(x=0,y=0):
#     plposx = spriteposx + x
#     plposy = spriteposy + y

#     newspriteposx = plposx
#     newspriteposy = plposy
#     print(newspriteposx, newspriteposy)
#     return newspriteposx, newspriteposy


# def Inputs():
#     while True:
#         def Movecommandx(x):
#             moveVector = Player_position(x,0)
#             return moveVector

#         def Movecommandy(y):
#             moveVector = Player_position(0,y)
#             print('jabadabadu')
#             return moveVector
        
#         Emergency_Stop()
#         for event in pygame.event.get():
#                         if event.type == KEYDOWN:
#                             if event.key == pygame.K_s:
#        
#                          Movecommandy(-1)


def Update():
    Emergency_Stop()
    zmiana_y = 0
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_w]:
        zmiana_y = -3
        return zmiana_y
    if keystate[pygame.K_s]:
        zmiana_y = 3
        return zmiana_y
    print(zmiana_y)
Update()