#Exercicio não resolvido

numeros = list()

#laço for p por os numeros na lista
for cont in range(0,5):
    num = int(input(f"Digite o {cont} numero: "))

    if cont==0 or num > numeros[-1]:
        numeros.append(num)
    else:
        pos=0

        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos,num)
                break
            pos += 1

print(numeros)

#Solução usando a função <insort> do modulo bisect
'''from bisect import insort

numeros = list()

for cont in range(5):
    num = int(input("Digite um número: "))

    # Insere o número na posição correta
    insort(numeros, num)  

print(numeros)'''
