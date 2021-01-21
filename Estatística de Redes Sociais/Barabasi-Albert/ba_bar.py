from barabasi_albert import BAEvolve
import networkx as nx
import matplotlib.pyplot as plt
import gif
import random
import sys
from matplotlib.cm import ScalarMappable
plt.style.use('ggplot')

fig = plt.figure()

T = 500 ## Time of iteration

G = nx.Graph()
G.add_nodes_from(range(2))
## Randomly starts with an edge between first nodes
if random.randint(0,1):
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
