from ex108 import moeda

#
num=int(input("Digite um numero: "))

print(f"O aumento de 10% de {moeda.moeda(num)} e {moeda.moeda(moeda.aumentar(num, 10))}")
print(f"O desconto de 10% de {moeda.moeda(num)} e {moeda.moeda(moeda.diminuir(num, 10))}")
print(f"0 dobro de {moeda.moeda(num)} e {moeda.moeda(moeda.dobro(num))}")
print(f"A metade de {moeda.moeda(num)} e {moeda.moeda(moeda.metade(num))}")
