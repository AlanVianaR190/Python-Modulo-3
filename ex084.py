pessoa = list()
lista = list()

pesado = leve = 0

while True:
    nome = str(input("Digite o nome da pessoa: ")).upper().strip()
    pessoa.append(nome)
    peso = float(input("Digite o peso da pessoa: "))
    pessoa.append(peso)

    #condição p descobrir o menor e o maior peso
    if len(lista) == 0 or peso < leve:
        leve = peso
    if len(lista) == 0 or peso > pesado:
        pesado = peso

    #colocando [:] faz uma copia da pessoa para lista
    lista.append(pessoa[:])
    #a função <.clear> limpa o cadastro anterior
    pessoa.clear()

    resp = str(input("Deseja continuar [S/N]: ")).upper().strip()[0]
    while resp not in("S","N"):
        print("Resposta Invalida")
        resp = str(input("Deseja continuar [S/N]: ")).upper().strip()[0]

    if resp in("N"):
        break


print("END")
print(f"Foram cadastradas {len(lista)} pessoas")

#mais pesados
print(f"O maior peso e {pesado:.1f} peso do/da")
for nome, peso in lista:
    if peso == pesado:
        print(nome, end=" - ")
print("!")

#mais leves
print(f"\nO menor peso e {leve:.1f} peso do/da")
for nome, peso in lista:
    if peso == leve:
        print(nome, end=" - ")
print("!")

