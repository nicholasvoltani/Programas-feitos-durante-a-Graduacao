import numpy as np
import matplotlib.pyplot as plt
from solvers import RK4

## Pos : [0:x, 1:y, 2:z]
## Params : [0:A1, 1:A2, 2:A3, 3:A4, 4:m0, 5:m1]

def fx(t,pos,params):
	dx = params[0]*(pos[1] - pos[0])
	## +Termo não-linear g(x)
	dx += (params[0]*(-params[5]*pos[0] + params[5] - params[4])/2)*(abs(pos[0]+1) - abs(pos[0]-1))
	return dx

def fy(t,pos,params):
	dy = params[1]*(pos[0] - pos[1] + pos[2])
	return dy

def fz(t,pos,params):
	dz = -params[2]*pos[1] + params[3]*pos[2]
	return dz

funcs = [fx,fy,fz]

## Condições iniciais

## Condições de iteração:
T = 300
dt = 0.01
fator_transiente = 0.8
	
## Parametros a serem variados
cs = [50, 35, 33.8, 33]
ds = [0.1,0.2,0.4,1]

fig = plt.figure()

for i in range(len(ds)):
	## Pontos iniciais
	x = [0.1]
	y = [0.1]
	z = [0.1]
	params = [15.6, 1, cs[i], 0, -8/7, -5/7]

	for t in range(int(T/dt)):
		pos = np.array([x[t],y[t],z[t]])
		pos = RK4(t,dt,pos,params,funcs)

		x.append(pos[0])
		y.append(pos[1])
		z.append(pos[2])

	x = x[int(fator_transiente*len(x)):]
	y = y[int(fator_transiente*len(y)):]
	z = z[int(fator_transiente*len(z)):]

	ax = fig.add_subplot(1 + i//4, 4, i+1, projection='3d')
	ax.plot3D(x,y,z,',k')
	plt.grid(b=True, color="DarkTurquoise",alpha=0.2)
	plt.title(f"A_3 = {cs[i]}")
	plt.savefig("A4s.png")
#plt.show()