#função criada para calcular a area
def area(c, l):
    '''
    :param c: entrada do valor de comprimento
    :param l: entrada do valor de largura
    :return: retornar o valor da area
    '''
    a = c * l
    return a


#programa q vai pedir comprimento e largura
com=float(input("Digite o comprimento: "))
lar=float(input("Digite a largura: "))

#usando a função com as variaveis do programa
print(area(com,lar))



