import numpy as np
import matplotlib.pyplot as plt

def quadratic(x,C):
    return C - x**2

C = np.linspace(-0.5, 2, 10000)
Ttrans = 1000
Test = 100
xs = []
cs = []
for c in C:
    x = 0.9
    for _ in range(Ttrans):
        x = quadratic(x,c)
    for _ in range(Test):
        x = quadratic(x,c)
        xs.append(x)
        cs.append(c)

x_menos = 0.5*(-1-np.sqrt(1+4*np.array(cs))) 
plt.plot(cs, xs , ',k',label = r"Diagrama de Bifurcação: $x_{n+1} = C - x_n^2$")
plt.plot(cs, x_menos, ',r', label = r"$x^*_- = \frac{-1-\sqrt{1+4C}}{2}$")
plt.title(r"Exercício $71$")
plt.legend()
plt.show()
