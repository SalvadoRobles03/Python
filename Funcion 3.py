def precioFinal(iva):
    
    if iva == "S" or iva == "s":
        return 1.16
    else:
        return 1

def pideProducto():
    precio = float(input("Dame el Precio: "))
    iva = input("S/N: ")
    
    
    factor = precioFinal(iva)
    
    return precio * factor

precio = pideProducto()
print("precio", precio)    
