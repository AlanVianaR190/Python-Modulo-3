def escreva(msg):
    '''
    Coloca bordas na mensagem
    :param msg: escreva o que deseja
    '''
    tam = len(msg) * 2
    print("-=" * tam)
    print(f"  {msg:^{tam}}")
    print("=-" * tam)

esc=str(input("Digite seu texto: "))

escreva(esc)

