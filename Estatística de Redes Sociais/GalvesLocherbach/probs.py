import random
import numpy as np

def InitializeGalvesLocherbach(N):
	G = np.array([0 for k in range(N)])
	
	## Guarantees that G has at least one 0 (not really necessary at first, but still)
	sample = random.sample(range(N),1)[0]
	
	## Giving each agent some initial social pressure
	for k in range(N):
		if k != sample:
			## Arbitrary choice of min/max initial pressures, could be anything else
			G[k] = random.randint(-5,5)

	return G

def r(a,U):
	'''a \in [0,len(U)]'''
	denom = np.sum(np.cosh(U))

	return np.cosh(U[a])/denom

def Cumulative_r(a,U,k):
	r = 0
	## k >= 0, first index
	for i in range(k+1):
		r += r(i,U)

	return r


def O_Plus(U,A):
	denom = 1 + np.exp(-2*U[a])
	return 1/denom

def ChooseAgentAndOpinion(U):
	## To choose opinionating agent from U
	xi_1 = random.uniform(0,1)
	## To choose their opinion
	xi_2 = random.uniform(0,1)

	
	#### Choosing agent A
	cumulatives = list(map(Cumulative_r,U))
	cumulatives = list(map(lambda x: x>xi_1, cumulatives))
	
	## Chooses agent A whose cumulative is the first to be >xi_1
	A = cumulatives.index(True)


	#### Choosing A's opinion
	if xi_2 > O_Plus(U,A):
		o = 1
	else:
		o = -1

	return A, o

def AdvanceChain(U,A,o):
	new_U = U.copy()

	## All social pressures change by o
	new_U += o
	## Agent who opinionated resets his social pressure
	new_U[A] = 0
	
	return new_U