## Importa LeTxts, AutoCorr
from funcs import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

TodasTensoes = LeTxts('Txts')
#TodasTensoes = TodasTensoes[2:3]
fatorTransiente = 0.8

for Tensao in TodasTensoes:
	TensaoFloat = np.array(Tensao[:-1])
	nome = Tensao[-1]
	## Remover transiente
	TensaoFloat = TensaoFloat[int(fatorTransiente*len(TensaoFloat)):]
	TensaoFloat1 = TensaoFloat[1:]
	plt.plot(TensaoFloat[:-1], TensaoFloat1,',k')
	plt.xlabel(r"VC1_i")
	plt.ylabel(r"VC1_{i+1}")
	plt.title(f"Primeiro retorno para {nome}")
	plt.show()