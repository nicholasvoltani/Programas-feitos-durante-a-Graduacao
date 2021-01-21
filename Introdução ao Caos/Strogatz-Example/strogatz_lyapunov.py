import numpy as np
import matplotlib.pyplot as plt

iteration = lambda x,p: np.sin(x)/p
derivative = lambda x,p: np.cos(x)/p

ps = np.linspace(1.3, 0, 3000)
x0 = 0.001
x1 = -0.001
Ttrans = 1000
Tstat = 1000

## Points which will be plotted
xf = []
pf = []
lyapunov_u = []

for p in ps:
    xu = x0
    xb = x1
    lyap_u = 0

    ## Removing the transient
    for i in range(Ttrans):
        xu = iteration(xu,p)
        xb = iteration(xb,p)
        lyap_u += np.log(abs(derivative(xu,p)))
    
    ## Plotting fixed points
    for i in range(Tstat):
        xu = iteration(xu,p)
        xf.append(xu)
        pf.append(p)
        xb = iteration(xb,p)
        xf.append(xb)
        pf.append(p)
        lyap_u += np.log(abs(derivative(xu,p)))
    
    lyapunov_u.append(lyap_u/(Ttrans+Tstat))

plt.subplot(2,1,1)
plt.plot(pf,xf,',k')
plt.title(r"Bifurcation diagram: $x_{n+1} = \frac{\sin(x)}{p}$")
plt.subplot(2,1,2)
plt.plot(ps,lyapunov_u,'r')
plt.title("Lyapunov Exponents")

plt.show()