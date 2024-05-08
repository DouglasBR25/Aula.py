#Faça um programa em Python que imprima os números de 1 a 50 de 1 em 1 e de 52 a100 de 2 em 2.
n=int(input('Digite um valor positivo: '))
if n<0:
    print('Não é valor positivo')
else:
    for i in range(0, 1/n+1):
        print(i, end=" ")