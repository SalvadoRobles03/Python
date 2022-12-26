import pandas as pd
pd.options.mode.chained_assignment = None #default="warn"
import matplotlib.pyplot as plt
import numpy as np
import datetime
import openpyxl
import xlsxwriter
import random

#Lecturas para español
def Lecturas(x):
    if(x==1):
        print("Lectura 1")
        print("\nLos especialistas en derechos humanos piensan que la representación de las personas en la publicidad es injusta y discriminatoria. En el caso de hombres y mujeres, existe una fuerte tendencia a presentar a los primeros como los protectores, los fuertes, mientras que a las segundas las vemos básicamente en roles secundarios. Sin embargo, las escenas discriminatorias no se circunscriben a esos ámbitos, ya que al mostrar a un tipo de personas en las que predomina la piel blanca y los cabellos claros, dejan de lado la diversidad racial que existe en nuestro país (andinos, mestizos, afrodescendientes, etc.).")
        print("\nMariela Jara señala que los mensajes publicitarios también discriminan cuando exponen situaciones en las que priman momentos de realización, felicidad y prosperidad económica en un país en el que una gran parte de la población (24,8%) vive en la pobreza.")
        print("\nPara sus defensores, la publicidad es el espejo de la cultura que hemos adquirido a lo largo de los años. David Solari Martín explica que el individuo presta a los anuncios comerciales ideales de belleza y comportamiento. La sociedad acepta un modelo y la publicidad lo acoge. Es seguro que el color de tinte que más se vende en el País es el rubio y acá las mujeres no son rubias. Entonces, estos mensajes nos alienan o tenemos parámetros de belleza que no corresponden a nuestra realidad, pero los aceptamos. Además, algunos spots publicitarios son androcéntricos (comerciales de cerveza), sexistas (productos de limpieza) o se centran en una determinada raza (productos de belleza). Por ejemplo, si vendemos mototaxis no vamos a utilizar modelos de ojos azules, porque ese no es el público consumidor.")
        print("\nPor otro lado, las marcas de algunas instituciones bancarias y bebidas gaseosas tienen promociones en las que aparecen modelos con rasgos andinos. Lo que sucede es que hay un problema de identidad que provoca una falta de unidad entre los criterios y los mensajes que se emplean para elaborar los avisos publicitarios.")     
    else:
        print("Lectura 2")
        print("\nAntes de discutir sobre la contaminación sonora, se debe esclarecer qué se entiende por ruido. Probablemente, todos tengan una definición de él, pero los estudios técnicos deben proveerse de una forma objetiva de definirlo. Desde esta perspectiva, el ruido es el sonido no deseado que genera molestia, perjudica o afecta la salud de las personas. En otras palabras, la contaminación sonora es la presencia en el ambiente de niveles de ruido que implique molestia, genere riesgos, perjudique o afecte la salud y al bienestar humano, los bienes de cualquier naturaleza o que cause efectos significativos sobre el medio ambiente.")
        print("\nActualmente, este tipo de contaminación es uno de los problemas más importantes que pueden afectar a la población de la capital, ya que la exposición de las personas a niveles de ruido intenso puede producir estrés, presión alta, vértigo, insomnio, dificultades en el habla y la pérdida de audición, cuando el contacto con este agente nocivo es prolongado. Además, los sonidos estridentes afectan, particularmente, la capacidad de aprendizaje de los menores de edad y pueden causar estragos en el desarrollo de sus capacidades cognitivas cuando todavía no han salido de la infancia. ")
        print("\nLa intensidad de los distintos ruidos se mide en decibeles (dB). Los decibeles son las unidades en las que habitualmente se expresa el nivel de presión sonora, es decir, la potencia o intensidad de los ruidos. Además, son la variación sonora más pequeña perceptible para el oído humano. El umbral de audición humano medido en dB tiene una escala que se inicia con 0 dB (nivel mínimo) y que alcanza su grado máximo con 120 dB (que es el nivel de estímulo en el que las personas empiezan a sentir dolor), un nivel de ruido que se produce, por ejemplo, durante un concierto de rock.")

#Funcion para validar letras, funciona para todos las materias
#Este es uno solo para todo el codigo
def ABCD (mensaje):
    n=True
    while(n==True):
        texto=input(mensaje)
        texto=texto.upper()
        texto=texto.strip()
        if (texto=="A" or texto=="B" or texto=="C" or texto=="D"):
            n=False
        else:
            print("Respuesta no valida, ingrese de nuevo")
    return texto

#Funcion para siguiente pregunta o Anterior
#Funciona para todos los codigos
def dobleOpc(mensaje, v1, v2):
    n=True
    while(n==True):
        texto=input(mensaje)
        texto=texto.upper()
        texto=texto.strip()
        if (texto==v1 or texto==v2):
            n=False
        else:
            print("Respuesta no valida, ingrese de nuevo")
    return texto

#Para cambiar entre preguntas
#Funciona para todas las materias
def definirX(x,final):
    if (x==0):
        x=x+1
    elif(x>0 and x<final):
        acc=dobleOpc("Siguiente pregunta (S), Anterior pregunta (A): ", "S", "A")
        ("------------------------------")
        if(acc=="S"):
            x=x+1
        else:
            x=x-1
    else:
        acc=dobleOpc("Terminar sección (T), Anterior pregunta (A): ","T", "A")
        ("------------------------------")
        if(acc=="A"):
            x=x-1
        else:
            x=10
    return x

#Para sacar la otra casilla de los incisos de español
def casilla2(mEsp):
    if(mEsp=="A"):
        cas2="A2"
    elif(mEsp=="B"):
        cas2="B2"
    elif(mEsp=="C"):
        cas2="C2"
    else:
        cas2="D2"
    return cas2

#Funcion para mostrar las preguntas de matemáticas
def CambiarMate(x):
    pMate=tMate.groupby("Numero").get_group(mMate[x][0])
    print("------------------------------")
    print("Pregunta #",(x+1))
    print(pMate["Ppregunta"].to_string(index=False)," ",pMate["Spregunta"].to_string(index=False))
    print(pMate["Tpregunta"].to_string(index=False)," ",pMate["Cpregunta"].to_string(index=False))
    print("------------------------------")
    print(pMate["A"].to_string(index=False))
    print(pMate["B"].to_string(index=False))
    print(pMate["C"].to_string(index=False))
    print(pMate["D"].to_string(index=False))
    ("------------------------------")
    
    if(mMate[x][4]!="N"):
        print("Habias escogido el inciso: ",mMate[x][4]) 
        acc=dobleOpc("Modificar respuesta (M), Dejar igual (D): ", "M", "D")
    
    if(mMate[x][4]=="N" or acc=="M"):
        #Funcion (Ingresar variable valida)
        letra=ABCD("Ingresa el Inciso correcto: ")
        mMate[x][4]=letra
    ("------------------------------")
    #Funcion para cambiar valores de x
    x = definirX(x,9) #9 porque estamos en mate
    if(x<10):
        CambiarMate(x)
    return

#Funcion para mostrar las preguntas de Español
def CambiarEsp(x):
    pEsp=tEsp.groupby("Numero").get_group(mEsp[x][0])
    print("------------------------------")
    print("Pregunta #",(x+1))
    print(pEsp["Ppregunta"].to_string(index=False)," ",pEsp["Spregunta"].to_string(index=False))
    print(pEsp["Tpregunta"].to_string(index=False))
    print("------------------------------")
    print(pEsp["A"].to_string(index=False)," ", pEsp["A2"].to_string(index=False))
    print(pEsp["B"].to_string(index=False)," ", pEsp["B2"].to_string(index=False))
    print(pEsp["C"].to_string(index=False)," ", pEsp["C2"].to_string(index=False))
    print(pEsp["D"].to_string(index=False)," ", pEsp["D2"].to_string(index=False))
    ("------------------------------")
    
    if(mEsp[x][4]!="N"):
        print("Habias escogido el inciso: ",mEsp[x][4]) 
        acc=dobleOpc("Modificar respuesta (M), Dejar igual (D): ", "M", "D")
    
    if(mEsp[x][4]=="N" or acc=="M"):
        #Funcion (Ingresar variable valida)
        letra=ABCD("Ingresa el Inciso correcto: ")
        mEsp[x][4]=letra
    ("------------------------------")
    #Funcion para cambiar valores de x
    x = definirX(x,4) #4 porque estamos en español
    if(x<10):
        CambiarEsp(x)
    return

#Funcion para mostrar las preguntas de Ciencias
def CambiarCie(x):
    pCie=tCie.groupby("Numero").get_group(mCie[x][0])
    print("------------------------------")
    print("Pregunta #",(x+1))
    print(pCie["Ppregunta"].to_string(index=False)," ",pCie["Spregunta"].to_string(index=False))
    print(pCie["Tpregunta"].to_string(index=False)," ",pCie["Cpregunta"].to_string(index=False))
    print("------------------------------")
    print(pCie["A"].to_string(index=False))
    print(pCie["B"].to_string(index=False))
    print(pCie["C"].to_string(index=False))
    print(pCie["D"].to_string(index=False))
    ("------------------------------")
    
    if(mCie[x][4]!="N"):
        print("Habias escogido el inciso: ",mCie[x][4]) 
        acc=dobleOpc("Modificar respuesta (M), Dejar igual (D): ", "M", "D")
    
    if(mCie[x][4]=="N" or acc=="M"):
        #Funcion (Ingresar variable valida)
        letra=ABCD("Ingresa el Inciso correcto: ")
        mCie[x][4]=letra
    ("------------------------------")
    #Funcion para cambiar valores de x
    x = definirX(x,4) #4 porque estamos en ciencias
    if(x<10):
        CambiarCie(x)
    return

#Funciones para dar retroalimentación
#Retro de matemáticas
def retroMate():
    for x in range (10):
        pMate=tMate.groupby("Numero").get_group(mMate[x][0])
        print("------------------------------")
        print("Retroalimentación Pregunta #",(x+1))
        print(pMate["Ppregunta"].to_string(index=False)," ",pMate["Spregunta"].to_string(index=False))
        print(pMate["Tpregunta"].to_string(index=False)," ",pMate["Cpregunta"].to_string(index=False))
        print("------------------------------")
        
        if(mMate[x][4]==mMate[x][3]):
            print("Seleccionaste: ", mMate[x][4])
            print(pMate[mMate[x][4]].to_string(index=False))
            print("Respuesta Correcta")
            print("------------------------------")
        else:
            print("Seleccionaste: ", mMate[x][4])
            print(pMate[mMate[x][4]].to_string(index=False))
            print("La respuesta correcta era")
            print(pMate[mMate[x][3]].to_string(index=False))
            print("------------------------------")
        #presione C para continuar
        acc=dobleOpc("Presione (C) para continuar: ", "C", "C")

#Retro de Español
def retroEsp():
    for x in range (5):
        pEsp=tEsp.groupby("Numero").get_group(mEsp[x][0])
        print("------------------------------")
        print("Retroalimentación Pregunta #",(x+1))
        print(pEsp["Ppregunta"].to_string(index=False)," ",pEsp["Spregunta"].to_string(index=False))
        print(pEsp["Tpregunta"].to_string(index=False))
        print("------------------------------")
        
        if(mEsp[x][4]==mEsp[x][3]):
            var=casilla2(mEsp[x][4])
            print("Seleccionaste: ", mEsp[x][4])
            print(pEsp[mEsp[x][4]].to_string(index=False)," ",pEsp[var].to_string(index=False))
            print("Respuesta Correcta")
            print("------------------------------")
        else:
            print("Seleccionaste: ", mEsp[x][4])
            var=casilla2(mEsp[x][4])
            print(pEsp[mEsp[x][4]].to_string(index=False)," ",pEsp[var].to_string(index=False))
            print("La respuesta correcta era")
            var=casilla2(mEsp[x][3])
            print(pEsp[mEsp[x][3]].to_string(index=False)," ",pEsp[var].to_string(index=False))
            print("------------------------------")
        #presione C para continuar
        acc=dobleOpc("Presione (C) para continuar: ", "C", "C")

#Retro de Ciencias
def retroCie():
    for x in range (5):
        pCie=tCie.groupby("Numero").get_group(mCie[x][0])
        print("------------------------------")
        print("Retroalimentación Pregunta #",(x+1))
        print(pCie["Ppregunta"].to_string(index=False)," ",pCie["Spregunta"].to_string(index=False))
        print(pCie["Tpregunta"].to_string(index=False)," ",pCie["Cpregunta"].to_string(index=False))
        print("------------------------------")
        
        if(mCie[x][4]==mCie[x][3]):
            print("Seleccionaste: ", mCie[x][4])
            print(pCie[mCie[x][4]].to_string(index=False))
            print("Respuesta Correcta")
            print("------------------------------")
        else:
            print("Seleccionaste: ", mCie[x][4])
            print(pCie[mCie[x][4]].to_string(index=False))
            print("La respuesta correcta era")
            print(pCie[mCie[x][3]].to_string(index=False))
            print("------------------------------")
        #presione C para continuar
        acc=dobleOpc("Presione (C) para continuar: ", "C", "C")

#define las preguntas Aleatorias:
preMate=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
gLista=random.sample(preMate,20)
selMate=gLista[:10]

preCie=[1,2,3,4,5,6,7,8,9,10]
gLista=random.sample(preCie,10)
selCie=gLista[:5]

ppEsp=[1,2]
gLista=random.sample(ppEsp,2)
ppEsp=gLista[:1]
preEsp1=[1,2,3,4,5]
preEsp2=[6,7,8,9,10]
if(ppEsp[0]==1):
    gLista=random.sample(preEsp1,5)
    selEsp=gLista
else:
    gLista=random.sample(preEsp2,5)
    selEsp=gLista
#Aqui termina las preguntas aleatorias

#Cambiar nombre de archivo y nombre de hoja de excel
#Este es uno solo para todo el codigo
todo=pd.read_excel("ProyectoProgras.xlsx","Preguntas") #Cambiar según computadora

##Seleciona las preguntas ya aleatorias de cada categoria
#Seleccion de mate
tMate=todo.groupby("Categoria").get_group("Mate")
mMate=[]
pMate=[]
ct=0
for i in selMate:
    lineMate=[]
    pMate=tMate.groupby("Numero").get_group(i)
    lineMate.append(i)
    lineMate.append(pMate["Numero"].to_string(index=False))
    lineMate.append(ct+1)
    lineMate.append(pMate["Inciso"].to_string(index=False))
    lineMate.append("N")
    mMate.append(lineMate)
    ct=ct+1
    
#Seleccion de Español
tEsp=todo.groupby("Categoria").get_group("Español")
mEsp=[]
pEsp=[]
ct=0
for i in selEsp:
    lineEsp=[]
    pEsp=tEsp.groupby("Numero").get_group(i)
    lineEsp.append(i)
    lineEsp.append(pMate["Numero"].to_string(index=False))
    lineEsp.append(ct+1)
    lineEsp.append(pMate["Inciso"].to_string(index=False))
    lineEsp.append("N")
    mEsp.append(lineEsp)
    ct=ct+1
#Seleccion de Ciencias
tCie=todo.groupby("Categoria").get_group("Ciencias")
mCie=[]
pCie=[]
ct=0
for i in selCie:
    lineCie=[]
    pCie=tCie.groupby("Numero").get_group(i)
    lineCie.append(i)
    lineCie.append(pMate["Numero"].to_string(index=False))
    lineCie.append(ct+1)
    lineCie.append(pMate["Inciso"].to_string(index=False))
    lineCie.append("N")
    mCie.append(lineCie)
    ct=ct+1
##Aqui termina la seleccion de las preguntas aleatorias de cada materia

#presenta las preguntas de Ciencias
CambiarCie(0)
#presenta las preguntas de Mate
CambiarMate(0)
#presenta las preguntas de Español
Lecturas(ppEsp[0])
CambiarEsp(0)

#Aciertos Mate
acMate=0
for i in range (10):
    if(mMate[i][4]==mMate[i][3]):
        acMate=acMate+1
#Aciertos Esp
acEsp=0
for i in range (5):
    if(mEsp[i][4]==mEsp[i][3]):
        acEsp=acEsp+1
#Aciertos Esp
acCie=0
for i in range (5):
    if(mCie[i][4]==mCie[i][3]):
        acCie=acCie+1
        
print(acCie, " de 5 en Ciencias")
retroCie()

print(acMate, " de 10 en Matemáticas")
retroMate()

print(acEsp, " de 5 en Español")
retroEsp()
