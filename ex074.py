'''import random

#A função <random.sample> ira prencher a tupla com 5 numeros aleatorios
numeros=tuple(random.sample(range(1,99),5))
maior=menor=cont=0

for cont in range(0, len(numeros)):
    print(numeros[cont], end=" ")

    #Forma para mostrar o maior e o menor
    if cont == 0 or numeros[cont] < menor:
        menor = numeros[cont]

    if cont == 0 or numeros[cont] > maior:
        maior = numeros[cont]

print(f"\nO menor numero da lista e {menor} e o maior e {maior}")'''

#solução Curso
import random

#A função <random.sample> ira prencher a tupla com 5 numeros aleatorios
numeros = tuple(random.sample(range(1,99),5))

for numero in numeros:
    print(numero, end=" ")

#A função <min> pega o menor numero da lista
print(f"\nO menor numero da lista e {min(numeros)}")

#A função <max> pega o maior numero da lista
print(f"O maior numero da lista e {max(numeros)}")
