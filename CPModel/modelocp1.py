import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,PillowWriter
import random
import networkx as nx
import copy
import gif
from funcs import *

random.seed(93593651)

T = 50 ## Max iterations
N = 13  ## Number of nodes
O = [1,-1] ## Possible opinions

## Start with a circular population
G = nx.Graph()
G.add_nodes_from(range(N))
edges = [(i,(i+1)%N) for i in range(N)]
G.add_edges_from(edges)

## Randomly initialize opinions
opinions = random.choices(O, k = N)

##### Functions to draw the gif ###################

gif.options.matplotlib['dpi']=300

@gif.frame
def plot(it):
    global opinions
    plotGraph(G, opinions, it)

    ## Sample an agent who will opine
    sample = random.sample(list(G.nodes()),1)[0]

    ## Updating opinions vector, changing only sample's opinions
    ## weighted by its influencers (neighbors)
    opinions[sample] = ChooseOpinion(G,opinions,sample)

    ############  CP Model intricacies ###############
    neighbors = list(G.neighbors(sample))[:]
    nbr = random.sample(neighbors, 1)[0]

    if opinions[nbr] != opinions[sample]:
       ## *** Removing edges ***
        PeerPressureBrief(G, opinions, sample, nbr)

    else: ## opinions[nbr] == opinions[sample]
        ## *** Adding new edges ***
        AddNewEdgeBrief(G, opinions, sample, nbr)

        ## There is a chance that some neighbor of "nbr" (not already neighbor of "sample")
        ## also becomes a neighbor of "sample" (if not already neighbor of sample)
        

#########################################################

## Drawing each frame
frames = []
for it in range(T):
    frame = plot(it)
    frames.append(frame)
    
gif.save(frames,sys.argv[1],duration = 15, unit='s', between='startend')


