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


def leiaFloat(msg):
    while True:
        try:
            num=float(input(msg))
        except (ValueError, TypeError):
            print("Valor inválido. Digite um número inteiro.")
            continue
        except (KeyboardInterrupt):
            print("Programa Encerrado")
            return 0
        else:
            return num


# Exemplo de uso
dig1 = leiaInt("Digite um valor: ")
print(f"O valor digitado foi {dig1}")

dig2 = leiaFloat("Digite um valor: ")
print(f"O valor digitado foi {dig2}")
