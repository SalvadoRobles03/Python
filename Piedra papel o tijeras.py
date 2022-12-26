
def pidenombre():
    
    nombre=input("Dame tu nombre: ")
    
    return nombre
def eleccionJuego(jugador1):
    
    print("Hola ", jugador1, "\nBienvenido a Piedra, Papel o Tijeras")
    
    elección=input("Piedra, Papel o Tijeras: ")
    elección= elección.upper()
    elección= elección.strip()
    
    if (elección=="PIEDRA" or elección=="PAPEL" or elección=="TIJERAS"):
        return elección
    else:
        print("Perdiste")
        return "Pongale las cosas bien"
    
def ganador(jugador1juega,jugador2juega):
    if (jugador1juega == jugador2juega):
        print("Empate")
    elif (jugador1juega == "PIEDRA" and jugador2juega == "TIJERAS" or jugador1juega == "TIJERAS" and jugador2juega == "PAPEL" or jugador1juega == "PAPEL" and jugador2juega == "PIEDRA"):
        respuesta=jugador1,"es el ganador"
        
        return respuesta
    else:
        respuesta=jugador2,"es el ganador"
        
        return respuesta
        
        

jugador1=pidenombre()
jugador2=pidenombre()

jugador1juega=eleccionJuego(jugador1)
jugador2juega=eleccionJuego(jugador2)

if(jugador1juega=="Pongale las cosas bien" and jugador2juega=="Pongale las cosas bien"):
    print("No son aptos para este juego")

elif(jugador1juega=="Pongale las cosas bien"):
    print("Gana", jugador2, "porque", jugador1,"Esta bien tonto")

elif(jugador2juega=="Pongale las cosas bien"):
    print("Gana", jugador1, "porque", jugador2,"Esta bien tonto")
    
else:
    print(ganador(jugador1juega,jugador2juega))
    

