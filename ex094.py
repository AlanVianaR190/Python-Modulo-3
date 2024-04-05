#dicionario pessoa
pessoa=dict()

#listas de pessoas
lista=list()

#
somIdad=medIdad=0

#
while True:

    #
    pessoa["Nome"] = str(input("Digite o nome: ")).upper().strip()


    pessoa["Sexo"] = str(input("Digite o sexo: ")).upper()[0]
    while pessoa["Sexo"] not in("M","F"):
        print("Opção Invalida")
        pessoa["Sexo"] = str(input("Digite o sexo: ")).upper()[0]


    pessoa["Idade"] = int(input("Digite a idade: "))

    #acrescentar pessoa na lista, acumulador de idade
    lista.append(pessoa.copy())
    somIdad+=pessoa["Idade"]

    #
    opc = str(input("Deseja continuar cadastrando [S/N]: ")).upper().strip()[0]
    while opc not in("S","N"):
        print("Opção Invalida")
        opc = str(input("Deseja continuar cadastrando [S/N]: ")).upper().strip()[0]
    if opc in("N"):
        break

#a
print("---"*20)
print(f"A quantidade de pessoas cadastradas e de {len(lista)}")

#b
medIdad=somIdad/len(lista)
print("---"*20)
print(f"A media de idade e de {medIdad:.0f}")

#c
print("---"*20)
print("As mulheres da lista são: ")
for pessoa in lista:
    if pessoa["Sexo"] in("F"):
        print(f"{pessoa['Nome']}")
print()

#d
print("---"*20)
print("A lista com pessoas acima da media: ")
for pessoa in lista:
    if pessoa["Idade"] > medIdad:

        for key, value in pessoa.items():
            print(f"{key}: {value}; ",end=" ")
        print()
print("FIM")




