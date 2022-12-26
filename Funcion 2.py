def pideDatos():
    
    nombre=input("Dame tu Nombre: ")
    Edad=int(input("Dame tu Edad: "))
    Estatura=float(input("Dame tu estatura: "))
    Peso=float(input("Dame tu peso: "))
    Needy=bool(input("Tienes Novia? "))
    
    return nombre, Edad, Estatura, Peso, Needy

def ValidaPositivo(numero, texto):
    if(numero>0):
        print("El valor de ",texto, "es válido")
        
    else:
        print("El valor de ",texto, "es inválido")
        

nombre, Edad, Estatura, Peso, Needy = pideDatos()

ValidaPositivo(Edad, "Edad")
ValidaPositivo(Estatura, "Estatura")
ValidaPositivo(Peso, "Peso")

if(Needy==False):
    print("Pongase a jalar")
else:
    print("Fino, Caballero")

