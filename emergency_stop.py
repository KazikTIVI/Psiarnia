import pygame, sys
from pygame.locals import *

def Emergency_Stop():
    for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()