#Salvador Alejandro Robles Hernandez A01562588
#Maria del Cielo Ramirez Zavala A01562798

Calculator=int(0)
pc=int(0)
Input=int(0)
Output=int(0)
memoria = []



def leerLine(inst):
    sepa=inst.split(sep=",")
    memoria[int(sepa[0])]=int(sepa[1])
    
def leerInst(inst):
    dato=inst
    global Calculator
    global pc
    global Input
    global output
    if (dato>=100 and dato<200):
        dato=dato-100
        Calculator=Calculator+memoria[dato] #ADD
        pc=pc+1
    elif (dato>=200 and dato<300):
        dato=dato-200
        Calculator=Calculator-memoria[dato] #Subt
        pc=pc+1
    elif (dato>=300 and dato<400):
        dato=dato-300
        memoria[dato]=Calculator #Store
        pc=pc+1
    elif (dato>=500 and dato<600):
        dato=dato-500
        Calculator=memoria[dato] #Load
        pc=pc+1
    elif (dato>=600 and dato<700):#B
        dato=dato-600
        pc=dato
    elif (dato>=700 and dato<800): #BZ
        dato=dato-700
        if(Calculator==0):
            pc=dato
        else:
            pc=pc+1
    elif (dato>=800 and dato<900): #BP
        dato=dato-800
        if(Calculator>=0):
            pc=dato
        else:
            pc=pc+1
    elif (dato>=900 and dato<1000):
        dato=dato-900
        if dato==1:
            Input=int(input("Input: "))#INPUT
            Calculator=Input
        if dato==2:
            Output=Calculator
            print("Output: ",Output)#OUTPUT
        pc=pc+1
    else:
        pc=pc+1
    
   



#main()
while(len(memoria)!=100):
    memoria.append(0)

with open("for.txt") as archivo: #Poner el nombre del archivo que desea leer
    for linea in archivo:
        leerLine(linea)



while(memoria[pc]>000):
    leerInst(memoria[pc]) 
print(memoria)

