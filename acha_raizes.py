import math
import numpy

rang = numpy.arange(-6*math.pi+0.0001,0,0.00001)

def funcao_B(x,k):
    if k == 1:
        return (5*math.sin((3*math.pi)/5)*math.sin(x/2)) - (3*math.sin((8*math.pi)/5)*math.sin(4*x/3))
    if k ==2:
        return (5*math.sin((6*math.pi)/5)*math.sin(x/2)) - (3*math.sin((16*math.pi)/5)*math.sin(4*x/3))
    if k ==3:
        return (5*math.sin((9*math.pi)/5)*math.sin(x/2)) - (3*math.sin((24*math.pi)/5)*math.sin(4*x/3))
    if k ==4:
        return (5*math.sin((12*math.pi)/5)*math.sin(x/2)) - (3*math.sin((32*math.pi)/5)*math.sin(4*x/3))

def acha_raiz(k):
    raizes = []
    for i in rang:
        if round(funcao_B(i,k),4) == 0.0000:
            raizes.append(i)
    return raizes

def curva(x):
    return (5*math.cos(x)-3*math.cos(8*x/3),5*math.sin(x)-3*math.sin(8*x/3))

raizes_k1 = acha_raiz(1)
raizes_k2 = acha_raiz(2)
raizes_k3 = acha_raiz(3)
raizes_k4= acha_raiz(4)



#para k0 u+v = pi/2 ||| raiz + 2v = pi/2 --> v = (p/2 - raiz)/2 || u = pi/2 - v

uvs_k1 = []
uvs_k2 = []
uvs_k3 = []
uvs_k4 = []
for raiz in raizes_k1:
    variavel = (6*math.pi)/5
    v = ((variavel)-raiz)/2
    u = (variavel) - v
    uvs_k1.append((u,v))

for raiz in raizes_k2:
    variavel = (12*math.pi)/5
    v = ((variavel)-raiz)/2
    u = (variavel) - v
    uvs_k2.append((u,v))

for raiz in raizes_k3:
    variavel = (18*math.pi)/5
    v = ((variavel)-raiz)/2
    u = (variavel) - v
    uvs_k3.append((u,v))

for raiz in raizes_k4:
    variavel = (24*math.pi)/5
    v = ((variavel)-raiz)/2
    u = (variavel) - v
    uvs_k4.append((u,v))

print(uvs_k4)