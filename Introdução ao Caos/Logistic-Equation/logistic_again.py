import numpy as np
import matplotlib.pyplot as plt
def f2(x,p):
    return p**2*x*(1-x)*(1-p*x+p*x**2)

def df2dt(x,p):
    return p**2*(2*x-1)*(1-2*p*x+2*p*x**2)

p = np.linspace(1,5, 1000)

x1 = 0
x2 = (p-1)/p
x3 = (1+p + np.sqrt(p**2-2*p-3))/(2*p)
x4 = (1+p - np.sqrt(p**2-2*p-3))/(2*p)

#plt.plot(p,x1)
plt.plot(p,x2, label = r' $\frac{p-1}{p}$')
plt.plot(p,x3, label = r' $\frac{1 + p + \sqrt{p²-2p-3}}{2p}$ ')
plt.plot(p,x4, label = r' $\frac{1 + p - \sqrt{p²-2p-3}}{2p}$ ')
plt.legend()
plt.xlabel('p')
plt.ylabel('x')
plt.show()
