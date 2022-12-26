# -*- coding: utf-8 -*-
"""Entregable final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wE3QUWEZ8LePIWEAM_3Oudj1DvPR8Er3
"""

#Ángel David Ávila Pérez- A01562833
#Salvador Alejandro Robles Hernández- A01562588
#Giuliana Herrera López- A01562646
#Maria del Cielo Ramirez Zavala- A01562798

import matplotlib.pyplot as plt
import numpy as np

T1=30 #Variable para definir tamaño de placa1      (No Mayor a 60)
Q1=100 #Variable para definir carga de placa1
P1=4 #Variable para definir la posición de placa1  (No mayor a 10)

T2=15 #Variable para definir tamaño de placa2      (No Mayor a 60)
Q2=-100 #Variable para definir carga de placa2
P2=9 #Variable para definir la posición de placa2  (No mayor a 10)

def generador(q,t,Q,x):
    #t=t*(58/t)
    X=np.linspace(.1,20,50)
    Y=np.linspace(-2,t,50)
    X,Y=np.meshgrid(X,Y)
    x0=x
    y0=q
    rx=X-x0
    ry=Y-y0  
    Ex=(1*Q*10**(-6))*(1*10**9)*rx/np.sqrt(rx**2+ry**2+1)**3
    Ey=(1*Q*10**(-6))*(1*10**9)*ry/np.sqrt(rx**2+ry**2+1)**3
    return Ex,Ey,x0,y0

X=np.linspace(.1,10,50)
if(T1<T2):
    Y=np.linspace(-3,T2,50)
    y= np.linspace(.1,T2,40)
else:
    Y=np.linspace(-3,T1,50)
    y= np.linspace(.1,T1,40)

E_x_t=0
E_y_t=0

q2=0
q1=0

if(T1>T2):
    q2=(T1-T2)/2
else:
    q1=(T2-T1)/2

for i in range(T1):
    E_x,E_y,x_0,y_0=generador(q1,T1,Q1,P1*2)
    q1=q1+1
    E_x_t=E_x_t+E_x
    E_y_t=E_y_t+E_y
    plt.scatter(((x_0/2)-.05),y_0,color="purple")

for i in range(T2):
    E_x,E_y,x_0,y_0=generador(q2,T1,Q2,P2*2)
    q2=q2+1
    E_x_t=E_x_t+E_x
    E_y_t=E_y_t+E_y
    plt.scatter(((x_0/2)+.05),y_0,color="red")

E_mag=(E_x_t**2+E_y_t**2)
alpha=1


plt.quiver(X,Y,E_x_t,E_y_t)


E_mag=(E_x_t**2+E_y_t**2)
alpha=1
x= np.linspace(P1,P2,40)

x,y = np.meshgrid(X,Y)

for h in range(3):
    i=np.random.randint(.40*len(y),.60*len(y))
    j=np.random.randint(.40*len(x),.60*len(x))
    plt.quiver(x[i,j],y[i,j],alpha*np.gradient(E_mag)[1][i,j]/2,alpha*np.gradient(E_mag)[0][i,j]/2,color="red")


plt.contour(X,Y,E_mag)

plt.show()