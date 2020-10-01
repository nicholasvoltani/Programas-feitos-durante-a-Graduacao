import sys
from matplotlib.animation import FuncAnimation,PillowWriter
import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import gif
from math import comb
from erdosrenyi import ErdosRenyiAdj, GenerateErdosRenyi

## Initially, N = 2
N = 2
fig = plt.figure()
ax = plt.subplot(1,1,1)
for p in [0.1*t for t in range(11)]:
          M = ErdosRenyiAdj(N,p) ## Reminder that M is upper-triangular
          G = GenerateErdosRenyi(N,p,M)

          maxlikelihoods = [M.sum()/(comb(N,2))] ## Max Lklhd for N=2
          ## Iterate T times
          T = 500
          for t in range(1,T):
              ## Create to-be-adjacency matrix
              M_t = np.zeros((N+t,N+t))
              ## Left upper portion is previous adj matrix
              M_t[0:t+1,0:t+1] = M
              M_t[0:t+1,t+1] = random.choices([0,1],k=t+1,weights=[(1-p),p])

              ## We call it the new adjacency matrix, of size N + t
              M = M_t
              maxlikelihoods.append(M.sum()/(comb(N+t,2)))

          ax.plot(list(range(2,T+2)), maxlikelihoods, label = f"Max. Likelihood for p={p:.2f}.")
          plt.xlim(2,T)


chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.6, chartBox.height])
ax.legend(loc='upper center', bbox_to_anchor=(1.45, 0.8), shadow=True, ncol=1)

plt.show()
