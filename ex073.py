#Tupla
times = tuple(("BOTAFOGO","FLAMENGO","FLUMINENSE","PALMEIRAS","BRAGANTINO","GREMIO","ATHLETICO-PR",
       "CUIABA","SÃO PAULO","ATLETICO-MG","CRUZEIRO","INTERNACIONAL","FORTALEZA","CORINTHIANS",
       "GOIAS","BAHIA","SANTOS","CURITIBA","VASCO DA GAMA","AMERICA"))

#A laço mostrara os 5 primeiros colocados, a função <len> mostrara a quantidade de caracteres na tupla
print("Os 5 primeiros colocados são: ")
for time in times[0:5]:
    print(time)
print("---"*10)

#
print("\nOs 4 ultimos colocados são: ")
for time in times[16:]:
    print(time)
print("---"*10)

#A função <sorted> mostra em ordem crescente
print("\nOs times em ordem alfabetica fica: ")
print(sorted(times),)
print("---"*10)

#A função index mostrara a posição do valor especifico
print("O time do CORINTHINAS se encontra na: ")
print(f"O Corinthians esta na {times.index('CORINTHIANS')+1}ª posição")
