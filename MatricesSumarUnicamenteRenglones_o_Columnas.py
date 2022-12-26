import numpy as np


def pideNumeroPositivo(mensaje):
    num=int(input(mensaje))
    if (num < 0):
        pideNumeroPositivo(mensaje)
            
    return num

def pideNumeroPositivo2():
    num=int(input())
    if (num != 1 and num != 2):
        pideNumeroPositivo2()
            
    return num

print("Captura y creación de matrices\n")
renglones = pideNumeroPositivo("Dame los renglones: ")
Columnas = pideNumeroPositivo("Dame los columnas: ")


matriz=np.zeros((renglones, Columnas))


for i in range (renglones):
    renglonTemp=[]
    for j in range (Columnas):
        posicion= "["+ str(i+1) + "][" + str(j+1) +"]="
        elemento = int(input(posicion))
        matriz[i][j]=elemento
        
print(matriz)
    
print("Elige que quieres sumar, por favor")
print("\n1. Renglones")
print("2. Columnas\n")
eleccion=pideNumeroPositivo2()
if (eleccion ==1):
    renglonSuma=pideNumeroPositivo("Dame el renglon a sumar: ")
    print("Suma de renglón: ", matriz[renglonSuma,:].sum())
else:
    columnaSuma=pideNumeroPositivo("Dame la columna a sumar: ")
    print("Suma de columna: ", matriz[:,columnaSuma].sum())


