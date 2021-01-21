import numpy as np
import matplotlib.pyplot as plt

iteration = lambda x,p: np.sin(x)/p
ps = np.linspace(1.1, 0, 5000)
x0 = 0.001
x1 = -0.001
Ttrans = 1000
Tstat = 1000

plt.figure()
## Points which will be plotted
xf = []
pf = []

for p in ps:
    xu = x0
    xb = x1
    
    ## Removing the transient
    for i in range(Ttrans):
        xu = iteration(xu,p)
        xb = iteration(xb,p)
    
    ## Plotting fixed points
    for i in range(Tstat):
        xu = iteration(xu,p)
        xf.append(xu)
        pf.append(p)
        xb = iteration(xb,p)
        xf.append(xb)
        pf.append(p)
        #plt.scatter([p,p],[xu,xb], c='black')

plt.plot(pf,xf,',')
at_0 = []
for n in range(10):
    if n==0:
        at_0.append(n*np.pi)
    else:
        at_0.append(n*np.pi)
        at_0.append(-n*np.pi)
ps_0 = [0 for k in at_0]

plt.plot(ps_0,at_0,',k')
plt.title("Bifurcation Diagram:\n" + r"$ x_{n+1} = \frac{\sin(x_n)}{p}$")
plt.xlabel('p')
plt.ylabel('x')
plt.ylim(-10*np.pi-5,10*np.pi+5)
plt.show()
