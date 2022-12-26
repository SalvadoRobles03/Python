import matplotlib.pyplot as plt
import numpy as np

T=50 #Variable para definir tamaño de placa

def generador(q,t):
    X=np.linspace(.1,20,50)
    Y=np.linspace(-2,t,50)
    X,Y=np.meshgrid(X,Y)
    x0=10
    y0=q
    rx=X-x0
    ry=Y-y0  
    Ex=(1*10**(-6))*(1*10**9)*rx/np.sqrt(rx**2+ry**2+1)**3
    Ey=(1*10**(-6))*(1*10**9)*ry/np.sqrt(rx**2+ry**2+1)**3
    return Ex,Ey,x0,y0

X=np.linspace(.1,10,50)
Y=np.linspace(-3,T,50)

E_x_t=0
E_y_t=0
q=0

for i in range(T):
    E_x,E_y,x_0,y_0=generador(q,T)
    q=q+1
    E_x_t=E_x_t+E_x
    E_y_t=E_y_t+E_y
    plt.scatter(4.976,y_0,color="purple")



plt.quiver(X,Y,E_x_t,E_y_t)
plt.show()