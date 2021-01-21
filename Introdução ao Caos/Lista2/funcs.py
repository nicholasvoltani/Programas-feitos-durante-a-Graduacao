def LeTxts(dir):
	'''
	Lê todos os arquivos no diretório "dir",
	e cria listas de valores (float) pra cada arquivo.
	Retorna uma lista de VC1's pra cada arquivo.
	'''

	import os

	## Pegar diretório com os txt's
	cwd = os.getcwd()
	dir_txts = os.path.join(cwd, dir)
	arquivos = os.listdir(dir_txts)

	## Onde armazenaremos as listas de tensões VC1 pra diferentes parâmetros
	todas_tensoes = []
	for arquivo in arquivos:
		
		## Ler o arquivo
		path_txt = os.path.join(dir_txts, arquivo)
		linhas = open(path_txt, 'r')
		
		## Desconsideramos as primeiras 4 linhas
		for _ in range(4):
			linhas.readline()

		## Lê o resto do txt 
		valores_VC1 = linhas.read()

		## Cria a lista dos VC1's (strings)
		valores_VC1 = valores_VC1.split("\n")

		## Remove '' no final da leitura da lista
		valores_VC1.remove('')

		## Transforma lista de strings 
		## numa lista valores de ponto flutuante
		valores_VC1 = list(map(float, valores_VC1))

		## Adiciona lista de VC1's 
		todas_tensoes.append(valores_VC1)

		## Para saber depois, de qual parâmetro a lista "valores_VC1" veio
		todas_tensoes[-1].append(arquivo)

	return todas_tensoes

def AutoCorr(X,tau):
	'''
	Calcula a autocorrelação (normalizada) da variável $X$, com passo $tau$.
	Autocorr = sum(X[0:end-tau].*X[tau:end])/sum(X[0:end-tau].*X[0:end-tau])

	'''
	import numpy as np

	## Por definição, temos Autocorr(X,0) = 1
	if tau == 0:
		return 1

	##### Caso tau != 0 ############################

	## Vetores que vão se multiplicar
	## precisam ter mesmo tamanho [len(X) - tau]
	numerador1 = X[tau:]
	numerador2 = X[:-tau]

	## Multiplica ponto a ponto Num1.*Num2, e soma tudo
	numerador = np.multiply(numerador1,numerador2)	
	numerador = sum(numerador)

	## Calcula o denominador
	denominador = np.multiply(numerador2,numerador2)
	denominador = sum(denominador)
	
	return numerador/denominador


def PlotaAutoCorrs(X, ran = 100):
	import matplotlib.pyplot as plt

	autocorrs = []
	taus = list(range(ran))
	for tau in taus:
		autocorr = AutoCorr(X, tau)
		autocorrs.append(autocorr)
	
	plt.plot(taus, autocorrs,'r')
	plt.title(f"Autocorrelação")

def PlotaMaxMins(X, fatorTransiente):
	import numpy as np
	import matplotlib.pyplot as plt

	## Para plotar X em função das iterações
	X = X[int(fatorTransiente*len(X)):]
	EixoX = list(range(len(X[1:-1])))
	EixoX = np.array(EixoX)

	##### Para gerar a lista de máximos locais ########

	##         V_{i+1} <- é max local
	## 		  /       \
	## 		 /		   \		
	## 	  V_i	        \	
	##                 V_{i+2}

	Bool1 = (X[1:-1] - X[:-2]) >=  0
	Bool2 = (X[2:] - X[1:-1]) < 0

	## Fazendo o operador AND a cada elemento
	BoolMax = np.multiply(Bool1,Bool2)
	
	## Aplicando a "máscara" booleana no vetor VC1
	EixoXMax = EixoX[BoolMax]
	Maximos = X[1:-1][BoolMax]

	##### Para gerar a lista de mínimos locais ########

	##      V_i 
	## 		   \		   V_{i+2}
	## 		    \		  /
	## 	     	 \	     /
	##            V_{i+1} <- é min local

	Bool1 = (X[1:-1] - X[:-2]) <  0
	Bool2 = (X[2:] - X[1:-1]) >= 0

	## Fazendo o operador AND a cada elemento
	BoolMin = np.multiply(Bool1,Bool2)
	
	## Aplicando a "máscara" booleana no vetor VC1
	EixoXMin = EixoX[BoolMin]
	Minimos = X[1:-1][BoolMin]

	plt.plot(EixoX, X[1:-1], ',k')
	plt.plot(EixoXMax,Maximos,'.g')
	plt.plot(EixoXMin,Minimos, '.r')
	plt.ylabel("VC1")
	plt.title("Máximos (verde) e mínimos (vermelho) locais")

	## Para fazer os mapas de primeiro retorno
	return Maximos, Minimos

def PrimeiroRetornoMaximos(Maximos):
	import matplotlib.pyplot as plt

	Maximos1 = Maximos[1:]
	plt.plot(Maximos[:-1], Maximos1,'.k')
	plt.xlabel(r"max_i")
	plt.ylabel(r"max_{i+1}")
	plt.title("Mapa de primeiro retorno dos máximos locais")

