def limpiar(mensaje):
    texto=input(mensaje)
    texto=texto.strip()
    texto=texto.lower()
    return texto

nombres = ["juan", "pedro", "ximena", "sofia", "ana"]

continua="s"

while(continua == "s"):
    name=limpiar("Dame un nombre: ")
    
    for i in nombres:
        if(i == name):
            print("Adivinaste")
            explota="KABOOM"
            break
        else:
            print(i, "es diferente de", name)
            print("Ni siquiera se quien eres")
            print("-------------------------------------")
            continua=limpiar("Continuar? S/N: ")
            if(continua == "n"):
                explota="KABOOM"
                break
            
        

print("Explotó el universo")
        