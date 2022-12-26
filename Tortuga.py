from time import sleep
import turtle

turtle.shape("turtle")
turtle.color("green")

lados=int(input("Dame el número de lados: "))

for i in range(lados):
    
   
    turtle.setheading(360/lados*i)
    turtle.forward(100)
    
sleep(10000)   