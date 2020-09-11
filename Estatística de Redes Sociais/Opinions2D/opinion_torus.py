import sys
import random
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d as plt3d

random.seed(3)

T = 1000 ## Max iterations
N = 10  ## Number of nodes
O = [0,1] ## Possible opinions

def TorusCoordinates(theta,phi):
    r,R=0.7,0.7
    return ((R+r*np.cos(theta))*np.cos(phi),
            (R+r*np.cos(theta))*np.sin(phi),
            r*np.sin(theta))

## Torus's points

theta = (2*np.pi/N)*np.array(range(N))
phi = (2*np.pi/N)*np.array(range(N))
print(theta)
theta_var,phi_var = np.meshgrid(theta,phi)
X,Y,Z = TorusCoordinates(theta_var,phi_var)

## Create 3D figure
fig = plt.figure()
ax = fig.gca(projection="3d")
## Plotting entire torus
ax.plot_surface(X,Y,Z,cmap = 'Greys',alpha=0.75)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

## Initialize random opinions for NxN population
opinions = np.array([random.choices(O,k=N) for i in range(N)])

def update(iteration):
    global opinions
    ## Pick person (theta,phi) at random (not really theta/phi, just indices)
    sample_theta = random.sample(list(range(N)),1)[0]
    sample_phi = random.sample(list(range(N)),1)[0]
    influencers = [[(sample_theta+1)%N, sample_phi],
                   [(sample_theta-1)%N, sample_phi],
                   [sample_theta,(sample_phi+1)%N],
                   [sample_theta,(sample_phi-1)%N]]
    ## Choose random influencer, and change opinion to match theirs
    chosen = random.choice(influencers)
    opinions[sample_theta][sample_phi] = opinions[chosen[0]][chosen[1]]

    ## Only plot few iterations (will take some time...)
    if iteration%10 == 0:
        categories = opinions.flatten()
        ## Creating a color map for different opinions
        colormap = np.array(['r', 'b'])
        ## Plotting individual points
        ax.scatter3D(X,Y,Z, c = colormap[categories])
        plt.title(f"Iteration {iteration}")


    
if __name__ == "__main__":
    anim = FuncAnimation(fig, update, frames = range(T), interval = 40)
    if len(sys.argv) > 1:
        writer = PillowWriter(fps=25)
        anim.save(sys.argv[1], writer = writer)
        plt.show()
    else:
        plt.show()

