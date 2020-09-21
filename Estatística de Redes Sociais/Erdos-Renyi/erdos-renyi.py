import sys
from matplotlib.animation import FuncAnimation,PillowWriter
import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import gif
from math import comb

T = 50
N = 20
O = [-1,1]
p = 0.3
opinions = random.choices(O, k=N)

def ErdosRenyiAdj(N,p):
    adj = []
    for l in range(N):
        ## Creating upper triangular matrix
        m = np.array([0 for i in range(l+1)])
        n = np.random.uniform(size=N-l-1)
        n = np.where(n<=p,1,0)
        m = np.concatenate((m,n))
        adj.append(m)
    ## Symmetrizing 
    adj = np.array(adj)
    adj = adj + adj.T
    return adj

def GenerateErdosRenyi(N,p,adj):
    G=nx.Graph()
    rows,cols = np.where(adj==1)
    edges = zip(rows.tolist(),cols.tolist())
    G.add_nodes_from(range(N))
    G.add_edges_from(edges)
    return G

def degree(G,v):
    deg = 0
    for w in G.nodes():
        deg += M[v][w]
    return int(deg)

def local_clustering(G,M,v):
    '''Given a graph G and its adjacency matrix M, as well as some vertex v, 
    compute the local clustering of v.
    '''
    cv = 0
    if degree(G,v) < 2:
        ## Thus, impossible to form triangles with other vertices
        return cv
    for v1 in range(N): ## G.nodes() == range(N)
        for v2 in range(v1,N):
            cv += (1/comb(degree(G,v),2))*M[v][v1]*M[v1][v2]*M[v2][v]
    return cv

def average_clustering(G,M):
    c = 0
    N = len(G.nodes())
    for v in G.nodes():
        c += (1/N)*local_clustering(G,M,v)
    return c

M = ErdosRenyiAdj(N,p)
G = GenerateErdosRenyi(N,p,M)
cc = nx.triangles(G)
cc = {k:(cc[k]/comb(degree(G,k),2) if degree(G,k)>=2 else 0) for k in cc.keys()}
cc = np.sum(list(cc.values()))/N
print(cc)
nx.draw(G)
plt.title(f"Average Clustering {cc}")
plt.show()












#samples = random.choices(list(G.nodes()),k=T)
#gif.options.matplotlib['dpi']=300

#@gif.frame
#def plot(iteration, opinions):
    ## Print previous iteration
#    coloring = lambda x: 'b' if x==1 else 'r'
 #   colors = list(map(coloring,opinions))
  #  nx.draw_networkx(G,node_color=colors,pos=nx.spring_layout(G))
   # plt.title(f"Iteration {iteration}")

#frames = []
#for it in range(T):
 #   frame = plot(it,opinions)
  #  frames.append(frame)
    
    ## Updating
   # sample = samples[it]
   # influencers = list(G.edges(sample))
   # if len(influencers)>0:
   #     influencer = random.choice(influencers)[1]
   #     opinions[sample] = opinions[influencer]

#gif.save(frames,sys.argv[1],duration = 3.5,unit='s', between='startend')
