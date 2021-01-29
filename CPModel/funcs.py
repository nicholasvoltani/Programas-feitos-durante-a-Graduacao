import numpy as np
import random
import networkx as nx
import copy

def ChooseOpinion(G, opinions, sample):
    '''Given a population "G" with opinion vector "opinions", and an opining agent "A", chooses its opinion based on his neighbors' opinions.'''

    ## See neighbors' opinions
    influencing_opinions = [opinions[infl] for infl in G.neighbors(sample)]
    ## How many opinions are +1
    probplus = influencing_opinions.count(1)
    ## How many opinions are -1
    probminus = influencing_opinions.count(-1)

    
    probs = [probplus, probminus]
    ## Normalizing probabilities
    probs = [probplus/len(probs), probminus/len(probs)] 

    ## Updating opinions vector, changing only sample's opinions
    ## weighted by its influencers (neighbors)
    opinion = random.choices([1, -1], k=1, weights=probs)[0]
    return opinion


def PeerPressureBrief(G, opinions, sample, nbr):
    ''' When opinions[sample] != opinions[nbr], *nbr* may cut relations with "sample",
    if *they* randomly find a neighbor of *theirs* who also disagrees with "sample". Else, *they* don't cut relations, by "peer pressure".
    Changes G.edges inplace.'''

    ## nbr searches for a peer's opinion
    other = random.sample(list(G.neighbors(nbr)), 1)[0]

    ## If other also agree with nbr, then nbr considers cutting relations with sample
    ## with prob = #(equal opinions)/3
    if opinions[other] != opinions[nbr]:
        mu = random.random()
        if mu > 2/3:
            G.remove_edge(sample,nbr)
            #print(f"Removed edge {(sample,nbr)}!")


def PeerPressureFull(G, opinions, sample, nbr):
    ''' When opinions[sample] != opinions[nbr], *nbr* may cut relations with "sample",
    if most of *their* neighbors also disagree with "sample". Else, *they* don't cut relations by "peer pressure".
    Changes G.edges inplace.'''

    ## Check for nbr's influencing opinions
    influencing_opinions = [opinions[infl] for infl in G.neighbors(nbr)]
    probequal = influencing_opinions.count(opinions[nbr])
    probdiff = influencing_opinions.count(-opinions[nbr])
    tocancelornot = probequal/(probequal+probdiff)

    ## With probability "tocancelornot", cut relations with "sample"
    mu = random.random()
    if mu < tocancelornot:
        G.remove_edge(sample,nbr)
        #print(f"Removed edge {(sample,nbr)}!")

def AddNewEdgeBrief(G, opinions, sample, nbr):
    '''When opinions[sample] == opinions[nbr], a neighbor of "nbr" may consider creating relations with "sample".
    Only considers agents that aren't already neighbors of "sample". Changes G.edges inplace. '''

    ## Consider neighbors of "nbr" that aren't connected to "sample" 
    A = set(G.neighbors(sample))
    B = set(G.neighbors(nbr))
    possible_incomers = B - A - {sample,nbr} ## Also disregarding "sample" and "nbr"
    
    ## If there are any so neighbors
    if possible_incomers != set():
        ## Sample one out
        incomer = random.sample(possible_incomers,1)[0]
        
        if opinions[incomer] == opinions[sample]:
            G.add_edge(incomer, sample)
            #print(f"Added edge {(incomer,sample)}!")


def AddNewEdgeFull(G, opinions, sample, nbr):
    '''When opinions[sample] == opinions[nbr], a neighbor of "nbr" may consider creating relations with "sample".
    Only considers agents that aren't already neighbors of "sample". Changes G.edges inplace. '''

    ## Consider neighbors of "nbr" that aren't connected to "sample" 
    A = set(G.neighbors(sample))
    B = set(G.neighbors(nbr))
    possible_incomers = B - A - {sample,nbr} ## Can't have edges (v,v)
    
    ## If there are any so neighbors
    if possible_incomers != set():
        ## Sample one out
        incomer = random.sample(possible_incomers,1)[0]
        
        ## Check for incomer's influencing opinions
        influencing_opinions = [opinions[infl] for infl in G.neighbors(incomer)]
        probequal = influencing_opinions.count(opinions[nbr])
        probdiff = influencing_opinions.count(-opinions[nbr])
        toaddornot = probequal/(probequal+probdiff)
        
        ## With probability "toaddornot", add relations with "sample"
        mu = random.random()
        if mu < toaddornot:
            if not (incomer, sample) in G.edges():
                G.add_edge(incomer, sample)
                #print(f"Added edge {(incomer,sample)}!")


def plotGraph(G, opinions, it):
    import networkx as nx
    import matplotlib.pyplot as plt

    coloring = lambda x: 'b' if x == 1 else 'r'
    colors = list(map(coloring,opinions))
    plt.figure()
    nx.draw_networkx(G,pos = nx.kamada_kawai_layout(G),node_color=colors)
    plt.title(f"Iteration {it}")

    print(f"Iteration {it}")
    