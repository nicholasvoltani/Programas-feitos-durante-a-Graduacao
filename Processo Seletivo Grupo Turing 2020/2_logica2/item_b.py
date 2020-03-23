## Desculpe-me, Grupo Turing ateuehomossexualpaidacienciadacomputação
## mas não vou precisar do item 2a) :)

def solve_josephus(n):
    '''Dado um número n>0 de pessoas, prevê em qual posição Flavius Josephus sobreviveria,
    num grupo circular desesperado no qual cada pessoa mata quem está à sua direita.
    '''
    ##Cria grupo de tamanho n
    grupinho=[pessoinha for pessoinha in range(0,n)]
    
    ##Tamanho inicial do grupo (iteramos até que reste só um)
    L = len(grupinho)
    
    ##There can be only one
    while L!=1:
        ##Como estamos mudando a lista conforme analisamos seus indices
        ##precisamos de uma copia dela inteira para saber o que remover
        
        copia = grupinho.copy()
        for i in range(0,L):
        ##Os ímpares são mortos pelos pares antecedentes (contando com o 0 (ócios do ofício)) 
            if i%2==1:
               grupinho.remove(copia[i])
        
        ##Se o tamanho do grupo era ímpar (maior que 1) antes das mortes, 
        ##o último do grupo mata o primeiro
        if L%2==1 and L!=1:
            grupinho.remove(copia[0])
            
        ##Atualiza o tamanho do grupo para proxima iteração
        L = len(grupinho)
        
    ## Ao final, retorna o índice original do sobrevivente
    return grupinho[0]

## PS: Não sei se é só o Spyder,
## mas a função não roda dentro de um "for"...