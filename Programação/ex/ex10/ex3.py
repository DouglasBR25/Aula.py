#item a
somaI = 0#acumulador
contI=0#contador
#item b
somaS = 0 #acumulador
contS = 0 #contador
#item c
qtde=0#contador

while True:#loop infinito
    idade=int(input('Digite sua idade: '))
    salario=float(input('Digite seu salario: '))
    if idade < 0:
        break
    #item a
    somaI= somaI + idade
    contI= contI + 1
    #item b
    if idade >= 40:
        somaS = somaS + salario
        contS = contS + 1
    #item c
        if salario < 2000:
            qtde = qtde + 1

if somaI > 0:
    #item a
    mediaI = somaI/contI
    #item b
    mediaS= somaS/contS

    print('Media das idades', mediaI)
    print('Salário médio das pessoas >=40: ', mediaS)
    print('Quantidade de pessoas com salário <2000: ', qtde)