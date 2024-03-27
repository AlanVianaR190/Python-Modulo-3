#Tupla
numeros = tuple(("Zero","Um","Dois","Tres","Quatro","Cinco","Seis","Sete","Oito",
               "Nove","Dez","Onze","Doze","Treze","Quatorze","Quinze","Dezeseis",
               "Dezesete","Dezoito","Dezenove","Vinte"))

while True:
    num = int(input("Digite um numero de 0 a 20: "))

    # loop caso o numero digitado não seja entre 0 e 20
    while num < 0 or num > 20:
        print("Numero invalido!")
        num = int(input("Digite um numero de 0 a 20: "))

    print(f"O numero {num} escrito por extenso e >>> {numeros[num]}")

    #
    res = str(input("Deseja continuar [S/N]: ")).upper()[0]
    while res not in("S","N"):
        print("Resposta Invalida")
        res = str(input("Deseja continuar [S/N]: ")).upper()[0]
    if res in("N"):
        break

print("Fim")
