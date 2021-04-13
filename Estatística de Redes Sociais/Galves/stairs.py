from funcs_galves import *
import numpy as np

N = 5
G = InitializeGalvesLocherbach(N)
S = StairChain(N)
print(f"G = {G} \nS = {S}")
equals = np.equal(G,S)
t = 0
Tmax = 1000000

while any(equals) != True or t < Tmax:
	A, o = ChooseAgentAndOpinion(G)
	G = AdvanceChain(G,A,o)
	equals = np.equal(G,S)
	t += 1
	if abs(sum(G)-sum(S)) <= 2:
		print(G)

print(f"t = {t} \nG = {G}\nS = {S}")