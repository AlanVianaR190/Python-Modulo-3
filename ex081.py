lista = list()

while True:
    num = int(input("Digite um numero: "))
    lista.append(num)

    resp = str(input("Deseja digitar mais [S/N]: ")).upper().strip()[0]
    while resp not in("S","N"):
        print("Opção Invalida")
        resp = str(input("Deseja digitar mais [S/N]: ")).upper().strip()[0]

    if resp in("N"):
        break

print(lista)

#função <len()> para mostrar a quantidade
print(f"Foram digitados {len(lista)} numeros na lista")

#<sort(reverse=True) para por os numeros em ordem decrescente>
lista.sort(reverse=True)
print(f"Os numeros organizados na forma descrescente {lista}")

#condição p verificar se o numero 5 esta na lista
if 5 in(lista):
    print("O numero 5 esta na lista!")
else:
    print("O numero 5 não esta na lista")