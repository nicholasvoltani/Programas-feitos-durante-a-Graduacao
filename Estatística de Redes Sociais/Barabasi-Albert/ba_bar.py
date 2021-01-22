from barabasi_albert import BAEvolve
import networkx as nx
import matplotlib.pyplot as plt
import gif
import random
import sys
from matplotlib.cm import ScalarMappable
plt.style.use('ggplot')

if len(sys.argv) != 2:
    raise Exception("Usage: $python3 ba_bar.py <gifname.gif>")

fig = plt.figure()

T = 100 ## Time of iteration

G = nx.Graph()
G.add_nodes_from(range(2))
## Starts with an edge between first nodes
G.add_edge(0,1)

@gif.frame
def plot_bar(it,G):
    nodes = list(G.nodes())
    degrees = list(map(G.degree, nodes))
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
    G = BAEvolve(G)
    
gif.save(frames, sys.argv[1], duration = 10, unit='s', between='startend')
