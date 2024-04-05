#
info = dict()

#lista para armazenar gols
jogadores = list()

while True:

    #
    info["Nome"] = str(input("Digite o nome do jogador: ")).upper().strip()
    info["Nº Partidas"] = int(input("Digite a quantidade de partidas: "))

    #lista gols dentro do laço, cada jogador tera  sua lista!
    gols = list()

    #laço para adicionar a quantidade de gols a lista
    for c in range(0, info["Nº Partidas"]):
        gols.append(int(input(f"Digite a quantidade de gols da {c+1} partida: ")))

    #acrescentar a lista no dicionario, junto com o total de gol
    info["Gols"] = gols
    info["Total de Gols"] = sum(gols)

    #
    jogadores.append(info.copy())

    opc = str(input("Deseja continuar cadastrando [S/N]: ")).upper().strip()[0]
    while opc not in("S","N"):
        print("Opção Invalida")
        opc = str(input("Deseja continuar cadastrando [S/N]: ")).upper().strip()[0]
    if opc in("N"):
        break

#
print("----- Lista de Jogadores -----")
for pos,info in enumerate(jogadores):

    print(f"[{pos}] Jogador: {info['Nome']}; Gols: {info['Total de Gols']}.")

#verificar informações
print("---"*20)
while True:

    esc = int(input("Digite o numero do jogador p/ verificar [999 p/ encerrar]: "))
    if esc == 999:
        break

    if esc <= len(jogadores)-1:
        info = jogadores[esc]
        print(f"O jogador: {info['Nome']}; jogou {info['Nº Partidas']} partidas e fez {info['Total de Gols']} gols.")

        for pos,gol in enumerate(info["Gols"]):
            print(f"Na {pos+1}ª partida fez {gol} gols;")

    print("---"*20)

print("Encerrando")




