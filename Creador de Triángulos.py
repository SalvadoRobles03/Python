import turtle
turtle.shape ("turtle")
turtle.color("red")

import math

def pideEnteros(num):
    while(True):
        numero=(float(input(num)))
        if (numero>0 and numero%1==0):
            break
        
    return numero


#AQUI EMPIEZA EL CÓDIGO

while (True):
    ladoA=pideEnteros("Dame el valor del primer lado: ")
    ladoB=pideEnteros("Dame el valor del segundo lado: ")
    ladoC=pideEnteros("Dame el valor del tercer lado: ")

    if(ladoA>0 and ladoB>0 and ladoC>0 and (ladoA+ladoB)>ladoC and ladoA+ladoC>ladoB and ladoB+ladoC>ladoA):
        break
            
    else:
        print("Medidas no válidas, intenta de nuevo")
        
#CALCULO DE ANGULOS
cosA=(ladoB**2+ladoC**2-ladoA**2)/(2*ladoB*ladoC)

anguloA=math.acos(cosA)
anguloA=math.degrees(anguloA)

cosB=(ladoA**2+ladoC**2-ladoB**2)/(2*ladoA*ladoC)
    
anguloB=math.acos(cosB)
anguloB=math.degrees(anguloB)

anguloC=180-anguloA-anguloB     


#TRES LADOS IGUALES
if (ladoA==ladoB and ladoA==ladoC):
    
    print ("triángulo equilatero")


   #DOS LADOS IGUALES
elif (ladoA==ladoB or ladoA==ladoC or ladoC==ladoB):

    print("triangulo isóceles")      


 #LADOS DIFERENTES
else:

    print ("triángulo escaleno")



#MOVIMIENTO TORTUGA
    
turtle.forward(ladoA*10)
turtle.setheading(180-anguloC)
turtle.forward(ladoB*10)
turtle.setheading(180+anguloB)
turtle.forward(ladoC*10)

print(anguloA,anguloB,anguloC)


