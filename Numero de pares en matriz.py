import numpy as np


def pideNumeroPositivo(mensaje):
    num=int(input(mensaje))
    if (num < 0):
        pideNumeroPositivo(mensaje)
            
    return num

print("Captura y creación de matrices\n")
renglones = pideNumeroPositivo("Dame los renglones: ")
Columnas = pideNumeroPositivo("Dame los columnas: ")


matriz=np.zeros((renglones, Columnas))
print(matriz)

for i in range (renglones):
    renglonTemp=[]
    for j in range (Columnas):
        posicion= "["+ str(i+1) + "][" + str(j+1) +"]="
        elemento = int(input(posicion))
        matriz[i][j]=elemento
    
listadepares=[]

for i in range (renglones):
    renglonTemp=[]
    pares=0
    for j in range (Columnas):
        if(matriz[i][j]%2==0):
            pares +=1
    listadepares.append(pares)
    
print("\n", listadepares)
