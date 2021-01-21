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
			G[k] = random.randint(-50,50)

	return G

def Probs(U,beta=1):
	'''
	Vector of each agent's probability function.
	'''
	DontReadMe = np.exp(beta*U) + np.exp(-beta*U)
	denom = sum(DontReadMe)

	num = np.exp(beta*U)

	return num/denom


def r(a,U, beta = 1):
	'''
	Probability that agent 'a' is chosen.
	'''
	DontReadMe = np.cosh(beta*U)
	denom = sum(DontReadMe)

	return np.cosh(beta*U[a])/denom

# def Cumulative_r(U):
# 	new_u = []
# 	cumulative = 0
# 	for i in range(len(U)):
# 		cumulative += r(i,U)
# 		new_u.append(cumulative)
# 	new_u = np.array(new_u)
# 	return new_u


def O_Plus(U,A, beta = 1):
	denom = 1 + np.exp(-2*beta*U[A])
	return 1/denom

def ChooseO(U,A,beta=1):
	p = O_Plus(U,A,beta=beta)
	xi = random.uniform(0,1)
	if xi < p:
		return 1
	else:
		return -1

def A1O1(U, beta = 1,xi_1 = random.uniform(0,1), xi_2 = random.uniform(0,1)):
	'''
	Yields an agent A and their opinion O, prioritizing agents "a" with the highest |U["a"]| values.
	'''
	
	## Sorting U by decreasing abs value
	U_agents = [(U[i],i) for i in range(len(U))]
	U_agents.sort(key=lambda x: -abs(x[0]))
	
	## To keep track of original agents' indexing
	sorted_U, perms = zip(*U_agents)
	#### Choosing agent A:
	#### Prioritize higher |U[A]| first!
	cumulative = 0
	for i in perms:
		A = perms.index(i)
		cumulative += r(A,U,beta)
		if cumulative > xi_1:
			break

	#### Choosing A's opinion
	if xi_2 < O_Plus(U,A, beta):
		o = 1
	else:
		o = -1
	#print(f"{A} emitted opinion {o}!")
	return A, o

def A2O2(U, permuts, beta = 1, xi_1 = random.uniform(0,1), xi_2 = random.uniform(0,1)):
	'''
	Yields an agent A and their opinion O, via given permutation "permuts".
	Also returns "permuts" with each index shifted to the left (first becomes last).
	'''
	## Sorting U by permuts's order
	## First element to be analyzed will be permuts[0]
	## and we have permuts[k] = (permuts[0] - k)%len(U)
	first = permuts[0]
	U_permut = np.concatenate((U[first:], U[:first]))
	
	#### Choosing agent A:
	#### Prioritize first ones in permuts!
	cumulative = 0
	for i in permuts:
		A = permuts.index(i)
		cumulative += r(A,U, beta)
		if cumulative > xi_1:
			break

	#### Choosing A's opinion
	if xi_2 < O_Plus(U,A,beta):
		o = 1
	else:
		o = -1
	#print(f"{A} emitted opinion {o}!")

	#### Return new permutation
	#### Reminder that our list will be 
	#### of the form [k, (k-1)%, ..., (k+2)%, (k+1)%)]
	#shift = lambda x: (x-1)%len(U)
	#new_permuts = sorted(permuts, key = shift)
	new_permuts = permuts[1:] + permuts[0:1]
	return A, o, new_permuts



def AdvanceChain(U,A,o):
	new_U = U.copy()

	## All social pressures change by o
	new_U += o
	## Agent who opined resets his social pressure
	new_U[A] = 0
	
	return new_U

def Iterate(N,U, beta):
	A = random.choices(range(N),weights=Probs(U,beta=beta))
	o = ChooseO(U,A,beta=beta)
	Un = AdvanceChain(U,A,o)
	return Un


def StairChain(N):
	S = [i for i in range(N)]
	return np.array(S)