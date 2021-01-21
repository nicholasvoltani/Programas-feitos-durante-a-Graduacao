import networkx as nx
import matplotlib.pyplot as plt
import random

def BA_Dir_Evolve(G): 
    '''Given a graph G, evolve it according to the Barabási-Albert model.
    That is, it adds a new node to it (equal to len(G.nodes()) ), and gives it a connection with
    some other previously present node, chosen with its degree as a 
    probabilistic weight.
    If the graph is directed, then each iteration adds an edge *from* and an edge *towards* the newly added node, same rule as above.'''
    
    H = G.copy()
    
    ## To weigh on nodes' influences upon new_node
    INfluences = list(map(G.in_degree, list(G.nodes()))) ## To weigh in over nodes' inward-pointing edges
    OUTfluences = list(map(G.out_degree, list(G.nodes()))) ## To weigh in over nodes' outward-pointing edges
    old_nodes = list(G.nodes())
    new_node = len(G.nodes())
    H.add_node(new_node)

    in_chosen = random.choices(old_nodes,weights = INfluences)[0]
    out_chosen = random.choices(old_nodes,weights = OUTfluences)[0]
    
    new_edge_in = (new_node, in_chosen)
    new_edge_out = (new_node, out_chosen)
    H.add_edge(*new_edge_in)
    H.add_edge(*new_edge_out)
    
    return H
