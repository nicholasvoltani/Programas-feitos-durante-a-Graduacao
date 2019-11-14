

            ###############################################
            ## MAC 0115 - Introdução à Computação         #
            ## IF-USP - Segundo Semestre de 2017          #
            ## Turma 2017221 - Marco Dimas Gubitoso       #
            ##                                            #
            ## Nicholas Funari Voltani                    # 
            ## N° USP: 9359365                            #
            ###############################################
 






################################# Funções #####################################
def PrintMat(matriz):
    '''Imprime a matriz linha por linha, elemento a elemento.'''
    
    for i in range(len(matriz)):
        print('\n',end='')
        
        for j in range(len(matriz[i])):
            print('\t',end='')   
            print(matriz[i][j],end='  ')  
    
    print('\n')


def Roda(matriz):
    '''Gira a matriz em 90° na direção horária.
    
    Procedimento: 
        A primeira coluna (de baixo para cima) se torna a primeira linha,
        a segunda coluna (idem), a segunda linha, etc.'''
    
    m=[]
    for i in range(len(matriz)):
        m.append([])
        
        for j in range(len(matriz[i])-1, -1, -1): #Contando de baixo para cima
            m[i].append(matriz[j][i])  # Colunas se tornando linhas
    
    return m


def Transp1(matriz):
    '''Função que retorna a transposta da 
    matriz original pela diagonal principal.
    
    Procedimento: 
        Os elementos da linha i, da esquerda para a direita,
        se tornarão os elementos da coluna j, de cima para baixo.'''
    
    uma_matriz_que_vai_desaparecer=[]
    
    for i in range(len(matriz)):
        uma_matriz_que_vai_desaparecer.append([])
        
        for j in range(len(matriz[0])):
            uma_matriz_que_vai_desaparecer[i].append(matriz[j][i])
    
    return uma_matriz_que_vai_desaparecer


def Transp2(matriz):
    '''Função que retorna a transposta da 
    matriz original pela diagonal secundária
    
    Procedimento: 
        Os elementos da linha i, da esquerda para a direita,
        se tornarão os elementos da coluna j, de baixo para cima.'''
    
    uma_outra_matriz_que_sumira=[]
    
    for i in range(len(matriz)):
        uma_outra_matriz_que_sumira.append([])
        
        for j in range( len(matriz[i])-1 , -1 , -1 ):
            uma_outra_matriz_que_sumira[i].append(matriz[j][len(matriz)-1-i])
            # Percorre uma coluna, de baixo (último elemento) 
            # para cima (primeiro elemento)
            
    return uma_outra_matriz_que_sumira


def InvH(matriz):
    '''Troca as linhas da matriz entre si: 
    a primeira linha se torna a última, 
    a segunda linha se torna a penúltima, etc.
    
    Procedimento: 
        Cria uma nova matriz, a partir da matriz original,
        das linhas de baixo para cima
        i.e. a primeira linha da nova matriz é a última linha da matriz original, 
        a segunda nova linha é a penúltima linha original, etc'''
    
    mais_uma_matriz_evanescente=[]
    
    for i in range(len(matriz)):
        mais_uma_matriz_evanescente.append(matriz[len(matriz)-1 - i])
        # Tomando as linhas de baixo (elemento [len(M)-1] )
        # para cima (elemento [0] )
    return mais_uma_matriz_evanescente


def InvV(matriz):
    '''Troca as colunas da matriz entre si:
        a primeira coluna se torna a última,
        a segunda coluna se torna a penúltima, etc.
        
        Procedimento: 
            Transpõe a matriz original, inverte suas linhas, 
            e a transpõe novamente; 
            o resultado final terá as colunas trocadas entre si.'''
        
    transposta = Transp1(matriz)
        
    invertida_H = InvH(transposta)
        
    invertida_novamente = Transp1(invertida_H)
        
    return invertida_novamente


## ************************* Funções Bônus ******************************** ##


def TrocaLinhas(matriz):
    '''Troca a primeira e a segunda linhas entre si,
    e a terceira e a quarta linhas entre si.
    
    Somente funciona corretamente para matrizes com quatro (4) linhas.'''
    matriz_muda = []
    
    for i in range(2):
        matriz_muda.append(matriz[1-i])
        # Adiciona linha [1] (segunda) e [0] (primeira)
    
    for j in range(2):
        matriz_muda.append(matriz[3-j])
        # Adiciona linha [3] (quarta) e [2] (terceira)
        
    return matriz_muda


def TrocaColunas(matriz):
    '''Troca a primeira e a segunda colunas entre si,
    e a terceira e a quarta colunas entre si.
    
    Somente funciona corretamente para matrizes com quatro (4) colunas.
    
    Procedimento: 
        Transpõe a matriz original,
        troca suas linhas novas (ou seja, suas antigas colunas),
        e a transpõe novamente;
        a matriz resultante terá suas colunas originais trocadas.'''
    
    matriz_horizontalizada = Transp1(matriz)
    
    matriz_linhas_trocadas = TrocaLinhas(matriz_horizontalizada)
    
    matriz_final = Transp1(matriz_linhas_trocadas)
    
    return matriz_final


def TrocaInicio(matriz):
    ''' Troca primeira e segunda linhas entre si,
    e então troca primeira e segunda colunas.
    
    Funcionamento: 
        A primeira linha é retirada (função pop) e reinserida (função insert) na posição 1.
        A matriz é, então, transposta.
        A primeira coluna (agora, primeira linha) é retirada e reinserida na posição 1.
        A matriz é, então, re-transposta. 
        
    Somente funciona corretamente para funções 4x4.
    '''
    linha_0 = matriz.pop(0)
    matriz.insert(1,linha_0)
    
    transposta = Transp1(matriz)
    
    coluna_0 = transposta.pop(0)
    transposta.insert(1,coluna_0)
    
    matriz_final_da_troca_inicio = Transp1(transposta)
    
    return matriz_final_da_troca_inicio



def TrocaFim(matriz):
    '''Troca terceira e quarta linhas entre si,
    e então troca terceira e quarta colunas entre si.
    
    Funcionamento: 
        Invertemos as linhas com a função InvH, 
        invertemos as colunas com a função InvV,
        e seguimos os procedimentos da função TrocaInicio.
        Reinvertemos a matriz resultante para o fim desejado.
    
    Somente funciona para matrizes 4x4.'''
    
    matriz_invertida_horizontal = InvH(matriz)
    
    matriz_invertida_vertical = InvV(matriz_invertida_horizontal)
    
    matriz_trocada_vertical = TrocaInicio(matriz_invertida_vertical)
      
    matriz_final = InvV(InvH(matriz_trocada_vertical))
    
    return matriz_final











######################### Comandos Iniciais ###################################


n=int(input("Entre com a soma invariante da matriz, entre 1 e 100: "))

while n<1 or n>100:
    n=int(input("Entre com a soma invariante da matriz, entre 1 e 100: "))

m=n-21

quadrado_perfeito=[ 
                    [11, 8, m,  2],
                    [m+1,1, 12, 7],
                    [4, m+2, 6, 9],
                    [5, 10, 3, m+3]
                    ]


####################### Loop de comandos do usuário ##########################

PrintMat(quadrado_perfeito)
print("""Escolha a operação desejada:
    0 - Sair
    1 - Girar para direita
    2 - Transpor pela diagonal principal
    3 - Transpor pela diagonal secundária
    4 - Refletir horizontalmente
    5 - Refletir verticalmente
    6 - Trocar linhas 1-2 e 3-4
    7 - Trocar colunas 1-2 e 3-4
    8 - Trocar linhas 1-2 e colunas 1-2
    9 - Trocar linhas 3-4 e colunas 3-4""")


# Criando cópia da matriz que será utilizada no loop
matriz_dentro_do_loop = quadrado_perfeito[:]


# Primeiro comando do usuário
input_do_usuario = int(input('>>> '))


while input_do_usuario != 0:
    ## Para cada input, a matriz do loop é substituida pela
    ## função do input aplicada a si mesma
    
    if input_do_usuario == 1:
        
        matriz_dentro_do_loop = Roda(matriz_dentro_do_loop)
        PrintMat(matriz_dentro_do_loop)
        print("""Escolha a operação desejada:
    0 - Sair
    1 - Girar para direita
    2 - Transpor pela diagonal principal
    3 - Transpor pela diagonal secundária
    4 - Refletir horizontalmente
    5 - Refletir verticalmente
    6 - Trocar linhas 1-2 e 3-4
    7 - Trocar colunas 1-2 e 3-4
    8 - Trocar linhas 1-2 e colunas 1-2
    9 - Trocar linhas 3-4 e colunas 3-4""")
        input_do_usuario=int(input(">>> "))
     
    
    if input_do_usuario == 2:
        
        matriz_dentro_do_loop = Transp1(matriz_dentro_do_loop)
        PrintMat(matriz_dentro_do_loop)
        print("""Escolha a operação desejada:
    0 - Sair
    1 - Girar para direita
    2 - Transpor pela diagonal principal
    3 - Transpor pela diagonal secundária
    4 - Refletir horizontalmente
    5 - Refletir verticalmente
    6 - Trocar linhas 1-2 e 3-4
    7 - Trocar colunas 1-2 e 3-4
    8 - Trocar linhas 1-2 e colunas 1-2
    9 - Trocar linhas 3-4 e colunas 3-4""")
        input_do_usuario=int(input(">>> "))
    
    
    if input_do_usuario == 3:
        
        matriz_dentro_do_loop = Transp2(matriz_dentro_do_loop)
        PrintMat(matriz_dentro_do_loop)
        print("""Escolha a operação desejada:
    0 - Sair
    1 - Girar para direita
    2 - Transpor pela diagonal principal
    3 - Transpor pela diagonal secundária
    4 - Refletir horizontalmente
    5 - Refletir verticalmente
    6 - Trocar linhas 1-2 e 3-4
    7 - Trocar colunas 1-2 e 3-4
    8 - Trocar linhas 1-2 e colunas 1-2
    9 - Trocar linhas 3-4 e colunas 3-4""")
        input_do_usuario=int(input(">>> "))
    
    
    if input_do_usuario == 4:
        
        matriz_dentro_do_loop = InvH(matriz_dentro_do_loop)
        PrintMat(matriz_dentro_do_loop)
        print("""Escolha a operação desejada:
    0 - Sair
    1 - Girar para direita
    2 - Transpor pela diagonal principal
    3 - Transpor pela diagonal secundária
    4 - Refletir horizontalmente
    5 - Refletir verticalmente
    6 - Trocar linhas 1-2 e 3-4
    7 - Trocar colunas 1-2 e 3-4
    8 - Trocar linhas 1-2 e colunas 1-2
    9 - Trocar linhas 3-4 e colunas 3-4""")
        input_do_usuario = int(input(">>> "))
    
    
    if input_do_usuario == 5:
        
        matriz_dentro_do_loop = InvV(matriz_dentro_do_loop)
        PrintMat(matriz_dentro_do_loop)
        print("""Escolha a operação desejada:
    0 - Sair
    1 - Girar para direita
    2 - Transpor pela diagonal principal
    3 - Transpor pela diagonal secundária
    4 - Refletir horizontalmente
    5 - Refletir verticalmente
    6 - Trocar linhas 1-2 e 3-4
    7 - Trocar colunas 1-2 e 3-4
    8 - Trocar linhas 1-2 e colunas 1-2
    9 - Trocar linhas 3-4 e colunas 3-4""")
        input_do_usuario = int(input(">>> "))
        
    
    if input_do_usuario == 6:
        
        matriz_dentro_do_loop = TrocaLinhas(matriz_dentro_do_loop)
        PrintMat(matriz_dentro_do_loop)
        print("""Escolha a operação desejada:
    0 - Sair
    1 - Girar para direita
    2 - Transpor pela diagonal principal
    3 - Transpor pela diagonal secundária
    4 - Refletir horizontalmente
    5 - Refletir verticalmente
    6 - Trocar linhas 1-2 e 3-4
    7 - Trocar colunas 1-2 e 3-4
    8 - Trocar linhas 1-2 e colunas 1-2
    9 - Trocar linhas 3-4 e colunas 3-4""")
        input_do_usuario = int(input(">>> "))
    
    
    if input_do_usuario == 7:
        
        matriz_dentro_do_loop = TrocaColunas(matriz_dentro_do_loop)
        PrintMat(matriz_dentro_do_loop)
        print("""Escolha a operação desejada:
    0 - Sair
    1 - Girar para direita
    2 - Transpor pela diagonal principal
    3 - Transpor pela diagonal secundária
    4 - Refletir horizontalmente
    5 - Refletir verticalmente
    6 - Trocar linhas 1-2 e 3-4
    7 - Trocar colunas 1-2 e 3-4
    8 - Trocar linhas 1-2 e colunas 1-2
    9 - Trocar linhas 3-4 e colunas 3-4""")
        input_do_usuario = int(input(">>> "))
        

    if input_do_usuario == 8:
        
        matriz_dentro_do_loop = TrocaInicio(matriz_dentro_do_loop)
        PrintMat(matriz_dentro_do_loop)
        print("""Escolha a operação desejada:
    0 - Sair
    1 - Girar para direita
    2 - Transpor pela diagonal principal
    3 - Transpor pela diagonal secundária
    4 - Refletir horizontalmente
    5 - Refletir verticalmente
    6 - Trocar linhas 1-2 e 3-4
    7 - Trocar colunas 1-2 e 3-4
    8 - Trocar linhas 1-2 e colunas 1-2
    9 - Trocar linhas 3-4 e colunas 3-4""")
        input_do_usuario = int(input(">>> "))

        
    if input_do_usuario == 9:
        
        matriz_dentro_do_loop = TrocaFim(matriz_dentro_do_loop)
        PrintMat(matriz_dentro_do_loop)
        print("""Escolha a operação desejada:
    0 - Sair
    1 - Girar para direita
    2 - Transpor pela diagonal principal
    3 - Transpor pela diagonal secundária
    4 - Refletir horizontalmente
    5 - Refletir verticalmente
    6 - Trocar linhas 1-2 e 3-4
    7 - Trocar colunas 1-2 e 3-4
    8 - Trocar linhas 1-2 e colunas 1-2
    9 - Trocar linhas 3-4 e colunas 3-4""")
        input_do_usuario = int(input(">>> "))


############################## Só um Easter Egg ##############################

from random import randint
Goodbye_Moonman = randint(0,3)

if Goodbye_Moonman == 0:
    print(">>> Tchau!")
if Goodbye_Moonman == 1:
    print(">>> ¡Hasta la vista!")
if Goodbye_Moonman == 2:
    print(">>> Ciao!")
if Goodbye_Moonman == 3:
    print(">>> Goodbye!")