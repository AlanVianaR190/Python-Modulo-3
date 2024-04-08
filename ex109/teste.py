from ex109 import moeda

#
num=int(input("Digite um numero: "))

print(f"O aumento de 10% de {moeda.moeda(num)} e {moeda.aumentar(num, 10, True)}")
print(f"O desconto de 10% de {moeda.moeda(num)} e {moeda.diminuir(num, 10, True)}")
print(f"0 dobro de {moeda.moeda(num)} e {moeda.dobro(num, True)}")
print(f"A metade de {moeda.moeda(num)} e {moeda.metade(num, True)}")
