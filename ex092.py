from datetime import date

#
cadastro = dict()

cadastro["Nome"] = str(input("Digite o nome: ")).upper().strip()

#
ano = int(input("Digite o ano de nascimento: "))
cadastro["Idade"] = date.today().year - ano

#
ctps = int(input("Digite o numero da carteira de trabalho ou digite [0] se não tiver: "))
if ctps == 0:
    print("Cadastrado não possui CTPS.")

else:
    cadastro["CTPS"] = ctps
    cadastro["Contratação"] = int(input("Digite o ano de contratação: "))
    cadastro["Salario"] = float(input("Digite o valor do salario: R$"))

    #
    aposentadoria = (cadastro["Contratação"] + 35) - date.today().year
    cadastro["Aposentadoria"] = aposentadoria

print("---"*20)

#
for key,values in cadastro.items():
    print(f"O Campo [{key}] tem o valor [{values}]")



