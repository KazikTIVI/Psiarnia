import pygame,sys
from pygame.locals import *
from consts import *
from emergency_stop import Emergency_Stop

def Renderowanie_Postaci():
    def imgtosprite(photo):
        img = pygame.image.load(photo).convert()
        img.set_colorkey((0,0,0))
        img = pygame.transform.scale(img, blockwymiary)

        return img
    
    sprite = imgtosprite('./imgs/spritetest.png')

    while True:
        Emergency_Stop()
        display.blit(sprite, spritepos)

        screen.blit(pygame.transform.scale(display, screen.get_size()), (0,0))
        pygame.display.update()
 
Renderowanie_Postaci()
    
