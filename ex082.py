#listas para numeros, numeros pares e impares
numeros = list()
pares = list()
impares = list()

while True:
    num = int(input("Digite um numero: "))
    numeros.append(num)

    resp = str(input("Deseja continuar [S/N]: ")).upper().strip()[0]
    while resp not in ("S", "N"):
        print("Opção Invalida")
        resp = str(input("Deseja digitar mais [S/N]: ")).upper().strip()[0]

    if resp in("N"):
        break

print(numeros)

#laço para verificar os numeros
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Os numeros pares são {pares}")

print(f"Os numeros impares são {impares}")