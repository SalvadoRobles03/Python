#12Oct,13Oct,14Oct


import pandas as pd
pd.options.mode.chained_assignment = None #default="warn"
import matplotlib.pyplot as plt
import numpy as np
import datetime
import openpyxl

def pideCiudades(mensaje,listaCiudades):
    texto=input(mensaje)
    texto=texto.upper()
    texto=texto.strip()
    #print(np.isin(listaCiudades,texto))
    #print(np.argwhere(np.isin(listaCiudades,texto)))
    if(len(np.argwhere(np.isin(listaCiudades,texto)))==0):
        texto=pideCiudades(mensajes,listaCiudades)
    return texto
        
    
    
def pideNumeroPositivo(mensaje):
    num=int(input(mensaje))
    if (num < 0):
        pideNumeroPositivo(mensaje)        
    return num

hoy=datetime.datetime.now()


ayer=str(int(hoy.strftime("%d"))-1)+hoy.strftime("%b")
resultados=pd.read_excel("Resultados1.xlsx",ayer)


ciudades=resultados["Ciudad"]
listaCiudades=ciudades.unique()
print("Lista de ciudades disponibles", listaCiudades)

ciudad=pideCiudades("Ingrese la ciudad: ",listaCiudades)

resultadosCiudad=resultados.groupby("Ciudad").get_group(ciudad)

print(resultadosCiudad)

idCambio=pideNumeroPositivo("Dame el ID para el cambio: ")
puntosCambio=pideNumeroPositivo("Dame el nuevo puntaje: ")



IDs=resultados["ID"]
indice=np.where(IDs==idCambio)

resultados["Puntaje"][indice[0][0]]=puntosCambio

fecha=hoy.strftime("%d%b")

workbook=pd.ExcelWriter("Resultados1.xlsx",engine="openpyxl", mode="a")

resultados.to_excel(workbook,fecha,index=False)

workbook.save()

puntos=[]

for i in listaCiudades:
    resultadosCiudad=resultados.groupby("Ciudad").get_group(i)
    puntaje=resultadosCiudad["Puntaje"]
    puntos.append(round(puntaje.mean(),0))
    
print(listaCiudades)
print(puntos)

barlist=plt.bar(listaCiudades,puntos)
barlist[0].set_color("r")
barlist[1].set_color("g")
barlist[2].set_color("m")
barlist[3].set_color("c")
barlist[4].set_color("b")
plt.xlabel("Ciudades")
plt.ylabel("Puntaje")
plt.xticks(rotation=90)
plt.title("Donkeys")
plt.show()



