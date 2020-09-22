import numpy as np
import matplotlib.pyplot as plt

iteration = lambda x,p: np.sin(x)/p
ps = np.linspace(0.000001, 0.0000000001, 5000)
x0 = 0.001
x1 = -0.001
Ttrans = 3000
Tstat = 2000

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
for n in range(100):
    if n==0:
        at_0.append(n*np.pi)
    else:
        at_0.append(n*np.pi)
        at_0.append(-n*np.pi)
ps_0 = [0 for k in at_0]
plt.plot(ps_0,at_0,',k')
plt.title("Bifurcation Diagram:\n" + r"$ \frac{dx}{dt} = \sin(x) - px$")
plt.xlabel('p')
plt.ylabel('x')
plt.ylim(-100*np.pi-50,100*np.pi+50)
plt.show()
