#
def aumentar(valor, porcent=0, formata=False):
    resposta= valor + (valor * porcent/100)
    if formata == True:
        return moeda(resposta)
    else:
        return resposta
#
def diminuir(valor, porcent=0, formata=False):
    resposta= valor - (valor * porcent/100)
    if formata == True:
        return moeda(resposta)
    else:
        return resposta

#
def dobro(valor, formata=False):
    resposta = valor * 2
    if formata == True:
        return moeda(resposta)
    else:
        return resposta

#
def metade(valor, formata=False):
    resposta= valor/2
    if formata == True:
        return moeda(resposta)
    else:
        return resposta

#
def moeda(valor, monetario="R$"):
    return f"{monetario}{valor:.2f}".replace(".",",")

def resumo(valor, taxaA=0, taxaD=0 ):
    print("---"*20)
    print("RESUMO DO VALOR".center(60))
    print("---"*20)
    print(f"\t\t\tPreço Analisado: \t\t\t{moeda(valor)}")
    print(f"\t\t\tMetade do Valor: \t\t\t{metade(valor, True)}")
    print(f"\t\t\tDobro do Valor: \t\t\t{dobro(valor, True)}")
    print(f"\t\t\tAumento de {taxaA}%: \t\t\t{aumentar(valor, taxaA, True)}")
    print(f"\t\t\tDesconto de {taxaD}%: \t\t\t{diminuir(valor,taxaD, True)}")
    print("---"*20)

