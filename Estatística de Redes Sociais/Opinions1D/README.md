# Modelo de Votantes em 1D 

Suponha uma população de agentes {1, ..., N} disposta como nos gifs abaixo. 
* Cada agente é inicializado aleatoriamente com uma opinião (cor); 
* a cada iteração, algum agente é convocado a reconsiderar sua opinião; ele o faz, escolhendo aleatoriamente entre as opiniões de seus vizinhos, e mudando sua opinião para esta escolhida.

Pode-se ver abaixo que a tendência é de uma polarização/consenso das opiniões.

<p align = "center">
  <img src = "https://media4.giphy.com/media/QYkQ00pFTlWKq52qyh/giphy.gif">
  <img src = "https://media1.giphy.com/media/cNeAntF728Caa3t1EF/giphy.gif">
</p>
Inicialmente, eu pensei que, a cada iteração, TODOS os agentes eram convocados a reconsiderar suas respectivas opiniões, baseado em seus vizinhos. 

Esperaria-se que a tendência fosse ao consenso como acima, mas há uma alternativa: uma órbita de período 2, em que todos os agentes "flipam" suas opiniões a cada iteração. Mesmo não tendo tanta relevância como um modelo, é um fenômeno interessante.

<p align="center">
  <img src = "https://media2.giphy.com/media/cNeXir6JZALffvcvLD/giphy.gif">
</p>
