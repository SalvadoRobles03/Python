def pideNumeroPositivo(mensaje):
    num=int(input(mensaje))
    if (num < 0):
        pideNumeroPositivo(mensaje)
            
    return num

def pideNumeroPositivo1a4():    
    num=int(input())
    if (num < 1 or num > 4):
        pideNumeroPositivo1a4()
            
    return num


def pideLimpiaTexto(mensaje):
    texto=input(mensaje)
    texto=texto.upper()
    texto=texto.strip()
    return texto

def capturaPerros(dataBasePerruna):
    print ("Captura perrillos: ")
    data = []
    nombre=pideLimpiaTexto("Dame el nombre: ")  
    peso=pideNumeroPositivo("Dame el peso: ")
    color=pideLimpiaTexto("Dame el color: ")
    edad=pideNumeroPositivo("Dame la edad: ")
    data.append(peso)
    data.append(color)
    data.append(edad)
    dataBasePerruna[nombre]=data
    
    opcion=pideLimpiaTexto("Continuar S/N: ")
    if(opcion=="S"):
        dataBasePerruna=capturaPerros(dataBasePerruna)
    
    return dataBasePerruna

def consultaDato(dataBasePerruna, nombre):
    
    print("\n¿Qué deseas consultar de ",nombre)
    print("1. Peso")
    print("2. Color")
    print("3. Edad")
    print("4. Regresar")
    
    opcion=pideNumeroPositivo1a4()
    
    if(opcion==1):
        print("El Peso de ", nombre, "es ",dataBasePerruna[nombre][0])
    elif(opcion==2):
        print("El Color de ", nombre, "es ",dataBasePerruna[nombre][1])
    elif(opcion==3):
        print("La edad de ", nombre, "es ",dataBasePerruna[nombre][2])   
    else:
        return
        
    consultaDato(dataBasePerruna, nombre)
 
    
def pideNombre(dataBasePerruna):
    
    nombre = pideLimpiaTexto("Dame el nombre: ")
    if(nombre!="BASTA"):
        consultaDato(dataBasePerruna,nombre)
    
    
    
    

#inicio
#perros es un dicccionario
dataBasePerruna={}

dataBasePerruna=capturaPerros(dataBasePerruna)
print("------------------")
pideNombre(dataBasePerruna)


    
    
    
    
    
    
    
    
    
    