#solicita 10 número e mostrar a soma

#acumulador
soma=0
for a in range(10):
    n = float(input('Digite um número: '))
    #acumulador
    soma = soma + n
    media = soma/10
    print('Soma dos valores digitados: ', soma)
    print('Média dos valores: ', media)