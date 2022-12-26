import matplotlib.pyplot as plt
import numpy as np

def generador(q):
    X=np.linspace(.1,10,20)
    Y=np.linspace(.1,10,20)
    X,Y=np.meshgrid(X,Y)
    x0=10*np.random.rand()
    y0=10*np.random.rand()
    rx=X-x0
    ry=Y-y0  
    Ex=(1*10**(-6))*(1*10**9)*rx/np.sqrt(rx**2+ry**2+1)**3
    Ey=(1*10**(-6))*(1*10**9)*ry/np.sqrt(rx**2+ry**2+1)**3
    return Ex,Ey,x0,y0

X=np.linspace(.1,10,20)
Y=np.linspace(.1,10,20)
X,Y=np.meshgrid(X,Y)
E_x_t=0
E_y_t=0
for i in range(2):
    q=np.random.rand()-.5
    E_x,E_y,x_0,y_0=generador(q)
    E_x_t=E_x_t+E_x
    E_y_t=E_y_t+E_y
    plt.scatter(x_0,y_0,color="purple")

plt.quiver(X,Y,E_x_t,E_y_t)
plt.show()