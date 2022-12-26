import numpy as np 



ex1=np.array([5,2,3,10])
ex2=np.array([2,-5,10,7]) #Aquí se ponen los coeficientes de las ecuaciones
ex3=np.array([4,17,23,11])

ex1=ex1/ex1[0]
ex2=ex2-ex2[0]*ex1
ex3=ex3-ex3[0]*ex1

ex2=ex2/ex2[1]
ex3=ex3-ex2*ex3[1]
ex3=ex3/ex3[2]

M=[ex1,ex2,ex3]

print("")
print(np.matrix(M))
print("")






