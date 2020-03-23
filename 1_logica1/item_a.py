def VerificaMinas(listaCPF):
    '''
    Dada lista de CPFs, retorna lista somente com CPFs cujo 9º número seja igual a 6.'''
    for CPF in listaCPF:
        ##só pra garantir que é string
        CPFstr=str(CPF)
        if CPFstr[8]!='6':
            listaCPF.remove(CPF)
    return listaCPF