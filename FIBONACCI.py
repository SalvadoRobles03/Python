import time

def fibonacci (number):
    if(number==0 or number==1):
        return number
    else:
        return fibonacci(number-1)+fibonacci(number-2)

def printfibonacci(number):
    print([fibonacci(x) for x in range (number+1)])
    

printfibonacci(32)
