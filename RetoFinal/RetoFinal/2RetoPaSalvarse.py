from turtle import Turtle, Screen
import random

#en estas líneas se crea el cielo
ventana = Screen()
ventana.bgcolor("navy")

tortuga = Turtle()
tortuga.speed(100)

#aquí va la luna
def DibujarLuna():
    tortuga.up()
    tortuga.goto(250,150)
    tortuga.down()
    tortuga.color("white")
    
    tortuga.fillcolor("white")
    tortuga.begin_fill()
    tortuga.circle(100)
    tortuga.end_fill()
    
    tortuga.up()
    tortuga.goto(200,100)
    tortuga.down()
    tortuga.color("navy")
    
    tortuga.fillcolor("navy")
    tortuga.begin_fill()
    tortuga.circle(100)
    tortuga.end_fill()

#aquí van las estrellas
def DibujarEstrellas(paramNumEstrellas):
    #Aquí va el código
    #posición donde se dibuje la estrella es random
    print()

def DibujarEstrella(paramTamano, paramPosX, paramPosY):
    tortuga.up()
    tortuga.goto(paramPosX,paramPosY)
    tortuga.down()
    tortuga.color("white")
    
    tortuga.fillcolor("white")
    tortuga.begin_fill()
    
    
    for i in range(5):
        tortuga.forward(paramTamano)
        tortuga.right(144)
        
   
    tortuga.end_fill()
    
#Aquí inicia el código para dibujar el cielo con estrellas
DibujarLuna()

starSize = random.randint(10,50)
DibujarEstrella(starSize, 0, 0)


DibujarEstrellas(1)

tortuga.hideturtle()