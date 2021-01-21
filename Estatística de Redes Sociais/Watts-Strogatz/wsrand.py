import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

def WattsStrogatzRandomizer(G,p):
    '''Given a graph G, randomly changes the destination of each edge,
    with probability p'''
    H = G.copy()
    for e in G.edges():
        n = random.random()
        if n < p:
            while True:
                v = random.choice(list(G.nodes()))
                print(e)
                print((e[0],v) in G.edges())
                if not (v in list(G.neighbors(e[0])) or v == e[0]):
                    H.add_edge(e[0],v)
                    H.remove_edge(e[0],e[1])
                    break
                

    return H



G = nx.Graph()
G.add_nodes_from(range(5))
G.add_edges_from([(n-1)%5, (n+1)%5] for n in G.nodes())
print(G.edges())
plt.subplot(211)
nx.draw(G)

H = WattsStrogatzRandomizer(G,0.1)
plt.subplot(221)
nx.draw(H)
plt.show()
