

#Sacar el perimetro de un cuadrado o Rectangulo

def Perimetro():
    
    PerimetroFinal = (Lado1*2)+(Lado2*2)
    
    return PerimetroFinal

Lado1 = float(input("Deme el Lado 1 en centimetros: "))
Lado2 = float(input("Deme el Lado 2 en centimetros: "))


print("El perimetro de su cuadrado es: ", Perimetro(), "Cm")