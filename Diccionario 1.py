
azul="blue"
rojo="red"
amarillo="yellow"

tonto=False


while(tonto==False):
    print("Dime estas palabras en Inglés")
    palabra1=input("Azul: ")
    palabra1=palabra1.lower()
    palabra1=palabra1.strip()
    
    palabra2=input("Rojo: ")
    palabra2=palabra2.lower()
    palabra2=palabra2.strip()
    
    palabra3=input("Amarillo: ")
    palabra3=palabra3.lower()
    palabra3=palabra3.strip()
    
    if(palabra1 ==azul and palabra2==rojo and palabra3==amarillo):
        tonto=True
    else:
        print("La regaste")
        print("--------------------")
        
print("Felicidades, estan bien")
    