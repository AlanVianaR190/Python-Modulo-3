def voto(ano):
    '''
    Verifica se uma pessoa pode ou não votar
    :param ano: digita o ano de nascimento
    :return: se e ou não obrigatorio votar
    '''
    from datetime import date

    #pondo em uma variavel a função data do sitema
    atual = date.today().year
    result = atual-ano

    #
    if result < 16:
        return f"Com {result} anos, VOTO NEGADO"
    elif result >= 16 and result < 18 or result >= 70:
        return f"Com {result} anos, VOTO OPCIONAL"
    elif result >= 18 and result < 70:
        return f"Com {result} anos, VOTO OBRIGATORIO"


#
ano=int(input("Digite o ano de nascimento: "))
print(voto(ano))
