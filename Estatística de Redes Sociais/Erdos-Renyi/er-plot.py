import sys
from matplotlib.animation import FuncAnimation,PillowWriter
import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import gif
from math import comb
from erdosrenyi import ErdosRenyiAdj, GenerateErdosRenyi
N = 100
p=0.3

M = ErdosRenyiAdj(N,p)
G = GenerateErdosRenyi(N,p,M)
cc = nx.triangles(G)
cc = {k:(cc[k]/comb(nx.degree(G,k),2) if nx.degree(G,k)>=2 else 0) for k in cc.keys()}
cc = np.sum(list(cc.values()))/N
print(cc)
nx.draw(G)
plt.title(f"Average Clustering {cc}")
plt.show()
