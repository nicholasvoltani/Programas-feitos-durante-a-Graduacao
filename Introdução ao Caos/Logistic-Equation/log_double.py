import numpy as np
import matplotlib.pyplot as plt

## Fórmula da derivada de f(f(x))
def df2dt(x,p):
	return p**2*(1-2*x)*(1+2*p*(x-1)*x)

p = np.linspace(0,5, 1000)

## Pontos fixos
x2 = (p-1)/p
x3 = (1+p + np.sqrt(p**2-2*p-3))/(2*p)
x4 = (1+p - np.sqrt(p**2-2*p-3))/(2*p)

plt.plot(p, abs(df2dt(x2,p)), label =  r'Módulo da derivada para $X^* = \frac{p-1}{p}$')
plt.plot(p, abs(df2dt(x3,p)), label =  r'Módulo da derivada para $X_+^* = \frac{1 + p + \sqrt{p²-2p-3}}{2p}$')
plt.plot(p, abs(df2dt(x4,p)), label =  r'Módulo da derivada para $X_-^* = \frac{1 + p - \sqrt{p²-2p-3}}{2p}$')
plt.plot(p,[1 for _ in p], '--')
plt.xlabel('p')
plt.ylabel(r'$\left|\frac{df^2}{dx}\right|$')
plt.legend()
plt.ylim(0,3)
plt.show()
