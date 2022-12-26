"""
Ejercicio 2
Escribe un programa que dados 3 números enteros, que representan la longitud de los lados de un triángulo,
muestre en la pantalla el tipo de triángulo de que se trata (equilátero, isósceles o escaleno).

Considera que X, Y y Z son los lados de un triángulo si cumplen con las siguientes condiciones:

Todos los números son mayores que cero
X + Y > Z
X + Z > Y
Y + Z > X
es decir, la suma de dos de las medidas debe ser estrictamente mayor que la tercera.    

Recuerda que el triángulo equilátero tiene 3 lados iguales, el isósceles tiene 2 lados iguales y
el escaleno tiene los 3 lados diferentes.
"""

X=int(input("Dame el lado X: "))
Y=int(input("Dame el lado Y: "))
Z=int(input("Dame el lado Z: "))

#es triángulo válido si...
if(X>0 and Y>0 and Z>0 and (X + Y) > Z and (X + Z) > Y and (Y + Z) > X):
    print("SI es un triángulo válido")
    #equilátero
    if(X==Y and X==Z and Y==Z):
       print("Triángulo equilátero")      
    
    #isósceles
    #elif( (X==Y and X!=Z) or(X==Z and X!=Y) or ( Y==Z and Y!=X)):
    elif( X==Y or X==Z or Y==Z ):
        print("Triángulo isósceles")
    
    #escaleno
    else:
        print("Triángulo escaleno")
    
else:
    print("NO es un triángulo válido")
    