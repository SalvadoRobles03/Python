#Programa para calcular velocidad

Distancia= float (input("Dame la Distancia en Km: "))
Tiempo= float (input("Dame el Tiempo en Horas: "))



if (Distancia>0 and Tiempo>0):

    Velocidad= Distancia/Tiempo

    print ("La velocidad es: ", Velocidad, "Km/h")

else:
    
    print ("Ponga valores validos")
    
