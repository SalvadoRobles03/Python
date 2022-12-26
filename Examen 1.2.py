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


    

Acción= "R"

while Acción == "R":
    print("\n\nBienvenido a Locos por los Triángulos")
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
        
    eleccion = int(input("MENU: ingrese el número de la opción que desea elegir \n 1. Área y perímetro \n 2. Tipo \n 3. Componentes \n Eleccion: "))

    

    if (eleccion == 1):
        
        
        areaCalculado=area(ladoA,ladoB,ladoC)
        perimetroCalculado=perimetro(ladoA, ladoB, ladoC)
        
        if(areaCalculado == "NO es un triángulo válido"):
            print("\nNO es un triángulo válido")
            continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I), volver al menú anterior (R) o salir del programa (S): ")
            if(continuar=="I"):
                Acción="Iarea"
            elif(continuar=="R"):
                Acción="R"
            elif(continuar=="S"):
                print("FIN DEL PROGRAMA")
                break
            else:
                print("Ingrese una letra válida: ")
                continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I), volver al menú anterior (R) o salir del programa (S): ")
        else:
            print("\nEl Área del triangulo es de:", areaCalculado, "metros cuadrados\n")
            print("El Perímetro del triangulo es de:", perimetroCalculado, "metros")
            continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I), volver al menú anterior (R) o salir del programa (S): ")
            if(continuar=="I"):
                Acción="Iarea"
            elif(continuar=="R"):
                Acción="R"
            elif(continuar=="S"):
                print("FIN DEL PROGRAMA")
                break
            else:
                print("Ingrese una letra válida: ")
                continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I), volver al menú anterior (R) o salir del programa (S): ")
                
    elif (eleccion == 2):
        triangulo=tipoTriangulo(ladoA,ladoB,ladoC)
        if (triangulo == "equilátero"):
            print("\n       *\n\n    *******\n\n  ***********\n\n***************")
            print("\nEs un Triángulo equilátero") 
            continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I), volver al menú anterior (R) o salir del programa (S): ")
        if(triangulo == "isósceles"):
            print("\n    *\n\n   ****\n\n  ********\n\n************")
            print("\nEs un Triángulo isósceles")
            continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I), volver al menú anterior (R) o salir del programa (S): ")
        if(triangulo == "escaleno"):
            print("\n*\n\n *     *\n\n  *           *\n\n   **************")
            print("\nEs un Triángulo escaleno")
            continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I), volver al menú anterior (R) o salir del programa (S): ")
        if(triangulo == "NO es un triángulo válido"):
            print("\nNO es un triángulo válido")
            continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I), volver al menú anterior (R) o salir del programa (S): ")
        if(continuar=="I"):
            Acción="Itriangulo"
        elif(continuar=="R"):
            Acción="R"
        elif(continuar=="S"):
            print("FIN DEL PROGRAMA")
            break
        else:
            print("Ingrese una letra válida: ")
            continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I), volver al menú anterior (R) o salir del programa (S): ")
    elif (eleccion == 3):
        
        print("\nSe presentarán todos los componentes del Triángulo")
        ENTER=input("(Presione ENTER para continuar)")
        print("\nVértices: Se trata de los puntos que definen un triángulo al unir dos de ellos con una línea recta. Así, si tenemos los puntos A, B y C, uniéndolos con las rectas AB, BC y CA nos dará como resultado un triángulo. Además, los vértices se hallan del lado opuesto de los ángulos interiores del polígono.")
        ENTER=input("(Presione ENTER para continuar)")
        print("\nLados: Se llama así a cada una de las rectas que unen los vértices de un triángulo, delimitando la figura (el adentro del afuera).")
        ENTER=input("(Presione ENTER para continuar)")
        print("\nÁngulos: Cada dos lados de un triángulo forman en su vértice común algún tipo de ángulo, que se denomina ángulo interior, pues da hacia el adentro del polígono. Estos ángulos son, al igual que los lados y los vértices, siempre tres.\n\n- Fuente: https://concepto.de/triangulo/")
        continuar=limpiaTexto("Deseas reiniciar el programa (I), volver al menú anterior (R) o salir del programa (S): ")
        if(continuar=="I"):
            Acción="Icompo"
        elif(continuar=="R"):
            Acción="R"
        elif(continuar=="S"):
            print("FIN DEL PROGRAMA")
            break
        else:
            print("Ingrese una letra válida: ")
            continuar=limpiaTexto("Deseas reiniciar el programa (I), volver al menú anterior (R) o salir del programa (S): ")
    else:
        print("\n\nIngrese un número que este dentro de la lista") 
        
while Acción == "Iarea":
    ladoA= int(input("Ingrese el lado A del triángulo, por favor: "))
    ladoB= int(input("Ingrese el lado B del triángulo, por favor: "))
    ladoC= int(input("Ingrese el lado C del triángulo, por favor: "))
    
    areaCalculado=area(ladoA,ladoB,ladoC)
    perimetroCalculado=perimetro(ladoA, ladoB, ladoC)
    
    print("\nEl Área del triangulo es de:", areaCalculado, "metros cuadrados\n")
    print("El Perímetro del triangulo es de:", perimetroCalculado, "metros")
    continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I), volver al menú anterior (R) o salir del programa (S): ")
    if(continuar=="I"):
        Acción="Iarea"
    elif(continuar=="R"):
        Acción="R"
    elif(continuar=="S"):
        print("FIN DEL PROGRAMA")
        break
    else:
        print("Ingrese una letra válida: ")
        continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I), volver al menú anterior (R) o salir del programa (S): ")

while Acción == "Itriangulo":
    ladoA= int(input("Ingrese el lado A del triángulo, por favor: "))
    ladoB= int(input("Ingrese el lado B del triángulo, por favor: "))
    ladoC= int(input("Ingrese el lado C del triángulo, por favor: "))
    
    triangulo=tipoTriangulo(ladoA,ladoB,ladoC)
    if (triangulo == "equilátero"):
        print("\n       *\n\n    *******\n\n  ***********\n\n***************")
        print("Triángulo equilátero") 
        continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I), volver al menú anterior (R) o salir del programa (S): ")
    if(triangulo == "isósceles"):
        print("\n    *\n\n   ****\n\n  ********\n\n************")
        print("Triángulo isósceles")
        continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I), volver al menú anterior (R) o salir del programa (S): ")
    if(triangulo == "escaleno"):
        print("\n*\n\n *     *\n\n  *           *\n\n   **************")
        print("Triángulo escaleno")
        continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I), volver al menú anterior (R) o salir del programa (S): ")
    if(triangulo == "NO es un triángulo válido"):
        print("\nNO es un triángulo válido")
        continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I), volver al menú anterior (R) o salir del programa (S): ")
    if(continuar=="I"):
        Acción="Itriangulo"
    elif(continuar=="R"):
        Acción="R"
    elif(continuar=="S"):
        print("FIN DEL PROGRAMA")
        break
    else:
        print("Ingrese una letra válida: ")
        continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I), volver al menú anterior (R) o salir del programa (S): ")

while Acción == "Icompo":
    print("Se presentarán todos los componentes del Triángulo")
    ENTER=input("(Presione ENTER para continuar)")
    print("Vértices. Se trata de los puntos que definen un triángulo al unir dos de ellos con una línea recta. Así, si tenemos los puntos A, B y C, uniéndolos con las rectas AB, BC y CA nos dará como resultado un triángulo. Además, los vértices se hallan del lado opuesto de los ángulos interiores del polígono.")
    ENTER=input("(Presione ENTER para continuar)")
    print("Lados. Se llama así a cada una de las rectas que unen los vértices de un triángulo, delimitando la figura (el adentro del afuera).")
    ENTER=input("(Presione ENTER para continuar)")
    print("Ángulos. Cada dos lados de un triángulo forman en su vértice común algún tipo de ángulo, que se denomina ángulo interior, pues da hacia el adentro del polígono. Estos ángulos son, al igual que los lados y los vértices, siempre tres.\n\n- Fuente: https://concepto.de/triangulo/")
    continuar=limpiaTexto("Deseas iniciar el programa e ingresar nuevos valores (I), volver al menú anterior (R) o salir del programa (S): ")
    if(continuar=="I"):
        Acción="Icompo"
    elif(continuar=="R"):
        Acción="R"
    elif(continuar=="S"):
        print("FIN DEL PROGRAMA")
        break
    else:
        print("Ingrese una letra válida: ")
        continuar=limpiaTexto("Deseas reiniciar el programa (I), volver al menú anterior (R) o salir del programa (S): ")
    
    
      
        
   
    
   


