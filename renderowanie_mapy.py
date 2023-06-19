import pygame, sys
from pygame.locals import *
from emergency_stop import Emergency_Stop

def Renderowanie_Ziemi():

    # def ustawienia okna
    # pygame.init()
    pygame.display.set_caption('base game')
    screen = pygame.display.set_mode((900, 900), 0, 32)
    display = pygame.Surface((300, 300))
    

    # consty
    lista_img = []
    lista_map = []
    blockwymiary = (40,44)
    scianawymiary = (40,44)

    def images(photo,wymiary):
        img = pygame.image.load(photo).convert()
        img.set_colorkey((0,0,0))
        img = pygame.transform.scale(img, wymiary)

        lista_img.append(img)
        return img

    # fotki 
    # !! ustawiac w kolejnosci do renderowania !!
    # !! indx == liczba w mapach
    
    # 1 pietro
    """0"""
    grass_img = images('./imgs/grasstest.png',blockwymiary)
    
    # 2 pietro 
    """1"""
    sciana_img = images('./imgs/gruba_scianal.png',scianawymiary)
    """2"""
    scianasr_img = images('./imgs/gruba_scianasr.png',scianawymiary) 
    """3"""
    sciana2_img = images('./imgs/gruba_scianap.png',scianawymiary) 



    def mapy(mapa):
        mapa = open(mapa)
        map_data = [[int(c) for c in row] for row in mapa.read().split('\n')]
        mapa.close
        lista_map.append(map_data)
        return map_data

    # mapy
    mapa_ziemia = mapy('./mapy/mapa_parter.txt')
    mapa_1_pietro = mapy('./mapy/mapa_1_pietro.txt')


    while True:
        display.fill((0,0,0))
        Emergency_Stop()

        def mapowanie_parter(mapa,img):
            for y, row in enumerate(mapa):
                for x, tile in enumerate(row):
                    if tile == 1:
                        pygame.draw.rect(display, (255,255,255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                        display.blit(img, (150 + x*20 - y*20, 100 + x*8 + y*8))

        def mapowanie_2_pietro(mapa,nr_1_img_do_renderowania,nr_ostatniego_img_do_renderowania):
            for y, row in enumerate(mapa):
                for x, tile in enumerate(row):
                    for kafelka in range(nr_1_img_do_renderowania,nr_ostatniego_img_do_renderowania+1):
                        if tile == kafelka:
                            img = lista_img[kafelka]
                            pygame.draw.rect(display, (255,255,255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                            display.blit(img, (150 + x*20 - y*20, 100 + x*8 + y*8-29))

        mapowanie_parter(mapa_ziemia,grass_img)
        mapowanie_2_pietro(mapa_1_pietro,1,3)


        screen.blit(pygame.transform.scale(display, screen.get_size()), (0,0))
        pygame.display.update()
        return lista_map

Renderowanie_Ziemi()