#dicionario
aluno = dict()

aluno["nome"] = str(input("Digite nome do aluno: ")).upper().strip()
aluno["media"] = float(input("Digite a media do aluno: "))

#laço de repetição caso a pessoa digite uma nota acima de 10 e menos que 0
while aluno["media"] < 0 or aluno["media"] > 10.0:
    print("Media invalida")
    aluno["media"] = float(input("Digite a media do aluno: "))

#
if aluno["media"] < 5.0:
    aluno["status"]="REPROVADO"

elif aluno["media"] >= 5.0 and aluno["media"] < 7.0:
    aluno["status"] = "RECUPERAÇÃO"

elif aluno["media"] >= 7.0:
    aluno["status"] = "APROVADO"

#
for key, values in aluno.items():
    print(f"O campo: {key} tem o valor: {values}")
