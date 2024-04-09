from ex115.util.modulos import*

#
def arquivoExist(nome):
    '''
    verificador de existencia de arquivo
    :param nome: nome do arquivo
    :return: True(Existe), False(Não existe)
    '''
    try:
        abrir = open(nome, "rt")#rt - read text(ler arquivo)
        abrir.close()
    except (FileNotFoundError):
        return False
    else:
        return True


#
def criarArquivo(nome):
    '''
    criar um arquivo
    :param nome: nome do arquivo
    :return:
    '''
    try:
        abrir = open(nome, "wt+")#wt+ - write text(escrever arquivo)
        abrir.close()
    except:
        print("Houve um erro na criação do arquivo!")
    else:
        print("Arquivo criado com sucesso!")


#
def lerArquivo(nome):
    try:
        abrir = open(nome, "rt")
    except:
        print("Erro na leitura do arquivo")
    else:
        titulo("Pessoas Cadastradas")
        for linha in abrir:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n"," ")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        abrir.close()


#
def cadastrar(arq, nome = "desconhecido", idade = 0):
    try:
        abrir = open(arq, "at")#at - append text(adicionar arquivo)
    except:
        print("Houve um erro na hora de escrever o arquivo")
    else:
        try:
            abrir.write(f"{nome};{idade}\n")
        except:
            print("Houve um erro na hora de escrever os dados")
        else:
            print(f"Registro de {nome} cadastrado com sucesso")
            abrir.close()

