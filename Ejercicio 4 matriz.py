"""
|a    b|
|c    d|

det = a*d - c*b

numero1,numero2=map(int,input("Please Enter your numbers: ").split())
"""

import numpy as np


def pideNumeroPositivo(mensaje):
    num=int(input(mensaje))
    if (num < 0):
        pideNumeroPositivo(mensaje)
            
    return num

print("Captura y creación de matrices\n")
renglones = 2
Columnas = 2


matriz=np.zeros((renglones, Columnas))
print(matriz)

for i in range (renglones):
    renglonTemp=[]
    for j in range (Columnas):
        posicion= "["+ str(i+1) + "][" + str(j+1) +"]="
        elemento = float(input(posicion))
        matriz[i][j]=elemento
    
det = matriz[0][0]*matriz[1][1]-matriz[1][0]*matriz[0][1]

print("\n", det)
