#
from ex115.util.arquivos import*
from time import sleep

#
arq="Curso.txt"
#
if not arquivoExist(arq):
    criarArquivo(arq)

#
while True:
    resposta = menu(["Ver cadastros", "Cadastrar", "Sair"])
    if resposta == 1:
        #opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #opções para cadastrar uma nova pessoaa
        titulo("Novo Cadsatro")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        #opção para sair do sistema
        titulo("Encerrando o sistema...")
        break
    else:
        print("ERRO... Digite uma opção valida!")
        sleep(1)

