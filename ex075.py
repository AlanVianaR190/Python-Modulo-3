''''#Uma tupla p acrescentar os numros
tupla=tuple(())

#Uma tupla p acrescentar os pares
pares=tuple(())

#laço para digitar os numeros
for cont in range(0,4):
    num=int(input("Digite um numero: "))

    #Esta forma de acrescentar com a virgula e necessario em caso de tupla
    tupla+=num,

    #Condição p pegar os pares
    if num%2==0:

        #Para acrescentar os pares
        pares+=num,

print(tupla)

#condição caso apareca o num 3 na tupla
if 3 in tupla:
    print(f"O numero 3 apareceu na posição {tupla.index(3)}")
else:
    print("O numero 3 não apareceu na tupla!")

#A função <count> mostra a quantidade
print(f"O numero 9 apareceu {tupla.count(9)} vezes")
print(f"Os numeros pares são {pares}")'''

#75 versão melhorada
numeros = tuple(())

for cont in range(0,4):
       num = int(input("Digite um numero: "))

       numeros += num,

print(numeros)

#Verificar se o numero 9 apareceu
print(f"O valor 9 (nove) apareceu {numeros.count(9)}")#A função <count> mostra a quantidade

#Verificar numero 3
if 3 in numeros:
       print(f"O numero 3 apareceu na posição {numeros.index(3)}")
else:
       print("Não tem o numero 3")

#verificar os pares
print("Os numeros pares são:")
for numero in numeros:

       if numero % 2 == 0:
              print(numero, end=" ")

