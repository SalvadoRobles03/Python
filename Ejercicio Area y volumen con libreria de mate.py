#programa para calcular área y volumen de una esfera
import math

radio=float(input("Dame el Radio, por favor: "))

area=4*(math.pi)*(radio**2)
volumen= (4*(math.pi)*(radio**3))/3

print("El área de la esfera es: ", area)
print ("El Volumen de la esfera es: ", volumen)