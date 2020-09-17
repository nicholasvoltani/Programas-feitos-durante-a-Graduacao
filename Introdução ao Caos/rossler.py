import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def Euler(dt,vars,params,funcs):
    update = np.array([f(*vars,*params) for f in funcs])
    return vars + update*dt

def fx(x,y,z,a,b,c):
    return -z -y
def fy(x,y,z,a,b,c):
    return x + a*y
def fz(x,y,z,a,b,c):
    return b + (x-c)*z

x = np.array([-0.006])
y = np.array([0.1])
z = np.array([0.1])
params = np.array([0.1,0.1,5.3])
funcs = np.array([fx,fy,fz])

T = 1000
dt = 0.01
for t in range(int(T/dt)):
    varss = np.array([x[t],y[t],z[t]])
    xt,yt,zt=Euler(dt,varss,params,funcs)
    x = np.append(x,xt)
    y = np.append(y,yt)
    z = np.append(z,zt)

fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.plot(x,y,z)
plt.show()
