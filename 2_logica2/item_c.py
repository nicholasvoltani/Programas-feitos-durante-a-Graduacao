def solve_var_josephus(lista_alvos):
    '''Dado uma lista de tamanho n, cada i-ésima pessoa busca matar a ((posicao(i)+lista_alvos[i])%n)-ésima pessoa do grupo.
    Ou seja, num grupo circular, ela busca matar a pessoa "lista_alvos[i] mais adiante" à sua "direita" (que não seja ela mesma).
    Por exemplo, num grupo de 3 pessoas, se a 1ª (0-ésima) pessoa tem lista[0]=2, então ela busca matar a 3ª pessoa (2-ésima) do grupo.
    '''
    ##Grupo das pessoas
    grupo = [i for i in range(len(lista_alvos))]
        
    ##There can be only one
    while len(grupo)!=1:
    ##A iteração pelo grupo se dá através de copia_grupo
    ##pois o tamanho do grupo está mudando junto das iterações
        copia_grupo = grupo.copy()
        for pessoa in copia_grupo:
        ##Iteramos sobre todas as pessoas vivas do grupo (no começo da iteração), via copia_grupo
            if pessoa in grupo:
            ##Só veremos os alvos das pessoas que ainda estão vivas durante a iteração
                if (grupo.index(pessoa)+lista_alvos[pessoa])%len(grupo) == 0:
                    grupo.remove(copia_grupo[(grupo.index(pessoa)+1)%len(grupo)])
                else:
                    grupo.remove(copia_grupo[(grupo.index(pessoa)+lista_alvos[pessoa])%len(grupo)])
    ##i-ésima posição mata (posicao(i)+n_i)%(len(grupo))-ésima pessoa, 
    ##que não seja ela mesma 
    ## (%len(grupo) traz a ideia matemática do grupo ser circular)
    ##P. ex.: digamos que, de 10, restam [7,9], com lista_alvos [2,7] respectivamente
    ##então 7 (posição 0) teria de se matar, pois (0+2)%2 = 0, mas não queremos isso;
    ##no caso, ela só "se pula" e mata a próxima pessoa, 9 (posição (0+1)%2 = 1)
    ##e então a função retornaria ->7
    return grupo[0]

## P.S.: Para o exemplo dado no Case Intermediário:
## tem-se que solve_var_josephus(circulo) = 2 (Terceira pessoa), que é diferente da resposta dada,
## pois na imagem disponível, não se toma em conta que [3] mata [0], e por fim [2] mata [3]
## ([i] indicando índice i correspondente, 
##não os números dentro das bolinhas da imagem, que são lista_alvos[i])