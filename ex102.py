def fatorial(n, show=False):
    '''
    :param n: um valor para calcular o fatorial
    :param show: e opcional para mostrar o fatorial, colocando True mostra
    :return: mostra apenas o resultado
    '''
    f = 1
    for c in range(n, 0, -1):

        #condição p mostrar o fatorial
        if show:
            print(c, end=" ")
            if c > 1:
                print(" x ", end=" ")
            else:
                print(" = ", end=" ")

        f *= c
    return f"O fatorial e: {f}"


#
num=int(input("Digite um numero: "))
print(fatorial(num))

#a função <help> mostra a descrição da função
help(fatorial)
