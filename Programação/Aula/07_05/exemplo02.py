nomes= list()
for i in range(5):
    n = input('Digite um nome: ')
    #armazenamento na lista
    nomes.insert(i, n) #i = indice, n = valor

#saída
for i in range (len(nomes)): #len= qtde de elementos da lista
    print(nomes[i])
    #exibe o nome armazenado índice 2
    print(nomes[2])

    #ordena a lista
    nomes.sort()#ordem alfabética
    print(nomes)

    nomes.reverse()#ordem alfabética inversa
    print(nomes)
