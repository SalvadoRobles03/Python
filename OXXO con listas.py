import math

def limpiaTexto(mensaje):
    texto=input(mensaje)
    texto=texto.upper()
    texto=texto.strip()
    
    return texto

continua="S"

cliente=[]

while(continua=="S"):
    item=[]
    producto=limpiaTexto("Producto: ")
    cantidad=int(input("Cantidad: "))
    precio=float(input("Precio: "))
    totalItem=cantidad*precio
    
    item.append(producto)
    item.append(cantidad)
    item.append(precio)
    item.append(totalItem)
    
    cliente.append(item)
    
    continua=limpiaTexto("Más? S/N: ")
    
totalcosas=len(cliente)
Total=0
for i in range (totalcosas):
    Total+=cliente[i][3]
    


print("Total a Pagar: ", Total)
redondea=limpiaTexto("Redondea? S/N: ")

if (redondea=="S"):
    Total=math.ceil(Total)
print("Total a Pagar: ", Total)
    
dinero=float(input("Dinero: "))

cambio=dinero-Total

while(cambio<0):
    print("Saldo pendiente: ", cambio*(-1))
    dinero=float(input("Dinero: "))
    cambio=cambio+dinero

print("Cambio:",cambio)

     
     