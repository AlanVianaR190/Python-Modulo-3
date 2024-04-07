#função de contador inicio, fim & pulo
def contador(b, e, p):
    """
    :param b: de qual numero iniciara a contagem
    :param e: ate que numero sera a contagem
    :param p: se quizer que duarante a contagem pule numeros
    :return: sem retorno
    """
    from time import sleep

    #condição caso o valor do pulo seja 0 passa a ser 1, ou caso seja um valor negativo passa a ser positivo
    if p == 0:
        p = 1
    if p < 0:
        p *= -1

    #condição caso o valor d inicio seja menor
    if b < e:
        cont = b
        while cont <= e:
            print(cont, end="  "),sleep(0.5)
            cont += p
        print("FIM")

    #condição caso o valor d inicio seja maior
    else:
        cont = b
        while cont >= e:
            print(cont, end="  "),sleep(0.5)
            cont -= p
        print("FIM")


#
#usando a função
contador(1, 10, 1)
contador(10, 0, 2)

#definindo inicio, fim & pulo p aplicar na função
inic=int(input("Digite o inicio: "))
fina=int(input("Digite o final: "))
pulo=int(input("Digite o pulo: "))

#
contador(inic, fina, pulo)



