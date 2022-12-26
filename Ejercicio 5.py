
precio= float(input("Dame el precio del producto por Kilo en pesos: "))
peso=float(input("Dame el peso del producto en Kilogramos: "))


if (precio>0 and peso>0):
    
    Cantidadfinal = precio*peso

    print (Cantidadfinal)

else:
    print("Ingrese valores validos")