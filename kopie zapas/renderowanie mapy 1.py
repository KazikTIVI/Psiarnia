import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption('base game')
screen = pygame.display.set_mode((900, 900), 0, 32)
display = pygame.Surface((300, 300))

grass_img = pygame.image.load('grasstestfull.png').convert()
grass_img.set_colorkey((0, 0, 0))
grass_img = pygame.transform.scale(grass_img, (20,22))

sciana_img = pygame.image.load('sciana.png').convert()
sciana_img.set_colorkey((0, 0, 0))

sciana2_img = pygame.image.load('sciana2.png').convert()
sciana2_img.set_colorkey((0, 0, 0))

mapa_ziemia = open('map2.txt')
map_data = [[int(c) for c in row] for row in mapa_ziemia.read().split('\n')]
mapa_ziemia.close

mapa_sciany = open('map3.txt')
map2_data = [[int(c) for c in row] for row in mapa_sciany.read().split('\n')]
mapa_sciany.close

mapa2_sciany = open('map4.txt')
map2vol2_data = [[int(c) for c in row] for row in mapa2_sciany.read().split('\n')]
mapa2_sciany.close

while True:
    display.fill((0,0,0))

    # renderowanie mapy
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile:
                pygame.draw.rect(display, (255,255,255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                display.blit(grass_img, (150 + x*10 - y*10, 100 + x*4 + y*4))

    for y, row in enumerate(map2_data):
        for x, tile in enumerate(row):
            if tile:
                pygame.draw.rect(display, (255,255,255), pygame.Rect(x * 10, y * 10, 10, 10), 1)           
                display.blit(sciana_img, (150 + x*10 - y*10, 100 + x*4 + y*4 - 21))

    for y, row in enumerate(map2vol2_data):
        for x, tile in enumerate(row):
            if tile:
                pygame.draw.rect(display, (255,255,255), pygame.Rect(x * 10, y * 10, 10, 10), 1)           
                display.blit(sciana2_img, (150 + x*10 - y*10, 100 + x*4 + y*4 - 21))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0,0))
    pygame.display.update()

