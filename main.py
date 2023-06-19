import pygame, sys
from pygame.locals import *
from renderowanie_mapy import Renderowanie_Ziemi
from player_inputs import Player_Inputs
from emergency_stop import Emergency_Stop

running = True
def MainTree():
    pygame.init()

    Emergency_Stop()
    Renderowanie_Ziemi()
    

MainTree()