import matplotlib.pyplot as plt
import numpy as np

tamaño = 100
plt.xlim(0,100)
plt.ylim(0,100)

Xs=10 * [tamaño*np.random.rand(),tamaño * np.random.rand()]
Ys=10 * [tamaño*np.random.rand(),tamaño * np.random.rand()]
plt.scatter(Xs,Ys,marker="8", color="Green")


r0 = np.array((Xs[0], Ys[0]))
r1 = np.array((Xs[1], Ys[1]))
r = r0

r = r1 - r0
rmag=np.sqrt(r[0]**2+r[1]**2)

F = -(9*10**9)*(2)*(1)*r/rmag**3/1000000
print(F)

plt.arrow(r0[0],r0[1], F[0],F[1],width=2)
plt.xlim(-50,150)
plt.ylim(-50,150)
plt.scatter(Xs,Ys,marker="s", color="Yellow")


X=np.linspace(.1,10,20)
Y=np.linspace(.1,10,20)
X,Y=np.meshgrid(X,Y)
plt.scatter(X,Y)
plt.quiver(X,Y,1,1)
Ex=(1*10**(-6))*(9*10**9)*X/np.sqrt(X**2+Y**2+1)**3
Ey=(1*10**(-6))*(9*10**9)*Y/np.sqrt(X**2+Y**2+1)**3
plt.quiver(X,Y,Ex,Ey)
plt.show()

