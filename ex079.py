lista = list()

#laço p digitar os numeros
while True:
    num = (int(input("Digite um numero: ")))

    #condição para adicionar um numero a lista
    if num not in(lista):
        lista.append(num)
    else:
        print("Numero repetido, digite outro!")

    #laço caso a respsta seja respondida errada
    res = str(input("Deseja continuar digitando [S/N]: ")).upper().strip()[0]
    while res not in("S","N"):
        print("Resposta Invalida")
        res = str(input("Deseja continuar digitando [S/N]: ")).upper().strip()[0]

    #condição p encerrar o laço
    if res in("N"):
        break

#a função <.sort> deixa em ordem crescente
lista.sort()

print(lista)
print("Fim")