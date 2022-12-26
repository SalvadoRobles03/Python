def validarTriangulo (X,Y,Z):
    if(X>0 and Y>0 and Z>0 and (X+Y)>Z and (X+Z)>Y and (Y+Z)>X):
        
        Valido=True
    else:
        Valido=False
    
    return Valido

X=int(input("Dame X: "))
Y=int(input("Dame Y: "))
Z=int(input("Dame Z: "))

Valido =validarTriangulo (X,Y,Z)

if(Valido):
    print("Triángulo Válido")
    
    if (X==Y and X==Z and Y==Z):
        print("Triángulo Equilatero")
    
    elif(X==Y or X==Z or Z==Y):
       print("Triángulo Isósceles")
       
    else:
        print("Triángulo Escaleno")
        
        
else:
    print("Triángulo Inválido")
    
