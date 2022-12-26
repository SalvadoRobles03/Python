def limpiaTexto(Peticion):
    texto=input(Peticion)
    texto=texto.upper()
    texto=texto.strip()
    
    return texto

cuenta=0

while (True):
    Producto=limpiaTexto("Deme el nombre del producto: ")    
    precio=float(input("Deme el precio del producto: "))

    if (Producto == "GANSITO"):
        break
    
    if(precio>0):
        cuenta=cuenta+precio
    else:
        print("Agregue valores positivos")
    
    
    
for i in range(5):
    print("\n\nFELICIDADES EL OXXO TE REGALA ALGO")
print("Su precio total es:", cuenta, "pesos")
            