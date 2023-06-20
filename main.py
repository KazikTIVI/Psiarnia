import pygame, sys
from pygame.locals import *
from renderowanie_mapy import Renderowanie_Ziemi
from renderowanie_spritea import Sprite_Movement
from emergency_stop import Emergency_Stop
from player_inputs import *

running = True
pygame.init()

def MainTree():
    Emergency_Stop()
    Renderowanie_Ziemi()
    Sprite_Movement()
    
    
    
while running:
    MainTree()