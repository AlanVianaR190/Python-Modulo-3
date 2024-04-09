def leiaDinheiro(msg):
    valid = False
    while not valid:
        entrada=str(input(msg)).strip().replace(",",".")

        if entrada.isalpha() or entrada == " ":
            print("ERRO, entrada invalida!")

        else:
            valid=True
            return float(entrada)
