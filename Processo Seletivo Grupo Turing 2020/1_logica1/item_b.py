def PrimeiroDigito(CPF):
    '''Dado um CPF (verdadeiro ou falso), retorna o que seria seu primeiro dígito verificador, com a regra 
    prim = \sum_{i=1}^10 ((11-i)*CPF[i])
    onde CPF[i] é o i-ésimo número do CPF.'''
    ## Converter pra string primeiro
    CPFstr=str(CPF)
    prim=0
    
    ##Soma sobre os primeiros 9 digitos
    for i in range(0,9):
        prim+=(10-i)*int(CPFstr[i])
    prim = prim%11
    
    if prim==0 or prim==1:
        return 0
    else:
        return (11-prim)

def SegundoDigito(CPF):
    '''Dado um CPF (verdadeiro ou falso), retorna o que seria seu segundo dígito verificador, com a regra 
    prim = \sum_{i=1}^11 ((12-i)*CPF[i])
    onde CPF[i] é o i-ésimo número do CPF.'''
    CPFstr=str(CPF)
    seg=0
    
    ##Soma sobre os primeiros 9 digitos
    for i in range(0,9):
        seg+=(11-i)*int(CPFstr[i])
    ##Soma ponderada com o primeiro digito verificador "de facto" do CPF dado
    seg += PrimeiroDigito(CPF)*2
    seg = seg%11
     
    if seg==0 or seg==1:
        return 0
    else:
        return (11-seg)
    
def VerificaCPF(CPF):
    '''Dado CPF, verifica se ele é verdadeiro ou falso, via seus dígitos verificadores.'''
    CPFstr=str(CPF)
    prim = PrimeiroDigito(CPF)
    seg = SegundoDigito(CPF)
    if (CPFstr[-2]+ CPFstr[-1]) == str(prim)+str(seg):
        return True
    else:
        return False
