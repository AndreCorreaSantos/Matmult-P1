from math import *
def primitiva(t):
    # t1 = (135*sin(5*t/3))/10
    # t2 = -(135*sin(11*t/3))/22
    # t3 = -26*t
    # t4 = 25*sin(t)*cos(t)/2
    # t5 = 9*sin(8*t/3)*cos(8*t/3)/2
    t1 = -25*(t-(sin(t)*cos(t)))
    t2 = 45*((3*sin(5*t/3)/5)-(3*sin(11*t/3)/11))
    t3 = -9*((8*t/3)-(sin(8*t/3)*cos(8*t/3)))
    return t1+t2+t3

def calcula_integral(t1,t2):
    return primitiva(t2) - primitiva(t1)

#intervalos_integracao = [(5.266,6.043),(12.806,13.583),(1.496,2.273),(9.036,9.813),(-2.273,-1.496)]

intervalos_integracao = [[1.4966044077181078, 2.2733138154634673],[5.266518553152036,  6.043217960897396],[ 9.036419737459788, 9.813134145205147],[12.806, 13.5830403295129],[16.5765, 17.3529]]


integral = 0
for i in intervalos_integracao:
    integral += abs(calcula_integral(i[0],i[1]))
print(integral)