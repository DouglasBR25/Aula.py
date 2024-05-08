#quantidade indeterminada de valores
nros = []# criando a lista
soma = 0
qtde = 0
while True:
    nro = int(input('Digite um número: '))
    if nro == 0:
        break

    nros.append(nro)
#acumula valores
soma= sum(nros)
#calcula a média
media = soma/len(nros)
#conta quantos valores estão acima da média
for n in nros:
    if n> media:
        qtde = qtde + 1

print('Média: ', media)
print('Acima da média', qtde)