#lista
matriz = [[],[],[]]
somaPar = 0
soma3bloc = 0

#laço para o bloco
for bloco in range(0,3):

    #laço para posição
    for pos in range(0,3):
        num = int(input(f"Digite o numero de {[bloco,pos]}: "))

        #acrescentar a lista
        matriz[bloco].append(num)

        #
        if num % 2 == 0:
           somaPar += num

#
print(matriz)
print(f"A soma de todos os numeros pares e {somaPar}")

#versão correta para fazer a soma dos valores, e necessario varrer
for val in matriz[2]:
    soma3bloc += val

print(f"A soma dos valores da terceira coluna e {soma3bloc}")

#
print(f"O maior valor da segunda linha e {max(matriz[1])}")

