## Importa LeTxts, AutoCorr
from funcs import *
import matplotlib.pyplot as plt
import numpy as np

TodasTensoes = LeTxts('Txts')
#TodasTensoes = TodasTensoes[0:1]
fatorTransiente = 0.8

for k in range(len(TodasTensoes)):
	Tensao = TodasTensoes[k]
	X = Tensao[:-1]
	X = X[int(fatorTransiente*len(X)):]
	X = np.array(X)
	Txt = Tensao[-1]
	
	##### Para plotar a autocorrelação #################
	
	## Título com o nome do arquivo
	plt.suptitle(f"Correlações")
	
	plt.subplot(2,3,k+1)
	PlotaAutoCorrs(X)
	plt.title(f"Arquivo {Txt}")

	plt.savefig("plotcorrs46.png")
plt.show()