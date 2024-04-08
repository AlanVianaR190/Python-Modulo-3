#função
def ajuda(nm):

    if nm not in("fim"):
        info = help(nm)
        return info



#programa principal
while True:
    inform = str(input("Digite um METODO ou FUNÇÃO: ")).lower().strip()
    ajuda(inform)

    print("---"*30)

    if inform in("fim"):
        break

print("ENCERRADO")
