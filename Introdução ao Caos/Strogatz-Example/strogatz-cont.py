import numpy as np
import matplotlib.pyplot as plt

def f(p):
    return lambda x: np.sin(x) - p*x

def derivative(x,p):
    return np.cos(x) - p

range_of_intersect = np.linspace(-30,30,12000)
threshold = 5e-05
ps = np.linspace(0, 1.2, 1000)

plt.figure()
## Points which will be plotted
xf = np.array([])
pf = np.array([])

for p in ps:
    ## We seek points x \in range_of_intersect which make (dx/dt=)f==0
    diffs = np.array(list(map(f(p), range_of_intersect)))
    indices_zeros_p = np.where(np.isclose(0.0,diffs,atol=threshold))
    indices_zeros_p = np.array(indices_zeros_p).ravel()
    if len(indices_zeros_p)==0:
        continue
    points_x_p = [range_of_intersect[i] for i in indices_zeros_p]
    if 0 in points_x_p:
        print(f"0 está no intervalo para {p}")
    points_p = [p for _ in points_x_p]
    
    xf = np.r_[xf,points_x_p]
    pf = np.r_[pf,points_p]


plt.plot(pf,xf,'.k',markersize=8)
plt.xlabel('p')
plt.ylabel('x')
plt.ylim(-30,30)
plt.title(r"Bifurcation diagram for $\frac{dx}{dt} = \sin(x) - px$")
#plt.savefig("bifurc1.png")
