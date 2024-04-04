#matriz
'''matriz=[[],[],[]]

#laço de repetição pra passar em cada grupo, ira passar apos o de baixo concluir o ciclo
for bloco in range(0,3):

    #laço de repetição para depositar o valor em cada posição
    for posicao in range(0,3):
        valor=int(input(f"Digite o valor da {[bloco,posicao]} posição: "))
        matriz[bloco].append(valor)

for grupo in matriz:
        print(grupo)'''

#solução do professor

#lista
matriz=[[0,0,0],[0,0,0],[0,0,0]]

#bloco
for bloco in range(0,3):

    #posição
    for pos in range(0,3):
        matriz[bloco][pos]=int(input(f"Digite o valor de [{bloco},{pos}] :"))

#mostrar a matriz

#linha
for b in range(0,3):

    #coluna
    for p in range(0,3):
        print(f"[{matriz[b][p]:^6}]",end="")
    print()


