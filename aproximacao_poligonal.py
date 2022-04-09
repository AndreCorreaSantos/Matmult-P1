from math import *
import numpy as np

def calcula_dist(p1,p2):
    return sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

def funcao(t):
    return (5*cos(t)-3*cos(8*t/3),5*sin(t)-3*sin(8*t/3))



range_t = np.arange(0,pi*6,0.00005)

lista_pontos = []
for i in range_t:
    lista_pontos.append(funcao(i))

dist = 0
for i in range(0,len(lista_pontos)):
    if i != 0:
        dist += calcula_dist(lista_pontos[i],lista_pontos[i-1])

print(dist)