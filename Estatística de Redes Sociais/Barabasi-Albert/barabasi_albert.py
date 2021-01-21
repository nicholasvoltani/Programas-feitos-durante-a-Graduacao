import networkx as nx
import matplotlib.pyplot as plt
import random

def BAEvolve(G): 
    '''Given a graph G, evolve it according to the Barabási-Albert model.
    That is, it adds a new node to it (equal to len(G.nodes()) ), and gives it a connection with
    some other previously present node, chosen with its degree as a 
    probabilistic weight.
    If the graph is directed, then each iteration adds an edge *from* and an edge *towards* the newly added node, same rule as above.'''
    
    H = G.copy()
    
    ## To weigh on nodes' influences upon new_node
    influences = list(map(G.degree, list(G.nodes()))) ## To weigh in over nodes' influence
    old_nodes = list(G.nodes())
    new_node = len(G.nodes())
    H.add_node(new_node)

    chosen = random.choices(old_nodes,weights = influences)[0]
    new_edge = (new_node, chosen)
    H.add_edge(*new_edge)
    
    return H
