import pygame, sys
from pygame.locals import *
from renderowanie_mapy import Renderowanie_Ziemi
from renderowanie_spritea import Renderowanie_Postaci
from emergency_stop import Emergency_Stop

running = True
pygame.init()

def MainTree():
    Emergency_Stop()
    Renderowanie_Postaci()
    Renderowanie_Ziemi()
    
    
while running:
    MainTree()