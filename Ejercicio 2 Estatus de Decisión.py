'''
Ejercicio 2
Escribe un programa que dados 3 números enteros, que representan la longitud de los lados de un triángulo, muestre en la pantalla el tipo de triángulo de que se trata (equilátero, isósceles o escaleno).

Considera que X, Y y Z son los lados de un triángulo si cumplen con las siguientes condiciones:

Todos los números son mayores que cero
X + Y > Z
X + Z > Y
Y + Z > X
es decir, la suma de dos de las medidas debe ser estrictamente mayor que la tercera.   

Recuerda que el triángulo equilátero tiene 3 lados iguales, el isósceles tiene 2 lados iguales y el escaleno tiene los 3 lados diferentes.
'''

X=int(input("Dame X: "))
Y=int(input("Dame Y: "))
Z=int(input("Dame Z: "))

if(X>0 and Y>0 and Z>0 and (X+Y)>Z and (X+Z)>Y and (Y+Z)>X):
    print("Triángulo Válido")
    
    if (X==Y and X==Z and Y==Z):
        print("Triángulo Equilatero")
    
    elif(X==Y or X==Z or Z==Y):
       print("Triángulo Isósceles")
       
    else:
        print("Triángulo Escaleno")
        
        
else:
    print("Triángulo Inválido")
    
