#laço condicional

contador=0 #contador
soma=0 #acumulador
resp='s'#inicialização da variavel de controle

while resp== 's' or resp=='S': #s = sim
    n=int(input('Digite um número: '))
    soma=soma+n#acumula os valores digitados
    contador= contador+1#conta de qtde de numeros digitados
    #atualização da variavel de controle
    resp=input('Deseja continuar (s = sim /n = não)')

media = soma/contador
print('Média =',media)