import networkx as nx
import matplotlib.pyplot as plt

def WattsStrogatzGraph(N, k):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for v in G.nodes():
        ## Add edges (v,(v-k)%N,(v,(v-(k-1))%N),
        ## ..., (v,(v+k-1)%N), (v,(v+k)%N)
        G.add_edges_from([((v+i)%N, v) for i in range(1,k+1)])
        G.add_edges_from([((v-i)%N, v) for i in range(-k,0)])
    return G

nx.draw_circular(G)
plt.show()
