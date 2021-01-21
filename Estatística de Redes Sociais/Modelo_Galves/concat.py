from funcs_galves import *
import numpy as np
import matplotlib.pyplot as plt
import gif
import random

## Some initial suggestions:

## beta = 1
	## seed = 93593651: k ~= 225
	## seed = 1200: k ~= 381

#random.seed(93593651)

## Max number of iteration blocks
M = 1000
## Size of population
N = 5
## Polarization parameter
beta = 1

## Initialize convictions for u and v
Uu = np.array([0,3,2,4,6])
Uv = np.array([6,4,2,3,0])
#Uu = InitializeGalvesLocherbach(N)
#Uv = InitializeGalvesLocherbach(N)

## History of the lists
Uus = [Uu]
Uvs = [Uv]

## To plot bar graphs
x = list(range(N))
## To check for convergence
S = StairChain(N)

## Permutations for Algorithm 2
permuts = list(range(N))
permuts.reverse()

def plot(it,x,k,beta, msg = ''):
	plt.figure()
	plt.bar(x,Uus[it],color = 'red')
	plt.bar(x,Uvs[it],color = 'blue')
	plt.bar(x,S, color = 'yellow')
	plt.title(f"{k}-th batch; beta = {beta}" + msg)
	plt.legend(["Uu","Uv","Stair"])

count = 0
plot(count,x,0,beta)
eq = True

for k in range(M):
	#### First block: Algorithm 1
	print(f"{k}-th first block: Algorithm 1")
	for k1 in range(N):
		## Both lists need to be advanced with
		## same random xi's
		xi_1 = random.uniform(0,1)
		xi_2 = random.uniform(0,1)

		## Advance u
		A1u, o1u = A1O1(Uu, beta, xi_1, xi_2)
		Uu = AdvanceChain(Uu, A1u, o1u)
		Uus.append(Uu)
		
		## Advance v
		A1v, o1v = A1O1(Uv, beta,xi_1, xi_2)
		Uv = AdvanceChain(Uv, A1v, o1v)
		Uvs.append(Uv)
		count += 1 

	#### Second blocK: Algorithm 2
	print(f"{k}-th second block: Algorithm 2")
	for k2 in range(N):
		## Both lists need to be advanced with
		## same random xi's
		xi_1 = random.uniform(0,1)
		xi_2 = random.uniform(0,1)

		## Advance u
		A2u, o2u, _ = A2O2(Uu, permuts,beta,xi_1,xi_2)
		AdvanceChain(Uu,A1u,o1u)
		Uus.append(Uu)

		## Advance v
		## save permuts for next iteration
		A2v, o2v, permuts = A2O2(Uv,permuts,beta,xi_1,xi_2)
		Uvs.append(Uv)
		count += 1

	print(f"End of {k}-th batch\n")
	#if k % 80 == 0:
		#pass
		# plot(count,x)
		# plt.show()


	## Stopping condition: both lists are stair-chain
	if np.array_equal(Uu,Uv):
		if eq:
			print("Both lists are equal!\n")
			plot(count,x,k+1, beta, msg = "\nUu and Uv equal to each other!")
			eq = False

		if np.array_equal(Uu,S):
			print(f"{Uu}, {Uv}, {S}")
			print(f"And they're equal to {S}!!!\n")
			plot(count,x,k+1, beta, msg = "\nBoth lists equal to the stair chain!!")
			break
	else:
		print("Both lists are different...\n")

plt.show()
