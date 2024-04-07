def ficha(n="<null>", g=0):
    '''
    função para guardar nome, e numero de gols ou o que desejar
    :param n: guardar o nome (não e obrigatorio)
    :param g: quantidade de gols, não e obrigatorio
    :return: sem retorno, apenas mostra um print
    '''
    print(f"JOGADOR: {n}; GOLS: {g}")



#
nome = str(input("Digite nome: ")).upper().strip()
gols = str(input("Digite a quantidade de gols: "))

#essa condição modifica a variavel gols para o tipo int
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

#esta condição faz com que mesmo que não ponha o nome siga para a parte gols
if nome.strip() == "":
    ficha(g=gols)
else:
    ficha(nome,gols)
