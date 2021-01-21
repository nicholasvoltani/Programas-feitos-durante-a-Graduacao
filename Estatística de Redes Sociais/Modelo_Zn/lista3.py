import numpy as np
import random
import matplotlib.pyplot as plt


def sign(x):
	if x > 0:
		return 1
	elif x < 0:
		return -1
	else:
		return 0

def Zn(N):
	return range(-N,N+1)

def Probs(l,z):
	'''
	Returns probabilities that [O = +1, O = -1]
	'''

	denom = np.exp(l*sign(z)) + np.exp(-l*sign(z))
	positive = np.exp(l*sign(z))/denom
	negative = 1-positive
	return [positive,negative]

def ChooseO(probs,z):
	O = random.choices([1,-1],weights=probs)[0]
	return O

def AdvanceSn(N,l,z):
	probs = Probs(l,z)
	o = ChooseO(probs,z)
	Sn = z + o

	if Sn > N:
		Sn = N
	if Sn < -N:
		Sn = -N
	return Sn


l = 0
T = 100000
N = 5
z = 0
hist = [z]
avgs = [z]

for k in range(1,T):
	z = AdvanceSn(N,l,z)
	hist.append(z)
	avg = (k*(avgs[-1])+z)/(k+1)
	avgs.append(avg)


## Histograma dos S^{\lambda}
plt.hist(hist,bins=40)
plt.title("Histograma de "+ r"$S^{\lambda}_n$"+"\n"+r"$\lambda =$" + f"{l}; " + r"$T = $" + f"{T}")
plt.show()

if l == 0:
	## Pressão média 
	plt.plot(range(T),avgs)
	plt.plot(range(T),[0 for k in range(T)], '--')
	plt.xlabel("Iteração")
	plt.ylabel("Pressão Média")
	plt.title("Valor médio de "+r"$S_n^{\lambda}$"+r"$\lambda =$" +f"{l}; " + r"$T = $" + f"{T}")
	plt.show()
