def definirangulo(angulo):
    
    angulofinal = angulo%360
    return angulofinal

angulo = float(input("Ingrese un ángulo, por favor: "))

angulopositivo= definirangulo(angulo)

if (angulopositivo%90==0):
    print("El ángulo es ", angulopositivo)
    print("Está en el eje")
    
elif(angulopositivo>0 and angulopositivo<90):
    print("El ángulo es ", angulopositivo)
    print("Está en el Cuadrante 1")
    
elif(angulopositivo>90 and angulopositivo<180):
    print("El ángulo es ", angulopositivo)
    print("Está en el Cuadrante 2")
    
elif(angulopositivo>180 and angulopositivo<270):
    print("El ángulo es ", angulopositivo)
    print("Está en el Cuadrante 3")
    
elif(angulopositivo>270 and angulopositivo<360):
    print("El ángulo es ", angulopositivo)
    print("Está en el Cuadrante 4")
    
else:
    print("Quiseso?????, pongase buso")
    


