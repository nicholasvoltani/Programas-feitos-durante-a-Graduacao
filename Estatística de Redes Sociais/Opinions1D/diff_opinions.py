import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,PillowWriter
import random
import networkx as nx
import copy
random.seed(49359365)

T = 80 ## Max iterations
N = 10  ## Number of nodes
O = [1,-1] ## Possible opinions

fig, ax = plt.subplots()
G = nx.Graph()
G.add_nodes_from(range(N))
edges = [(i,(i+1)%N) for i in range(N)]
G.add_edges_from(edges)
opinions = random.choices(O, k = N, weights = [0.7,0.3])
nx.draw_circular(G)

opinions_matrix = []
opinions_matrix.append(opinions)

for i in range(0,T):
    new_opinions = copy.deepcopy(opinions_matrix[i])
    sample = random.sample(list(G.nodes()),1)[0]
    influencers = [(sample-1)%N, (sample+1)%N]
    influencing_opinions = [opinions_matrix[i][infl] for infl in influencers]

    ## Code below commented, since it's equivalent to choosing randomly between infls' opinions
    #probplus = influencing_opinions.count(1)
    #probminus = influencing_opinions.count(-1)
    #probs = [probplus, probminus]
    #probs = [probplus/len(probs), probminus/len(probs)] ## Normalizing probabilities

    ## Updating past opinions vector, changing only sample's opinions
    new_opinions[sample] = random.choice(influencing_opinions)
    opinions_matrix.append(new_opinions)
    
def update(iteration):
    colors = []
    for node in list(G.nodes()):
        if opinions_matrix[iteration][node] == 1:
            colors.append('b')
        elif opinions_matrix[iteration][node] == -1:
            colors.append('r')
    nx.draw_circular(G, node_color=colors)
    plt.title(f"Prob($O_0 = $Blue +1) = $0.7$ || Iteration {iteration}")


if __name__ == "__main__":
    anim = FuncAnimation(fig, update, frames = range(T), interval = 100)
    if len(sys.argv) > 1:
        writer = PillowWriter(fps=20)
        anim.save(sys.argv[1], writer = writer)
        plt.show()
    else:
        plt.show()
