'''
Ejercicio 1
Escribe un programa que pida que se teclee un valor entero e indique si el número es:

Par positivo
Impar positivo
Par negativo
Impar negativo
Para este ejercicio considera el valor 0 como par positivo.
'''
numero=int(input("Deme su número por favor: "))
residuo=numero%2

if(numero>=0):
    
    if (residuo==0):
        print("Número Positivo Par")
    else:
        print("Numero Positivo Impar")
else:
    
    if (residuo==0):
        print("Número Negativo Par")
    else:
        print("Numero Negativo Impar")
    