def validarTriangulo (X,Y,Z):
    if(X>0 and Y>0 and Z>0 and (X+Y)>Z and (X+Z)>Y and (Y+Z)>X):
        
        Valido=True
    else:
        Valido=False
        print("Pon valores validos, crack")
    
    return Valido

valido=False
while(valido==False):
    X=int(input("Dame X: "))
    Y=int(input("Dame Y: "))
    Z=int(input("Dame Z: "))
    
    Valido =validarTriangulo (X,Y,Z)
    
    if (X==Y and X==Z and Y==Z):
        print("Triángulo Equilatero")
        valido=True
    
    elif(X==Y or X==Z or Z==Y):
        print("Triángulo Isósceles")
        valido=True
    
    else:
        print("Triángulo Escaleno")
        valido=True

    
