def leiaInt(msg):
    #
    valor = 0
    on = False
    #
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            on = True
        if on:
            break

        else:
            print("DADO INVALIDO")

    return valor


#
numero = leiaInt("Digite um numero: ")
print(f"Voce digitou o numero: {numero}")


