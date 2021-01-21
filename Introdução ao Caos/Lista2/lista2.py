## Importa LeTxts, AutoCorr
from funcs import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

TodasTensoes = LeTxts('Txts')
#TodasTensoes = TodasTensoes[2:3]
fatorTransiente = 0.8


for Tensao in TodasTensoes:
	TensaoFloat = Tensao[:-1]
	TensaoFloat = np.array(TensaoFloat)
	Txt = Tensao[-1]
	
	## Título com o nome do arquivo
	fig = plt.figure()
	plt.suptitle(f"Arquivo {Txt}")
	
	
	##### 1) Plotar a autocorrelação #######################
	plt.subplot(2,2,1)
	PlotaAutoCorrs(TensaoFloat)

	##### 2) Plotar os máximos & mínimos locais ##############
	plt.subplot(2,2,2)
	Maximos, Minimos = PlotaMaxMins(TensaoFloat,fatorTransiente)
	
	##### 3) Plotar mapa de primeiro retorno ##################
	plt.subplot(2,2,3)
	PrimeiroRetornoMaximos(Maximos)

	##### 4) Reconstrução do espaço de fases ################

	## Por inspeção dos gráficos de autocorrelação,
	## tau = 44, que dividimos por 2 
	tau_corr = int(44/2)
	Z = TensaoFloat[:-2*tau_corr]
	Y = TensaoFloat[tau_corr:-tau_corr]
	X = TensaoFloat[2*tau_corr:]

	ax = fig.add_subplot(224, projection='3d')
	ax.plot3D(X,Y,Z,',k')
	ax.set_xlabel("X")
	ax.set_ylabel("Y")
	ax.set_zlabel("Z")
	ax.set_title("Reconstrução do espaço de fases")

	## Mostrando o plot total
	plt.show()