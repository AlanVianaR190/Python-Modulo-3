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
    resposta= valor*2
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
