import math

Ni=float(input("Población Inicial: "))
r=float(input("Tasa: "))
t=float(input("Tiempo: "))

población=Ni*math.exp(r*t)
población=math.floor(población)

print("El número de población es: ", población)