from funcs_galves import *
import matplotlib.animation as animation  
import matplotlib.pyplot as plt  
import numpy as np  

#random.seed(42)

#xi_1 = [0.76,0.89,0.21,0.17,0.03,0.12,0.48,0.58]
#xi_2 = [0.51,0.45,0.26,0.47,0.21,0.7,0.83,0.84]

xi_1 = 0.63
xi_2 = 0.51

#U1 = [np.array([0,-4,4,7])]
#U2 = [np.array([-5,0,3,1])]
U1 = [np.array([0,4,-5])]
U2 = [np.array([-2,0,10])]
print(f"xi_1 = {xi_1}")
print(f"xi_2 = {xi_2}")
print(f"U1_0 = {U1[0]}")
print(f"U2_0 = {U2[0]}\n")

i=0
print(f"Iteração {i+1}: U1")
A1,o1 = A1O1(U1[i], xi_1,xi_2)
new_u1 = AdvanceChain(U1[i],A1,o1)
U1.append(new_u1)
print("")

print(f"Iteração {i+1}: U2")
A2,o2 = A1O1(U2[i], xi_1,xi_2)
new_u2 = AdvanceChain(U2[i],A2,o2)
U2.append(new_u2)
print("")

print(f"Iteração {i+1}: U1 = {new_u1}")
print(f"Iteração {i+1}: U2 = {new_u2}\n\n")

i=1
print(f"Iteração {i+1}: U1")
A1,o1, new_permuts = A2O2(U1[i], [1,0,2])
new_u1 = AdvanceChain(U1[i],A1,o1)
U1.append(new_u1)
print("")

print(f"Iteração {1+i}: U2")
A2,o2, new_permuts = A2O2(U2[i], [1,0,2])
new_u2 = AdvanceChain(U2[i],A2,o2)
U2.append(new_u2)
print("")

print(f"Iteração {i+1}: U1 = {new_u1}")
print(f"Iteração {i+1}: U2 = {new_u2}")
