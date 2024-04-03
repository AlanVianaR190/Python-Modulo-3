
'''numerosPar=list()

numerosImpar=list()

numeros=list()

for pos in range(1, 8):
    num=int(input(f"Digite o {pos}º numero: "))

    #utilizar a função <.clear> pra limpar o cadastro anterior, nesta posição evita apagar tudo
    numeros.clear()

    #condição para pegar os pares e os impares
    if num%2==0:
        numerosPar.append(num)
    else:
        numerosImpar.append(num)

    #adicionalos a lista geral
    numeros.append(numerosPar)
    numeros.append(numerosImpar)

numerosPar.sort()
numerosImpar.sort()

print("A lista com todos os numeros - ",numeros)
print("Os numeros PARES - ",numerosPar)
print("Os numeros IMPARES - ",numerosImpar)'''

#versão do professor
valores = [[], []]

for v in range(1, 8):
    valor = int(input(f'Digite o {v}° valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

print(f'Os valores pares digitados foram: {valores[0].sort()}')
print(f'Os valores ímpares digitados foram: {valores[1].sort()}')


