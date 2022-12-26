import numpy as np
import math

#A01562588 Alejandro Robles

def Deter(F,M):
    P=0
    if(math.sqrt(np.size(F))==2):
        val = F[0][0] * F[1][1] - F[1][0] * F[0][1]
        return val
    else:
        for i in range(size):
            F=M
            F=np.delete(M,(0), axis = 0)
            F=np.delete(F,(i), axis=1)
            if(math.sqrt(np.size(F))==2):
                P = P+(F[0][0] * F[1][1] - F[1][0] * F[0][1])
                if(i==size):
                    return P
            else:
                break
        Deter(F,F)

M= np.matrix(([np.array([2, 1, 2]),np.array([1, 2, 4]),np.array([7,8,9])]))
F=0
i=0

size=math.sqrt(np.size(M))

print("Matriz: ")
print(M)
print("Determinante: ")
print(np.linalg.det(M))
    
