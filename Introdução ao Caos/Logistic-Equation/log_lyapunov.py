import numpy as np
import matplotlib.pyplot as plt

def logistic(x,p):
    return p*x*(1-x)

def derivative(x,p):
    return p*(1-2*x)

ps = np.linspace(1, 4, 667)
x0 = 0.6
Ttrans = 5000
Test = 200
lyapunovs = []
pps = []
xs = []

for p in ps:
    x = x0
    lyapunov = np.log(abs(derivative(x,p)))
    for _ in range(Ttrans):
        x = logistic(x,p)
        lyapunov += np.log(abs(derivative(x,p)))
    for _ in range(Test):
        x = logistic(x,p)
        xs.append(x)
        pps.append(p)
        lyapunov += np.log(abs(derivative(x,p)))
    lyapunov /= (Ttrans+Test)
    lyapunovs.append(lyapunov)

plt.subplot(2,1,1)
plt.title("Exercício 73")
plt.plot(pps,xs, ',k')
plt.subplot(2,1,2)
plt.plot(ps,lyapunovs,',k')
plt.show()
        
