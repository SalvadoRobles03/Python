import math

area= float(input("Área a pintar: "))
metroslitros= float(input("Metros por litro: "))

litros=math.ceil(area/metroslitros)

print("Litros a comprar: ", litros)