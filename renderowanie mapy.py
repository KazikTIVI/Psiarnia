import pygame, sys
from pygame.locals import *

def Renderowanie_Ziemi():

    pygame.init()
    pygame.display.set_caption('base game')
    screen = pygame.display.set_mode((900, 900), 0, 32)
    display = pygame.Surface((300, 300))

    lista_img = []
    blockwymiary = (40,44)
    scianawymiary = (40,44)
    def images(photo,wymiary):
        img = pygame.image.load(photo).convert()
        img.set_colorkey((0,0,0))
        img = pygame.transform.scale(img, wymiary)

        lista_img.append(img)
        return img

    grass_img = images('grasstest.png',blockwymiary)
    sciana_img = images('gruba_scianal.png',scianawymiary)
    sciana2_img = images('scianap.png',scianawymiary)


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
                        display.blit(img, (150 + x*20 - y*20, 100 + x*8 + y*8-offset))

        mapowanie(mapa2_sciany,sciana2_img,36)
        mapowanie(mapa_ziemia,grass_img,0)
        mapowanie(mapa_sciany,sciana_img,29)


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

Renderowanie_Ziemi()