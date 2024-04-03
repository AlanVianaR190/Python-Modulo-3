# listas p pegar os parenteses abertos e fechados
dir = list()
esq = list()

expr = str(input("Digite a expressão: "))

# condição pra verificar se a expressão esta correta no inicio
if expr[0] in ("("):

    # laço p verificar cada caracter
    for carac in expr:

        # condições p pegar os caracteres de parenteses
        if carac in ("("):
            dir.append(carac)

        if carac in (")"):
            esq.append(carac)

    # condição p verificar se as lista tem o mesmo valor de caracteres
    if len(dir) == len(esq):
        print("A expressão esta Correta!")
    else:
        print("E expressão esta Incorreta!")

else:
    print("E expressão esta Incorreta!")

print("Fim")

