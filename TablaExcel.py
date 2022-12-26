#Day	Hour	Minute	Temperature	pH	Turbidity


import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

def pideNumeroPositivo(mensaje):
    num=int(input(mensaje))
    if (num < 0):
        pideNumeroPositivo(mensaje)        
    return num

tabla= pd.read_excel("SensorData.xlsx")

dia=pideNumeroPositivo("Dame el día: ")
grupoDia="2020-01-"+str(dia)

tableDay=tabla.groupby("Day").get_group(grupoDia)

hora=pideNumeroPositivo("Dame la hora: ")
tableHour=tableDay.groupby("Hour").get_group(hora)

#print (tableHour)

temperature=tableHour["Temperature"]

print ("\nTemperatura")
print ( "Min: ", temperature.min())
print ("Max: ", temperature.max())
print("Promedio: ", temperature.mean())

ph=tableHour["pH"]

print ("\npH")
print ( "Min: ", ph.min())
print ("Max: ", ph.max())
print("Promedio: ", ph.mean())

turbidity=tableHour["Turbidity"]

print ("\nTurbidity (NTU)")
print ("Max: ", turbidity.max())
