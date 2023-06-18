import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption('base game')
screen = pygame.display.set_mode((900, 900), 0, 32)
display = pygame.Surface((300, 300))

lista_img = []

def images(photo):
    img = pygame.image.load(photo).convert()
    img.set_colorkey((0,0,0))
    if photo == 'grasstestfull.png':
        img = pygame.transform.scale(img, (20,22))

    lista_img.append(img)
    return img

grass_img = images('grasstestfull.png')
sciana_img = images('sciana.png')
sciana2_img = images('sciana2.png')


lista_map = []

def mapy(mapa):
    mapa = open(mapa)
    map_data = [[int(c) for c in row] for row in mapa.read().split('\n')]
    mapa.close
    lista_map.append(map_data)
    return map_data

mapa_ziemia = mapy('map2.txt')
mapa_sciany = mapy('map3.txt')
mapa2_sciany = mapy('map4.txt')


while True:
    display.fill((0,0,0))

    def mapowanie(mapa,img,offset):
        for y, row in enumerate(mapa):
            for x, tile in enumerate(row):
                if tile:
                    pygame.draw.rect(display, (255,255,255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                    display.blit(img, (150 + x*10 - y*10, 100 + x*4 + y*4-offset))

    mapowanie(mapa_ziemia,grass_img,0)
    mapowanie(mapa_sciany,sciana_img,21)
    mapowanie(mapa2_sciany,sciana2_img,21)
    

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

