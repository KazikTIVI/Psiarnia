import pygame,sys
from pygame.locals import *
from conf_mapy import *
from emergency_stop import *

print(lista_map)

def kolizje():
    warstwa = 0
    xprzedwyprowadzeniem = 0
    yprzedwyprowadzeniem = 0

    for warstwa_mapa in lista_map:
        warstwa += 1
        for mapa in warstwa_mapa:
            yprzedwyprowadzeniem += 1
            for szerokosc_mapy in mapa:
                xprzedwyprowadzeniem += 1

    ywlasciwy = int(yprzedwyprowadzeniem/warstwa)
    xwlasciwy = int(xprzedwyprowadzeniem/(ywlasciwy*warstwa))
    print('ilosc warstw ', warstwa)
    print('wartosc y ', ywlasciwy)
    print('wartosc x ', xwlasciwy)

    
    
kolizje()