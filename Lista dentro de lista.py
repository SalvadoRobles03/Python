def pideLimpiaTexto(mensaje):
    texto=input(mensaje)
    texto=texto.upper()
    texto=texto.strip()
    
    return texto

lista=[]

for i in range (3):
    
    humane=[]
    
    nombre=pideLimpiaTexto("Dame tu Nombre:")
    humane.append(nombre)
    
    equipo=pideLimpiaTexto("Dame tu Equipo de la NFL:")
    humane.append(equipo)
    
    rating=int(input("Rating del equipo (0-10):"))
    humane.append(rating)
    
    lista.append(humane)
    


print(lista)