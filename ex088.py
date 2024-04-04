import random
import time

#
jogos = list()

#
op = int(input("Quantos jogos deseja fazer: "))
print("---"*15)

#laço p quantidade de jogos
for c in range(0, op):
    jogo = list(random.sample(range(1,80,),5))

    #
    jogos.append(jogo)

#laço p mostrar os jogos
for pos,jogo in enumerate(jogos):
    print(f"O jogo {pos+1} --> {jogo}"),time.sleep(1)

print("Boa sorte!!!")
