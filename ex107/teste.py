from ex107 import moeda

#
num=int(input("Digite um numero: "))

print(f"O aumento de 10% de {num} e {moeda.aumentar(num, 10)}")
print(f"O desconto de 10% de {num} e {moeda.diminuir(num, 10)}")
print(f"0 dobro de {num} e {moeda.dobro(num)}")
print(f"A metade de {num} e {moeda.metade(num)}")
