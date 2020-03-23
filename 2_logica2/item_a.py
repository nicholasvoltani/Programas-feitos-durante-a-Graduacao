def reset_array(lista,k):
    '''Dada uma lista, faz com que o k-ésimo elemento (0 <= k < len(lista)) se torne o primeiro elemento da lista (lista[0]),
    de forma que os elementos depois dele "andem" junto desse element, e os antes dele fiquem ao final da lista, na mesma ordem original.
    '''
    ##Tamanho da lista
    n=len(lista)
    ##Copia da lista, que será igual à lista original "shiftada"
    copia=lista.copy()
    for i in range(0,n):
        copia[i] = lista[k-i]
    return copia