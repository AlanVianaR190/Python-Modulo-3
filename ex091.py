import random

#dicionario
dicionario = {"Jogador 1": random.randint(1,6),
            "Jogador 2": random.randint(1,6),
            "Jogador 3": random.randint(1,6),
            "Jogador 4": random.randint(1,6)}

#vizualizar o dicionario 1 por vez
for jogador, jogo in dicionario.items():
    print(f"O {jogador} tirou {jogo}")

#deixar em ordem decrescente
dicionario = sorted(dicionario.items(), key= lambda item: item[1], reverse=True)

'''Apos usar o <sorted> o dicionario passa a ser lista'''

#vizualizar a partir da ordem decrescente
for pos, jogo in enumerate(dicionario):
    print(f"O {pos+1}º foi o {jogo[0]} com {jogo[1]} ")

'''a função enumerate funciona apenas em listas e tuplas! Mostrando primeiro a posição e depois o conteudo'''










