'''palavras=tuple(("Alan","Onze","Bota","Dinheiro"))

#tupla p pegar as vogais
vogal=tuple(())

#laço for p mostrar as palavras
for palavra in palavras:
    print(f"A palavra {palavra}")

    #uma tupla p pegar as letras da palavra
    palavra=tuple((palavra.lower()))

    #um laço com condição p poder pegar as vogais e por numa tupla
    for letra in palavra:

        if letra in("a","e","i","o","u"):
            vogal+=letra,

    print(f"Tem as vogais {vogal}")
    print("---"*10)

    #<del> para deletar a tupla pois ela não tem como zerar
    del(vogal)

    #tupla novamente criada e vazia para ser uzada novamente na proxima palavra
    vogal = tuple(())

print("Fim")'''

#77 versão melhorada
palavras = tuple(("Garafa", "Celular", "Chave", "Copo", "Lapis", "Video game",
                "Estojo", "Remedio", "Lapis", "Caixa", "Caderno", "Relogio"))

#laço para mostrar as palvras
for palavra in palavras:
    print(f"\nA palavra {palavra.upper()} tem as vogais:",end=" ")

    #Laço com condição p pegar as vogais
    for vogais in palavra.lower():

        if vogais in("a","e","i","o","u"):
            print(vogais,end=" ")

print("Fim")
