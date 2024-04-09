#
def leiaInt(msg):
    while True:
        try:
            num=int(input(msg))
        except (ValueError, TypeError):
            print("Valor inválido. Digite um número inteiro.")
            continue
        except (KeyboardInterrupt):
            print("Programa Encerrado")
            return 0
        else:
            return num


#
def linha(tam=50):
    '''
    Traça uma linha pontilhada horizontal
    :param tam: tamanho da linha ou quantos pontilhados tera, padrão 50
    :return: a linha
    '''
    return "-"*tam


#
def titulo(txt):
    '''
    Inseri um titulo entre linhas pontilhadas
    :param txt: insira o texto ou titulo que deseja
    :return: o titulo
    '''
    print(linha())
    print(txt.center(50))
    print(linha())


#
def menu(lista):
    '''
    Inserir um menu no programa
    :param lista: colocar os itens que deseja, por entre conchetes para entrar como lista
    :return: a opção escolhida
    '''
    titulo("Menu")
    cont=1
    for item in lista:
        print(f"{cont} - {item}")
        cont += 1
    print(linha())
    opc = leiaInt("Opção: ")
    return opc
