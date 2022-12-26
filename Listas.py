def limpiaTexto(mensaje):
    texto=input(mensaje)
    texto=texto.upper()
    texto=texto.strip()
    
    return texto

listaNombres=[]
listaEquipos=[]
listaRating=[]


for i in range(3):
    nombre=limpiaTexto("Dame tu nombre: ")
    listaNombres.append(nombre)
    
    equipo=limpiaTexto("Dame tu equipo de NFL: ")
    listaEquipos.append(equipo)
    
    rating=int(input("Rating: del equipo (0-10): "))
    listaRating.append(rating)
    
    
    
print(listaNombres)
print(listaEquipos)
print(listaRating)
    

