import numpy as np


def pideNumeroPositivo(mensaje):
    num=int(input(mensaje))
    if (num < 0):
        pideNumeroPositivo(mensaje)
            
    return num

print("Captura y creación de matrices\n")
renglones = pideNumeroPositivo("Dame los renglones: ")
Columnas = pideNumeroPositivo("Dame los columnas: ")

if(renglones==Columnas):
    matriz=np.zeros((renglones, Columnas))
    
    for i in range (renglones):
        renglonTemp=[]
        for j in range (Columnas):
            posicion= "["+ str(i+1) + "][" + str(j+1) +"]="
            elemento = int(input(posicion))
            matriz[i][j]=elemento
    print(matriz)
    diagonal = np.diag(matriz)
    print("\nDiagonal=",diagonal)
else:
    print("Ni volviendo a nacer...")
    

    

