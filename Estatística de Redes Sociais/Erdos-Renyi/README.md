# Grafos de Erdős-Rényi

Dada uma população de *N* agentes e uma probabilidade *0 < p < 1*, então para todos os pares distintos *(i,j)*  adicionamos uma aresta entre estes agentes com probabilidade *p*. Seguem abaixo exemplos de grafos de Erdős-Rényi. 

<p align = "center">
	<img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Erdős–Rényi_model_random_graphs.pdf/page1-800px-Erdős–Rényi_model_random_graphs.pdf.jpg">
</p>


## Caso Especial: Matrizes de Adjacência Encaixadas

Tenha-se uma sequência de grafos de Erdős-Rényi <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;\{G(N,p)_{N=2}\}^{\infty}" title="G(N,p)_{N=2}^{\infty}" />, definidos de tal forma que:
<p align = "center"> 
	<img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;M_{N&plus;1}&space;(v,&space;v')&space;=&space;M_{N}(v,v')&space;\,\,&space;\forall&space;v,v'&space;\in&space;\{1,&space;\dots,&space;N\}" title="M_{N+1} (v, v') = M_{N}(v,v') \,\, \forall v,v' \in \{1, \dots, N\}" />
</p>
Ou seja, as matrizes estão encaixadas como na figura abaixo, para cada *N*:
<p align = "center">
	<img src = "nestedmatrices.svg">
</p>

Desejamos avaliar como a máxima verossimilhança evolui conforme

<p align = "center">
	<img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;\lim\limits_{N&space;\to&space;\infty}&space;\hat{p}_{p,N}" title="\lim\limits_{N \to \infty} \hat{p}_{p,N}" />
</p>

<p align = "center">
	<img src = "maxlikelihood.png">
</p>

<p align = "center">
	<img src = "maxlikelihood2.png">
</p>
