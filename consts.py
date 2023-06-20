import pygame
displaywymiary = 900
blocky = 40
blockx = 40
blockwymiary = (blockx,blocky)
scianawymiary = (blockx,blocky)

pygame.display.set_caption('base game')
screen = pygame.display.set_mode((displaywymiary, displaywymiary), 0, 32)
display = pygame.Surface((displaywymiary/3, displaywymiary/3))
clock = pygame.time.Clock()

spriteposx = displaywymiary/6-20
spriteposy = displaywymiary/6-70