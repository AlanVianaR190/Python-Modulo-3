#função p identificar o numero maior
def maior(* num):
    '''
    :param num: pode entrar varios valores
    :return: o maior valor
    '''

    cont = maior = 0

    #pegar o maior valor
    for valor in num:
        if cont == 0 or valor > maior:
            maior = valor
        cont += 1
    #print(f"O maior valor de {cont} numeros e {maior}")
    return maior


print(maior(1,4,5,9,2,))
print(maior(10,5,7,3))




