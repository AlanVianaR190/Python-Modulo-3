#função para sortear 5 numeros
def sorteia(nums):
    '''
    :param nums: sorteia 5 valores aleatorios
    :return: sem retorno
    '''

    #função random
    from random import randint

    #
    for c in range(0,5):
        n = randint(1, 80)
        nums.append(n)
        print(n, end=" - ")
    print("PRONTO")

#função para somar os pares
def somaPar(lista):
    '''
    :param lista: entra uma lista com valores
    :return: a soma dos numeros pares
    '''

    #
    acum = 0

    #varrer os numeros para pegar os pares
    for valor in lista:
        if valor % 2 == 0:
            acum += valor
    return acum



#
lista=list()

#a função sorteia ira por os numeros na lista
sorteia(lista)

#a função executara com base os numeros da lista
print(f"A soma dos numeros pares{somaPar(lista)}")





