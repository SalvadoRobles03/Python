import matplotlib.pyplot as plt
import numpy as np

def gen_part(q, y1,z):

  x = np.linspace(-16,25,50)
  y = np.linspace(-16,25,50)
  
  x,y=np.meshgrid(x,y)
  x_0 = 10
  y_0 = y1
  r_x = x-x_0
  r_y = y-y_0
 
  r_z= z

  E_x= (1*q*10**(-6))*(9*10**9)*r_x/np.sqrt(r_x**2+r_y**2+r_z**2+2)**3
  E_y= (1*q*10**(-6))*(9*10**9)*r_y/np.sqrt(r_x**2+r_y**2+r_z**2+2)**3

  return E_x, E_y, x_0, y_0

x = np.linspace(-16,25,50)
y = np.linspace(-16,25,50)
x,y = np.meshgrid(x,y)
E_x_t = 0
E_y_t = 0
p = -10
for j in np.linspace(0,100,50):
  for i in range(100):
    q = 1000
    E_x,E_y, x_0, y_0 = gen_part(q,p,j)
    E_x_t = E_x_t + E_x
    E_y_t = E_y_t + E_y
    p = p+0.5
    plt.scatter(x_0,y_0, color ="red")
    

plt.quiver(x,y,E_x_t, E_y_t)
plt.xlim(5,15)
plt.ylim(0,25)

plt.show()