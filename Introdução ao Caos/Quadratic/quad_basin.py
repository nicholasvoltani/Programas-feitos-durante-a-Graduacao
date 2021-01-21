import numpy as np
import matplotlib.pyplot as plt

def quadratic(x,C):
    return C - x**2

Cs = [i*0.75/4 for i in range(4)]

for i in range(4):
	C = Cs[i]
	## Pontos fixos
	x_mais = 0.5*(-1+np.sqrt(1+4*C))
	x_menos = 0.5*(-1-np.sqrt(1+4*C))

	## Queremos ver se a bacia de atração
	## tem raio igual a |x_menos|
	x0s = np.linspace(x_mais-abs(x_mais-x_menos)- 1, x_mais+abs(x_mais-x_menos)+ 1, 5000)
	ys = []
	color = []
	Tit = 1000

	for x0 in x0s:
	    x = x0
	    for _ in range(Tit):
	        x = quadratic(x,C)
	    
	    ## Se o ponto da órbita estiver próximo do ponto estável (i.e. dentro da bacia), plotar em azul   
	    if np.isclose(x, x_mais, atol = 5e-05):
	        color.append('b')
	    else:
	    ## Caso contrário, plota em vermelho	
	        color.append('r')
	    ys.append(0)

	plt.subplot(2,2,i+1)
	plt.scatter(x0s,ys,color=color)
	## Visualizar a fronteira da bacia, dada pelo valor absoluto de x_menos
	plt.scatter([x_menos, -x_menos],[0,0],color='y')
	plt.title(r"Bacia de atração, $x_{n+1} = C - x_n^2$; " + f"C = {C}")
	plt.legend(["Fora da bacia de atração",r"$x^*_- = \left|\frac{-1-\sqrt{1+4C}}{2}\right|$"])
plt.show()
