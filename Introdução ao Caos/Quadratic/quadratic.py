import numpy as np
import matplotlib.pyplot as plt

def quadratic(x,C):
    return C - x**2

## We have x_{n+1} = quad(x,C)
C = np.linspace(-0.5, 2, 10000)
Ttrans = 1000
Test = 100
xs = []
cs = []


x1 = (-1 + np.sqrt(1 + 4*C))/2
x2 = (-1 -  np.sqrt(1 + 4*C))/2

plt.plot(C,x1, label = r'x^*_1 =\frac{-1 + \sqrt(1 + 4c}}{2}') 
plt.plot(C,x2, label = r'x^*_2 =\frac{-1 - \sqrt(1 + 4c}}{2}')
plt.legend()
plt.show()
