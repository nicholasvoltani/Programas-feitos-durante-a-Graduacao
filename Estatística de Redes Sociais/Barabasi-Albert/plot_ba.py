from barabasi_albert import BAEvolve
import networkx as nx
import matplotlib.pyplot as plt
import gif
import random
import sys
from matplotlib.cm import ScalarMappable
fig = plt.figure()

T = 50 ## Time of iteration

if len(sys.argv) != 2:
    raise Exception("Usage: $python3 plot_ba.py <gifname.gif>")

## Initializing graph 
G = nx.Graph()
G.add_nodes_from(range(2))
## Starts with an edge between both nodes
G.add_edge(0,1)

@gif.frame
def plot_node(it,G):
    coloring = list(map(G.degree,list(G.nodes())))
    cmap = plt.get_cmap("OrRd")
    nx.draw_networkx(G, pos= nx.kamada_kawai_layout(G), node_color = coloring,cmap = cmap)
    sm = ScalarMappable(cmap = cmap, norm = plt.Normalize(0, max(coloring)))
    sm.set_array([])
    cbar = plt.colorbar(sm)
    cbar.set_label("Degree",labelpad=20)
    plt.title(f"Iteration {it}")

frames = []
for it in range(T):
    ## Plot
    frame = plot_node(it,G)
    frames.append(frame)
    ## Update
    G = BAEvolve(G)
    
gif.save(frames, sys.argv[1], duration = 20, unit='s', between='startend')
