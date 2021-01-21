import numpy as np
import matplotlib.pyplot as plt

def Henon(x,y, a,b):
    return (a - x**2 + b*y, x)

a = 1.4
b = 0.3
T = 30000
xs = []
ys = []
x = 1
y = 1
for _ in range(T):
    x, y = Henon(x,y,a,b)
    xs.append(x)
    ys.append(y)

plt.plot(xs,ys,',')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
