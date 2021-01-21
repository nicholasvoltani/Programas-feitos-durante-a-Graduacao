                    ###############################################
                    ## MAC 0115 - Introdução à Computação        ##
                    ## IF-USP - Segundo Semestre de 2017         ##
                    ## Turma 2017221 - Marco Dimas Gubitoso      ##
                    ##                                           ##
                    ## Nicholas Funari Voltani                   ## 
                    ## N° USP: 9359365                           ##
                    ###############################################
 

###############################################################################
from pylab import *
from tkinter import *
import sys

mw=Tk()  ## Janela Principal

### Cada Frame possui duas entradas: 
## posição vertical inicial 
## e carga da i-ésima partícula ###

F1=Frame(mw)
F1.pack(side=TOP, fill='x',expand=True)

F2=Frame(mw)
F2.pack(side=TOP, fill='x',expand=True)

F3=Frame(mw)
F3.pack(side=TOP, fill='x',expand=True)

F4=Frame(mw)
F4.pack(side=TOP, fill='x',expand=True)

F5=Frame(mw)
F5.pack(side=TOP, fill='x',expand=True)

Ftime=Frame(mw)
Ftime.pack(side=TOP,fill='x',expand=True)

Fbottom=Frame(mw)
Fbottom.pack(side=TOP, fill='x',expand=True)

######## Variáveis a serem coletadas ###########
######## yi, qi , 1 <= i <= 5        ###########

y1=DoubleVar()
y1.set(20)
q1=DoubleVar()
q1.set(20)

Label(F1,text='Posição 1').pack(side=LEFT)
Entry(F1, bd=2, textvariable=y1).pack(side=LEFT)
Label(F1,text='Carga 1').pack(side=LEFT)
Entry(F1,bd=2,textvariable=q1).pack(side=LEFT)



y2=DoubleVar()
y2.set(2.5)
q2=DoubleVar()
q2.set(0)

Label(F2,text='Posição 2').pack(side=LEFT)
Entry(F2, bd=2, textvariable=y2).pack(side=LEFT)
Label(F2,text='Carga 2').pack(side=LEFT)
Entry(F2,bd=2,textvariable=q2).pack(side=LEFT)



y3=DoubleVar()
y3.set(0)
q3=DoubleVar()
q3.set(0)

Label(F3,text='Posição 3').pack(side=LEFT)
Entry(F3, bd=2, textvariable=y3).pack(side=LEFT)
Label(F3,text='Carga 3').pack(side=LEFT)
Entry(F3,bd=2,textvariable=q3).pack(side=LEFT)



y4=DoubleVar()
y4.set(-2.5)
q4=DoubleVar()
q4.set(0)

Label(F4,text='Posição 4').pack(side=LEFT)
Entry(F4, bd=2, textvariable=y4).pack(side=LEFT)
Label(F4,text='Carga 4').pack(side=LEFT)
Entry(F4,bd=2,textvariable=q4).pack(side=LEFT)


y5=DoubleVar()
y5.set(-20)
q5=DoubleVar()
q5.set(-20)

Label(F5,text='Posição 5').pack(side=LEFT)
Entry(F5, bd=2, textvariable=y5).pack(side=LEFT)
Label(F5,text='Carga 5').pack(side=LEFT)
Entry(F5,bd=2,textvariable=q5).pack(side=LEFT)


## Entradas de tempo 

## Tempo total de simulação
sim_time=DoubleVar()
sim_time.set(9.8)  
## Intervalos (steps) 
dt_entry=DoubleVar()  
dt_entry.set(0.05)

Label(Ftime, text='Tempo de Simulação').pack(side=LEFT)
Entry(Ftime,bd=3,textvariable=sim_time).pack(side=LEFT)
Label(Ftime,text='Intervalos de Interpolação').pack(side=LEFT)
Entry(Ftime,bd=3, textvariable=dt_entry).pack(side=LEFT)

############################# Programa Principal ##########################################

def plotar():
        
    ## Variáveis iniciais:
    
    ## y1, ... , y5
    ## q1, ... , q5
    ## delta_t (tempo total)
    ## dt (tempo dos intervalos) 
    ## Vetor posicoes possui somente zeros
    ## Vetor velocidades nulo
    ## Vetor Acelerações nulo ##
        
    ## Considerações feitas:
    ## - Massa das partículas = constante elétrica K = \frac{1}{4 \pi \epsilon_0}
    ## - Velocidade horizontal de todas as partículas é igual a 1
    
    delta_t = float(sim_time.get())
    dt = float(dt_entry.get())
    
    ####################### Posições iniciais ###########################################
    
    ## Como vx=1, x[i] = T[i]
    ## Posição horizontal <=> Tempo
    ## Vetor do tempo (discretizado)
    T = np.linspace(0,delta_t,int(delta_t/dt),endpoint=True)   
    
    ## Definindo Matriz de posições horizontais (para uma posterior matriz de distâncias)
    Tpos=np.zeros((5,int(delta_t/dt)))
    for i in range(5):
        for j in range(int(delta_t/dt)):
    ## Como todas as partículas possuem mesma posição horizontal entre si, a todos os instantes:
            Tpos[i,j] = T[j]
            
    ## Posição vertical                    
    # i-ésima linha: i-ésima partícula     
    # j-ésima coluna: j-ésimo intervalo de tempo
    ypos = np.zeros((5, int(delta_t/dt)))  
    ypos[0,0]=float(y1.get())               
    ypos[1,0]=float(y2.get())
    ypos[2,0]=float(y3.get())
    ypos[3,0]=float(y4.get())
    ypos[4,0]=float(y5.get())            
    
    ## "Vetor" das cargas
    q=zeros(5)                          
    q[0]=float(q1.get())
    q[1]=float(q2.get())
    q[2]=float(q3.get())
    q[3]=float(q4.get())
    q[4]=float(q5.get())

    ## Matriz de Velocidades Verticais 
    ## Inicialmente, velocidades iniciais são nulas
    Vy = np.zeros((5, int(delta_t/dt)))  
    
    ## Matriz de Acelerações Verticais, a determinar
    Ay = np.zeros((5,int(delta_t/dt))) 
   
    
    ##################### Cálculos para cada instância de tempo ##########################
    
    ## Sinais da direção da força elétrica entre partículas i,j
    def sign(i,j,time):
        ## Será utilizado para iteração em j
        ## então as considerações valem para a partícula i
        
        if q[i]*q[j]>0 and ypos[i,time] > ypos[j,time]:
            return 1
        elif q[i]*q[j]>0 and ypos[i,time] < ypos[j,time]:
            return -1
        
        elif q[i]*q[j]<0 and ypos[i,time] > ypos[j,time]:
            return 1 # Componente da força já será negativa, pois q[i]*q[j]<0
        elif q[i]*q[j]<0 and ypos[i,time] < ypos[j,time]:
            return -1 # Componente da força deve ser positiva
        else:
            return 1
        
   ########################  Iteração Principal  ########################
    for time in range(1,int(delta_t/dt)):
      ## Vetor posição (x,y) de cada partícula no momento anterior (time-1) (começa em t=0)
        R = np.array(list(zip(Tpos[:,time-1],ypos[:,time-1])))
        
        for i in range(5):
            ## Cálculo para todas as partículas
            for j_prime in range(5):
                    ## Somente computa distâncias entre partículas diferentes
                    if j_prime != i:
                        Ay[i,time-1] += sign(i,j_prime,time-1)*q[i]*q[j_prime]/dist(R[i],R[j_prime])**2
                        ## Cálculo da aceleração durante o intervalo passado
                        # Sidenote: função dist está inclusa em matplotlib.mlab 
            
            ## Cálculo das posições e velocidades do intervalo atual (começa em t = 0+1dt)
            ypos[i,time] = ypos[i,time-1] + Vy[i,time-1]*dt + 0.5*Ay[i,time-1]*(dt**2)
            Vy[i,time] = Vy[i,time-1] + Ay[i,time-1]*dt
     
    ## Plotando as trajetórias
    plot(Tpos[0,:],ypos[0,:])
    plot(Tpos[1,:],ypos[1,:])
    plot(Tpos[2,:],ypos[2,:])
    plot(Tpos[3,:],ypos[3,:])
    plot(Tpos[4,:],ypos[4,:])
    show()

## Botões 'Plot' e 'Sair'
Button(Fbottom,text='Plot',command=plotar).pack(side=LEFT,expand=TRUE,fill='x')
Button(Fbottom,text='Fim',command = lambda: sys.exit(0)).pack(side=LEFT,expand=TRUE,fill='x')

mainloop()
