# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 13:10:04 2017

@author: Cliente
"""
def main():
    '''
            Mastermind
Um jogo para todas as idades etc.
Descubra a senha em até 10 tentativas
    
Regras:
Pinos Pretos: Pinos em comum em posições iguais
Pinos Brancos: Pinos em comum em posições diferentes
    '''
     
    ## Número de Dígitos ##
    k = int(input('Digite o numero de digitos: '))
    
    
                         ## Funções do programa ##
       
    def GeraSenha():
        import random
        senhasecreta = random.randint(10**(k-1),10**k-1)
        return senhasecreta
    
    ## A senha já é assinada à variável senhasecreta
    ## Como o número aleatório de GeraSenha()
    senhasecreta=GeraSenha()
    
    def ContaPreto(m,n):
        '''
        ContaPreto(m,n)
    
        Conta quantos pinos estão no local correto
        em relação à senha
        '''
        BlackPins=0
        for i in range(k):
            if m%10 == n%10:
                BlackPins+=1
            m//=10
            n//=10
        return(BlackPins)
    
    def ContaDigito(d,n):
        '''
        Conta quantos dígitos d há em
        um dado número n
        '''
        cont=0
        ## Analisar termos em comum com cada 0<= i <= 9 
        ## De cada casa decimal de n (por função % & // )
        for i in range(k):
            if d==n%10:
                cont+=1
            n//=10
        return(cont)
    
    def ContaRepeticao(m,n):
        '''
        Conta quantos números há em comum
        entre dados m e n
        '''
        cont=0
        ## Analisar quantos termos em comum entre m e n
        ## De dígito a dígito, 0 <= i <= 9
        for i in range(0,10):
            if ContaDigito(i,m)>=1 and ContaDigito(i,n)>=1:
                cont+=min(ContaDigito(i,m),ContaDigito(i,n))
        return(cont)
    
    def ContaBranco(m,n):
        '''
        Conta quantos dígitos em comum
        dados m e n possuem, mas em locais diferentes'''
        ## O número total de pinos repetidos
        ## é igual aos pinos repetidos nos mesmos locais
        ## mais os pinos repetidos em locais diferentes
        c=ContaPreto(m,n)
        d=ContaRepeticao(m,n)
        WhitePins=abs(c-d)
        return(WhitePins)

##**************************************************************************************##

##Início do Programa
    n=1
    YourTry=int(input("Turno {}: Digite a sua tentativa: ".format(n)))
    
    ## Tentativas / Senha não-adivinhada
    while YourTry!=senhasecreta and n!=10:
        ## Resultado da tentativa anterior
        print("{} pretos e {} brancos".format(ContaPreto(YourTry,senhasecreta),ContaBranco(YourTry,senhasecreta)))
        n+=1
        ## Caso de n=10
        if n==10:
            YourTry=int(input("Último turno! Digite sua tentativa: "))
            continue  # Ignorar resto do loop #
        
        ## Casos 2 <= n <= 9
        YourTry=int(input("Turno {}: Digite a sua tentativa: ".format(n)))
    
## Final do Programa
    
    ## Beginner's luck
    if YourTry==senhasecreta and n==1:
        print("Parabéns! Você adivinhou na primeira tentativa!")    
    
    ## Acerto comum, 2 <= n <= 9
    if YourTry==senhasecreta and n>1 and n<10:
        print("Parabéns! Você adivinhou em %d turnos"%(n))
    
    ## wow such luck much skill very turing
    ## Acertando no último turno
    if YourTry==senhasecreta and n==10:        
            print('''\tWe_Are_The_Champions.mp3
    Você acertou na última tentativa! Parabéns!''')
    
    ## Outta time
    if YourTry!=senhasecreta and n==10:
        print("\nO tempo acabou (metaforicamente)! A senha era %d"%(senhasecreta))
 