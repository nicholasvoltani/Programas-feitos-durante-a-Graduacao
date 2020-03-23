from random import randint
from item_b import PrimeiroDigito, SegundoDigito
def CPFAleatorio():
    CPF9 = randint(10**8, 10**9-1)
    ##Posso usar PrimeiroDigito e SegundoDigito em CPF10
    ##pois ele não assume o tamanho da variavel "CPF" dada
    prim = PrimeiroDigito(CPF9)
    seg = SegundoDigito(CPF9)
    CPF = str(CPF9) + str(prim) + str(seg)
    return CPF