#função
def notas(*n, stat=False):
    '''
    Esta função exibe um dicionario com o TOTAL, MAIOR, MENOR & MEDIA
    :param n: colocar as notas
    :param stat: se false não exibe, se true exibe a situação de acordo com as notas e media
    :return: um dicionario com estas informações
    '''

    #
    dicionario = dict()
    dicionario["Total"] = len(n)
    dicionario["Maior"] = max(n)
    dicionario["Menor"] = min(n)
    #função <sum> soma todos os numeros
    dicionario["Media"] = round(sum(n) / len(n), 1)

    #
    if stat==True:
        if dicionario["Media"] < 4:
            dicionario["Situação"] = "Ruim"
        elif dicionario["Media"] >= 4 and dicionario["Media"] < 6:
            dicionario["Situação"] = "Regular"
        elif dicionario["Media"] >= 6 and dicionario["Media"] < 8:
            dicionario["Situação"] = "Bom"
        else:
            dicionario["Situação"] = "Otimo"

    #
    return dicionario


#program
resp = notas(5, 6, 9, stat=True)
print(resp)

help(notas)

