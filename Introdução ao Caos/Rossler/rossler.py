import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from solvers import Euler, RK4

def fx(t,x,y,z,a,b,c):
    return -z -y
def fy(t,x,y,z,a,b,c):
    return x + a*y
def fz(t,x,y,z,a,b,c):
    return b + (x-c)*z

x = [-0.006]
y = [0.1]
z = [0.1]
params = np.array([0.1,0.8,8.5])
funcs = np.array([fx,fy,fz])

T = 500
dt = 0.01
for t in range(int(T/dt)):
    pos = np.array([x[t],y[t],z[t]])
    pos = RK4(t,dt,pos,params,funcs)
    x.append(pos[0])
    y.append(pos[1])
    z.append(pos[2])

fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.plot(x,y,z)
plt.show()

