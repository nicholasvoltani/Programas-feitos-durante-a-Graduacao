import sys
import random
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

T = 50 ## Max iterations
N = 10  ## Size of square
O = [0,1] ## Possible opinions
random.seed(9359365)

def get_neighbors(i,j,N):
	nbrs = []
	nbrs.append(((i+1)%N,j))
	nbrs.append(((i-1)%N,j))
	nbrs.append((i,(j+1)%N))
	nbrs.append((i,(j-1)%N))

	return nbrs

def ChooseOpinion(influencers,opinions,N):
	list_opinions = []

	for infl in influencers:
		list_opinions.append(opinions.iloc[infl])

	opinion = random.choices(list_opinions, k=1)[0]
	return opinion

def ColorMap(x):
	if x == 0:
		return 'r'
	elif x == 1:
		return 'b'
	else:
		raise Exception("x != {0,1}")

x = []
y = []

for i in range(N):
	for j in range(N):
		x.append(i)
		y.append(j)

population = list(zip(x,y))
opinions = pd.DataFrame(np.random.randint(0,high=2,size=(N,N)))

color = ['r' if opinions[i][j]==0 else 'b' for (i,j) in zip(x,y)]
iteration = 0
fig = plt.figure()
plt.scatter(x,y,color=color)
plt.title(f"Iteração {iteration}")


def update(iteration):
    
    for _ in range(10):
        ## Chosen node (i,j)
    	sample = random.choices(population,k=1)[0]
    	
    	## Its influencers above, below, to left and to right (mod N)
    	influencers = get_neighbors(*sample,N)

    	## Chooses opinion by randomly choosing some influencer's
    	opinion = ChooseOpinion(influencers, opinions, N)

    	opinions.iloc[sample] = opinion

    	## Plots grid of points
    	color = ['r' if opinions[i][j]==0 else 'b' for (i,j) in zip(x,y)]
    	plt.scatter(x,y,color=color)
    	plt.title(f"Iteração {iteration*10}")

    
if __name__ == "__main__":
    anim = FuncAnimation(fig, update, frames = range(T), interval = 100)
    if len(sys.argv) > 1:
        writer = PillowWriter(fps=5)
        anim.save(sys.argv[1], writer = writer)
        plt.show()
    else:
        plt.show()
