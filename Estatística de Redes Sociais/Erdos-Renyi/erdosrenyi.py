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
    m = np.zeros((N,N))
    print(m)
    for l in range(N-1):
    	n = random.choices([1,0], weights = [p,1-p],k= N-l-1)
    	m[l,l+1:] = n
    	print(m)
    return m

def GenerateErdosRenyi(N,p,adj):
    G=nx.Graph()
    rows,cols = np.where(adj==1)
    edges = zip(rows.tolist(),cols.tolist())
    G.add_nodes_from(range(N))
    G.add_edges_from(edges)
    return G

def local_clustering(G,M,v):
    '''Given a graph G and its adjacency matrix M, as well as some vertex v, 
    compute the local clustering of v.
    '''
    cv = 0
    if G.degree(v) < 2:
        ## Thus, impossible to form triangles with other vertices
        return cv
    for v1 in range(N): ## G.nodes() == range(N)
        for v2 in range(v1,N):
            cv += (1/comb(G.degree(v),2))*M[v][v1]*M[v1][v2]*M[v2][v]
    return cv

def average_clustering(G,M):
    c = 0
    N = len(G.nodes())
    for v in G.nodes():
        c += (1/N)*local_clustering(G,M,v)
    return c



