#Escreva um algoritmo que leia um grupo de valores reais e determine quantos valoressão positivos e quantos são negativos. Determine, também, qual é o menor dessesvalores. Utilize o comando de repetição que desejar.

numeros = []

while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    resp = input('Deseja continuar? (s/n): ')
    if resp == 'n':
        break
    elif resp != 's':
        print('Letra inválida')

for num in numeros:
    if num < 0:
        print('Número negativo:', num)
    elif num > 0:
        print('Número positivo:', num)

menor=min(numeros)
print('O menor número é ', menor)