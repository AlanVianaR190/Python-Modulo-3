#lista
lista = list()

# laço com a função <.append> para adicionar elemento a lista
for cont in range(0, 5):
    lista.append(int(input(f"Digite o numero da posição {cont} : ")))

# elemento minimo da lista <min>
valMin = min(lista)
# elemento maximo da lista <max>
valMax = max(lista)

print("---" * 20)

print(lista)

#
print(f"O numero menor da lista e {valMin} na posição...")

# laço com condição p pegar as posições do valor minimo
for pos, numero in enumerate(lista):

    if valMin == numero:
        print(f"{pos}...", end="")

#
print(f"\nO numero maior da lista e {valMax} com a posição...")

# laço com condição p pegar as posições do valor maximo
for pos, numero in enumerate(lista):

    if valMax == numero:
        print(f"{pos}...", end=" ")

print("\nFim")