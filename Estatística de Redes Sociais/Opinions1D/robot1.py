import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,PillowWriter
import random
import networkx as nx
import copy
random.seed(49359365)

T = 700 ## Max iterations
N = 10  ## Number of nodes
O = [1,-1] ## Possible opinions

fig, ax = plt.subplots()
G = nx.Graph()
G.add_nodes_from(range(N))
edges = [(i,(i+1)%N) for i in range(N-1)]
G.add_edges_from(edges)
G.add_node(N)
G.add_edges_from([(N-1,N),(N,0)])

opinions = random.choices(O, k = N)
opinions.append(1) ## We assume N is like a bot, parroting only $O_N = +1$
nx.draw_circular(G)

    
def update(iteration):
    global opinions
    ## Prints population's previous opinions
    colors = []
    for node in list(G.nodes()):
        if opinions[node] == 1:
            colors.append('b')
        elif opinions[node] == -1:
            colors.append('r')
    nx.draw_circular(G, node_color=colors)
    plt.title(f"Iteration {iteration}")

    ## Update t = (it-1) -> t = it
    sample = random.sample(list(range(N)),1)[0]
    influencers = [(sample-1)%(N+1), (sample+1)%(N+1)]
    influencing_opinions = [opinions[infl] for infl in influencers]
    opinions[sample] = random.choice(influencing_opinions)
    

if __name__ == "__main__":
    anim = FuncAnimation(fig, update, frames = range(T), interval = 40)
    if len(sys.argv) > 1:
        writer = PillowWriter(fps=25)
        anim.save(sys.argv[1], writer = writer)
        plt.show()
    else:
        plt.show()
