import numpy as np
import matplotlib.pyplot as plt

x0 = 0.8
C = np.linspace(-0.25, 2, 6)
T = 1000

plt.subplots(3, 2)

def quadratic(x, C):
	return C - x**2

def solution(x0,t,C):
	return x0 + np.sqrt(C)*np.tan(t/np.sqrt(C))


for i in range(1,7):
	plt.subplot(3,2,i)
	xn1s = [x0]
	ys = [x0]
	for j in range(T):
		xn1 = quadratic(xn1s[j],C[i-1])
		xn1s.append(xn1)
		y = solution(x0,ys[j],C[i-1])
		ys.append(y)
	plt.plot(list(range(T+1)), xn1s, 'k')
	plt.plot(list(range(T+1)), ys, ',r')
	plt.title(f"C = {C[i-1]}")

plt.show()