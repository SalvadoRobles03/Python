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
    
sumaColumna=0
textoSalida= "["
for j in range (Columnas):
    pares=0
    for i in range (renglones):
        sumaColumna+=matriz[i][j]
    textoSalida=textoSalida+str(sumaColumna)+" "

textoSalida=textoSalida.strip()
textoSalida=textoSalida+"]"
    
print("\n",textoSalida)
