import math

a= float(input("Por favor ponga el Ángulo A: "))
b= float(input("Por favor ponga el Ángulo B: "))
c= float(input("Por favor ponga el Ángulo C: "))

s=(a+b+c)/2

area= math.sqrt(s*(s-a)*(s-b)*(s-c))

print("El area es: ", area)