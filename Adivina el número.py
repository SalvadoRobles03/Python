
max= 99
min=1

adivina = 0

numero=int(input("Escoge un número entre 1 y 99: "))
if(numero>99 or numero<0):
    print("Número fuera de rango")
else:
    
    while(adivina==0):
        mitad=(max+min)//2
        if(numero>mitad):
            min=mitad
        else:
            max=mitad
        if((max-min)<=1):
            adivina=max
            print(min,"  ",max)



    print("Tu número es", adivina)
        
    
        
    
    