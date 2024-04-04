#
boletins = list()
boletim = list()

#
media = 0

while True:
    #dados do boletim aluno
    nome = str(input("Digite o nume do aluno: ")).upper().strip()
    boletim.append(nome)
    nota1 = float(input("Digite a primeira nota: "))
    boletim.append(nota1)
    nota2 = float(input("Digite a segunda nota: "))
    boletim.append(nota2)

    #media do aluno
    media = (nota1 + nota2) / 2
    boletim.append(media)

    #copiar o boletim do aluno
    boletins.append(boletim[:])
    boletim.clear()

    #
    resp = str(input("Deseja continuar registrando [S/N]: ")).upper().strip()[0]
    while resp not in("S","N"):
        print("Opção Invalida")
        resp = str(input("Deseja continuar registrando [S/N]: ")).upper().strip()[0]

    #
    if resp in("N"):
        break

print("FIM")

#ver todos os boletins
for pos, boletim in enumerate(boletins):
    print(f"[{pos}] Aluno: {boletim[0]} Media: {boletim[3]}")

print("---"*20)

#laço p ver um boletim especifico
while True:

    #
    opc = int(input("Digite o numero do aluno que deseja verificar ou digite 100 p/ ENCERRAR: "))

    if opc == 100:
        break

    #
    if opc <= len(boletins)-1:
        aluno = boletins[opc]
        print(f"Aluno: {aluno[0]} / N1: {aluno[1]} / N2: {aluno[2]} / Media: {aluno[3]}")
    else:
        print("Aluno não Cadastrado!")

    print("---"*20)

print("Programa Encerado")
