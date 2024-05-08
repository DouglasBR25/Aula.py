nomes = []#criando a lista
#solicitar 5 nomes e amarzerna na lista
for i in range(5):
    n=input('Digite um nome: ')
    nomes.append(n) #Armazena o valor de n no final da lista

#saída
print(nomes)

for nome in nomes:
    print(nomes)

#função enumerate
for x,e in enumerate(nomes):
    print('[%d] - %s' %((x+1), e))