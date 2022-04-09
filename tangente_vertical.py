import numpy as np
import math

def processa(lista):
    lista2 = []

    for i in lista:
        dif = True
        for u in lista2:
            if abs(i-u)/(i) < 0.01:
                dif = False
                break
        if dif:
            lista2.append(i)
    return lista2


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



tan_v = processa(tangente_vertical)
tan_h = processa(tangente_horizontal)

tan_v = tan_v[3:]


print(tan_h)
print(tan_v)
