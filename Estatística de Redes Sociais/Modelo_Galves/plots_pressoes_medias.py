from funcs_galves import *
import numpy as np
import matplotlib.pyplot as plt
import random

## Mudar valores aqui!
beta = 2
N = 10
T = 10000
##

U = InitializeGalvesLocherbach(N)
#U = StairChain(N)
totalsum = [U[0]] ## /1

for k in range(1,T):
	## Pressões |maiores| falam primeiro
	U = Iterate(N,U,beta)
	totalsum.append(((k)*totalsum[-1]+U[0])/(k+1))

x = [k for k in range(T)]

plt.plot(x,totalsum)

if beta > 1:
	plt.plot(x,[(N-1)/2 for _ in range(T)])
	plt.legend(["Valor médio",r"$\frac{N-1}{2} = $"+f"{(N-1)/2}"])
if beta == 0:
	plt.plot(range(T),[0 for k in range(T)], '--')

plt.xlabel("Iteração")
plt.ylabel("Valor médio de U[0]")
plt.title(r"$\beta =$" + f"{beta}; " + r"$T = $" + f"{T}")
plt.show()