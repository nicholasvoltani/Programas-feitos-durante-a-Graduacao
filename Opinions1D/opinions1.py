import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,PillowWriter
import random
import networkx as nx
import copy

T = 200 ## Max iterations
N = 10  ## Number of nodes
O = [1,-1] ## Possible opinions

fig, ax = plt.subplots()
G = nx.Graph()
G.add_nodes_from(range(N))
edges = [(i,(i+1)%N) for i in range(N)]
G.add_edges_from(edges)
opinions = random.choices(O, k = N)
nx.draw_circular(G)

opinions_matrix = []
opinions_matrix.append(opinions)

for i in range(0,T):
    new_opinions = copy.deepcopy(opinions_matrix[i])
    samples = random.sample(list(G.nodes()),N)
    for sample in samples:
        influencers = [(sample-1)%N, (sample+1)%N]
        influencing_opinions = [opinions_matrix[i][infl] for infl in influencers]
        probplus = influencing_opinions.count(1)
        probminus = influencing_opinions.count(-1)
        probs = [probplus, probminus]
        probs = [probplus/len(probs), probminus/len(probs)] ## Normalizing probabilities
        new_opinions[sample] = random.choices(O, k=1, weights=probs)[0]
    opinions_matrix.append(new_opinions)
    
def update(iteration):
    colors = []
    for node in list(G.nodes()):
        if opinions_matrix[iteration][node] == 1:
            colors.append('b')
        elif opinions_matrix[iteration][node] == -1:
            colors.append('r')
    nx.draw_circular(G, node_color=colors)
    plt.title(f"Iteration {iteration}")


if __name__ == "__main__":
    anim = FuncAnimation(fig, update, frames = range(T), interval = 100)
    if len(sys.argv) > 1:
        writer = PillowWriter(fps=20)
        anim.save(sys.argv[1], writer = writer)
        plt.show()
    else:
        plt.show()
