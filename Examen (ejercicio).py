def limpiar(mensaje):
    texto=input(mensaje)
    texto=texto.strip()
    texto=texto.upper()
    return texto

a=int(input("Dame el valor de A: "))
b=int(input("Dame el valor de B: "))
c=int(input("Dame el valor de C: "))
d=int(input("Dame el valor de D: "))

puntos=0

for i in range(4):
   
    if(i==0):
        suma= int(limpiar("Dame el resultado de la operación A+B: "))
        if(suma==(a+b)):
            puntos=puntos+25
            print("CORRECTO")
    elif(i==1):
        resta= int(limpiar("Dame el resultado de la operación A-B: "))
        if(resta==(a-b)):
            puntos=puntos+25
            print("CORRECTO")
        else:
            
            print("INCORRECTO")
    elif(i==2):
        multiplicar= int(limpiar("Dame el resultado de la operación C*D: "))
        if(multiplicar==(c*d)):
            puntos=puntos+25
            print("CORRECTO")
        else:
            
            print("INCORRECTO")
    else:
        divide= int(limpiar("Dame el resultado de la operación C/D: "))
        if(divide==(c/d)):
            puntos=puntos+25
            print("CORRECTO")
        else:
            
            print("INCORRECTO")
            
if(puntos>50):
    print("Sacaste", puntos, "Puntos")
    print("Felicidades, has aprobado")
else:
    print("Sacaste", puntos, "Puntos")
    print("REPROBADO")
            
