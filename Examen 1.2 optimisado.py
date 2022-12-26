import math



def limpiaTexto(variable):
    texto=input(variable)
    texto=texto.upper()
    texto=texto.strip()
    
    return texto

def area(ladoA,ladoB,ladoC):
    
    X=ladoA
    Y=ladoB
    Z=ladoC
    
    if(X>0 and Y>0 and Z>0 and (X + Y) > Z and (X + Z) > Y and (Y + Z) > X):
        
        S=((ladoA+ladoB+ladoC)/2)
        
        areaEntrada= math.sqrt(S*(S-ladoA)*(S-ladoB)*(S-ladoC))
        
        return areaEntrada
        
    else:
        return "NO es un triángulo válido"
    
    
   

def perimetro(ladoA,ladoB,ladoC):
    
    perimetroEntrada= ladoA + ladoB + ladoC
    
    return perimetroEntrada

def tipoTriangulo(ladoA,ladoB,ladoC):
    X=ladoA
    Y=ladoB
    Z=ladoC
    
    if(X>0 and Y>0 and Z>0 and (X + Y) > Z and (X + Z) > Y and (Y + Z) > X):
        
        #equilátero
        if(X==Y and X==Z and Y==Z):
           return "equilátero"    
        
        #isósceles
        #elif( (X==Y and X!=Z) or(X==Z and X!=Y) or ( Y==Z and Y!=X)):
        elif( X==Y or X==Z or Y==Z ):
            return "isósceles"
        
        #escaleno
        else:
            return "escaleno"
        
    else:
        return "NO es un triángulo válido"

def continuarFun(continuar):
    
    if(continuar=="I" and eleccion == 1):
        Acción="Iarea"
        return Acción
    if(continuar=="I" and eleccion == 2):
        Acción="Itriangulo"
        return Acción
    if(continuar=="I" and eleccion == 3):
        Acción="Icompo"
        return Acción
    if(continuar=="R"):
        Acción="R"
        return Acción
    if(continuar=="S"):
        Acción="S"
        return Acción
    else:
        print("Ingrese una letra válida: ")
        continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I)\nvolver al menú anterior (R)\nsalir del programa (S)\nElección: ")


def eleccion1 (ladoA,ladoB,ladoC):
     
        areaCalculado=area(ladoA,ladoB,ladoC)
        perimetroCalculado=perimetro(ladoA, ladoB, ladoC)
        
        if(areaCalculado == "NO es un triángulo válido"):
            print("\nNO es un triángulo válido")
           
        else:
            print("\nEl Área del triangulo es de:", areaCalculado, "metros cuadrados\n")
            print("El Perímetro del triangulo es de:", perimetroCalculado, "metros")
            
            
def eleccion2 (ladoA,ladoB,ladoC):
    triangulo=tipoTriangulo(ladoA,ladoB,ladoC)
    if (triangulo == "equilátero"):
        print("\n       *\n\n    *******\n\n  ***********\n\n***************")
        print("\nEs un Triángulo equilátero") 
        
        
    if(triangulo == "isósceles"):
        print("\n    *\n\n   ****\n\n  ********\n\n************")
        print("\nEs un Triángulo isósceles")
        
    if(triangulo == "escaleno"):
        print("\n*\n\n *     *\n\n  *           *\n\n   **************")
        print("\nEs un Triángulo escaleno")
        
    if(triangulo == "NO es un triángulo válido"):
        print("\nNO es un triángulo válido")
        
def eleccion3():
    
        print("\nSe presentarán todos los componentes del Triángulo")
        ENTER=input("(Presione ENTER para continuar)")
        print("\nVértices: Se trata de los puntos que definen un triángulo al unir dos de ellos con una línea recta. Así, si tenemos los puntos A, B y C, uniéndolos con las rectas AB, BC y CA nos dará como resultado un triángulo. Además, los vértices se hallan del lado opuesto de los ángulos interiores del polígono.")
        ENTER=input("(Presione ENTER para continuar)")
        print("\nLados: Se llama así a cada una de las rectas que unen los vértices de un triángulo, delimitando la figura (el adentro del afuera).")
        ENTER=input("(Presione ENTER para continuar)")
        print("\nÁngulos: Cada dos lados de un triángulo forman en su vértice común algún tipo de ángulo, que se denomina ángulo interior, pues da hacia el adentro del polígono. Estos ángulos son, al igual que los lados y los vértices, siempre tres.\n\n- Fuente: https://concepto.de/triangulo/")
        
        
def pedirlados():
    
    ladoA= int(input("Ingrese el lado A del triángulo, por favor: "))
    ladoB= int(input("Ingrese el lado B del triángulo, por favor: "))
    ladoC= int(input("Ingrese el lado C del triángulo, por favor: "))
    if ((ladoA or ladoB or ladoC) < 0):
        print("\nIngrese números enteros positivos, por favor")
        ladoA= int(input("Ingrese el lado A del triángulo, por favor: "))
        ladoB= int(input("Ingrese el lado B del triángulo, por favor: "))
        ladoC= int(input("Ingrese el lado C del triángulo, por favor: "))
    else:
        ladoA=ladoA
        ladoB=ladoB
        ladoC=ladoC
        return ladoA,ladoB,ladoC


        
Acción = "R"   

while Acción == "R":
    print("\n\nBienvenido a Locos por los Triángulos")
    ladoA,ladoB,ladoC=pedirlados()
        
    eleccion = int(input("MENU: ingrese el número de la opción que desea elegir \n 1. Área y perímetro \n 2. Tipo \n 3. Componentes \n Eleccion: "))

    

    if (eleccion == 1):
        
        eleccion1(ladoA,ladoB,ladoC)
        continuar=limpiaTexto("\nDeseas iniciar el programa e ingresar nuevos valores (I)\nvolver al menú anterior (R)\nsalir del programa (S)\nElección: ")
        Acción=continuarFun(continuar)
    elif (eleccion == 2):
        
        eleccion2(ladoA,ladoB,ladoC)
        continuar=limpiaTexto("\nDeseas iniciar el programa e ingresar nuevos valores (I)\nvolver al menú anterior (R)\nsalir del programa (S)\nElección: ")
        Acción=continuarFun(continuar)
    elif (eleccion == 3):
        
        eleccion3()
        continuar=limpiaTexto("\nDeseas reiniciar el programa (I)\nvolver al menú anterior (R)\nsalir del programa (S)\nElección: ")
        Acción=continuarFun(continuar)
    else:
        print("\n\nIngrese un número que este dentro de la lista")   
    

        
while Acción == "Iarea":
    
    ladoA,ladoB,ladoC=pedirlados()
    
    eleccion1(ladoA,ladoB,ladoC)
    continuar=limpiaTexto("\nDeseas iniciar el programa e ingresar nuevos valores (I)\nvolver al menú anterior (R)\nsalir del programa (S)\nElección: ")
    Acción=continuarFun(continuar)

while Acción == "Itriangulo":
   
    ladoA,ladoB,ladoC=pedirlados()
    
    eleccion2(ladoA,ladoB,ladoC)
    continuar=limpiaTexto("\nDeseas iniciar el programa e ingresar nuevos valores (I)\nvolver al menú anterior (R)\nsalir del programa (S)\nElección: ")
    Acción=continuarFun(continuar)
    
while Acción == "Icompo":
    eleccion3()
    continuar=limpiaTexto("\nDeseas reiniciar el programa (I)\nvolver al menú anterior (R)\nsalir del programa (S)\nElección: ")
    Acción=continuarFun(continuar)
    
while Acción =="S":
    print("FIN DEL PROGRAMA")
    break
    
 
      
        
   
    
   


