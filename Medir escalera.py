import math

distanciapared=float(input("Altura de la pared: "))
angulo=float(input("Ángulo: "))


anguloradianes=math.radians(angulo)
Escalera= distanciapared/math.sin(anguloradianes)

print("Escalera mide: ", Escalera)