from barabasi_albert_directed import BA_Dir_Evolve
import networkx as nx
import matplotlib.pyplot as plt
import gif
import random
import sys
from matplotlib.cm import ScalarMappable
plt.style.use('ggplot')

fig = plt.figure()

T = 200 ## Time of iteration

G = nx.DiGraph()
G.add_nodes_from(range(2))

G.add_edge(0,1)
G.add_edge(1,0)

@gif.frame
def plot_bar(it,G):
    nodes = list(G.nodes())
    eff_degree = lambda x: G.in_degree(x) - G.out_degree(x)
    degrees = list(map(eff_degree, nodes))
    plt.bar(nodes, degrees)
    plt.xlabel("Node label")
    plt.ylabel("Degree of node")
    plt.title(f"Iteration {it}")
        
frames = []
for it in range(T):
    ## Plot
    frame = plot_bar(it,G)
    frames.append(frame)
    ## Update
    G = BA_Dir_Evolve(G)
    
gif.save(frames, sys.argv[1], duration = 20, unit='s', between='startend')
