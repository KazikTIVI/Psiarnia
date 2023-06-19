global lista_map

lista_map = []

def mapy(mapa):
        mapa = open(mapa)
        map_data = [[int(c) for c in row] for row in mapa.read().split('\n')]
        mapa.close
        
        lista_map.append(map_data)
        return map_data

mapa_ziemia = mapy('./mapy/mapa_parter.txt')
mapa_1_pietro = mapy('./mapy/mapa_1_pietro.txt')

print(lista_map)