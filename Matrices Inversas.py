import numpy as np
import math 


#A01562588 Alejandro Robles

#SOLO SE PUEDEN UTILIZAR MATRICES CUADRADAS

array=([np.array([2, 1, 2]),np.array([1, 2, 4]),np.array([7,8,9])]) #Introducir matriz
t=math.isqrt(np.size(array))

print("\nMatriz Original")
print(np.matrix(array),"\n")


#Creamos la Matriz junto su Matriz identidad vacia
matrix=np.zeros((t+1,2*t))
for i in range(t):
    for j in range(t):
        matrix[i][j]=array[i][j]

#Llenamos matriz identidad
for i in range(t):
    matrix[i][t+i]=1

#Utilizamos Gauss-Jordan
for j in range (t):
  for i in range(j,t):
    if(array[j][j]!=0):
      if (i==j):
        matrix[j][:]=matrix[j][:]/matrix[j][j]
      else:
        matrix[i][:]=(matrix[i][:]-matrix[i][j]*matrix[j][:])
        
#Sacamos Inversa
for j in range (t-1,0,-1):
  for i in range(j-1,-1,-1):
    if(matrix[i][j]!=0):
      matrix[i][:]=matrix[i][:]-matrix[i][j]*matrix[j][:]
      
      

print("Matriz Inversa")
for j in range (t):
  print(matrix[j][t:]) 

