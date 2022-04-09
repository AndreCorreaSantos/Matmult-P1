import math
import numpy

rang = numpy.arange(-6*math.pi+0.0001,0,0.00001)

def funcao_B(x,k):
    if k == 0:
        return (5*math.sin((3*math.pi)/5)*math.sin(x/2)) - (3*math.sin((8*math.pi)/5)*math.sin(4*x/3))

def acha_raiz(k):
    raizes = []
    for i in rang:
        if round(funcao_B(i,k),4) == 0.0000:
            raizes.append(i)
    return raizes

def curva(x):
    return (5*math.cos(x)-3*math.cos(8*x/3),5*math.sin(x)-3*math.sin(8*x/3))

raizes_k0 = acha_raiz(0)



#para k0 u+v = pi/2 ||| raiz + 2v = pi/2 --> v = (p/2 - raiz)/2 || u = pi/2 - v
uvs_k0 = []
uvs_k1 = []
uvs_k2 = []
for raiz in raizes_k0:
    variavel = (-6*math.pi)/5
    v = ((variavel)-raiz)/2
    u = (variavel) - v
    uvs_k0.append((u,v))

print(uvs_k0)