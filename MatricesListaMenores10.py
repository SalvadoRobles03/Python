import numpy as np


def pideNumeroPositivo(mensaje):
    num=int(input(mensaje))
    if (num < 0):
        pideNumeroPositivo(mensaje)
            
    return num
def capturaMatriz():
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
        return matriz, renglones,Columnas

def listaMenores10(matriz,renglones,Columnas):
    lista=[]
    for i in range (renglones):
        for j in range (Columnas):
            if (matriz[i][j]<10):
                lista.append(matriz[i][j])
    return lista

matriz,renglones,Columnas=capturaMatriz()
print(listaMenores10(matriz,renglones,Columnas))
        

    