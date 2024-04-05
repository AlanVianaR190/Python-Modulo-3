'''info = dict()

gols = 0

#
info["Nome"] = str(input("Digite o nome do jogador: ")).upper().strip()
info["Nº Partidas"] = int(input("Digite a quantidade de partidas: "))

#
for c in range(0, info["Nº Partidas"]):
    info["Partida " + str(c)] = int(input(f"Digite a quantidade de gols da {c} partida: "))

    #
    gols += info["Partida " + str(c)]

#
info["Total gols"] = gols

print("---"*20)

for key, value in info.items():
    print(f"O campo [{key}] tem o valor [{value}]")'''


#outra versão
#
info = dict()

#lista para armazenar gols, total de gols
gols = list()

#
info["Nome"] = str(input("Digite o nome do jogador: ")).upper().strip()
info["Nº Partidas"] = int(input("Digite a quantidade de partidas: "))

#laço para adicionar a quantidade de gols a lista
for c in range(0, info["Nº Partidas"]):
    gols.append(int(input(f"Digite a quantidade de gols da {c+1} partida: ")))

#acrescentar a lista no dicionario, junto com o total de gol
info["Gols"] = gols
info["Total de Gols"] = sum(gols)

print("---"*20)

#
for key, value in info.items():
    print(f"{key}: {value}")
