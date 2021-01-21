def Euler(dt,vars,params,funcs):
    update = np.array([f(*vars,*params) for f in funcs])
    return vars + update*dt

import numpy as np
import matplotlib.pyplot as plt

def logistic(x,p):
    return p*x*(1-x)

ps = [1,1.2,1.5,2.5] ## Parameters of the logistic equation
x = {p:[0.3] for p in ps} ## Initial conditions
params = {p:[p] for p in ps}
funcs = [logistic]
T = 100
dt = 0.01
ts = list(range(int(T/dt)+1))

for p in ps:
    for t in range(int(T/dt)):
        pos = np.array([x[p][t]])
        pos = Euler(dt,pos,params[p],funcs)
        x[p].append(pos[0])

for p in ps:
    plt.plot(ts,x[p])
plt.show()
