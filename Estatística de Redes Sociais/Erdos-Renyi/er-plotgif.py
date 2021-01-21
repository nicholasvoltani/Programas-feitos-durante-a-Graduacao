import sys
from matplotlib.animation import FuncAnimation,PillowWriter
import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import gif
from math import comb
from erdosrenyi import ErdosRenyiAdj, GenerateErdosRenyi

T = 50
N = 20
O = [-1,1]
p = 0.3
opinions = random.choices(O, k=N)

M = ErdosRenyiAdj(N,p)
G = GenerateErdosRenyi(N,p,M)
samples = random.choices(list(G.nodes()),k=T)
gif.options.matplotlib['dpi']=300

@gif.frame
def plot(iteration, opinions):
    ## Print previous iteration
    coloring = lambda x: 'b' if x==1 else 'r'
    colors = list(map(coloring,opinions))
    nx.draw_networkx(G,node_color=colors,pos=nx.spring_layout(G))
    plt.title(f"Iteration {iteration}")

frames = []
for it in range(T):
    frame = plot(it,opinions)
    frames.append(frame)
    
    ## Updating
    sample = samples[it]
    influencers = list(G.edges(sample))
    if len(influencers)>0:
        influencer = random.choice(influencers)[1]
        opinions[sample] = opinions[influencer]

gif.save(frames,sys.argv[1],duration = 3.5,unit='s', between='startend')
