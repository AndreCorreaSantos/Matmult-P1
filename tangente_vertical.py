import numpy as np
import math

def processa(lista):
    dicionario = {}

    for i in range(0,len(lista)):

        if round(lista[i],3) not in dicionario.keys() and round(lista[i],3)+0.01 not in dicionario.keys() and round(lista[i],3)-0.01 not in dicionario.keys() :
            dicionario[round(lista[i],2)] = lista[i]


    return dicionario


range_t = np.arange(0,math.pi*6,0.0001)

def derivada_x(t):
    return -5*math.sin(t)+8*math.sin(8*t/3)

def derivada_y(t):
    return  5*math.cos(t)-8*math.cos(8*t/3)

tangente_vertical = []
tangente_horizontal = []

for t in range_t:
    dx = derivada_x(t)
    dy = derivada_y(t)
    if round(dx,2) == 0.000:
        tangente_vertical.append(t)
    if round(dy,2) == 0.000:
        tangente_horizontal.append(t)



print(len(processa(tangente_horizontal)))
tan_v = processa(tangente_vertical)

print(len(tan_v))