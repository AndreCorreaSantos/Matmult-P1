from math import *
import numpy as np



def calcula_dist_centro(p1):
    return sqrt((p1[0]**2)+(p1[1]**2))

def calcula_dist(p1,p2):
    return sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

def calcula_h(p1,p2):
    ponto_medio_segmento_p1p2 = (((p1[0]+p2[0])/2),((p1[1]+p2[1])/2))
    return calcula_dist_centro(ponto_medio_segmento_p1p2)


def funcao(t):
    return (5*cos(t)-3*cos(8*t/3),5*sin(t)-3*sin(8*t/3))



range_t = np.arange(0,pi*6,0.00005)

lista_pontos = []
min_dist = 7.6113
for i in range_t:
    lista_pontos.append(funcao(i))

app = False
dic_pontos_externos = {1:[],2:[],3:[],4:[],5:[],}

contador = 0
for i in range(0,len(lista_pontos)):
    if calcula_dist_centro(lista_pontos[i]) >= min_dist:
        if app == False:
            contador+=1
        app = True
        dic_pontos_externos[contador].append(lista_pontos[i])
    else:
        app = False


lista_pontos_ordenados = dic_pontos_externos[4] + dic_pontos_externos[1] + dic_pontos_externos[3] + dic_pontos_externos[5] + dic_pontos_externos[2]

area_interna = 0

for i in range(0,len(lista_pontos_ordenados)):
    if i != 0:
        base = calcula_dist(lista_pontos_ordenados[i],lista_pontos_ordenados[i-1])
        altura = calcula_h(lista_pontos_ordenados[i],lista_pontos_ordenados[i-1])
        area_interna += (base*altura)/2

print(area_interna)