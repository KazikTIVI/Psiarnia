import pygame,sys
from renderowanie_mapy import *

lista_map = Renderowanie_Ziemi()

# print(lista_map)

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