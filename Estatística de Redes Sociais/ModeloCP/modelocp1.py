import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,PillowWriter
import random
import networkx as nx
import copy
import gif

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
	coloring = lambda x: 'b' if x == 1 else 'r'
	colors = list(map(coloring,opinions))
	plt.figure()
	nx.draw_networkx(G,pos = nx.kamada_kawai_layout(G),node_color=colors)
	plt.title(f"Iteration {it}")

	print(f"Iteração {it}")
	## Sample an agent who will opine
	sample = random.sample(list(G.nodes()),1)[0]
	influencing_opinions = [opinions[infl] for infl in G.neighbors(sample)]
	probplus = influencing_opinions.count(1)
	probminus = influencing_opinions.count(-1)
	probs = [probplus, probminus]
	## Normalizing probabilities
	probs = [probplus/len(probs), probminus/len(probs)] 

	## Updating opinions vector, changing only sample's opinions
	## weighted by its influencers (neighbors)
	opinions[sample] = random.choices(O, k=1, weights=probs)[0]
	neighbors = list(G.neighbors(sample))[:]

	## Updating edges
	for nbr in neighbors:
	    ## After "sample" opines,
	    ## each of its neighbors reconsider their relations with it

	    if opinions[nbr] != opinions[sample]:
	    	## *** Removing edges ***
	        ## nbr may cut relations with "sample"

	        ## Check for nbr's influencing opinions
	        influencing_opinions =  [opinions[infl] for infl in G.neighbors(nbr)]
	        probequal = influencing_opinions.count(opinions[nbr])
	        probdiff = influencing_opinions.count(-opinions[nbr])
	        tocancelornot = probequal/(probequal+probdiff)

	        ## With probability "tocancelornot", cut relations with "sample"
	        mu = random.random()
	        if mu < tocancelornot:
	            G.remove_edge(sample,nbr)
	            print(f"Removed edge {(sample,nbr)}!")

	    else: ## opinions[nbr] == opinions[sample]
	    	## *** Adding edges ***
	        ## There is a chance that some neighbor of "nbr" (not already neighbor of "sample")
	        ## also becomes a neighbor of "sample"
			## Such as to choose someone who wasn't already neighbor of sample
	        A = set(G.neighbors(sample))
	        B = set(G.neighbors(nbr))
	        possible_incomers = A.union(B) - A.intersection(B) - {sample,nbr} ## Can't have edges (v,v)
	        
	        if possible_incomers != set():
	        	incomer = random.sample(possible_incomers,1)[0]
	        	## Check for incomer's influencing opinions
	        	influencing_opinions = [opinions[infl] for infl in G.neighbors(incomer)]
	        	probequal = influencing_opinions.count(opinions[nbr])
	        	probdiff = influencing_opinions.count(-opinions[nbr])
	        	toaddornot = probequal/(probequal+probdiff)
	        	mu = random.random()
	        	if mu<toaddornot:
	        		if not (incomer, sample) in G.edges():
	        			G.add_edge(incomer, sample)
	        			print(f"Added edge {(incomer,sample)}!")
	        
	        else: ## No possible incomers, just pass
	        	pass

#########################################################

## Drawing each frame
frames = []
for it in range(T):
    frame = plot(it)
    frames.append(frame)
    
gif.save(frames,sys.argv[1],duration = 15, unit='s', between='startend')


