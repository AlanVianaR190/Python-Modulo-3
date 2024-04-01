produtos = ("Bota",800,"Notebook",3000,"Iphone",4000,"Blusa",400)

#tupla apenas dos produtos
produto = tuple(())

#tupla apenas de preço
preco = tuple(())

print(f'{"TABELA DE PREÇOS":^40}')

#laço p pegar apenas os produtos
for cont in range(0, len(produtos),2):
    produto += produtos[cont],

#laço p pegar apenas os preços
for cont in range(1, len(produtos), 2):
    preco += produtos[cont],

#mostrar a tabela
for cont in range(0,4):
    print(f"{produto[cont]:.<30} R${preco[cont]:>7.2f}")


#outra versão
'''produtos=("Bota",800,"Notebook",3000,"Iphone",4000,"Blusa",400)

#tupla apenas dos produtos
produto=()

#tupla apenas de preço
preco=()

for cont in range(0, len(produtos)):

    if cont%2==0:
        produto += produtos[cont],

    else:
        preco += produtos[cont],

for cont in range(0, len(produto)):
    print(f"O produto {produto[cont]} tem o preço R${preco[cont]}")'''

